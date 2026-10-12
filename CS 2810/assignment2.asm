.globl main

.data
text1: 		.asciiz " divided by "
text2:		.asciiz " = "
text3:		.asciiz " with remainder "
text4:		.asciiz "The average of the three numbers is "
newline: 	.asciiz "\n"

.text
main:
			# Store int in vars
li $s0, 10		# a = 10
li $s1, 5		# b = 5
li $s2, 3		# c = 3

			# Printing 10/2 with remainder 0
# Dividing 10 from 5
move $t0, $s0
move $t1, $s1
div $t0, $t1
mflo $t2
mfhi $t3

# Printing 10
move $a0, $s0
li $v0, 1		# Prints integer
syscall

# Printing text1
la $a0, text1		
li $v0, 4		# Prints string
syscall

# Printing 5
move $a0, $s1
li $v0, 1
syscall

# Printing text2
la $a0, text2
li $v0, 4
syscall

# Printing result
move $a0, $t2
li $v0, 1
syscall

# Printing text3
la $a0, text3
li $v0, 4
syscall 

# Printing remainder
move $a0, $t3
li $v0, 1
syscall

# Printing newline
la $a0, newline
li $v0, 4
syscall

			# Now printing 10/3 with remainder 1

# Dividing 10 from 3
move $t0, $s0
move $t1, $s2
div $t0, $t1
mflo $t2
mfhi $t3

# Printing 10
move $a0, $s0
li $v0, 1		# Prints integer
syscall

# Printing text1
la $a0, text1		
li $v0, 4		# Prints string
syscall

# Printing 3
move $a0, $s2
li $v0, 1
syscall

# Printing text2
la $a0, text2
li $v0, 4
syscall

# Printing result
move $a0, $t2
li $v0, 1
syscall

# Printing text3
la $a0, text3
li $v0, 4
syscall 

# Printing remainder
move $a0, $t3
li $v0, 1
syscall

# Printing newline
la $a0, newline
li $v0, 4
syscall

			# Now printing the average of the three numbers

# Adding 10+5+3 and then dividing by 3
move $t0, $s0
move $t1, $s1
move $t2, $s2
add $t3, $t0, $t1
add $t4, $t2, $t3
div $t5, $t4, 3

# Printing text4
la $a0, text4		
li $v0, 4		# Prints string
syscall

# Printing the average
move $a0, $t5
li $v0, 1
syscall

