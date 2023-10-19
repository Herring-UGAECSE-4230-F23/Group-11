@ Deliverable 1: What is the function of the program?
@ Deliverable 2: What is the function of ".req"?
@ Deliverable 3: Describe the bhs instruction.  How does it work?  
@ Deliverable 4: What is the final value in R0 at end of program (In decimal)
@ Deliverable 5: Now, change the bhs instruction to an instruction that will find the lowest value.  Show your program with the change.

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
	ldr	next,[pointer]	@ load next with contents at address
					@ in pointer
	cmp	max, next		@ compare max and next
	bhs	ctnu			@ if max > next branch to ctnu
	mov	max, next		@ max = next
ctnu:	
	add	pointer, pointer, #4	@ increment pointer for next word
	subs	count, count, #1	@ decrement counter		
	bne	again			@ branch again if counter is not zero

	mov	r0, max
	mov 	r7, #1
	svc 0
