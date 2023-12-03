"""Tests for Take home assessment part 2"""
from unittest.mock import patch, MagicMock

from test_2 import find_valid_court, display_user_info


def test_get_nearest_desired_courts():
    """Tests all desired courts are found"""

    mock_get = MagicMock()

    mock_get.return_value.json.return_value = [
    {'name': 'Harrow Crown Court',
    'lat': 51.5938238213214,
    'lon': -0.339809325465158,
    'types': ['Crown Court'],
    'dx_number': 123,
    'distance': 23
    },
    {'name': 'Croydon Crown Court',
    'lat': 51.5938238213214,
    'lon': -0.339809325465158, 
    'types': ['Magistrates'],
    'dx_number': 456,
    'distance': 2},
    {'name': 'Brixton Tribunal',
    'lat': 51.5938238213214,
    'lon': -0.339809325465158,
    'types': ['Tribunal'],
    'dx_number': 789,
    'distance': 3}
    ]

    with patch('requests.get', mock_get):
        result = find_valid_court("CR26PG", "Tribunal")

    assert result == [
        {
        'name': 'Brixton Tribunal',
        'lat': 51.5938238213214, 'lon': -0.339809325465158,
        'types': ['Tribunal'],
        'dx_number': 789,
        'distance': 3
        }]


def test_displays_correctly():
    """Tests output for user is displayed correctly"""

    chosen_court = [{
        'name': 'Croydon Crown Court',
        'lat': 51.5938238213214,
        'lon': -0.339809325465158,
        'types': ['Magistrates'],
        'dx_number': 456,
        'distance': 2
        }]
    assert display_user_info(chosen_court, "Kayode", "SE193SH", "Magistrates") == (
    """
    Persons Name: Kayode
    Desired Court Type: Magistrates
    Home Postcode: SE193SH
    Nearest court of right type: Croydon Crown Court
    Dx_Number: 456
    Court Distance: 2 miles
    """
    )


def test_displays_correctly_no_dx():
    """Tests output for user is displayed correctly when no dx number"""

    chosen_court = [{
        'name': 'Croydon Crown Court',
        'lat': 51.5938238213214, 
        'lon': -0.339809325465158, 
        'types': ['Magistrates'], 
        'distance': 2}]

    assert display_user_info(chosen_court, "Kayode", "SE193SH", "Magistrates") == (
    """
    Persons Name: Kayode
    Desired Court Type: Magistrates
    Home Postcode: SE193SH
    Nearest court of right type: Croydon Crown Court
    Dx_Number: Dx number not found
    Court Distance: 2 miles
    """
    )


def test_no_court_found():
    """Tests output when no court is found"""

    chosen_court = []
    assert display_user_info(chosen_court, "Kayode", "SE193SH", "Magistrates") == (
        "Sorry, a Magistrates could be found for Kayode near SE193SH"
    )
