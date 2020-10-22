from rest_framework import serializers

from .models import Entry, User

class EntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entry
        fields = ['id', 'name', 'description', 'completed', 'parent_entry', 'type', 'difficulty', 'user', 'xp']

class UserSerializer(serializers.ModelSerializer):
    entries = EntrySerializer(many=True, read_only=True)
    class Meta:
        model = User
        fields = ['id', 'auth_id', 'level', 'xp', 'xp_to_lvlup', 'entries']
