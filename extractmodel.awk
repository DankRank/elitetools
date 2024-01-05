#!/usr/bin/awk -f
# ./extractmodel.awk ../disk-elite-beebasm/1-source-files/main-sources/elite-{missile,ships-?}.asm | ./parsemodel | ./dedupmodel.py > shipdata.js
# ./extractmodel.awk ../6502sp-elite-beebasm/1-source-files/main-sources/elite-source.asm | ./parsemodel | ./dedupmodel.py > shipdata.js

BEGIN { state == 0 }

{ sub(/\\.*/, "") }

state == 0 && /^\.SHIP_/ { print; state = 1 }
state == 1 && /^ VERTEX/ { print }
state == 1 && /^ EDGE/ { print }
state == 2 && /^ FACE/ { print }
state == 1 && /^ FACE/ { print; state = 2 }
state == 2 && !/^ FACE/ { print ""; state = 0 }
