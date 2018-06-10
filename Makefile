# Makefile for https://github.com/Naereen/ParcourSup.py
SHELL=/usr/bin/env /bin/bash
all:	test

# sender
send:	send_zamok
send_zamok:
	CP --exclude=.git ./ ${Szam}publis/ParcoursSup.py.git/

# environment
# TODO bring back this!
pypenv:
	virtualenv env
	source ./env/bin/activate ; type pip python
install:	pypenv
	source ./env/bin/activate ; pip install -r requirements.txt

# tests and runners
tests:	tests_ordreappel tests_propositions tests_donnees_xml

tests_ordreappel:
	cd ./parcoursup/ordreappel/ ; python3 ./__init__.py

tests_donnees_xml:
	cd ./donnees/ ; ./compare_avec_donnees_references.sh

tests_propositions:
	cd ./parcoursup/propositions/ ; python3 ./__init__.py

# Cleaner
clean:
	-rm -vfr __pycache__/ */__pycache__/ */*/__pycache__/ */*/*/__pycache__/ */*/*/*/__pycache__/
	-rm -vf *.pyc */*.pyc */*/*.pyc */*/*/*.pyc */*/*/*/*.pyc */*/*/*/*.pyc

# Linters
# NPROC = `nproc`
# NPROC = 1
NPROC = `getconf _NPROCESSORS_ONLN`

lint:
	cd ./parcoursup/ ; pylint -j $(NPROC) *.py */*.py | tee ../logs/pylint_log.txt
	cd ./parcoursup/ ; pylint --py3k -j $(NPROC) *.py */*.py | tee ../logs/pylint3_log.txt


#-----------------------------------------------------------------
#
# Minimal makefile for Sphinx documentation
#
# You can set these variables from the command line.
SPHINXOPTS    =
SPHINXBUILD   = sphinx-build
SPHINXPROJ    = ParcourSup.py
SOURCEDIR     = docs
BUILDDIR      = build

apidoc:
	# cd src ; sphinx-apidoc -f -o ../docs -e -M .
	sphinx-apidoc -f -o ./docs -e -M ./parcoursup

html:
	@$(SPHINXBUILD) -M html "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
