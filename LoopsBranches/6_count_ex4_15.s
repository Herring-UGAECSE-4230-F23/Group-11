@ Deliverable 1: What is the function of this program?
@ Deliverable 2: What is the function of the "addcs" instruction?
@ Deliverable 3: Add a lable so the you can break when the program does not loop.  Show your program.
@ Deliverable 4: Change the "addcs" instruction so that the program counts zeros. Show your program.


	.text
	.global _start
_start:
	ldr	r0, =0x34f37d36
	mov	r1, #0	
	mov	r2, #32	@ counter
begin:	movs	r0, r0, rrx	@ rotate right with carry the r0 register
	addcs	r1, r1, #1	@ if c = 1 then increment r1
	subs	r2, r2, #1	@ decrement counter
	bne	begin   	@ if counter is not equal to zero branch begin
	mov 	r7, #1
	svc 0
