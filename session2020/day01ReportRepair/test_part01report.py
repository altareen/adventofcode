###
#-------------------------------------------------------------------------------
# test_part01report.py
#-------------------------------------------------------------------------------
#
# Author:       Alwin Tareen
# Created:      Dec 01, 2020
# Execution:    pytest -vv
# Session:      Advent of Code 2020, Day 1, Part 1
#
# This program is the test bench for part01report.py using pytest.
#
##

from part01report import main

def test_part01report():
    assert main() == 788739

