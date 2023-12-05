# **EXTENDED BRAINFUCK**

Have you ever heard of traditional Brainfuck? It's a coding language designed to be incredibly stupid, tedious, aggressively inefficient, and to, as its' title states, fuck with your brain.
ExtendedBF takes this idea and takes it to a whole new level of brainfuckery. You can set up custom interpreters, import built-in libraries that can handle graphics, pseudorandom functionalities, and even design your own modules to add on to this *wonderful* language. 

Brainfuck's form of coding is purely whimsical. It is based on a three-thousand-celled mutable array called a stack, initially filled with zeroed out indexes.

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
 
You can also print the current cell, ask for user input, and loop commands. Here is the lexicon for the basic Brainfuck language:

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