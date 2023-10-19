@ Deliverable 1: Describe the function of the program.
@ Deliverable 2: At the finish of the program, what does r0 contain?  What does r2 contain?
@ Deliverable 3: What is the function of the "blo" instruction?
@ Deliverable 4: What is the function of the "b" instruction?
@ Deliverable 5: Change the "blo" instruction to another bxx instruction that will give the same result.  Show your code.

	.text
	.global _start
_start:
	   
	ldr	r0, =2012	@ r0 = 2012 (numerator)
				@ it will contain remainder
	mov	r1, #10	@ r1 = 10 (denominator)
	mov	r2, #0		@ r2 = 0 (quotient)
l1:	cmp	r0, r1		@ compare r0 with r1 to see if less than 10
	blo	finish		@ if r0 < r1 jump to finish
	sub	r0, r0, r1	@ r0 = r0 - r1 (division by subtraction)
	add	r2, r2, #1	@ r2 = r2 + 1 (quotient is incremented) 
	b	l1		@ goto l1 (b is discussed in the next section)
finish:
	mov 	r7,#1
	svc 	0
