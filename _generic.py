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
    camel_case_text,
    dot,
    dash,
    sentence,
    snake_case_text
)


letterMap = {
    "(alpha)": "a",
    "(bravo) ": "b",
    "(charlie) ": "c",
    "(delta) ": "d",
    "(echo|eck) ": "e",
    "(foxtrot) ": "f",
    "(golf) ": "g",
    "(hotel) ": "h",
    "(india|indigo|ish) ": "i",
    "(juliet) ": "j",
    "(kilo) ": "k",
    "(lima) ": "l",
    "(mike) ": "m",
    "(november|noy) ": "n",
    "(oscar|osh) ": "o",
    "(papa|poppa|pom) ": "p",
    "(quebec|quiche) ": "q",
    "(romeo|ree) ": "r",
    "(sierra|soy) ": "s",
    "(tango|tay) ": "t",
    "(uniform|umm) ": "u",
    "(victor|van) ": "v",
    "(whiskey|wes) ": "w",
    "(x-ray) ": "x",
    "(yankee|yaa) ": "y",
    "(zulu) ": "z",
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
# For repeating of characters.
specialCharMap = {
    "(bar|vertical bar|pipe)": "bar",
    "(dash|minus|hyphen)": "hyphen",
    "(dot|period)": "dot",
    "comma": "comma",
    "backslash": "backslash",
    "underscore": "underscore",
    "(star|asterisk)": "s-8",  #mac issue when "star"
    "colon": "colon",
    "(semicolon|semi-colon)": "semicolon",
    "at": "at",
    "quote": "s-squote",
    "sing quote": "squote",
    "hash": "hash",
    "dollar": "dollar",
    "percent": "percent",
    "and": "s-7",
    "slash": "slash",
    "equal": "equal",
    "plus": "plus",
    "space": "space",
    "langle": "langle",
    "rangle": "rangle",
    "rack": "lbracket",
    "lack": "rbracket",
    "race": "rbrace",
    "lace": "lbrace",
    "laren": "lparen",
    "raren": "rparen",
    }


pressKeyMap = {}
pressKeyMap.update(letterMap)
pressKeyMap.update(numberMap)
pressKeyMap.update(controlKeyMap)
pressKeyMap.update(specialCharMap)

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

mapping = {
    "fee": Key("escape"),

    # Functional keys.
    "ace [<n>]": Key("space:%(n)d"),
    "slap [<n>]": Key("enter:%(n)d"),
    "tab [<n>]": Key("tab:%(n)d"),
    "scratch [<n>]": Key("backspace:%(n)d"),

    # Closures.
    "angle brackets": Key("langle, rangle, left"),
    "brackets": Key("lbracket, rbracket, left"),
    "braces": Key("lbrace, rbrace, left"),
    "parens": Key("lparen, rparen, left"),
    "quotes": Key("s-squote, s-squote, left"),
    "backticks": Key("backtick:2, left"),
    "sing quotes": Key("squote, squote, left"),
    
    # Shorthand multiple characters.
    "double <char>": Key("%(char)s, %(char)s"),
    "triple <char>": Key("%(char)s, %(char)s, %(char)s"),
    "double escape": Key("escape, escape"),  # Exiting menus.

    # Punctuation and separation characters, for quick editing.
    "colon [<n>]": Key("colon:%(n)d"),
    "semi-colon [<n>]": Key("semicolon:%(n)d"),
    "comma [<n>]": Key("comma:%(n)d"),
    "(dot|period) [<n>]": Key("dot:%(n)d"),
    "(dash|hyphen|minus) [<n>]": Key("hyphen:%(n)d"),
    "underscore [<n>]": Key("underscore:%(n)d"),

    "<letters>": Text("%(letters)s"),
    "cap <letters>": Key("s-%(letters)s"),
    "<char>": Key("%(char)s"),

    # Format dictated words
    "snake <text>": Function(snake_case_text),
    "since <text>": Function(sentence),
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

