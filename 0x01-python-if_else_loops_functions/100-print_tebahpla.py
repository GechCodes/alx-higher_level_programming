#!/usr/bin/python3
# 100-print_tebahpla.py

"""Print the alphabet in reversre order aliternating upper- and lower-case."""
a = 0
for c in range(ord('z', ord('a') - 1, -1):
        print("{}".format(chr(c - a)), end="")
        a = 32 if a == 0 else 0

