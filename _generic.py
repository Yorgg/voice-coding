
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
    "left": "left",
    "right": "right",
    "up": "up",
    "down": "down",
    "ace": "space",
    "(enter|return)": "enter",
    "escape": "escape",
    "tab": "tab"
}

pressKeyMap = {}
pressKeyMap.update(letterMap)
pressKeyMap.update(numberMap)
pressKeyMap.update(controlKeyMap)











