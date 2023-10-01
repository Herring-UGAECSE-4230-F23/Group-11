@ This program looks at 8-bit signed numbers and how to use the sign extended instructions. Make sure you consider the answers as 8-bit.
@ Deliverable 1: What are the V, N, and C flags after the first adds instruction executes?
@ Deliverable 2: What is the expected and actual result?  Is it correct?
@ Deliverable 3: Now, look at the second example.  What does the ldsrb instruction do?
@ Deliverable 4: What are the V, N, and C flags after the second adds instruction?
@ Deliverable 5: What is the expected and actual result of the second adds?  Is it correct?


	.data
data1: 	.byte 	-128
data2: 	.byte  -2
result:	.byte	0

	.text
	.global _start

_start:
	
@First example

	ldr	r1, =data1
	ldr	r2, =data2
	ldr	r3, =result
	
	ldrb 	r4, [r1]	@ r4 = -128
	ldrb 	r5, [r2]	@ r5 = -2
	adds	r4, r4, r5	@ r4 = r4 + r5 = ???
	str	r4, [r3]	@store result in location result

@Second Example

	ldrsb 	r4, [r1]	@ r4 = -128
	ldrsb 	r5, [r2]	@ r5 = -2
	adds	r4, r4, r5	@ r4 = r4 + r5 = ???
	str	r4, [r3]	@store result in location


	mov 	r7, #1
	svc 0
