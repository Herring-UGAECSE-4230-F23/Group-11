@ Deliverable:  Describe the function of the program.
@ Deliverable:  Describe the bne instruction
@ Deliverable:  How many times does the program loop?
@ Deliverable:  What is the value of the sum at the end of the program?
@ Deliverable: What flag is being checked for the bne and what is the value of the flag for the loop to not go back to "again"?
@ Deliverable:  Change the program by adding a label so that you can set a breakpoint on the first instruction after the bne instruction.  Show your program with the change.

	.text
	.global _start
_start:	ldr 	r2, =1000	@ r2 = 1000 (decimal) for counter 
		mov	r0, #0 	@ r0 = 0 (sum)
again: 	add 	r0, r0, #9	@ r0 = r0 + 9 (add 09 to r0, r0 = sum)
		subs	r2, r2, #1	@ decrement counter and set the flags. 
		bne 	again		@ repeat until count = 0
		mov 	r4, r0		@ store the sum in r4
 	
		mov   	r7, #1
		svc  	0

