// Created by: Maxwell Young
//Date Retrieved: February 10, 2017

JFLAGS = -g
JCC = javac

default: client.class server.class 

client.class: client.java
	$(JCC) $(JFLAGS) client.java

server.class: server.java
	$(JCC) $(JFLAGS) server.java

clean: 
	$(RM) *.class received.txt