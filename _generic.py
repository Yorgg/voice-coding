from aenea import (
    Keyboard,
    Grammar,
    MappingRule,
    Text,
    Key,
    Function,
    Dictation,
    Choice,
    Integer,
    Alternative,
    CompoundRule,
)

from format import (
    uppercase_text,
    lowercase_text,
    snake_case_text,
    camel_case_text,
    dot,
    dash,
)

letterMap = {
    "(A|alpha)": "a",
    "(B|bravo) ": "b",
    "(C|charlie) ": "c",
    "(D|delta) ": "d",
    "(E|echo|eck) ": "e",
    "(F|foxtrot) ": "f",
    "(G|golf) ": "g",
    "(H|hotel) ": "h",
    "(I|india|indigo|ish) ": "i",
    "(J|juliet) ": "j",
    "(K|kilo) ": "k",
    "(L|lima) ": "l",
    "(M|mike) ": "m",
    "(N|november|noy) ": "n",
    "(O|oscar|osh) ": "o",
    "(P|papa|poppa|pom) ": "p",
    "(Q|quebec|quiche) ": "q",
    "(R|romeo|ree) ": "r",
    "(S|sierra|soy) ": "s",
    "(T|tango|tay) ": "t",
    "(U|uniform|umm) ": "u",
    "(V|victor|van) ": "v",
    "(W|whiskey|wes) ": "w",
    "(X|x-ray) ": "x",
    "(Y|yankee|yaa) ": "y",
    "(Z|zulu) ": "z",
}

