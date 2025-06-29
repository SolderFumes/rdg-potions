recipes = [
    {'name': 'Luck',            'recipe': ['Accrue',    'Abate']},
    {'name': 'Protection',      'recipe': ['Fervor',    'Ardor']},
    {'name': 'Regeneration',    'recipe': ['Virulent',  'Theriac']},
    {'name': 'Healing',         'recipe': ['Fervor',    'Accrue']},
    {'name': 'Stats Up',        'recipe': ['Tenebrous', 'Gambol']},
    {'name': 'Swiftness',       'recipe': ['Gambol',    'Skew']},
    {'name': 'Warping',         'recipe': ['Abate',     'Ichor']},
    {'name': 'Resistance',      'recipe': ['Vigor',     'Ardor']},
    {'name': 'Brawn',           'recipe': ['Vigor',     'Ichor']},
    {'name': 'Affluence',       'recipe': ['Virulent',  'Lucre']},
    {'name': 'Jumping',         'recipe': ['Cavort',    'Lucre']},
    {'name': 'Chance',          'recipe': ['Cavort',    'Skew']},
    {'name': 'Sustaining',      'recipe': ['Tenebrous', 'Theriac']},
    {'name': 'Ice Resistance',  'recipe': ['Luminous',  'Algid']},
    {'name': 'Fire Resistance', 'recipe': ['Luminous',  'Torrid']},
    {'name': 'Balance',         'recipe': ['Torrid',    'Algid']},
]
hadBerries = ['Torrid', 'Tenebrous', 'Gambol', 'Skew']


def check_craftable():
    for potion in recipes:
        if potion['recipe'][0] in hadBerries and potion['recipe'][1] in hadBerries:
            print(f'You can make {potion['name']}')

if __name__ == '__main__':
    check_craftable()
