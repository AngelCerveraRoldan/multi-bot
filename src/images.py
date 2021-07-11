from dotenv import load_dotenv

import os
import requests
import json

load_dotenv()
ACCESS_KEY = os.getenv('ACCESS_KEY')
SECRET_KEY = os.getenv('SECRET_KEY')

def get_photo(word, num=0):
    url = f'https://api.unsplash.com/search/photos/?query={word}&client_id={ACCESS_KEY}'
    response = requests.get(url)
    
    
    try:    
        image = response.json()['results'][num]['urls']['regular']
    except:
        image = response.json()['results'][0]['urls']['regular'] 


    return image

