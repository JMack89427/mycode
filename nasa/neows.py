#!/usr/bin/python3
import requests
from datetime import datetime
import pprint

## Define NEOW URL
NEOURL = "https://api.nasa.gov/neo/rest/v1/feed?"

# this function grabs our credentials
def returncreds():
    ## first I want to grab my credentials
    with open("/home/student/nasa.creds", "r") as mycreds:
        nasacreds = mycreds.read()
    ## remove any newline characters from the api_key
    nasacreds = "api_key=" + nasacreds.strip("\n")
    return nasacreds

# this function validates the date format
def validate_date(date_text):
    try:
        datetime.strptime(date_text, "%Y-%m-%d")
        return True
    except ValueError:
        return False

# this is our main function
def main():
    ## first grab credentials
    nasacreds = returncreds()

    ## prompt the user for a start date and validate it
    while True:
        user_start_date = input("Enter the start date (YYYY-MM-DD): ")
        if validate_date(user_start_date):
            break
        else:
            print("Invalid date format. Please enter the date in YYYY-MM-DD format.")
    startdate = f"start_date={user_start_date}"

    ## prompt the user for an optional end date and validate it if provided
    user_end_date = input("Enter the end date (YYYY-MM-DD) or press Enter to skip: ")
    if user_end_date:
        while not validate_date(user_end_date):
            print("Invalid date format. Please enter the date in YYYY-MM-DD format.")
            user_end_date = input("Enter the end date (YYYY-MM-DD) or press Enter to skip: ")
        enddate = f"&end_date={user_end_date}"
    else:
        enddate = ""  # no end date parameter if skipped

    ## make a request with the request library
    neowrequest = requests.get(NEOURL + startdate + enddate + "&" + nasacreds)

    # strip off json attachment from our response
    neodata = neowrequest.json()

    ## display NASAs NEOW data
    pprint.pprint(neodata)

if __name__ == "__main__":
    main()
