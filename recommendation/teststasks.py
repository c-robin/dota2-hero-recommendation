from django.test import TestCase
from django.test.utils import override_settings
from recommendation.tasks import update_hero

from recommendation.models import Hero
from recommendation.models import Duel
from recommendation.models import Team
from recommendation.models import Match

import requests_mock

class TasksTestCase(TestCase):

    def setUp(self):
        pass
     
    @override_settings(CELERY_ALWAYS_EAGER=True, TEST_RUNNER = 'djcelery.contrib.test_runner.CeleryTestSuiteRunner')
    @requests_mock.mock()
    def testUpdateHero(self, m):
        m.get(requests_mock.ANY, text='{"result": {"heroes": [{"name": "npc_dota_hero_antimage","id": 1,"localized_name": "Anti-Mage"},{"name": "npc_dota_hero_axe","id": 2,"localized_name": "Axe"}]}}')
        result = update_hero.delay()
        self.assertEqual(str(Hero.objects.get(dota2_hero_id="1")), "Anti-Mage")
        self.assertEqual(str(Hero.objects.get(dota2_hero_id="2")), "Axe")