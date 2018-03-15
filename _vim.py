from aenea import Grammar, Key, MappingRule, Choice, Function, Text, Integer, CompoundRule, Dictation
from aenea.proxy_contexts import ProxyAppContext
from time import sleep
from _generic import pressKeyMap

#helpers
location_on_host = '~/projects/aenea-grammar/_vim.py'
jump = Key('squote, squote')

def goto_line(n):
    for c in str(n):
        Key(c).execute()
    Key("s-g").execute()

def yank_lines(n, n2):
    goto_line(n)
    Key("s-v").execute()
    goto_line(n2)
    Key("y").execute()

def delete_lines(n, n2):
    goto_line(n)
    Key("s-v").execute()
    goto_line(n2)
    Key("d").execute()

general_mapping = {
    'match': Key('c-n'),

    #arithmetic
    'assign':           Text('= '),
    'compare eek':      Text('== '),
    'compare treek':    Text('=== '),
    'compare neek':     Text('!= '),
    'compare greater':  Text('> '),
    'compare less':     Text('< '),
    'compare geek':     Text('>= '),
    'compare leek':     Text('<= '),
    'times':            Text('* '),
    'divided':          Text('/ '),
    'plus':             Text('+ '),
    'minus':            Text('- '),
    'plus equal':       Text('+= '),
    'minus equal':      Text('-= '),
    'times equal':      Text('*= '),
    'divided equal':    Text('/= '),
}

normal_mode_mapping = {

    ### PLUGINS
    # easy-motion
    'fish <pressKey>': Key("space, space, s") + Text('%(pressKey)s'),

    # CTRL+P
    'hunt': Key('space, t'), 
  
    # Vim Grepper
    'grep': Key('space, f, p'),
    'grep buff':  Key('space, f, b'),

    # Filer
    'files': Text('`'),
    'files current': Text('~'),
    ###

    #TODO move elsewhere
    'go down':  Key("c-down"),
    'go left':  Key("c-left"),
    'go up':    Key("c-up"),
    'go right': Key("c-right"),
    
    #edit this _file
    'grammar vimmy': Text(':vsplit'+location_on_host) + Key('enter'),

    #viewport
    'scree top': Key('z, t'),
    'scree mid': Key('z, dot'),
    'scree bot': Key('z, b'),

    #panes
    'split': Text(':vsplit') + Key('enter'),

    'move down':  Key("c-j"),
    'move left':  Key("c-h"),
    'move up':    Key("c-u"),
    'move right': Key("c-l"),

    #motions 
    'matching': Key('ampersand'),
    'row [<n>]': Text('%(n)sG'),
    'jump': jump,
    'up   [<n>]': Key('k:%(n)d'),
    'down [<n>]': Key('j:%(n)d'),
    'left [<n>]': Key('h:%(n)d'),
    'right [<n>]': Key('l:%(n)d'),
    'jee-jee': Key('g, g'),
    'end-jee': Key('s-g'),

    'rinden': Key('rangle, rangle'),
    'linden': Key('langle, langle'),

    #line stuff
    'boop <n>': Function(goto_line) + Key("s-i"),
    'boop': Function(goto_line) + Key("s-i"),
    'noop <n>': Function(goto_line) + Key("s-a, enter"),
    'noop': Key("s-a, enter"),
    'nope': Key("s-a"),
    'nope <n>': Function(goto_line) + Key("s-a"),
    'nope <n>': Function(goto_line) + Key("s-a"),
 
    'dine': Key("d:2"),
    'dine <n>': Function(goto_line) + Key("d:2"),
    'dine <n> (thru|through|to) <n2>': Function(delete_lines),
    'you line': Key("y:2"),
    'you line <n>': Function(goto_line) + Key("y:2"),
    'you line <n> (thru|through|to) <n2>': Function(yank_lines),
     
    #general
    'save': Text(':update') + Key('enter'),
    'quit': Key('colon, q, enter'),
    'poop': Key('s-p'),
    'poo': Key('p'),
    'do': Text('.'),
    'undo': Key('u'),
    'redo': Key('c-r'),
    'insert': Key('i'),
    'app': Key('a'),

    #macro
    'mac': Key('q, q'),
    'repeat mac': Key('at, at'),
    'mac <n>': Key('at') + Text('%(n)'),
    
    #Finding text
    'nord': Key("s-8"),
    'bored': Key("hash"),
    'mash': Key("s-5"), #Matching char
    'ounce <pressKey>': Key("f, %(pressKey)s"),
    'bounce <pressKey>': Key("s-f, %(pressKey)s"),

    'find [<text>]': Key("slash") + Text("%(text)s"),
    'next': Key("n"),
    'prev|previous': Key("s-n"),
    'clear search': Key("colon, n, o, h, enter"),
    'lope <n>': Key("w:%(n)d"),
    'bope <n>': Key("b:%(n)d"),

    # Word operations
    '(doord|doored|gord)': Key("l, d, i, w, i"),
    '(doord|doored|gord) back': Key("l, b, d, w, i"),
    '(doord|doored|gord) <n>': Key("l, %(n)d, d, w, i"),
    '(doord|doored|gord) back <n>': Key("l, %(n)d, b, %(n)d, d, w, i"),
    'chord': Key("l, c, i, w"),
    'chord <n>': Key("l, c, %(n)d, w"),
    'sword': Key("l, v, e"),
    'sword <n>': Key("l, v, e:%(n)d"),
    'ef word':  Key("l, w, i"),
    'ef word <n>': Key("l, %(n)d, w, i"),
    'bee word': Key("b, i"),
    'bee word <n>': Key("%(n)d, b, i"),
    'dee till <pressKey>': Key("d, t, %(pressKey)s"),

    #Change in 
    'kit <pressKey>': Key("c, i, %(pressKey)s"),
}


def _esc():
    Key("escape").execute()
    sleep(0.06)  #fix annoying problem of esc key being held too long in vim

extras = [
    Integer("n", 0, 9999),
    Integer("n2", 0, 9999),
    Dictation('text'),
     Choice("pressKey", pressKeyMap),
]

defaults = {
    "n": 1,
    "n2": 1,
}

class NormalModeRule(MappingRule):
    mapping = normal_mode_mapping
    extras = extras
    defaults = defaults

    def _process_recognition(self, value, extras):
        # press escape before all normal mode commands
        _esc()
        MappingRule._process_recognition(self, value, extras)

class GeneralRule(MappingRule):
    mapping = general_mapping
    extras = extras
    defaults = defaults

grammar = Grammar('vim')
grammar.add_rule(GeneralRule())
grammar.add_rule(NormalModeRule())
grammar.load()

def unload():

    global grammar
    if grammar:
        grammar.unload()
    grammar = None


