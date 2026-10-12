.data

str: .asciiz "Hello world!"
newline: .asciiz "\n"

.text

.globl main

main:
# Main procedure
jal helloworld

# exit program
li $v0, 10
syscall

helloworld:
# write your code starting here
la $a0, str
li $v0, 4
syscall

la $a0, newline
li $v0, 4
syscall
