import pytest

from io import StringIO
from unittest.mock import patch

from classes import (
    InvalidCoords
)
from main import get_cup_amount


class TestWaterFlow:
    def test_invalid_location(self):
        # setup
        # execute
        # verify

        with pytest.raises(InvalidCoords):
            get_cup_amount(5,5,4)
    
    def test_no_overflow(self):
        # setup
        # execute
        # verify
        assert get_cup_amount(0,0,0.2) == 0.2 # mid
        assert get_cup_amount(1,0,0.2) == 0 # left 
        assert get_cup_amount(1,1,0.2) == 0 # right

    def test_overflow(self): 
        # test overflow distributes 
        assert get_cup_amount(0,0,0.55) == 0.25 # fill
        assert get_cup_amount(1,0,0.55) == 0.15 # left 
        assert get_cup_amount(1,1,0.55) == 0.15 # right

    def test_overflow_cascade(self): 
        """
        1 L poured
                                    0.25L 
                        0.25L                  0.25L
        (0.375-0.25)/2          (0.375-0.25)         (0.375-0.25)/2
        
            there fore (2,1) should have 0.125L 
        """
        assert get_cup_amount(0,0,1) == 0.25
        assert get_cup_amount(1,0,1) == 0.25
        assert get_cup_amount(1,1,1) == 0.25
        assert get_cup_amount(2,0,1) == 0.125/2
        assert get_cup_amount(2,1,1) == 0.125 
        assert get_cup_amount(2,2,1) == 0.125/2

