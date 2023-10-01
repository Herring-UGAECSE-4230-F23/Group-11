@ This program looks for the negative of a number.  It introduces the cmn instruction
@ Deliverable 1: Explain how the program works.  Make sure you describe the pointer/counters
@ Deliverable 2: What is the cmn instruction and how does it work?
@ Deliverable 3: What does the program do if a match is not found?
@ Deliverable 4: Change one instruction only so that the program finds the match of the number (not the negative of the number).  Show your program.

	.data
our_data:	.byte 	+13, -10, +13, +14, -18, -9, +12, +13, -19, +16

	.text
	.global _start
_start:

		mov	r5, #13
		ldr	r0, =our_data
		mov	r3, #9	
begin:
		ldrsb r1, [r0]   @ r1 = contents of loc. pointed to by r0 (sign extended)
		cmp	r1, r5		@ compare r1 and negative of r5
		beq 	found		@ branch if r1 is equal to negative of r5

		adds	r0, r0, #1	@ increment pointer
		subs	r3, r3, #1	@ decrement counter
		bne	begin		@ if r3 is not zero branch begin

not_found: 	b	not_found
found:		b	found
		mov 	r7, #1
		svc 	0
