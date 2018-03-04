from aenea import Grammar, MappingRule, Text, Key, Integer, Dictation, CompoundRule
from aenea.proxy_contexts import ProxyAppContext

grammar = Grammar('vim')

print 'Vim grammar: Loaded.'

LEADER = ' '

# PLUGINS

class Plugin(MappingRule):
    mapping = {

        # CTRL+P
        'hunt': Text(LEADER + 't'), 

        # Vim Grepper
        'grep': Text(LEADER + 'fp'),
        'grep buff': Text(LEADER + 'fb'),

        # FIler
        'files': Text('`'),
        'files current': Text('~'),
    }
  

class Word(CompoundRule):
    spec = ('(sentence | snake | dot-word | dash-word ) <dictation>')
    extras = [Dictation(name='dictation')]

    def _process_recognition(self, node, extras):
        words = node.words()
        if words[0] == 'sentence':
            words = ' '.join(words[1:])
        if words[0] == 'snake':
            words = '_'.join(words[1:])
        if words[0] == 'dotword':
            words = '.'.join(words[1:])
        if words[0] == 'dashword':
            words = '-'.join(words[1:])
        Text(words).execute()


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
            "dot": ".",
        }
        mapping = {}
        for k, v in long_letters_map.iteritems():
            mapping[k] = Text(long_letters_map[k])
        return mapping

    mapping = setup()

class Motion(MappingRule):
    mapping = {
        'up': Text('k'),
        'down': Text('j'),
        'left': Text('h'),
        'right': Text('l'),

        'lope': Text('b'),
        'yope': Text('w'),
        'jope': Text('e'),

        'care': Text('^'),
        'doll': Text('$'),

        'jee-jee': Text('gg'),
        'end-jee': Text('G'),
        
        'lake': Text('{'),
        'rake': Text('}'),

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
        'compare gack':     Text('>= '),
        'compare lack':     Text('<= '),
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
        'travel <motion>': Key("c-%(motion)s"),

        #panes
        'move down': Key("c-j"),
        'move left': Key("c-h"),
        'move up': Key("c-u"),
        'move right': Key("c-l"),
        

        'vim save': Text(':w') + Key('enter'),
        'vim quit': Text(':q') + Key('enter'),
        'vim scratch': Key('X'),
        'vim chuck': Key('x'),
        'vim undo': Key('u'),
        'plap': Key('P'),
        'plop': Key('p'),
        'ditto': Text('.'),
        'ripple': 'macro',
        
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

grammar.add_rule(Command())
grammar.add_rule(Plugin())
grammar.add_rule(Word())
grammar.add_rule(Letter())
grammar.add_rule(ArithmeticInsertion())
grammar.add_rule(KeyInsertion())
grammar.add_rule(Motion())
grammar.load()

def unload():
    global grammar
    if grammar:
        grammar.unload()
    grammar = None

