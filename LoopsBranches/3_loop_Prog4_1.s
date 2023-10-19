@ This program revisits the prior program but uses conditional instructions in place of some of the bxx instructions.
@ Deliverable 1: Describe the function of the program
@ Deliverable 2: What is the function of the movlo instruction, how does it work? 
@ Deliverable 3: What is another mov"xx" instruction that would have the same affect and give same result?  Change the instruction and show your new program.
@ Deliverable 4: Change the movlo instruction so that the program finds the lowest value.  Show your new program. 
@ Deliverable 5: What is another mov"xx" instruction that would have the same result to give lowest value?

   
count	.req	r0		@ count is the new name of r0
max	.req	r1		@ max is the new name of r1 
				@ (max has the highest value)
pointer .req	r2		@ pointer is the new name of r2
next	.req	r3		@ next is the new name of r3

	.data
mydata:	.word	69, 87, 96, 45, 75

	.text
	.global _start
_start:
	mov	count, #5		@ count = 5
	ldr	pointer, =mydata	@ pointer has the address of first data
        ldr 	max, [pointer]          @ load first value of data

again:
	ldr	next, [pointer]		@ load contents of pointer location to next
	cmp	max, next		@ compare max and next		
	movlo	max, next		@ if max is lower than next then max=next
	add	pointer, pointer, #4	@ pointer = pointer  +  4 to point to next 
	subs	count, count, #1	@ decrement counter
	bne	again			@ branch again if counter is not zero

	mov	r7, #1
	svc	0
