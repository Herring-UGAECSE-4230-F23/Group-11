@This program finds the lowest of signed numbers.  This program introduces b, beq, cmp, and movlt (conditional mov instruction)
@ Deliverable 1: Describe how the program works.  Make sure you describe the pointer and counter function.
@ Note: For each of 2-5, make sure you include flags in your discussion of "how does it work"
@ Deliverable 2: What is the beq instruction and how does it work?
@ Deliverable 3: What is the cmp instruction and how does it work?
@ Deliverable 4: What is the movlt instruction and how does it work?
@ Deliverable 5: What is the b instruction and how does it work?
@ Deliverable 6: Change the program by changing the conditional mov instruction so that the program finds the largest of the signed numbers.  Show your final code.

	.data
sign_dat:  .byte 	+13, -10, +19, +14, -18, -9, +12, -19, +16
	.align
lowest:	.word     0

	.text
	.global _start
_start:
       ldr	r0, =sign_dat
       mov	r3, #9
       ldrsb	r2, [r0]    @ bring first number into r2 and sign extend it
loop:  
	add   	r0, r0, #1  @ point to next
      	subs  	r3, r3, #1  @ decrement counter
      	beq  	done        @ if r3 is zero, done
      	ldrsb 	r1, [r0]    @ bring next number into r1 and sign extend it
      	cmp  	r1, r2      @ compare r1 and r2
      	movgt	r2, r1      @ if r1 is bigger, keep it in r2
      	b    	loop
done: 	
	ldr  	r0, =lowest @ r0 = address of lowest
      	str 	r2, [r0]    @ store r2 in location lowest
	mov 	r7, #1
	svc 	0
