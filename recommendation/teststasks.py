from django.test import TestCase
from django.test.utils import override_settings
from recommendation.tasks import update_hero

from recommendation.models import Hero
from recommendation.models import Duel
from recommendation.models import Team
from recommendation.models import Match

import responses

class TasksTestCase(TestCase):

    def setUp(self):
        pass
     
    @override_settings(CELERY_ALWAYS_EAGER=True, TEST_RUNNER = 'djcelery.contrib.test_runner.CeleryTestSuiteRunner')
    def testUpdateHero(self):
        config = {}
        with open("config.py") as f:
            code = compile(f.read(), "config.py", 'exec')
            exec(code, config)
        api_key = config['API_KEY']   
        responses.add(**{
            'method'         : responses.GET,
            'url'            : 'https://api.steampowered.com/IEconDOTA2_570/GetHeroes/v0001/?key='+ api_key+'&language=en_us',
            'body'           : '{"result": {"heroes": [{"name": "npc_dota_hero_antimage","id": 1,"localized_name": "Anti-Mage"},{"name": "npc_dota_hero_axe","id": 2,"localized_name": "Axe"}]}},',
            'status'         : 200,
            'content_type'   : 'application/json'
        })
        result = update_hero.delay()
        self.assertTrue(result.successful())