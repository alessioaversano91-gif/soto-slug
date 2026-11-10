#!/bin/bash
# Full regression. Tests that wait on the real clock (cardog, func, touch) are flaky when four browsers share the CPU,
# so they run one at a time; anything that fails is run once more alone before being reported.
cd "$(dirname "$0")"; L=${TMPDIR:-/tmp}/soto_reg; rm -rf "$L"; mkdir -p "$L"
SERIAL="cardog_test.py func_test.py"
bad(){ [ "$2" != 0 ] || grep -qE "FAIL|Traceback" "$L/$1.log"; }
run(){ python3 "$1" > "$L/$1.log" 2>&1; echo "$1 $?"; }
export -f run; export L
PAR=$(ls *_test.py | grep -vxF -f <(tr ' ' '\n' <<<"$SERIAL"))
{ echo "$PAR" | xargs -P 4 -I{} bash -c 'run {}'; for t in $SERIAL; do run $t; done; } > "$L/_res.txt"
FAILED=""; RETRIED=""
while read t rc; do if bad "$t" "$rc"; then RETRIED="$RETRIED $t"; python3 "$t" > "$L/$t.log" 2>&1; bad "$t" $? && FAILED="$FAILED $t"; fi; done < "$L/_res.txt"
echo "tests: $(wc -l < "$L/_res.txt")  retried:${RETRIED:- none}  failed:${FAILED:- none}  (logs in $L)"
[ -z "$FAILED" ]
