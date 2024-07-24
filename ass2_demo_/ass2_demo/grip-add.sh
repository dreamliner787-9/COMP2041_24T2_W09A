#!/bin/dash

for file_to_add in $@
do
    if ! [ -f $file_to_add ];
    then
        touch ".grip/master/staging/?$file_to_add"
        rm ".grip/master/staging/$file_to_add"
    else
        cp $file_to_add ".grip/master/staging/$file_to_add"
    fi
done