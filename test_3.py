"""Function which sums the numbers of time separators"""
# The below function doesn't work correctly. It should sum all the numbers at the
# current time. For example, 01:02:03 should return 6. Improve and fix the function,
# and write unit test(s) for it. Use any testing framework you're familiar with.
TIME_FORMAT_LENGTH = 2

def sum_current_time(time_str: str) -> str:
    """Sums the hour, minute and seconds from a given time in the format HH:MM:SS"""

    split_time = time_str.split(":")

    invalid_time = any(
        not time.isnumeric() or len(time) != TIME_FORMAT_LENGTH for time in split_time)
    if invalid_time:
        return "Invalid time given, time should be in format 'HH:MM:SS' with no negative integers"
    return str(sum(int(time) for time in split_time))


if __name__ == "__main__":
    print(sum_current_time("12:03:58"))
