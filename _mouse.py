from aenea import Grammar, Mouse, MappingRule, Integer
grammar = Grammar('mouse')

class MouseClickRule(MappingRule):
    mapping = {
        'vee box': Mouse('<1829, 304>, left'), #temporary
        'host': Mouse('<0, 304>, left'), #temporary
        'tick': Mouse('left'),
	'tick ra': Mouse('right'),
    }
    extras = [
	Integer("n", 0, 9999),
    ]

grammar.add_rule(MouseClickRule())

def unload():
    global grammar
    if grammar:
        grammar.unload()
    grammar = None

grammar.load()
