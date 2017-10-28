import sys
import inspect

""" Don't do something here... """
# getting all the attributes out of player_classes.py
def add(playerClass, playerClasses):
	for name, clazz in inspect.getmembers(playerClasses, inspect.isclass):
		for name, attr in inspect.getmembers(clazz):
			if not name.startswith('_'):
				# https://stackoverflow.com/questions/2357528/explanation-of-contribute-to-class
				if hasattr(attr, 'contribute_to_class'):
					attr.contribute_to_class(playerClass, name)
				else:
					setattr(playerClass, name, attr)
