@This program introduces the LDRB, LDRH, and LDR commands and [xx] indirect addressing
@Deliverable 1: What is loaded into R2?  and into R0?
@Deliverable 2: What is the ldrb instruction doing and how does the indirect addressing work?
@Deliverable 3: Change ldrb to ldrh.  Rerun the program.  What is the value of R0?  What is ldrh doing?
@Deliverable 4: change ldrh to ldr.  Rerun the program.  What is the value of R0?  Explain the difference in ldrb, ldrh, and ldr.
@Deliverable 5: What would you add to our_fixed_data to read the values in the .word line?  the .hword line?  Try ldr r0, [r2, #8].  What is r0?

@Deliverable 3: Use the include file.

	.text
	.global _start
_start:	ldr	r2, =our_fixed_data
	ldr	r0, [r2, #8]
	mov	r7, #1
	svc	0

our_fixed_data:
	.byte	0x55, 0x33, 1, 2, 3, 4, 5, 6
	.word 	0x23222120, 0x30
	.hword	0x4540, 0x50
