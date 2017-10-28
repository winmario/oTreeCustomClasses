from otree.api import models, widgets

######################################################################

""" Write your classes here! """
## Important formation as following
##
## class Classname
##      classnameAttributename = value
##      classnameAttributename = models.function()
##
## example

class StockMarket:
	#static
	stockMarketStatic = 20
	#dynamic
	stockMarketDynam = models.CharField()