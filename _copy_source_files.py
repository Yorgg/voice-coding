from shutil import copy
from os import listdir
from aenea import Grammar, CompoundRule

class CopyFiles(CompoundRule):
    spec = ('copy files')

    def _process_recognition(self, node, extras):  
        src = r"\\VBOXSVR\aenea-grammar\\"
        dst = r"C:\NatLink\Natlink\MacroSystem"

        source = listdir(src)

        for file in source:
            if file.endswith(".py"):
                copy(src+file,dst)
                print 'copied ' + file

grammar = Grammar('copy_source_files')
grammar.add_rule(CopyFiles())
grammar.load()
              

def unload():
    global grammar
    if grammar:
        grammar.unload()
    grammar = None

