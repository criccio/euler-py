#!/usr/bin/python
from riccio import get_permutations

value = "0123456789"
print sorted(get_permutations(value))[999999]