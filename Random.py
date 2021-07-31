# seed the pseudorandom number generator
from random import random
from random import seed


def random_id():
    # seed random number generator
    seed()
    # generate some random numbers
    return random()
