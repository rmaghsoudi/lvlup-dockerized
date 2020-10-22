from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

types = {'task': 1, 'pillar': 5, 'goal': 10}

def validate_type(value):
    if value not in types.keys():
        raise ValidationError(
            _('%(value)s is not an entry type'),
            params={'value': value},
        )


def calculate_xp(data):
    multiplier = types[data['type']]
    xp = (100 * int(data['difficulty'])) * multiplier
    data['xp'] = xp
    return data

def post_entry(dict):
    dict['difficulty'] = int(dict['difficulty'])
    dict['user'] = int(dict['user'])

    if 'completed' in dict.keys():
        dict['completed'] = True
        
    dict = calculate_xp(dict)

    return dict

# req data {'difficulty': '1', 'name': 'new test', 'type': 'task', 'user': ''}