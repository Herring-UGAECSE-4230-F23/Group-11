@Deliverable1: Based on a 32 bit architecture, what is the maximum value you can use for a loop variable?
@Deliverable2: How many total loops will this program run?  In other words, how many times will the subs instruction be run?
@Deliverable3: Approximately how long does the program take to run?
@Deliverable4: Given that the RP3 clock speed is 1.5GHz, approximately how many instruction cycles per loop are being used?
@  Note: use your approximate total run time and number of loops to help with this. Also note, that in ARM architecture each instruction is a clock (mostly).
@Deliverable5: Add a label to stop on each outer loop.  Add a label to stop when all loops are done but before the terminate.

	.text
	.global _start

_start:	

	mov	r2, #15		@ load 15 into r2 (outer loop count)

l1:	ldr	r1, =1000000000	@ r1 = 1,000,000,000 (inner loop count) 
l2:	subs	r1, r1, #1		@ r1 = r1 – 1, decrement r1 (inner loop) 
	bne	l2			@ repeat it until r1 = 0 
	subs	r2, r2, #1		@ r2 = r2 – 1, decrement r2 (outer loop) 
	bne	l1			@ repeat it until r2 = 0 

	@ terminate the program
	mov   	r7, #1
	svc   0
