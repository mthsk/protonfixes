""" DOOM Eternal
"""
#pylint: disable=C0103

from protonfixes import util

def main():
    """ Requires seccomp
    """

    util.use_seccomp()
