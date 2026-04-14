"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""
EXPECTED_BAKE_TIME=40
PREPARATION_TIME=2


def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(number_of_layers):
    
    """Calculate how long it would take (in minutes) to prepare the lasagna depending on how many layers you have (each layer taking 2 minutes).

    :param number_of_layers: int - The number of layers in the lasagna
    :return: int - how long it would take you to prepare the lasagna depending on how many layers you have

    Function that takes the amount of layers the lasagna needs as
    an argument and returns how many minutes will the preparation time take
    based on the 'number_of_layers'.
    """
    return number_of_layers*PREPARATION_TIME

def elapsed_time_in_minutes(number_of_layers,elapsed_bake_time):
    """Calculate how long have you been cooking the lasagna (in minutes) depending on how many layers the lasagna has, and how log have you been cooking the lasagna in the oven.

    :param number_of_layers: int - how many layers your lasagna has
    :param elapsed_bake_time: int - how much time has passed since you put the lasagna in the oven
    :return: int - how much time has passed since you started the whole lasagna

    Function that takes the amount of layers the lasagna needs as
    an argument and returns how many minutes will the preparation time take
    based on the 'number_of_layers'.
    """
    return preparation_time_in_minutes(number_of_layers)+elapsed_bake_time