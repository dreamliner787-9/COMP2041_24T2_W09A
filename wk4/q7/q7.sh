#!/bin/dash

zid=$1

acc $1 | grep -E '_Student' | cut -d':' -f2 | cut -d' ' -f2 | grep -E '^[A-Z]{4}[0-9]{4}t[123]' | cut -d'_' -f1 | sed -E 's/.{2}$//'
