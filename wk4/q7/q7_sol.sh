#!/bin/dash

acc | grep -E "[A-Z]{4}[0-9]{4}t._Student" | cut -d':' -f2 | cut -d' ' -f2 | cut -d'_' -f1 | sed -E 's/.{2}$//'
