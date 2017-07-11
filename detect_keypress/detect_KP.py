from pynput import keyboard
from s_char import special_char
import pyperclip, re
####################
# DEFINE CONSTANTS #
####################
sentence = "" # Stores user's key inputs
shift = False # Checks if shift keys are pressed/not (Default: False)

################
# Word Counter #
################
def words(sentence):
    count = len(re.findall("[a-zA-Z_]+", sentence))
    return count

################
# Key Listener #
################
def on_press(key):
    global sentence, shift
    try:
        if shift == True:
            if key.char in special_char:
                sentence += special_char[key.char]
            else:
                sentence += key.char.upper()
        else:
            sentence += key.char
        #print('alphanumeric key {0} pressed'.format(key.char))
    except AttributeError:
        if key == keyboard.Key.backspace:
            sentence = sentence[:-1]
        elif key == keyboard.Key.space:
            sentence += " "
        elif key == keyboard.Key.shift or key == keyboard.Key.shift_r:
            shift = True
        elif key == keyboard.Key.enter:
            sentence += "\n"
        #print('special key {0} pressed'.format(key))

def on_release(key):
    global shift, words
    print(sentence)
    pyperclip.copy(sentence)
    #print('{0} released'.format(key))
    if key == keyboard.Key.esc:
        # Stop listener
        pyperclip.copy(sentence)
        print('\nKey listener has stopped.\n'+'-'*30+'\nText:\n'+sentence+'\n'+
        '-'*30+'\n[Words: '+str(words(sentence))+
        ']\n\nYour text has been copied to your clipboard. (CTRL+V) to paste it.')
        return False
    elif key == keyboard.Key.shift or key == keyboard.Key.shift_r:
        shift = False

# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
