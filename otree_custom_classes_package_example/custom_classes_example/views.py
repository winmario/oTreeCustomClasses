from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants

class Survey(Page):
    form_model = models.Player
    form_fields = ['stockMarketDynam']

    def vars_for_template(self):
        return {'stockMarketStatic': models.Player.stockMarketStatic}


class Results(Page):
    pass

page_sequence = [
    Survey,
    Results
]
