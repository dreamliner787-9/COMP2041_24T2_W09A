#!/bin/dash

i=0
for commit_message in .grip/master/commits/*
do
    echo $i $(basename "$commit_message")
    i=$((i + 1))
done