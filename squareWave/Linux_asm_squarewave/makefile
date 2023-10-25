OBJS = Linux_asm_squarewave.o
ifdef DEBUG
DEBUGFLGS = -g
else
DEBUGFLGS =
endif

%.o : %.s
	as $(DEBUGFLGS) $< -o $@
GPIO_ON: $(OBJS)
	gcc -o Linux_asm_squarewave $(OBJS)

clean:
	rm *.o Linux_asm_squarewave
