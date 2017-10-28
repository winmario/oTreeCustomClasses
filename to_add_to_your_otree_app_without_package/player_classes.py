from otree.api import models, widgets
import sys
import inspect

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

######################################################################

""" Don't do something here... """
def add(playerClass):
	for name, clazz in inspect.getmembers(sys.modules[__name__], inspect.isclass):
		for name, attr in inspect.getmembers(clazz):
			if not name.startswith('_'):
				# https://stackoverflow.com/questions/2357528/explanation-of-contribute-to-class
				if hasattr(attr, 'contribute_to_class'):
					attr.contribute_to_class(playerClass, name)
				else:
					setattr(playerClass, name, attr)