numberMap = {
    "zero": "0",
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

controlKeyMap = {
    "ace": "space",
    "(enter|return)": "enter",
    "escape": "escape",
    "tab": "tab"
}

pressKeyMap = {}
pressKeyMap.update(letterMap)
pressKeyMap.update(numberMap)
pressKeyMap.update(controlKeyMap)

abbreviationMap = {
    "administrator": "admin",
    "administrators": "admins",
    "application": "app",
    "applications": "apps",
    "argument": "arg",
    "arguments": "args",
    "attribute": "attr",
    "attributes": "attrs",
    "(authenticate|authentication)": "auth",
    "binary": "bin",
    "button": "btn",
    "class": "cls",
    "command": "cmd",
    "(config|configuration)": "cfg",
    "context": "ctx",
    "control": "ctrl",
    "database": "db",
    "(define|definition)": "def",
    "description": "desc",
    "(develop|development)": "dev",
    "(dictionary|dictation)": "dict",
    "(direction|directory)": "dir",
    "dynamic": "dyn",
    "example": "ex",
    "execute": "exec",
    "exception": "exc",
    "expression": "exp",
    "(extension|extend)": "ext",
    "function": "func",
    "framework": "fw",
    "(initialize|initializer)": "init",
    "instance": "inst",
    "integer": "int",
    "iterate": "iter",
    "java archive": "jar",
    "javascript": "js",
    "keyword": "kw",
    "keyword arguments": "kwargs",
    "language": "lng",
    "library": "lib",
    "length": "len",
    "number": "num",
    "object": "obj",
    "okay": "ok",
    "package": "pkg",
    "parameter": "param",
    "parameters": "params",
    "pixel": "px",
    "position": "pos",
    "point": "pt",
    "previous": "prev",
    "property": "prop",
    "python": "py",
    "query string": "qs",
    "reference": "ref",
    "references": "refs",
    "(represent|representation)": "repr",
    "regular (expression|expressions)": "regex",
    "request": "req",
    "revision": "rev",
    "ruby": "rb",
    "session aidee": "sid",  # "session id" didn't work for some reason.
    "source": "src",
    "(special|specify|specific|specification)": "spec",
    "standard": "std",
    "standard in": "stdin",
    "standard out": "stdout",
    "string": "str",
    "(synchronize|synchronous)": "sync",
    "system": "sys",
    "utility": "util",
    "utilities": "utils",
    "temporary": "tmp",
    "text": "txt",
    "value": "val",
    "window": "win",
}

controlKeyMap = {
    "(enter|return)": "enter",
    "ack": "escape",
    "tab": "tab"
}

# For repeating of characters.
specialCharMap = {
    "(bar|vertical bar|pipe)": "|",
    "(dash|minus|hyphen)": "-",
    "(dot|period)": ".",
    "comma": ",",
    "backslash": "\\",
    "underscore": "_",
    "(star|asterisk)": "*",
    "colon": ":",
    "(semicolon|semi-colon)": ";",
    "at": "@",
    "[double] quote": '"',
    "single quote": "'",
    "hash": "#",
    "dollar": "$",
    "percent": "%",
    "and": "&",
    "slash": "/",
    "equal": "=",
    "plus": "+",
    "space": " ",
    "langle": "<",
    "rangle": ">",
    "rack": "]",
    "lack": "[",
    "race": "}",
    "lace": "{",
    }

mapping = {
    # Functional keys.
    "ace [<n>]": Key("space:%(n)d"),
    "slap [<n>]": Key("enter:%(n)d"),
    "tab [<n>]": Key("tab:%(n)d"),
    "scratch [<n>]": Key("backspace:%(n)d"),

    # Closures.
    "angle brackets": Key("langle, rangle, left/3"),
    "brackets": Key("lbracket, rbracket, left/3"),
    "braces": Key("lbrace, rbrace, left/3"),
    "parens": Key("lparen, rparen, left/3"),
    "quotes": Key("s-squote, s-squote, left/3"),
    "backticks": Key("backtick:2, left"),
    "sing quotes": Key("squote, squote, left/3"),
    
    # Shorthand multiple characters.
    "double <char>": Text("%(char)s%(char)s"),
    "triple <char>": Text("%(char)s%(char)s%(char)s"),
    "double escape": Key("escape, escape"),  # Exiting menus.

    # Punctuation and separation characters, for quick editing.
    "colon [<n>]": Key("colon/2:%(n)d"),
    "semi-colon [<n>]": Key("semicolon/2:%(n)d"),
    "comma [<n>]": Key("comma/2:%(n)d"),
    "(dot|period) [<n>]": Key("dot/2:%(n)d"),
    "(dash|hyphen|minus) [<n>]": Key("hyphen/2:%(n)d"),
    "underscore [<n>]": Key("underscore/2:%(n)d"),

    "<letters>": Text("%(letters)s"),
    "<char>": Text("%(char)s"),

    # Format dictated words
    "snake <text>": Function(snake_case_text),
    "upper <text>": Function(uppercase_text),
    "dashy <text>": Function(dash),
    "camel <text>": Function(camel_case_text),
    "dotty <text>": Function(dot),
    "low <text>": Function(lowercase_text),

    # For writing words that would otherwise be characters or commands.
    # Ex: "period", tab", "left", "right", "home".
#    "say <reservedWord>": Text("%(reservedWord)s"),

    # Abbreviate words commonly used in programming.
    # Ex: arguments -> args, parameters -> params.
    "tiny <abbreviation>": Text("%(abbreviation)s"),
}

class KeystrokeRule(MappingRule):
    mapping = mapping
    extras = [
        Integer("n", 1, 100),
        Dictation("text"),
        Dictation("text2"),
        Choice("char", specialCharMap),
        Choice("letters", letterMap),
#        Choice("modifier1", modifierMap),
#        Choice("modifier2", modifierMap),
#        Choice("modifierSingle", singleModifierMap),
#        Choice("pressKey", pressKeyMap),
        Choice("abbreviation", abbreviationMap),
    ]
    defaults = {
        "n": 1,
    }

grammar = Grammar("Generic edit")
grammar.add_rule(KeystrokeRule())  # Add the top-level rule.
grammar.load()  # Load the grammar.

def unload():
    global grammar
    if grammar:
        grammar.unload()
    grammar = None

