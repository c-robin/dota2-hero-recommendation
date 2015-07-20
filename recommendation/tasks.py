from __future__ import absolute_import

from celery import shared_task
from recommendation.models import Hero
import requests

@shared_task
def logger():
    with open("hello.txt", "w") as f:
        f.write("Hello World")
        
@shared_task
def update_hero():
    execfile("config.py", config)
    api_key = config['API_KEY']
    url = 'https://api.steampowered.com/IEconDOTA2_570/GetHeroes/v0001/?key='+ api_key+'&language=en_us'
    r = requests.get(url, timeout=None, proxies = None)
    json_heroes = json.loads(r)
    
    for hero in json_heroes['result']['heores']:
        try:
            Hero.objects.get(dota2_hero_id=hero['id'])
        except ObjectDoesNotExist:
            Hero.objects.create(dota2_hero_id=hero['id'], name=hero['localized_name'])