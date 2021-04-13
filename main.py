"""
Script that scrapes Trim dining hall at Babson and prints food + calories as strings
"""
import time
from datetime import date
import random
import requests
import json

class Food: #TODO: make the right attributes, ie ingredients and nutrients (which can be a dict), and filters (vegetarian, vegan etc)
    def __init__(self, id, name, type="", allergens="", calories=""):
        self.id = id
        self.name = name
        self.type = type
        self.allergens = allergens
        self.calories = calories
    def __str__(self):
        return '{self.name} has {self.calories} calories'.format(self=self)


def getBreakfast():
    headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9',
    'Host': 'api.dineoncampus.com',
    'Origin': 'https://dineoncampus.com',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'
    }
    today = date.today()
    bf = "https://api.dineoncampus.com/v1/location/5880da183191a21e8af61adc/periods/607505c13a585b19a5fed9b5?platform=0&date=2021-4-13"
    # bf somehow returns json with all the ids for every meal period, could be useful
    # the id is then plugged into .../periods/:id?platform=0...
    # not sure if id changes or something
    # once that is figured out we can concatenate today to the end -> &date=" + today

    response = requests.get("https://api.dineoncampus.com/v1/location/5880da183191a21e8af61adc/periods/6075221e5e42ad1ff3422dcb?platform=0&date=2021-4-13", headers=headers)
    #print(response.text)
    json_data = json.loads(response.text)
    #print(json_data)
    print(json_data["status"])


    bfList = []
    for category in json_data['menu']['periods']['categories']:
        for foodName in category['items']:
            bfList.append(Food(foodName['id'], foodName['name'], calories=foodName['calories'])) # append ingredients also
            # TODO: iterate through nutrients
            # for nutrients in foodName['nutrients']:
            # TODO: iterate through filters
            # for filters in foodName['filters']:
    print(len(bfList))
    for item in bfList:
        print(str(item))


def getLunch():
    lunch = "https://api.dineoncampus.com/v1/location/5880da183191a21e8af61adc/periods/607505c13a585b19a5fed9bf?platform=0&date=2021-4-13"
    pass
def getDinner():
    dinner = "https://api.dineoncampus.com/v1/location/5880da183191a21e8af61adc/periods/607505c13a585b19a5fed9b8?platform=0&date=2021-4-13"
    pass
if __name__ == '__main__':
    getBreakfast()
