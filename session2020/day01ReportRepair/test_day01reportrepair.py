###
#-------------------------------------------------------------------------------
# test_day01reportrepair.py
#-------------------------------------------------------------------------------
#
# Author:       Alwin Tareen
# Created:      Dec 01, 2020
# Execution:    pytest -v
#
# This program is the pytest test bench.
#
##

from part01report import report
from part02repair import repair
import pytest

# Part 1: report
@pytest.mark.parametrize('data, expected', [
    ('day01sampledata.txt', 514579),
    ('day01givendata.txt', 788739)
])
def test_report(data, expected):
    assert report(data) == expected

# Part 2: repair
@pytest.mark.parametrize('data, expected', [
    ('day01sampledata.txt', 241861950),
    ('day01givendata.txt', 178724430)
])
def test_repair(data, expected):
    assert repair(data) == expected

