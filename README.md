**EXTENDED BRAINFUCK**

A Python library to interpret Extended Brainfuck.
Extended Brainfuck is the same as standard Brainfuck, but with several extra instructions and cells with predefined uses.
To understand standard Brainfuck: https://docs.google.com/document/d/1M51AYmDR1Q9UBsoTrGysvuzar2_Hx69Hz14tsQXWV6M/edit

Added Instructions: 

".c": this is a way to specify if you want to print the character form or the pure int form of the current stack index you are on. if you add the c to the end of the ".", it will print the ASCII char value, but if you leave it blank, it prints the integer value.

*MAYBE MORE TO COME*


To initialize a EBF interpreter, first import EBF as

**import ExtendedBF as ebf**

Then, you can call:

**interpreter = ebf.Interpreter()**

now, to parse your EBF code, you can do one of two things. Firstly, you can run a string of EBF code:

**interpreter.parse("+++++[>++<-]>.")**

you can also run code from an EBF file:

**interpreter.parse(filepath = "/example.ebf")**

this is already a very mutable setup. however, EBF has a few more tricks up it's sleeve: *you can now add libraries to Brainfuck.* now, before you start bashing your head into a desk, let me explain:
Brainfuck's interpreters are set up where it loops through your program, checking to see each character. based on the character, it will run a specific function to modify the stack, it's pointer, and other things. now, you can write custom functions in python files and import them into your interpreter with one simple command. there are also some built-in modules that are better explained in the documentation. To import a module:

**interpreter = ebf.Interpreter(modules = ["module"])

that is it. no fancy command-line git pulls or advanced source-code editing, just adding your python file to your current code directory and placing it's name (without the .py) into a list.




cell [0] - How many cells to allocate for math and variables
cell [1] - Width of screen in pixels - Max 160
cell [2] - Heighth of screen in pixels - Max 160
cells [3] & [4] - Used to scale up the window, window size is multiplied by [3].[4]
cells [5]-[5+[0]] - Reserved for math and variables
cells [5+[0]+1]-[[5+[0]+1]+[3]x[4]] - contains color values for the screen
Example stack - [5][4][3][2][5][0][0][0][0][0][162]...[214]
Explanation - Allocate 5 cells for math.
              Set screen size to 4x3 pixels
              Scale up by 2.5 times
              5 empty cells for variables and math
              next 12 cells used to store colors for pixels
              the rest of the cells are not for a specific use

Because all cells are simulated 8 bit ints, they only store a value 0-255. To cover as many colors as possible, the ints are converted to binary when printed to the screen.
It uses the rgb color space with the first three bits red, the second three green, and the last two blue. so a yellow color could be: rgb | 00FFFF
                binary 8 bit | 00011111
                int 8 bit | 31
Color values:
000: 00
001: 18
010: 40
011: 68
100: 90
101: B9
110: E0
111: FF
00: 00
01: 3A
10: B8
11: FF

Example program - +++>++>++>+>>>>P++++++++++[>++++++++++<-]P+++++++++++++++++++++++++[>>++++++++++<<-]P++++++++++[>>>++++++++++<<<-]P+++++++++++++++++++++++++[>>>>++++++++++<<<<-]>.>.>.>.*
sets up 