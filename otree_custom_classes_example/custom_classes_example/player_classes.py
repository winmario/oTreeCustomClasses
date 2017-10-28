from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

class StockMarket:

	#static
	stockMarketStatic = 20

	#dynmaic
	stockMarketDynam = models.CharField()

	all_stockMarket_attributes = [
		stockMarketStatic,
		stockMarketDynam
	]

all_player_classes = [
	StockMarket
]