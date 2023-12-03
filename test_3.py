"""Function which sums the numbers of time separators"""
# The below function doesn't work correctly. It should sum all the numbers at the
# current time. For example, 01:02:03 should return 6. Improve and fix the function,
# and write unit test(s) for it. Use any testing framework you're familiar with.


def sum_current_time(time_str: str) -> int:
    """Sums the hour, minute and seconds from a given time in the format HH:MM:SS"""
    split_time = time_str.split(":")
    return sum(int(time) for time in split_time)


if __name__ == "__main__":
    print(sum_current_time("12:03:58"))
