"""Tests for Take home assessment part 1"""
from test_1 import is_log_line, get_dict

def test_input_is_a_log():
    """Tests input line is a valid log"""

    valid_input = "03/11/21 08:51:06 INFO    :...mailbox_register: mailbox allocated for timer"
    assert is_log_line(valid_input) is True


def test_input_is_invalid_log():
    """Tests response when input line is invalid log"""

    invalid_input = "03/11/21 08:51:06  :...mailbox_register: mailbox allocated for timer"
    assert is_log_line(invalid_input) is False


def test_log_is_correctly_converted():
    """Tests valid log converts to dictionary"""

    valid_log = "03/11/21 08:51:06 TRACE   :...read_physical_netif: Home list entries returned = 7"
    result = {
            "timestamp": "03/11/21 08:51:06",
            "log_level": "TRACE",
            "message": ":...read_physical_netif: Home list entries returned = 7",
        }

    assert get_dict(valid_log) == result
