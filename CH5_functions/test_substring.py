from substring import pos_leftmost_occ

assert pos_leftmost_occ("abcdef", "bcd") == 1
assert pos_leftmost_occ("abcdef", "bdc") == None
assert pos_leftmost_occ("abcdef", "abc") == 0
assert pos_leftmost_occ("abcdef", "def") == 3
assert pos_leftmost_occ("abcdef", "abcdef") == 0
assert pos_leftmost_occ("abcdef", "") == 0
assert pos_leftmost_occ("", "") == 0
assert pos_leftmost_occ("abcdef", "abcdefg") == None
assert pos_leftmost_occ("abcdef", "defg") == None
assert pos_leftmost_occ("abcdef", "zab") == None
assert pos_leftmost_occ("abcabd", "ab", 1, 5) == 3
assert pos_leftmost_occ("abab", "ab", 1, 2) == None
assert pos_leftmost_occ("abab", "ab", 2, 4) == 2