.globl main

.data
welcome: 	.asciiz 	"Welcome to the shape calculator\nChoose an option:\n1. Square\n2. Rectangle\nChoose: "
rectSideA: 	.asciiz 	"Enter the first side length: "
rectSideB: 	.asciiz 	"Enter the second side length: "
sqSide: 	.asciiz 	"Enter the side length: "
area: 		.asciiz 	"The area is: "
invalid: 	.asciiz 	"That's an invalid value!\n"

.text
main:

# Load welcome message and input choices
la $a0, welcome
li $v0, 4
syscall
					# Initialize the variables 
li $s1, 0  				# sideA = 0
li $s2, 0  				# sideB = 0
li $s3, 0  				# area = 0
li $s4, 0  				# valid = false

# Read user choice
li $v0, 5				# Ask user for input
syscall
move $s0, $v0  				# Store choice in $s0

beq $s0, 1, squareArea			# If option 1, branch to squareArea
beq $s0, 2, rectangleArea		# If option 2, branch to rectangleArea

# Default Case (if invalid)
la $a0, invalid
li $v0, 4
syscall
j endif

squareArea:
la $a0, sqSide
la $v0, 4
syscall

li $v0, 5
syscall

move $s1, $v0
move $a0, $s1
jal square
move $s3, $v0
li $s4, 1
j endif

rectangleArea:
la $a0, rectSideA
li $v0, 4
syscall
    
li $v0, 5
syscall

move $s1, $v0   
la $a0, rectSideB
li $v0, 4
syscall
    
li $v0, 5
syscall

move $s2, $v0 
move $a0, $s1
move $a1, $s2
jal rectangle
move $s3, $v0  
li $s4, 1

endif:
beq $s4, 0, exit
li $v0, 4
la $a0, area
syscall
    
li $v0, 1
move $a0, $s3
syscall

exit:
li $v0, 10
syscall

square:
mul $v0, $a0, $a0
jr $ra
    
rectangle:
mul $v0, $a0, $a1
jr $ra
