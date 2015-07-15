from django.db import models

# Create your models here.


class Hero(models.Model):
	dota2_hero_id = models.IntegerField(unique=True)
	name = models.CharField(max_length=25)

	def __str__(self):
		return self.name

class Duel(models.Model):
	hero1 = models.ForeignKey('Hero', related_name="hero_duel_1")
	hero2 = models.ForeignKey('Hero', related_name="hero_duel_2")
	hero1_victory = models.IntegerField()
	hero2_victory = models.IntegerField()
	
	def __str__(self):
		return str(self.hero1) + " - " + str(self.hero2) + " : " + str(self.hero1_victory) + " - "+  str(self.hero2_victory)
		
class Team(models.Model):
	hero1 = models.ForeignKey('Hero', related_name="hero_team_1")
	hero2 = models.ForeignKey('Hero', related_name="hero_team_2")
	hero3 = models.ForeignKey('Hero', related_name="hero_team_3")
	hero4 = models.ForeignKey('Hero', related_name="hero_team_4")
	hero5 = models.ForeignKey('Hero', related_name="hero_team_5")

	def __str__(self):
		heroes = [self.hero1, self.hero2, self.hero3, self.hero4, self.hero5]
		return " ".join(map(lambda x:str(x), heroes))
		
class Match(models.Model):
	team1 = models.ForeignKey('Team', related_name="team1")
	team2 = models.ForeignKey('Team', related_name="team2")
	team1_victory = models.IntegerField()
	team2_victory = models.IntegerField()

	def __str__(self):
		return str(self.team1) + " - " + str(self.team2) + " : " + str(self.team1_victory) + " - "+  str(self.team2_victory)