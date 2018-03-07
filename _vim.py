from aenea import Grammar, MappingRule, Text, Key, Integer, Dictation, CompoundRule
from aenea.proxy_contexts import ProxyAppContext

grammar = Grammar('vim')
LEADER = ' '

# open vim and edit
class Edit(MappingRule):
    mapping = {
        'grammar vimmy': Text(':vsplit ~/projects/aenea-grammar/_vim.py') + Key('enter')
    }

# PLUGINS
class Plugin(MappingRule):
    mapping = {
        # easy-motion
        'find': Key('space') + Key('space') + Key('s'),

        # CTRL+P
        'hunt': Text(LEADER + 't'), 

        # Vim Grepper
        'grep': Text(LEADER + 'fp'),
        'grep buff': Text(LEADER + 'fb'),

        # Filer
        'files': Text('`'),
        'files current': Text('~'),
    }
  

class Word(CompoundRule):
    spec = ('(sentence | snakey | dotty | dashy) <dictation>')
    extras = [Dictation(name='dictation')]

    def _process_recognition(self, node, extras):
        words = node.words()
        if len(node.words()) == 2:
            words.append('')
        if words[0] == 'sentence':
            words = ' '.join(words[1:])
        if words[0] == 'snakey':
            words = '_'.join(words[1:])
        if words[0] == 'dotty':
            words = '.'.join(words[1:])
        if words[0] == 'dashy':
            words = '-'.join(words[1:])
        Text(words).execute()


class Motion(MappingRule):
    mapping = {
        'up': Key('k'),
        'down': Key('j'),
        'left': Key('h'),
        'right': Key('l'),

        'lope': Key('b'),
        'yope': Key('w'),
        'jope': Key('e'),

        'care': Key('caret'),
        'doll': Key('dollar'),

        'jee-jee': Key('g, g'),
        'end-jee': Key('s-g'),
        
        'race': Key('rbrace'),
        'lace': Key('lbrace'),

        'rack': Key('rbracket'),
        'lack': Key('lbracket'),

        'slash': Key('slash'),

        'row [<count>]':  Text('%(count)sG'),
    }
    extras   = [
        Integer("count", 1, 99999),
    ]
    defaults = {
        "count": 1,
    }

class ArithmeticInsertion(MappingRule):
    mapping = {
        'assign':           Text('= '),
        'compare eek':      Text('== '),
        'compare treek':      Text('=== '),
        'compare neek':  Text('!= '),
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


class KeyInsertion(MappingRule):
    mapping = {
        'ace [<count>]':        Key('space:%(count)d'),
        'tab [<count>]':        Key('tab:%(count)d'),
        'slap [<count>]':       Key('enter:%(count)d'),
        'chuck [<count>]':      Key('del:%(count)d'),
        'scratch [<count>]':    Key('backspace:%(count)d'),
        'ack':                  Key('escape'),
    }
    extras   = [
        Integer("count", 1, 99),
    ]
    defaults = {
        "count": 1,
    }

class Command(MappingRule):
    mapping = {
        'vee split': Text(':vsplit') + Key('enter'),

        # general view switching for MAC (MOVE ELSEWHERE)
        'go right': Key("c-right"),
        'go left':  Key("c-left"),

        #panes
        'move down':  Key("c-j"),
        'move left':  Key("c-h"),
        'move up':    Key("c-u"),
        'move right': Key("c-l"),
        

        'vim save': Text(':update') + Key('enter'),
        'vim quit': Text(':q') + Key('enter'),
        'vim scratch': Key('X'),
        'vim chuck': Key('x'),
        'vim undo': Key('u'),
        'plap': Key('P'),
        'plop': Key('p'),
        'ditto': Text('.'),
        'macro': Text('qq'),
        
        'grab': Text('y'),
        'grab line':  Text('yy'),
        'chuck line':  Text('dd')
        }

    extras   = [
        Dictation("motion"),
    ]
    defaults = {
        "motion": 'right',
    }
#temporary put it here....
        
class Letter(MappingRule):
    def setup():
        long_letters_map = {
            "alpha": "a",
            "bravo": "b",
            "charlie": "c",
            "delta": "d",
            "echo": "e",
            "foxtrot": "f",
            "golf": "g",
            "hotel": "h",
            "india": "i",
            "juliet": "j",
            "kilo": "k",
            "lima": "l",
            "mike": "m",
            "november": "n",
            "oscar": "o",
            "poppa": "p",
            "quebec": "q",
            "romeo": "r",
            "sierra": "s",
            "tango": "t",
            "uniform": "u",
            "victor": "v",
            "whiskey": "w",
            "x-ray": "x",
            "yankee": "y",
            "zulu": "z",
        }
        mapping = {}
        for k, v in long_letters_map.iteritems():
            mapping[k] = Key(long_letters_map[k])
        return mapping

    mapping = setup()


grammar.add_rule(Command())
grammar.add_rule(Plugin())
grammar.add_rule(Word())
grammar.add_rule(Letter())
grammar.add_rule(ArithmeticInsertion())
grammar.add_rule(KeyInsertion())
grammar.add_rule(Motion())
grammar.add_rule(Edit())
grammar.load()

def unload():
    global grammar
    if grammar:
        grammar.unload()
    grammar = None

