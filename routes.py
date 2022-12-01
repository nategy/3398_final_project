from flask import Flask, render_template, request
from dotenv import load_dotenv, find_dotenv
import os
import sys
import requests
import json

load_dotenv(find_dotenv())

app = Flask(__name__)

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
     data_object = data
     #the below returns the name of the first business
     data_list = data_object['businesses'][1]['name']
     print(data_list, file=sys.stderr)
     return render_template("index.html")
     #return data

if __name__ == "__main__":
   app.run(debug=True) 