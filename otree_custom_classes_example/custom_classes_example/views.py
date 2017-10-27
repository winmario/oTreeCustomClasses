from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants
from . import player_classes

class Survey(Page):
    form_model = models.Player
    form_fields = [ 'name', 'age' ]


def PlayerPage(playerClass):

	class _PlayerPage(Page):

		def is_displayed(self):
			return self.role() == playerClass.__name__

	return _PlayerPage


class Results(Page):
    pass


player_pages = [PlayerPage(clazz) for clazz in player_classes.all_player_classes]
page_sequence = player_pages + [
    Results
]
