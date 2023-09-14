	@ Deliverable: State the contents of memory locations at data_store after the program is executed.  Add instructions prior to the 
 	@ the last two instructions to show the contents of data_store in registers R2 and R3
	@ Deliverable: What does the strb instruction do?
 	@ Deliverable: What does the .space compiler directive do?
	@ Deliverable: Add the classinclude.s include file with changes to last two lines.

.include "classinclude.s"

	.global _start
_start:
	mov	r1, #0x99	@ r1 = 0x99
	ldr	r6, =data_store	@ r6 = data_store pointer
	strb	r1, [r6]	@ store r1 into location pointed to by r6 
				@ 
	add	r6, r6, #1	@ r6 = r6 + 1
	mov	r1, #0x85	@ r1 = 0x85
	strb	r1, [r6]	@ store r1 into location pointed to by r6 
				@ 
	add	r6, r6, #1	@ r6 = r6 + 1
	mov	r1, #0x3f	@ r1 = 0x3f
	strb	r1, [r6]	@ store r1 into location pointed to by r6 

	add	r6, r6, #1	@ r6 = r6 + 1
	mov	r1, #0x63	@ r1 = 0x63
	strb	r1, [r6]	@ store r1 into location pointed to by r6 

	add	r6, r6, #1	@ r6 = r6 + 1
	mov	r1, #0x12	@ r1 = 0x12
	strb	r1, [r6]	


	ldr    r2, [r6, #-5]
	ldr	   r3, [r6, #-1]
	

	mov	r7, #sys_exit
	svc	#sys_restart_syscall
 
	.data
 data_store: .space 8
