from django.test import TestCase
from django.test.utils import override_settings
from recommendation.views import update_hero
from . import tasks
from mock import Mock, patch

class ViewsTestCase(TestCase):

    def testUpdateHero(self):
        request = ''
        with patch('recommendation.tasks.update_hero.delay') as patch_mock:
            response = update_hero(request)
            self.assertTrue(patch_mock.called)
        self.assertEqual(response.status_code, 200)