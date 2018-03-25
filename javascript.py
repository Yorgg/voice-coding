from aenea import Grammar, Key, MappingRule, Choice, Function, Text, Integer, CompoundRule, Dictation
from utilities import EscapeInsertRule 
from utilities import EscapeNewLineRule 

from time import sleep
from aenea.proxy_contexts import ProxyAppContext
from _generic import pressKeyMap
from formats import (
    pascal_case_text,
    camel_case_text
)

###helpers
location_on_host = '~/projects/aenea-grammar/javascript.py'
jump = Key('squote, squote')

def _esc():
    Key("escape").execute()
    sleep(0.06)  

def _const_assign(text=""):
    Key("c, o, n, s, t, space").execute()
    if (text != ""):
        camel_case_text(text)
    Text(' = ').execute()

def _let_assign(text=""):
    Key("l, e, t, space").execute()
    if (text != ""):
        camel_case_text(text)
    Text(' = ').execute()

def _func(text=""):
    Text('function ').execute()
    camel_case_text(text) 
    Text('() {').execute()
    Key('enter').execute()
    Key('rbrace').execute()

    _esc()

    if (text == ""):
	Key('k, s-4, h, h, h, i').execute()
    else: 
	Key('k, o').execute()

def _class(text2="", text=""):
    Key('c, l, a, s, s, space').execute()
    pascal_case_text(text)

    if (text2):
        Key('space').execute()
        Text('extends ').execute()
        pascal_case_text(text2)
        Key('space').execute()

    _esc()
    Key('s-4, a, space, lbrace, enter, rbrace').execute()
    _esc()

    if (text == ""):
	Key('k, s-4, h, h, a').execute()
    else: 
	Key('k, o').execute()


def _arrow_fnc_one_line():
    text = '() => '
    Text(text).execute()
    _esc()
    Key('s-f, lparen, a').execute()

def _arrow_fnc():
    _arrow_fnc_one_line()
    _esc()
    Key('s-4, a, lbrace, enter, rbrace').execute()
    _esc()
    Key('k, s-f, lparen, a').execute()


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

class JavascriptRuleAppend(EscapeInsertRule):
    mapping = { 
        'con <text>': Function(_const_assign),
        'let <text>': Function(_let_assign),
	'air lie': Function(_arrow_fnc_one_line),
	'air': Function(_arrow_fnc),
	'funk [<text>]': Function(_func),
    }
    extras = extras
    defaults = defaults

class JavascriptNewLineRule(EscapeNewLineRule):
    mapping = {
	 'class [<text>] [parent <text2>]': Function(_class),
    }
    extras = extras
    defaults = defaults

def get_javascript_grammar():
    grammar = Grammar('Javascript')
    grammar.add_rule(JavascriptNewLineRule())
    grammar.add_rule(JavascriptRuleAppend())
    return grammar

