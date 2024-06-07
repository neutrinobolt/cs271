// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

// Put your code here.

// While key is not pressed (white):

// Set open
@SCREEN
D=A
@0
M=A
// Set section
A=D
// Set Color
M=0
// Back to top if on final row
@0
M=D
@24575
D=A-D //...Dad? Is that you?
@15 // Skip to Stepper
D;JNE
@0
M=A
D=A
// Set D to next section
@0
M=M+1
D=M
// check if key is pressed
@KBD
D=M
@26 //Black Loop start
D;JNE
@0
D=M
// Reset White loop
@2
D;JMP

////////////////////////////////////////////////////////////////
// While key is pressed (black):

// Set open
@SCREEN
D=A
@0
M=A
// Set section and color
A=D
M=-1
// Back to top if on final row
@0
M=D
@24575
D=A-D //...Dad? Is that you?
@41 // Skip to Stepper
D;JNE
@0
M=A
D=A
// Set D to next section
@0
M=M+1
D=M
// check if key is pressed
@KBD
D=M
@0 //White Loop Start
D;JEQ
@0 // I know I just did that, but this keeps the program symmetrical
D=M
// Reset Black loop
@30
D;JMP
