// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)
//
// This program only needs to handle arguments that satisfy
// R0 >= 0, R1 >= 0, and R0*R1 < 32768.

// Put your code here.

// Clear R2
@2
M=0

// If R1 == 0, skip to end
@1
D=M
@END
D;JEQ

// Add R0 to R2
@0
D=M
@2
M=M+D

// Subtract 1 from R1
@1
M=M-1

// Return to loop start
@2
D;JMP