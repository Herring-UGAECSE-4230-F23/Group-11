@ This program will sum together a group of signed numbers.
@ This program also introduces our first loop using the bne instruction.  
@ Deliverable 1: What is the expected result of the sum of the numbers?
@ Deliverable 2: Describe how the program works
@ Deliverable 3: What is the bne instruction? 
@ Deliverable 4: What is the value of the Z flag when the program loops?  and when it does not loop?


.data
sign_dat: .byte 	+13, -10, +19, +14, -18, -9, +12, -19, +16
sum:	.word	0

.text

.global _start

_start:	
	ldr	r0, =sign_dat
	mov	r3, #9
	mov	r2, #0
loop:	ldrsb 	r1, [r0]  
	@ load into r1 and sign extend it.			
	add	r2, r2, r1	@ r2 = r2 + r1
	add	r0, r0, #1	@ point to next
	subs	r3, r3, #1	@ decrement counter
	bne	loop
	ldr 	r0, =sum
	str	r2, [r0]	@ store r2 in location sum
	mov 	r7, #1
	svc 	0
