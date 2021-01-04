###
#-------------------------------------------------------------------------------
# test_day02passwordphilosophy.py
#-------------------------------------------------------------------------------
#
# Author:       Alwin Tareen
# Created:      Dec 02, 2020
# Execution:    pytest -v
#
# This program is the pytest test bench.
#
##

from part01password import password
from part02philosophy import philosophy
import pytest

# Part 1: password
@pytest.mark.parametrize('data, expected', [
    ('day02sampledata.txt', 2),
    ('day02givendata.txt', 524)
])
def test_password(data, expected):
    assert password(data) == expected

# Part 2: philosophy
@pytest.mark.parametrize('data, expected', [
    ('day02sampledata.txt', 1),
    ('day02givendata.txt', 485)
])
def test_philosophy(data, expected):
    assert philosophy(data) == expected

