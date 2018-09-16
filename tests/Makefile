# Makefile pour lancer les tests avec behave
tests:	tests_ordreappel

tests_ordreappel:	tests_ordreappel1 tests_ordreappel2
tests_ordreappel1:
	behave ordreappel-4-1.feature
	behave ordreappel-4-1.feature > ../logs/ordreappel-4-1_tests.txt
tests_ordreappel2:
	behave ordreappel-4-2.feature
	behave ordreappel-4-2.feature > ../logs/ordreappel-4-2_tests.txt

tests_propositions:	tests_propositions1 tests_propositions2
tests_propositions1:
	behave propositions-5-1-bmax.feature
	behave propositions-5-1-bmax.feature > ../logs/propositions-5-1-bmax_tests.txt
tests_propositions2:
	behave propositions-5-1-internat-1.feature
	behave propositions-5-1-internat-1.feature > ../logs/propositions-5-1-internat-1_tests.txt
