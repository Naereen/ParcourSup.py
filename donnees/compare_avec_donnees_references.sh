#!/usr/bin/env bash
# Vérifie la concordance de CHAQUE fichier XML présents ici
# avec ceux des exemples de algorithmes-de-parcoursup.git
#
# ./compare_avec_donnees_references.sh
# Comportement par défaut, pour chaque fichier avec (au moins) une différence, affiche les différences
# puis attends que l'utilisateur appuie sur "entrée" pour continuer au suivant.
#
# ./compare_avec_donnees_references.sh --batch
# Affiche toutes les différences sans interactivité.
#

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
    if [ ! -f "$dossierref/$i" ]; then
        continue
    fi
    echo "- Checking $i ..."
    output="$($difftool {./,"$dossierref/"}"$i")"
    if [ ! -z "$output" ]; then
        echo -e "$output"
        [ ! X"$1" = X"--batch" ] && read  # DEBUG
    else
        echo "  Perfectly matching $dossierref/$i"
    fi
done