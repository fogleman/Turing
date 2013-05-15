all: turing.dll

turing.dll: turing.o
	gcc -shared -o turing.dll turing.o

turing.o: turing.c
	gcc -std=c99 -O3 -c -o turing.o turing.c
