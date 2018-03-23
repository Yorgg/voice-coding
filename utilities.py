from time import sleep
from aenea import MappingRule, Key

def _esc():
    Key("escape").execute()
    sleep(0.06)  

def _esc_insert():
    _esc()
    Key("a").execute()
    sleep(0.06) 

def _esc_newline():
    _esc()
    Key("o").execute()
    sleep(0.06) 

###
#to insert new text without worrying about Vim mode
#inherit from the following classes: 

class EscapeInsertRule(MappingRule):
    def _process_recognition(self, value, extras):
        _esc_insert() 
        MappingRule._process_recognition(self, value, extras)

class EscapeNewLineRule(MappingRule):
    def _process_recognition(self, value, extras):
        _esc_newline()
        MappingRule._process_recognition(self, value, extras)

###
