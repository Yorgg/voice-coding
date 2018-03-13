from aenea import Grammar, MappingRule, Integer, Key, Text
grammar = Grammar('tmux')

LEADER = 'c-b'

class Command(MappingRule):
    mapping = {
        'switch window [<n>]': Key(LEADER + ', ' + '%(n)s')
    }
    extras   = [
        Integer("n", 0, 10),
    ]
    defaults = {
        "n": 1,
    }

grammar.add_rule(Command())
grammar.load()

def unload():
    global grammar
    if grammar:
        grammar.unload()
    grammar = None

