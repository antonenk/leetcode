#!/bin/bash

for WORD in `cat words.txt`; do echo $WORD; done | sort | uniq -c | sort -n -r | awk '{print $2 " " $1}'
