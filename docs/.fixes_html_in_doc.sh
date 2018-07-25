#!/usr/bin/env bash
# Author: Lilian BESSON, (C) 2018
# Email: Lilian.BESSON[AT]ens-cachan[DOT]fr
# Date: 10/06/2018.
#
# Change the links from .md to .html in the documentation html pages
#
# Usage: ./.fixes_html_in_doc.sh
#

EMOJIZE=emojize.py

cd ..
BUILDDIR=_build/html

for i in "$BUILDDIR"/*.html; do
    # 1. fix links from .md to .html

    echo -e "\n${yellow}Search for wrong links to md files${white} in $i ..."
    grep --color=always '\.md"' "$i"
    # echo -e "${green}OK to replace these '.md\"' by '.html\"' ??${white}"
    # read  # DEBUG
    sed -i.backup -r \
        -e s/'\.md"'/'\.html"'/g \
        "$i"
    echo -e "${blue}Modification done${white}, here is the difference (old, new)"
    wdiff -3 "$i".backup "$i"
    mv -vf "$i".backup /tmp/

    # 3. fix link from Package/File.py to docs/Package.File.html
    echo -e "\n${yellow}Search for wrong links to Python files${white} in $i ..."
    grep --color=always 'href="[^"]*\.py"' "$i"
    # echo -e "${green}OK to replace these 'Package/File.py' by 'docs/Package.File.html' ??${white}"
    # read  # DEBUG
    sed -r \
        -e s_'href="parcoursup/([^"/]*)\.py"'_'href="docs/\1.html"'_g \
        -e s_'href="([^"/]*)\.py"'_'href="docs/\1.html"'_g \
        -e s_'href="parcoursup/([^"/]*)/([^"/]*)\.py"'_'href="docs/\1.\2.html"'_g \
        -e s_'href="([^"/]*)/([^"/]*)\.py"'_'href="docs/\1.\2.html"'_g \
        -e s_'href="parcoursup/([^"/]*)/([^"/]*)/([^"/]*)\.py"'_'href="docs/\1.\2.\3.html"'_g \
        -e s_'href="([^"/]*)/([^"/]*)/([^"/]*)\.py"'_'href="docs/\1.\2.\3.html"'_g \
        -e s_'href="parcoursup/([^"/]*)/([^"/]*)/([^"/]*)/([^"/]*)\.py"'_'href="docs/\1.\2.\3.\4.html"'_g \
        -e s_'href="([^"/]*)/([^"/]*)/([^"/]*)/([^"/]*)\.py"'_'href="docs/\1.\2.\3.\4.html"'_g \
        "$i" > "$i".new

    echo -e "${blue}Modification done${white}, here is the difference (old, new)"
    wdiff -3 "$i" "$i".new
    # read  # DEBUG
    mv -vf "$i".new "$i"

    # 3. convert :emojis: to UTF-8 in HTML output (from GFM Markdown), see https://stackoverflow.com/questions/42087466/sphinx-extension-to-use-github-markdown-emoji-in-sphinx#comment73617151_42256239
    if type $EMOJIZE &>/dev/null ; then
        $EMOJIZE "$i" > "$i".new
    fi
    wdiff -3 "$i" "$i".new
    # read  # DEBUG
    mv -vf "$i".new "$i"
    rm -vf "$i".new2
done

# End of newscript.sh
