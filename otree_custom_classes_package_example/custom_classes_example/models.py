from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

author = 'Mario Winkler'

doc = """
An easy survey for checking some simple economic questions.
"""


class Constants(BaseConstants):
    name_in_url = 'simple_survey'
    players_per_group = 2
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
	pass