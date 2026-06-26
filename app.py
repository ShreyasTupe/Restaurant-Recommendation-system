
import pandas as pd

restaurants = [
    {"name":"Spice Garden","cuisine":"Indian","rating":4.5,"distance":2},
    {"name":"Pizza Hub","cuisine":"Italian","rating":4.2,"distance":5},
    {"name":"Sushi World","cuisine":"Japanese","rating":4.8,"distance":8},
]

def recommend(cuisine):
    results = [r for r in restaurants if r["cuisine"].lower()==cuisine.lower()]
    return sorted(results, key=lambda x:(-x["rating"], x["distance"]))

if __name__ == "__main__":
    pref = input("Enter preferred cuisine: ")
    print(recommend(pref))
