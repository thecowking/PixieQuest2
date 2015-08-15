import random


def generate_equations(stage, level):
    '''
    Remember that the level starts at zero to align with the index of the lists.
    This function just determines which function to call next, gets three variables
    a, b and c where a <op> b = c.  It is up to the display module to create the correct
    '''
    stage_list = ['_number_line', '_addition', '_subtraction', '_multiplication', '_division', '_all']
    level_list = ['simple', 'medium', 'hard']
    function = stage_list[stage] + level_list[level]
    a, b, c = getattr(function)
    return a, b, c


def simple_addition():
    a = random.randrange(1, 6)
    b = random.randrange(1, 6)
    c = a + b
    return a, b, c


def medium_addition():
    a = random.randrange(1, 11)
    b = random.randrange(1, 11)
    c = a + b
    return a, b, c


def hard_addition():
    a = random.randrange(1,21)
    b = random.randrange(1,21)
    c = a +b
    return a, b, c



def simple_subtraction():
    pass


def medium_subtraction():
    pass


def hard_subtraction():
    pass


def simple_multiplication():
    pass


def medium_multiplication():
    pass


def hard_multiplication():
    pass


def simple_division():
    pass


def medium_division():
    pass


def hard_division():
    pass


def simple_all():
    pass


def medium_all():
    pass


def hard_all():
    pass
