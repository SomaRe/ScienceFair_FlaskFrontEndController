import datetime
import random
import requests

def get_three_things():
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
    return random.choice(three_things)

def get_reverse_word():
    reverse_words = ("APPLE","BIRD","DOG","FLOWER","GLASS","LAMP","PLATE","SONG","CAMERA","GLASS","PENCIL","CAR")
    return random.choice(reverse_words)

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

def get_image_link():
    image_links = {"wrist watch" : "https://i.pinimg.com/736x/11/13/0a/11130ac9de99eae78af686a9742a15e3.jpg",
                "airplane": 'https://thumbs.dreamstime.com/b/airplane-18327587.jpg',
                "car": 'https://vehicle-images.dealerinspire.com/stock-images/chrome/d51929e056d69529c5bf44c4ceaddf7e.png',
                }
    return random.choice(list(image_links.items()))
    
def get_words_to_click():
    words = ['hello', 'good', 'new', 'happy', 'beautiful']
    # return two random words
    return random.sample(words, 2)

def get_random_time():
    hour = random.randint(1, 12)
    minute = random.choice(range(0, 60, 5))
    return { "hour": hour, "minute": minute }


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


