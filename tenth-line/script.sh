#!/bin/bash

awk '{ if (NR == 10) { print $0; exit; }  }' file.txt
