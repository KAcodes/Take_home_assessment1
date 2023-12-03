"""Tests for Take home assessment part 3"""
import pytest

from test_3 import sum_current_time


@pytest.mark.parametrize("test_input,expected",
    [
        ("12:03:58", "73"),
        ("18:04:05", "27"),
        ("00:00:00", "0")
    ])
def test_time_is_added(test_input, expected):
    """Tests for multiple valid inputs"""

    assert sum_current_time(test_input) == expected


@pytest.mark.parametrize("test_input,expected",
    [
        ("2:03:58",
         "Invalid time given, time should be in format 'HH:MM:SS' with no negative integers"), 
        ("1e:04:05",
         "Invalid time given, time should be in format 'HH:MM:SS' with no negative integers"), 
        ("00:-1:00",
         "Invalid time given, time should be in format 'HH:MM:SS' with no negative integers")
    ])
def test_invalid_times_given(test_input, expected):
    """Tests for multiple invalid inputs"""

    assert sum_current_time(test_input) == expected
