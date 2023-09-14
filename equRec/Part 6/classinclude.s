@
@ Defines for the Linux system calls.
@ Original list is from Raspbian Buster
@ Shortened for class

.EQU sys_restart_syscall,		0	@ restart a system call after interruption by a stop signal
.EQU sys_exit,				1	@ cause normal process termination
.EQU sys_fork,				2	@ create a child process
.EQU sys_read,				3	@ read from a file descriptor
.EQU sys_write,				4	@ write to a file descriptor
.EQU sys_open,				5	@ open and possibly create a file
.EQU sys_close,				6	@ close a file descriptor
.EQU sys_creat,				8	@ create a new file or rewrite an existing one
.EQU sys_link,				9	@ make a new name for a file
.EQU sys_unlink,			10	@ delete a name and possibly the file it refers to
