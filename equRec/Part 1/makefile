#This OBJS is just a variable that we can define as the file we would like to create
OBJS = 1_AddInclude.o

#This statement is for if the user types make DEBUG=1 then the DEBUGFLGS variable is -g
ifdef DEBUG
DEBUGFLGS = -g

#If the user did not define the make DEBUG=1 then there are no debug flags
else
DEBUGFLGS =
endif

#The % is a wildcard character and in the case below it reads as for all .s files create a .o file with the DEBUGFLGS as outputs
%.o : %.s
	as $(DEBUGFLGS) $< -o $@
1_AddInclude: $(OBJS)
	ld -o 1_AddInclude $(OBJS)

#This allows the user to type make clean to remove all the .o files without having to manually delete them all
#the * is also a wildcard character character and says for all .o files remove
clean: $(OBJS)
	rm *.o 1_AddInclude