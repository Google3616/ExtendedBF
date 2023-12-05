**EXTENDED BRAINFUCK**

Have you ever heard of traditional Brainfuck? It's a coding language designed to be incredibly stupid, tedious, aggressively inefficient, and to, as its' title states, fuck with your brain. ExtendedBF takes this idea and takes it to a whole new level of brainfuckery. You can set up custom interpreters, import built-in libraries that can handle graphics, pseudorandom functionalities, and even design your own modules to add on to this *wonderful* language. 

Brainfuck's form of coding is purely whimsical. It is based on a three thousand-celled mutable array called a stack, initially filled with zeroed out indexes.

[0][0][0][0][0][0][0][0] ... [0]

You have a pointer that starts at the front of the stack that points to a specific cell in the stack, and you can move it left or right:

[0][0][0][0][0][0][0][0] ... [0]

 ^
 
And you can increment and decrement the stack index you are by one. 

[1][0][0][0][0][0][0][0] ... [0]

 ^ <- +1
 
You can also print the current cell, ask for user input, and 