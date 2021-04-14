"""
Script that scrapes Trim dining hall at Babson and prints food + calories as strings

Note: can only run each period before specific meal period, or else error is raised
"""
import time
from datetime import date
import random
import requests
import json

class Food: 
    """
    class Food, where attributes name, id and calories are string, and nutrients and filters are lists of strings
    """
    def __init__(self, id, name, ingredients="", nutrients=[], filters=[], calories=""):
        self.id = id
        self.name = name
        self.ingredients = ingredients
        self.nutrients = nutrients
        self.filters = filters
        self.calories = calories
    def __str__(self):
        return '{self.name} has {self.calories} calories'.format(self=self)

def getPeriod(period=None):
    """
    gets the period path for the meal period that is passed as a string parameter. returns period path as a string.
    """
    headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9',
    'Host': 'api.dineoncampus.com',
    'Origin': 'https://dineoncampus.com',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'
    }
    today = date.today()
    url = "https://api.dineoncampus.com/v1/location/5880da183191a21e8af61adc/periods/607505c13a585b19a5fed9b5?platform=0&date=" + str(today)
    response = requests.get(url, headers=headers) # send request with headers
    json_data = json.loads(response.text) # decode json that is returned into parsable dictionary
    # return the period id for each of the meal periods
    if period.lower() == "breakfast":
        for item in json_data['periods']:
            if item['name'] == 'Breakfast':
                return item['id']
    elif period.lower() == "lunch":
        for item in json_data['periods']:
            if item['name'] == 'Lunch':
                return item['id']
    elif period.lower() == "dinner":
        for item in json_data['periods']:
            if item['name'] == 'Dinner':
                return item['id']
    else:
        print("no period selected") # or we could raise exception actually


def getFoodItems(periodID):
    """
    returns a list of Food objects given the periodID parameter that is returned from getPeriod(). 
    """
    headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9',
    'Host': 'api.dineoncampus.com',
    'Origin': 'https://dineoncampus.com',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'
    }
    today = date.today()
    url = "https://api.dineoncampus.com/v1/location/5880da183191a21e8af61adc/periods/" + periodID + "?platform=0&date=" + str(today)

    response = requests.get(url, headers=headers) # send request wuth headers
    #print(response.text)
    json_data = json.loads(response.text) # decode json
    #print(json_data)
    if json_data["status"] != "success":
        raise Exception("Status not successful") # raise exception if status returned is not successful

    bfList = []
    for category in json_data['menu']['periods']['categories']:
        for foodName in category['items']: # assign attributes to each food item on the menu
            nutrients = [dict["name"] + ":" + dict["value"] + "(" + dict["uom"] + ")" for dict in foodName['nutrients']]
            filters = [dict["type"] + ":" + dict["name"] for dict in foodName['filters']]
            bfList.append(Food(foodName['id'], foodName['name'], nutrients=nutrients, ingredients=foodName['ingredients'], filters= filters, calories=foodName['calories']))

    print(len(bfList))
    #for item in bfList:
        #print(str(item))
        #pass
    #print(bfList[0].nutrients)
    #print(bfList[0].ingredients)
    #print(bfList[0].filters)
    return bfList



if __name__ == '__main__':
    #getBreakfast()
    getFoodItems(getPeriod("dinner"))
