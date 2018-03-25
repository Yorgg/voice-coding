from aenea import Choice, Grammar, MappingRule, Function

# Languages
from ruby import get_ruby_grammar
from javascript import get_javascript_grammar

generic_grammar = Grammar('generic')

language_map = {
    "ruby": get_ruby_grammar(), 
    "javascript": get_javascript_grammar()
}

def clear_mode():
    for _, grammar in language_map.iteritems():
        grammar.disable()

def switch_mode(language):
    clear_mode()
    language.enable()

basics_mapping =  {
    'lang <language>': Function(switch_mode),
    'clear lang': Function(clear_mode),
}

class Basics(MappingRule):
    mapping = basics_mapping
    extras = [
        Choice("language", language_map)
    ]

generic_grammar.add_rule(Basics())
generic_grammar.load()

# Start with no modes active
for _, grammar in language_map.iteritems():
    grammar.load()
    grammar.disable()

def unload():
    generic_grammar.unload()
    for _, grammar in language_map.iteritems():
         grammar.unload()



