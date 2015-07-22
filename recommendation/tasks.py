from __future__ import absolute_import

import requests
import subprocess
import json

from django.core.exceptions import ObjectDoesNotExist
from recommendation.models import Hero

from celery import shared_task

@shared_task
def logger():
    with open("hello.txt", "w") as f:
        f.write("Hello World")
        
@shared_task
def update_hero():
    config = {}
    with open("config.py") as f:
        code = compile(f.read(), "config.py", 'exec')
        exec(code, config)
    api_key = config['API_KEY']
    url = 'https://api.steampowered.com/IEconDOTA2_570/GetHeroes/v0001/?key='+ api_key+'&language=en_us'
    json_heroes = json.loads(get_json(url))
    
    for hero in json_heroes['result']['heroes']:
        try:
            Hero.objects.get(dota2_hero_id=hero['id'])
        except ObjectDoesNotExist:
            Hero.objects.create(dota2_hero_id=hero['id'], name=hero['localized_name'])
            
def get_json(url):
    r = requests.get(url, timeout=None, proxies = None)
    return r.text
    