"""
Script provides a person the closest court they ask for according to a given postcode,
using Ministry of Justice API
"""
import csv
import requests


COURT_URL = "https://www.find-court-tribunal.service.gov.uk/search/results.json?postcode="
FETCH_TIMEOUT = 30
NO_DX_NUMBER = "Dx number not found"


def get_user_data() -> list[dict]:
    "Returns users information and requests from csv file"

    with open('people.csv', 'r', encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        return list(reader)


def find_valid_court(given_postcode: str, desired_court: str) -> list[dict]:
    "Returns courts from Ministry of Justice API, which are of desired type"

    try:
        response = requests.get(
            f"{COURT_URL}{given_postcode}", timeout=FETCH_TIMEOUT)
        response.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print("HTTP Error")
        print(err.args[0])

    court_info = response.json()
    valid_courts = [court for court in court_info if desired_court in court.get("types")]

    return valid_courts


def display_user_info(court: list, user_name: str, user_postcode: str, user_court_type: str) -> str:
    "Prints out output of chosen court and user information"

    if not court:
        return f"Sorry, a {user_court_type} could be found for {user_name} near {user_postcode}"

    nearest_court = court[0]
    dx_number = (nearest_court.get("dx_number") if nearest_court.get("dx_number")
                  else NO_DX_NUMBER)

    return f"""
    Persons Name: {user_name}
    Desired Court Type: {user_court_type}
    Home Postcode: {user_postcode}
    Nearest court of right type: {nearest_court.get("name")}
    Dx_Number: {dx_number}
    Court Distance: {nearest_court.get("distance")} miles
    """


if __name__ == "__main__":

    data = get_user_data()
    for user in data:
        name = user.get("person_name")
        postcode = user.get("home_postcode")
        court_type = user.get("looking_for_court_type")

        chosen_courts = find_valid_court(postcode, court_type)
        print(display_user_info(chosen_courts, name, postcode, court_type))
