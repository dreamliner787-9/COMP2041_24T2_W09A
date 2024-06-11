#!/bin/dash

if [ "$#" = "1" ];
then

    begin="1"
    step="1"
    end="$1"

elif [ "$#" = "2" ];
then

    begin="$1"
    step="1"
    end="$2"

elif [ "$#" = "3" ];
then

    begin="$1"
    step="$2"
    end="$3"

fi

# example: how to check if a string/variable is a number:
if ! [ "$1" -eq "$1" ] 2>/dev/null;
then
    echo "first arg is not a number"
    exit 1
fi

cur="$begin"
while [ "$cur" -le "$end" ];
do
    echo "$cur"
    cur=$(( $cur + $step ))
done
