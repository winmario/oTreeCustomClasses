from importlib import import_module

from .class_parser import add

from otree.session import SESSION_CONFIGS_DICT

for session_config in SESSION_CONFIGS_DICT.values():
    app_name = session_config['name']
    dotted_path = app_name + '.models'
    try:
        module = import_module(dotted_path)
    except ImportError:
        continue

    dotted_path = app_name + '.player_classes'
    try:
        playerClasses = import_module(dotted_path)
    except ImportError:
        continue

    add(module.Player, playerClasses)