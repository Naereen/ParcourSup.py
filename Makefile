# Makefile for https://github.com/Naereen/ParcourSup.py
SHELL=/usr/bin/env /bin/bash
all:	test

# sender
send:	send_zamok
send_zamok:
	CP --exclude=.git ./ ${Szam}publis/ParcoursSup.py.git/

# environment
pypenv:
	virtualenv env
	source env/bin/activate ; type pip python

install:	pypenv
	source env/bin/activate ; pip install -r requirements.txt

# tests and runners TODO
test:
	python3 ./src/tests.py
