############
# Part 1   #
############


class MelonType(object):
    """A species of melon at a melon farm."""

    def __init__(self, code, name, first_harvest, color, is_seedless, 
                 is_bestseller):
        """Initialize a melon."""
        self.code = code
        self.name = name
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.pairings = []


    def add_pairings(self, pairings):
        """Add a food pairings to the instance's pairings list."""
        self.pairings.extend(pairings)

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""
        self.code = new_code


def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    musk = MelonType('musk', 'Muskmelon', 1998, 'green', True, True)
    musk.add_pairings(['mint'])

    casaba = MelonType('cas', 'Casaba', 2003, 'orange', False, False)
    casaba.add_pairings(['mint', 'strawberries'])

    crenshaw = MelonType('cren', 'Crenshaw', 1996, 'green', False, False)
    crenshaw.add_pairings(['proscuitto'])

    yellow_watermelon = MelonType('yw', 'Yellow Watermelon', 2013, 'yellow',
                                  False, True)
    yellow_watermelon.add_pairings(['ice cream'])

    all_melon_types.extend([casaba, crenshaw, yellow_watermelon, musk])

    return all_melon_types

make_melon_types()

def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""
    for melon in melon_types:
        print melon.name + " pairs with \n" + "-" + "\n-".join(melon.pairings)

print_pairing_info(make_melon_types())

def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    melon_dictionary = {}
    for melon_type in melon_types:
        melon_dictionary[melon_type.code] = melon_type
    return melon_dictionary

############
# Part 2   #
############

class Melon(object):
    """A melon in a melon harvest."""
    def __init__(self, melon_type, shape_rating, color_rating, field, harvester):
        self.melon_type = melon_type
        self.shape_rating = shape_rating
        self.color_rating = color_rating
        self.field = field
        self.harvester = harvester


def make_melons(melon_types):
    """Returns a list of Melon objects."""
    melon_types = make_melon_type_lookup(make_melon_types())
    melons = {
            'melon 1': Melon(melon_types['yw'], 8, 7, 2, 'Sheila'),
            'melon 2': Melon(melon_types['yw'], 3, 4, 2, 'Sheila'),
            'melon 3': Melon(melon_types['yw'], 9, 8, 3, 'Sheila'),
            'melon 4': Melon(melon_types['yw'], 10, 6, 35, 'Sheila'),
            'melon 5': Melon(melon_types['cren'], 8, 9, 35, 'Michael'),
            'melon 6': Melon(melon_types['cren'], 8, 2, 35, 'Michael'),
            'melon 7': Melon(melon_types['cren'], 2, 3, 4, 'Michael'),
            'melon 8': Melon(melon_types['musk'], 6, 7, 4, 'Michael'),
            'melon 9': Melon(melon_types['yw'], 7, 10, 3, 'Sheila')
            }
    
    melons_lst = melons.items()
    return melons_lst

print make_melons(make_melon_types())

def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    # Fill in the rest