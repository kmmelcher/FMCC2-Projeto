extra.o: extra.cpp
	g++ extra.cpp -o extra.o
	./extra.o

clean:
	rm *.o

run:
	./extra.o
