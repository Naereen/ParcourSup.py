#!/usr/bin/env bash

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
