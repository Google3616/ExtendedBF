# **EXTENDED BRAINF\*\*K**

Have you ever heard of traditional Brainf\*\*k? It's a coding language designed to be incredibly stupid, tedious, aggressively inefficient, and to, as its' title states, f\*\*k with your brain.
ExtendedBF takes this idea and takes it to a whole new level of brainf\*\*kery. You can set up custom interpreters, import built-in libraries that can handle graphics, pseudorandom functionalities, and even design your own modules to add on to this *wonderful* language. 

Brainf\*\*k's form of coding is purely whimsical. It is based on a three-thousand-celled mutable array called a stack, initially filled with zeroed out indexes.

```
[0][0][0][0][0][0][0][0] ... [0]
```

You have a pointer that starts at the front of the stack that points to a specific cell in the stack, and you can move it left or right:

```
[0][0][0][0][0][0][0][0] ... [0]
 ^ 
```

 
And you can increment and decrement the stack index you are by one. 

```
[1][0][0][0][0][0][0][0] ... [0]
 ^ #increment by 1
```
 
You can also print the current cell, ask for user input, and loop commands. Here is the lexicon for the basic Brainf\*\*k language:

```
<     move left in the stack
>     move right in the stack
+     increment current stack point by one 
-     decrement current stack pointer by one
,     ask for user input
.     print the current cell as a char
[     begin loop- if current stack point equals 0, the loop will stop.
]     end loop
```

An example program to print "A" (or the ASCII character 33) would look like:

`+++++++++++++++++++++++++++++++++.`

This is tacky and quite long. to fix this, we can use loops to repeatedly add to a stack point to equal 33.

`+++[>+++++++++++<-]>.`

Let's break this down. Mainly, this program runs off of a loop. Loops will run the code inbetween brackets of the same order (e.g. matching brackets) until it reaches the start of the loop and the current stack point equals 0. Here's what that looks like for a simple program where the looped program is only "-":

`+++[-]`

```
[3][0][0][0][0][0][0][0] ... [0]
 ^ #adds 1 three times (+++)
```

```
[2][0][0][0][0][0][0][0] ... [0]
 ^ #runs loop because current stack point is not 0, decrementing by 1
```

```
[1][0][0][0][0][0][0][0] ... [0]
 ^ #runs loop because current stack point is not 0, decrementing by 1
```

```
[0][0][0][0][0][0][0][0] ... [0]
 ^ #stops loop because current stack point is 0
```

ExtendedBF has added a few new characters to this lexicon to aid in the simplicity of the language.

```
".C", ",C ", ".I", and ",I":
If you add a capital "C" or "I" in front of a print command or input command, it will input or print the ASCII character or integer value of the cell value, respectively. For example, if the cell value is 33 and you call ".I", it will display "33", but if you call ".C", it will display "!" as it's ASCII value is 33 (https://www.asciitable.com/). If you leave it without the added "C" and "I", it will default to printing or inputting the integer value.

E.X. +++++.   -> 5
     
```