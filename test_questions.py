import datetime
import random
random.seed()

three_things = (
    ("car", "tree", "ball"),
    ("pencil", "moon", "shoe"),
    ("apple", "mountain", "watch"),
    ("flower", "book", "fridge"),
    ("guitar", "cloud", "spoon"),
    ("bird", "bottle", "chair"),
    ("lamp", "ocean", "hat"),
    ("computer", "banana", "door"),
    ("glass", "cat", "bridge"),
    ("phone", "sweater", "lake"),
    ("plate", "sky", "beach"),
    ("sandwich", "star", "key"),
    ("dog", "paper", "train"),
    ("pizza", "planet", "ring"),
    ("butterfly", "boot", "tower"),
    ("camera", "lemon", "bed"),
    ("song", "candle", "river"),
    ("grape", "pocket", "museum"),
    ("whistle", "island", "desk"),
    ("chocolate", "kite", "park")
)

reverse_words = ("APPLE","BIRD","DOG","FLOWER","GLASS","LAMP","PLATE","SONG","CAMERA","GLASS","PENCIL","CAR")

def get_season(month, day):
    if (month == 12 and day >= 21) or (month <= 2 and day <= 19):
        return "Winter"
    elif month <= 5 and day <= 20:
        return "Spring"
    elif month <= 8 and day <= 21:
        return "Summer"
    else:
        return "Fall"
    
def get_date_info():
    current_date = datetime.datetime.now()
    year = current_date.year
    month = current_date.month
    day = current_date.day
    day_of_week = current_date.strftime("%A")

    return {
        "Year": year,
        "Month": month,
        "Day": day,
        "DayOfWeek": day_of_week,
        "Season": get_season(month, day)
    }

def get_date_info_with_season():
    date_info = get_date_info()
    return date_info

# Example usage:
# date_info = get_date_info_with_season()
# print(date_info)

import requests

def get_location_info():
    try:
        response = requests.get("https://ipinfo.io/json")
        data = response.json()

        country = data.get("country", "Unknown")
        state = data.get("region", "Unknown")

        return {
            "Country": country,
            "State": state
        }
    except Exception as e:
        return {
            "Country": "Unknown",
            "State": "Unknown",
        }

# Example usage:
# location_info = get_location_info()
# print(location_info)

def get_random_thing():
    return random.choice(three_things)


