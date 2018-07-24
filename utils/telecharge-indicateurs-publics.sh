#!/usr/bin/env bash
# Author: Lilian Besson
# For https://github.com/Naereen/ParcourSup.py
# License: MIT (https://lbesson.mit-license.org/)
# Date: July 2018
#

# Change here if needed
baseURL="http://www.enseignementsup-recherche.gouv.fr/cid130714/tableaux-de-bord-des-indicateurs-de-parcoursup.html"
output="/tmp/telecharge-indicateurs-publics.html"

wget "$baseURL" -O "$output"

outdir="indicateursPublics/"
mkdir "$outdir"
cd "$outdir"

for pdf in $(grep -o '//cache.[^"]*.pdf' "$output" | uniq | sort | uniq); do
    wget "http:$pdf"
done
cd ..

ls -larth "$outdir"
du -khc "$outdir"
echo "Done..."
