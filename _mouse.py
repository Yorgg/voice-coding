from aenea import Grammar, Mouse, MappingRule

grammar = Grammar('mouse')

class MouseClickRule(MappingRule):
    mapping = {
        'tick': Mouse('left'),
	'tee tick': Mouse('left:2'),
	'tick ra': Mouse('right'),
    }

grammar.add_rule(MouseClickRule())

def unload():
    global grammar
    if grammar:
        grammar.unload()
    grammar = None

grammar.load()
