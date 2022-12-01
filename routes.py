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
     YELP_API_KEY = os.getenv('YELP_API_KEY')
    # print(YELP_API_KEY, file=sys.stderr)
     YELP_API_BASE_URL = 'https://api.yelp.com/v3'
     YELP_BUISNESS_URL = '/businesses/search'
     YELP_BUISNESS_SEARCH_URL='https://api.yelp.com/v3/businesses/search?term=tacos&latitude=29.88889&longitude=-97.93889'
     headers = {
        'Authorization': f'Bearer {YELP_API_KEY}',
        'Content-Type': 'application/json'
     }
     url_params = {'Authorization': f'Bearer {YELP_API_KEY}'}
     response = requests.get(YELP_BUISNESS_SEARCH_URL, headers=headers, params=url_params)

     data = response.json()
     pretty_json_data = json.dumps(data, indent=4, sort_keys=True)
     #print(pretty_json_data)

     for index in range(20):   ###MAX IS 20 WE SHOULD PROB DO LESS THO
      arr_names[index] = data['businesses'][index]['name']
      arr_urls[index] = data['businesses'][index]['url']
      arr_ratings[index] = data['businesses'][index]['rating']
      print("\n")

     for i in range(20):
      print(arr_names[i] + arr_urls[i] + str(arr_ratings[i]))
     
     return render_template("index.html")

app.run(debug=True)