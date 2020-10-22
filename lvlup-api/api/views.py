from .serializers import EntrySerializer, UserSerializer
from .models import Entry, User
from .helpers import post_entry
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from functools import wraps
import jwt
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny

from django.http import JsonResponse
# Create your views here.


@permission_classes([AllowAny])
class EntryDetail(APIView):
    """
    Retrieve, update or delete a entry instance.
    """

    def get_object(self, pk):
        try:
            return Entry.objects.get(pk=pk)
        except Entry.DoesNotExist:
            raise Http404

    def post(self, request, format=None):
        processed_entry = post_entry(request.data.dict())
        serializer = EntrySerializer(data=processed_entry)
        if serializer.is_valid():
            serializer.save()
            parent_user = User.objects.get(pk=serializer.data['user'])

            if serializer.data['completed'] == True:
                updated_user = parent_user.leveling_up(serializer.data['xp'])
                serializer = UserSerializer(parent_user, data=updated_user)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                serializer = UserSerializer(parent_user)
                return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):
        entry = self.get_object(pk)
        completion = entry.completed
        processed_data = entry.update_self(request.data.dict())
        entry_serializer = EntrySerializer(entry, data=processed_data)
        if entry_serializer.is_valid():
            entry_serializer.save()
            parent_user = User.objects.get(pk=entry_serializer.data['user'])

            if (entry_serializer.data['completed'] == True) and (completion == False):
                updated_user = parent_user.leveling_up(
                    entry_serializer.data['xp'])
                user_serializer = UserSerializer(
                    parent_user, data=updated_user)
                if user_serializer.is_valid():
                    user_serializer.save()
                    return Response(user_serializer.data, status=status.HTTP_200_OK)

            elif (entry_serializer.data['completed'] == False) and (completion == True):
                updated_user = parent_user.leveling_down(
                    entry_serializer.data['xp'])
                user_serializer = UserSerializer(
                    parent_user, data=updated_user)
                if user_serializer.is_valid():
                    user_serializer.save()
                    return Response(user_serializer.data, status=status.HTTP_200_OK)

            else:
                user_serializer = UserSerializer(parent_user)
                return Response(user_serializer.data, status=status.HTTP_200_OK)

        return Response(entry_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        entry = self.get_object(pk)
        entry.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@permission_classes([AllowAny])
class UserDetail(APIView):

    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def post(self, request, format=None):
        new_user = request.data.user
        serializer = UserSerializer(data=new_user)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):
        user = self.get_object(pk)
        updated_user = user.leveling_up(int(request.data['xp']))
        serializer = UserSerializer(user, data=updated_user)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


def get_token_auth_header(request):
    """Obtains the Access Token from the Authorization Header
    """
    auth = request.META.get("HTTP_AUTHORIZATION", None)
    parts = auth.split()
    token = parts[1]

    return token


def requires_scope(required_scope):
    """Determines if the required scope is present in the Access Token
    Args:
        required_scope (str): The scope required to access the resource
    """
    def require_scope(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            token = get_token_auth_header(args[0])
            decoded = jwt.decode(token, verify=False)
            if decoded.get("scope"):
                token_scopes = decoded["scope"].split()
                for token_scope in token_scopes:
                    if token_scope == required_scope:
                        return f(*args, **kwargs)
            response = JsonResponse(
                {'message': 'You don\'t have access to this resource'})
            response.status_code = 403
            return response
        return decorated
    return require_scope

# Views from Auth0 quickstart for reference
# @api_view(['GET'])
# @permission_classes([AllowAny])
# def public(request):
#     return JsonResponse({'message': 'Hello from a public endpoint! You don\'t need to be authenticated to see this.'})


# @api_view(['GET'])
# def private(request):
#     return JsonResponse({'message': 'Hello from a private endpoint! You need to be authenticated to see this.'})


# @api_view(['GET'])
# @requires_scope('read:messages')
# def private_scoped(request):
#     return JsonResponse({'message': 'Hello from a private endpoint! You need to be authenticated and have a scope of read:messages to see this.'})
