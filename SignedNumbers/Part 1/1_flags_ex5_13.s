@ Assume you are using signed 32 bit signed numbers
@ Deliverable1:What are the states of the V, N, and C flags after the first adds instruction?
@ Deliverable2:For the first adds, what is the expected and actual result?  Is the result correct?
@ Deliverable3:What are the states of the V, N, and C flags after the second adds instruction?
@ Deliverable4:For the second adds, what is the expected and actual result?  Is the result correct?
@ Deliverable5:What are the states of the V, N, and C flags after the third adds instruction?
@ Deliverable6:For the third adds, what is the expected and actual result?  Is the result correct?
@ Deliverable7:What are the states of the V, N, and C flags after the fourth adds instruction?
@ Deliverable8:For the fourth adds, what is the expected and actual result?  Is the result correct?
@ Deliverable9:What do the V, N, and C flags tell you?

	.data
data1: 	.word 0x6E2F356F
data2: 	.word 0x13D49530
data3:  .word 0x542F356F
data4:  .word 0x12E09530
data5:  .word 0x80000000
data6:  .word 0xFFFFFFFF
data7:  .word 0xFFFFFFFE
data8:  .word 0xFFFFFFFB
result:	.word 0
result2: .word 0
result3: .word 0
result4: .word 0

	.text
	.global _start

_start:
@First example
	
	ldr	r1, =data1
	ldr	r2, =data2
	ldr	r3, =result
	
	ldr 	r4, [r1]	@ r4 = ???
	ldr 	r5, [r2]	@ r5 = ???
	adds	r4, r4, r5	@ r4 = r4 + r5 = ???, or does it?
	str	r4, [r3]	@store result in location

@Second example
	ldr	r1, =data3
	ldr	r2, =data4
	ldr	r3, =result2
	
	ldr 	r4, [r1]	@ r4 = ??
	ldr	r5, [r2]	@ r5 = ??
	adds	r4, r4, r5	@ r4 = r4 + r5 = ???, or does it?
	str	r4, [r3]	@store result in location

@Third example
	ldr	r1, =data5
	ldr	r2, =data6
	ldr	r3, =result3
	
	ldr 	r4, [r1]	@ r4 = ??
	ldr 	r5, [r2]	@ r5 = ??
	adds	r4, r4, r5	@ r4 = r4 + r5 = ???, or does it?
	str	r4, [r3]	@store result in location

@Fourth example
	ldr	r1, =data7
	ldr	r2, =data8
	ldr	r3, =result4
	
	ldr 	r4, [r1]	@ r4 = ??
	ldr 	r5, [r2]	@ r5 = ??
	adds	r4, r4, r5	@ r4 = r4 + r5 = ???, or does it?
	str	r4, [r3]	@store result in location

	mov 	r7, #1
	svc 0
