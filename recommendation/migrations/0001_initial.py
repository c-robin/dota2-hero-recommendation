# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Duel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hero1_victory', models.IntegerField()),
                ('hero2_victory', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Hero',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dota2_hero_id', models.IntegerField(unique=True)),
                ('name', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team1_victory', models.IntegerField()),
                ('team2_victory', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hero1', models.ForeignKey(related_name='hero_team_1', to='recommendation.Hero')),
                ('hero2', models.ForeignKey(related_name='hero_team_2', to='recommendation.Hero')),
                ('hero3', models.ForeignKey(related_name='hero_team_3', to='recommendation.Hero')),
                ('hero4', models.ForeignKey(related_name='hero_team_4', to='recommendation.Hero')),
                ('hero5', models.ForeignKey(related_name='hero_team_5', to='recommendation.Hero')),
            ],
        ),
        migrations.AddField(
            model_name='match',
            name='team1',
            field=models.ForeignKey(related_name='team1', to='recommendation.Team'),
        ),
        migrations.AddField(
            model_name='match',
            name='team2',
            field=models.ForeignKey(related_name='team2', to='recommendation.Team'),
        ),
        migrations.AddField(
            model_name='duel',
            name='hero1',
            field=models.ForeignKey(related_name='hero_duel_1', to='recommendation.Hero'),
        ),
        migrations.AddField(
            model_name='duel',
            name='hero2',
            field=models.ForeignKey(related_name='hero_duel_2', to='recommendation.Hero'),
        ),
    ]
