#!/usr/bin/env bash
# Vérifie la concordance de CHAQUE fichier XML présents ici
# avec ceux des exemples de algorithmes-de-parcoursup.git

dossierref="algorithmes-de-parcoursup.git/doc/exemples"

difftool=diff
if type icdiff > /dev/null; then
    difftool=icdiff
fi

output=""
for i in *.xml; do
    if [ ! -z "$output" ]; then
        clear
    fi
    echo "- Checking $i ..."
    output="$($difftool {./,"$dossierref/"}"$i")"
    if [ ! -z "$output" ]; then
        read  # DEBUG
    else
        echo "  Perfectly matching $dossierref/$i"
    fi
done