from aenea import Grammar, Key, MappingRule, Choice, Function, Text, Integer, CompoundRule, Dictation
from utilities import EscapeInsertRule 
from utilities import EscapeNewLineRule 

from time import sleep
from aenea.proxy_contexts import ProxyAppContext
from _generic import pressKeyMap
from format import (
    pascal_case_text,
    snake_case_text
)

###helpers
location_on_host = '~/projects/aenea-grammar/_vim.py'
jump = Key('squote, squote')

def _esc():
    Key("escape").execute()
    sleep(0.06)  

def _call_implicit(text=""):
    snake_case_text(text) 
    Key("lparen, rparen").execute()
    _esc()
    if (text == ""):
        Key('h, i').execute()
    else:
        Key('i').execute()

def _call(text=""):
    Key("dot").execute() 
    _call_implicit(text)

def _instance(text2="", text=""):
    Key('at').execute()
    snake_case_text(text)
    Key('space, equal, space').execute()
    if (text2):
        snake_case_text(text2)
        Key('o').execute()

def _class(text2="", text=""):
    Key('c, l, a, s, s, space').execute()
    pascal_case_text(text)

    if (text2):
        Key('space, langle, space').execute()
        pascal_case_text(text2)

    Key('enter').execute()
    Key('e, n, d').execute()
    _esc()

    if (text == ""):
	Key('k, s-4, a').execute()
    else: 
	Key('k, o').execute()

def _block_one_line(method):
   def func():
        text = method + " {|| }"
        Text(text).execute()
        _esc()
        Key('h, h, i').execute()
   return func

def _block(method):
    def func():
        text = method + " do ||"
        Text(text).execute()
        Key('enter, e, n, d').execute()
        _esc()
        Key('k, s-4, h, a').execute()
    return func

def _method(text=""):
    Key('d, e, f, space').execute()
    snake_case_text(text)
    Key('lparen, rparen, enter').execute()
    Key('e, n, d').execute()
    _esc()
    if (text == ""):
	Key('k, s-4, h, a').execute()
    else: 
	Key('k, f, lparen, a').execute()

###

        
extras = [
    Integer("n", 0, 9999),
    Integer("n2", 0, 9999),
    Dictation('text'),
    Dictation('text2'),
    Choice("pressKey", pressKeyMap),
]

defaults = {
    "n": 1,
    "n2": 1,
}

class RubyRuleAppend(EscapeInsertRule):
    mapping = { 
        'sap': Function(_block_one_line(".map")),
        'map': Function(_block(".map")),
        'funk [<text>]': Function(_call),
        'punk [<text>]': Function(_call_implicit)
    }
    extras = extras
    defaults = defaults

class RubyNewLineRule(EscapeNewLineRule):
    mapping = {
	 'meth [<text>]': Function(_method),
	 'class [<text>] [parent <text2>]': Function(_class),
	 'ins [<text>] [nine <text2>]': Function(_instance),
    }
    extras = extras
    defaults = defaults

grammar = Grammar('ruby')
grammar.add_rule(RubyNewLineRule())
grammar.add_rule(RubyRuleAppend())
grammar.load()

def unload():
    global grammar
    if grammar:
        grammar.unload()
    grammar = None


