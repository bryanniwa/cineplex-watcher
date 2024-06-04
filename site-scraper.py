from datetime import datetime
from time import sleep

import requests

from config import FILM_ID, GMAIL_ADDRESS, GMAIL_PASSWORD, LOCATION_ID, SCREENING_DATE
from lib.send_email import Emailer


def get_time():
    return datetime.now().strftime("%H:%M:%S")


emailer = Emailer(GMAIL_ADDRESS, GMAIL_PASSWORD)

try:
    while True:
        r = requests.get(
            f"https://cineplex.com/api/v1/showtimes?language=en&locationId={LOCATION_ID}&date={SCREENING_DATE}&filmId={FILM_ID}"
        )

        if r.status_code != 200:
            print("Failed to get data:", r.status_code)

        data = r.json()["data"]
        if len(data) == 0:
            time = get_time()
            print(f"{time}: No showtimes found")
        else:
            time = get_time()
            print(f"{time}: Showtimes found!")
            emailer.send_success_email()
            break

        sleep(60 * 10)
except Exception as e:
    print("Error:", e)
    emailer.send_error_email(str(e))
    raise
