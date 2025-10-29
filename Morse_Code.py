from preloaded import MORSE_CODE

def decode_morse(morse_code):
    # Remember - you can use the preloaded MORSE_CODE dictionary:
    # For example: 
    # MORSE_CODE['.-'] = 'A'
    # MORSE_CODE['--...'] = '7'
    # MORSE_CODE['...-..-'] = '$'
    mo = morse_code.strip().split(' ')
    res = ''
    for i in mo:
        res = res + str(MORSE_CODE.get(i,' '))
    res1 = res.replace("  ", "~!~").replace(" ", "").replace("~!~", " ")
    return res1
