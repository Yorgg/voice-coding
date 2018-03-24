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
    'match lie': Key('c-x, c-l'),

    #arithmetic
    'assign':           Text('= '),
    'eek':      Text('== '),
    'treek':    Text('=== '),
    'neek':     Text('!= '),
    'greater':  Text('> '),
    'less':     Text('< '),
    'geek':     Text('>= '),
    'leek':     Text('<= '),
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
    'row [<n>]': Text('%(n)sG'),
    'jump': jump,
    'up   [<n>]': Key('k:%(n)d'),
    'down [<n>]': Key('j:%(n)d'),
    'left [<n>]': Key('h:%(n)d'),
    'right [<n>]': Key('l:%(n)d'),
    'jee-jee': Key('g, g'),
    'end-jee': Key('s-g'),

    'rinden [<n>]': Key('%(n), rangle, rangle'),
    'linden [<n>]': Key('%(n), langle, langle'),

    #line stuff
    'boop <n>': Function(goto_line) + Key("s-i"),
    'boop': Key("s-i"),

    'noop <n>': Function(goto_line) + Key("s-a, enter"),
    'noop': Key("s-a, enter"),
    'nope': Key("s-a"),
    'nope <n>': Function(goto_line) + Key("s-a"),
    'nope <n>': Function(goto_line) + Key("s-a"),
 
    'die': Key("d:2"),
    'dino': Key("s-d, a"),
    'diney': Key("0, s-d"),
    'diner <n>': Key("%(n)d, d:2"),
    'die <n>': Function(goto_line) + Key("d:2"),
    'die <n> (thru) <n2>': Function(delete_lines),
    'die till <pressKey>': Key("d, t, %(pressKey)s"),
    
    
    'you till <pressKey>': Key("y, t, %(pressKey)s"),
    'your <n>': Key("%(n)d, y, y"), 
    'you': Key("y:2"),
    'you <n>': Function(goto_line) + Key("y:2"),
    'you <n> (thru|through|to) <n2>': Function(yank_lines),
     
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
    'rep <pressKey>': Key('r, %(pressKey)s'),
    'rep': Key('r'),
    'sha': Text('g;'),
    'she': Text(';'),
    'cha': Key('x'),

    #macro
    'macro': Key('q, q'),
    'macro <n>': Key('q, %(n)s'),
    'repeat macro': Key('at, at'),
    'play macro <n>': Key('at, %(n)s'),
    'play macro': Key('at, q'),
    
    #Finding text
    'ma ford': Key("s-8"),
    'ma bored': Key("hash"),
    'mack': Key("s-5"), #Matching bracket 

    'ounce <pressKey>': Key("f, %(pressKey)s"),
    'bounce <pressKey>': Key("s-f, %(pressKey)s"),

    'find [<text>]': Key("slash") + Text("%(text)s"),
    'next': Key("n"),
    'prev|previous': Key("s-n"),
    'clears': Key("colon, n, o, h, enter"),
    'ford [<n>]': Key("w:%(n)d"),
    'bored [<n>]': Key("b:%(n)d"),

    # Word operations
    '(doord|doored)': Key("l, d, w, i"),
    '(doord|doored) back': Key("l, b, d, w, i"),
    '(doord|doored) <n>': Key("l, %(n)d, d, w, i"),
    '(doord|doored) back <n>': Key("l, %(n)d, b, %(n)d, d, w, i"),
    'chord': Key("l, c, i, w"),
    'chord <n>': Key("l, c, %(n)d, w"),
    'sword': Key("l, v, e"),
    'sword <n>': Key("l, v, e:%(n)d"),
    'ef word':  Key("l, w, i"),
    'ef word <n>': Key("l, %(n)d, w, i"),
    'bee word': Key("b, i"),
    'bee word <n>': Key("%(n)d, b, i"),

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

