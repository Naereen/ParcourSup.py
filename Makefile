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

# tests and runners

tests_ordreappel:
	cd ./src/ordreappel/ ; python3 ./__init__.py

tests_ordreappel.xml:
	cd donnees/ ; ./compare_avec_donnees_references.sh

tests_propositions:
	cd ./src/propositions/ ; python3 ./__init__.py

# Cleaner
clean:
	-rm -vfr __pycache__/ */__pycache__/ */*/__pycache__/ */*/*/__pycache__/ */*/*/*/__pycache__/
	-rm -vf *.pyc */*.pyc */*/*.pyc */*/*/*.pyc */*/*/*/*.pyc */*/*/*/*.pyc

# Linters
# NPROC = `nproc`
# NPROC = 1
NPROC = `getconf _NPROCESSORS_ONLN`

lint:
	cd src/ ; pylint -j $(NPROC) *.py */*.py | tee ../logs/pylint_log.txt
	cd src/ ; pylint --py3k -j $(NPROC) *.py */*.py | tee ../logs/pylint3_log.txt
