# KlipBoard
> A script that helps writing texts of information, and copied automatically to windows clipboard

This is part of my 'study-the-examples' series, of how certain things can be done in python through 3rd-party libraries. Scripts are designed as accord to me, and not for client use. You can however download and edit them to work on your computer.

## Features
* Auto-copies every key event
* Final Compile ('ESC' key to compile)
  * Word Counter
    * Split words intelligently by undefined spaces
    * Does not count element with special characters specficially
      * Accepts (eg. hi!23><)
      * Does not accept (eg. @#!}")
* Supports
  * Special Characters (eg. !,@,#,$,%,^,&,{,},>,?,..)
  * Newline (space) & Moves backward (backspace)
  * Windows ONLY
* Unsupported
  * Windows Alt Codes (eg. ™,†,,♥,♦,..)
  
## Documentation

### Libraries
- [pynput](https://pypi.python.org/pypi/pynput)
- [pyperclip](https://pypi.python.org/pypi/pyperclip)

### Usage
This script is not yet compiled into an executable, thus you will need to compile it manually.

This script automatically saves every key events that are being pressed into the windows clipboard. At the end of the script, it will also show the total number of words in the text.

I decided to create this script after my friends complained how poorly designed my school's website is that render them to unable save or write their responses in time.

#### Workflow
1. Run the script; the key listener begins
2. For every keys pressed, it will return as a string saved to windows clipboard
3. Hit the 'ESC' key when you're done. It will compiled everything to the clipboard and shows the total number of words in the sentence.

** Notes
This is an open-source project that can be view, edit, improve on by anyone. Contributions to support other OS are welcome as it only supports Windows now.
