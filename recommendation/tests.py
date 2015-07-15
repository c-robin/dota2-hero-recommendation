from django.test import TestCase
from recommendation.models import Hero
from recommendation.models import Duel
from recommendation.models import Team
from recommendation.models import Match

# Create your tests here.

class ModelTestCase(TestCase):
    def setUp(self):
        Hero.objects.create(dota2_hero_id="1", name="antimage")
        Hero.objects.create(dota2_hero_id="30", name="witch_doctor")
        Hero.objects.create(dota2_hero_id="46", name="templar_assassin")
        Hero.objects.create(dota2_hero_id="49", name="dragon_knight")
        Hero.objects.create(dota2_hero_id="69", name="bounty_hunter")
        
    def test_hero_str(self):
        antimage = Hero.objects.get(dota2_hero_id="1")
        self.assertEqual(str(antimage), 'antimage')

    def test_duel_str(self):
        am = Hero.objects.get(dota2_hero_id="1")
        bh = Hero.objects.get(dota2_hero_id="69")
        duel = Duel.objects.create(hero1=am, hero2=bh, hero1_victory=0, hero2_victory=2)
        self.assertEqual(str(duel), 'antimage - bounty_hunter : 0 - 2')

    def test_team_str(self):
        am = Hero.objects.get(dota2_hero_id="1")
        wd = Hero.objects.get(dota2_hero_id="30")
        ta = Hero.objects.get(dota2_hero_id="46")
        dk = Hero.objects.get(dota2_hero_id="49")
        bh = Hero.objects.get(dota2_hero_id="69")
        team = Team.objects.create(hero1=am, hero2=wd, hero3=ta, hero4=dk, hero5=bh)
        self.assertEqual(str(team), 'antimage witch_doctor templar_assassin dragon_knight bounty_hunter')
        
    def test_match_str(self):
        am = Hero.objects.get(dota2_hero_id="1")
        wd = Hero.objects.get(dota2_hero_id="30")
        ta = Hero.objects.get(dota2_hero_id="46")
        dk = Hero.objects.get(dota2_hero_id="49")
        bh = Hero.objects.get(dota2_hero_id="69")
        team = Team.objects.create(hero1=am, hero2=wd, hero3=ta, hero4=dk, hero5=bh)
        match = Match.objects.create(team1=team, team2=team, team1_victory=0, team2_victory=2)
        self.assertEqual(str(match), 'antimage witch_doctor templar_assassin dragon_knight bounty_hunter - antimage witch_doctor templar_assassin dragon_knight bounty_hunter : 0 - 2')