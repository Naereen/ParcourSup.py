#!/usr/bin/env bash
# Vérifie la concordance de CHAQUE fichier XML présents ici
# avec ceux des exemples de algorithmes-de-parcoursup.git

dossierref="/home/lilian/Bureau/algorithmes-de-parcoursup.git/doc/exemples/"

difftool=diff
if type icdiff > /dev/null; then
    difftool=icdiff
fi

for i in *.xml; do
    clear
    echo "Checking $i ..."
    $difftool {./,"$dossierref"}"$i"
    read  # DEBUG
done