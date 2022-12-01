import random
from flask import Flask, render_template, request
from dotenv import load_dotenv, find_dotenv
import os
import sys
import requests
import json

load_dotenv(find_dotenv())

app = Flask(__name__)

arr_names = {}
arr_urls = {}
arr_ratings = {}

@app.route('/')
def home():
     foods = ["tacos", "deli", "pizza", "wings", "sandwiches", "burgers", "pasta", "salad"]
     foodtype = random.randint(0, 7)
     rand_food = foods[foodtype]
     YELP_API_KEY = os.getenv('YELP_API_KEY')
     YELP_API_BASE_URL = 'https://api.yelp.com/v3'
     YELP_BUISNESS_URL = '/businesses/search'
     YELP_BUISNESS_SEARCH_URL= f'https://api.yelp.com/v3/businesses/search?term={rand_food}&latitude=29.88889&longitude=-97.93889'
     headers = {
        'Authorization': f'Bearer {YELP_API_KEY}',
        'Content-Type': 'application/json'
     }
     url_params = {'Authorization': f'Bearer {YELP_API_KEY}'}
     response = requests.get(YELP_BUISNESS_SEARCH_URL, headers=headers, params=url_params)

     data = response.json()

     for index in range(20):
        arr_names[index] = data['businesses'][index]['name']
        arr_urls[index] = data['businesses'][index]['image_url']
        arr_ratings[index] = data['businesses'][index]['rating']
     i = random.randint(0, 19)
     name = arr_names[i]
     img_url = arr_urls[i]
     rating = arr_ratings[i]
     
     return render_template("index.html", name=name, img_url=img_url, rating=rating)

