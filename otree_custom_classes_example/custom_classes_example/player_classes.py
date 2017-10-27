from .models import Player


class SurveyPlayer(Player):
	pass


class MarketPlayer(Player):
	pass


all_player_classes = [
	SurveyPlayer,
	MarketPlayer,
]