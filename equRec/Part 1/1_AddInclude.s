@look at the unistd.s file.  This introduces the .EQU directive which assigns values to variable.
@Deliverable 1: Compile and run the program
@Deliverable 2: Change the last two lines to use meaningful variable names from the classinclude.s file.  Rerun your program.  
@Deliverable 3: What does the .include mean/do in the program?

.include "classinclude.s"

.global _start

_start:
        @This stores 20 in R1 then adds 10 ro that and stores the it in R0
        MOV R1, #0x14
        ADD R0, R1, #0xA
        MOV R7, #sys_exit
        SWI #sys_restart_syscall
