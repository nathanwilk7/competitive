c = set([2, 3, 4, 7, 8, 9, 10])
d = set([2, 3, 4, 7, 8, 9])
e = set([2, 3, 4, 7, 8])
f = set([2, 3, 4, 7])
g = set([2, 3, 4])
a = set([2, 3])
b = set([2])
C = set([3])
D = set([1, 2, 3, 4, 7, 8, 9])
E = set([1, 2, 3, 4, 7, 8])
F = set([1, 2, 3, 4, 7])
G = set([1, 2, 3, 4])
A = set([1, 2, 3])
B = set([1, 2])

notes = {}
notes['c'] = c
notes['d'] = d
notes['e'] = e
notes['f'] = f
notes['g'] = g
notes['a'] = a
notes['b'] = b
notes['C'] = C
notes['D'] = D
notes['E'] = E
notes['F'] = F
notes['G'] = G
notes['A'] = A
notes['B'] = B

import sys

num_songs = int(sys.stdin.readline())

current = set()
next = set()
import pdb
for j in range(num_songs):
    counts = [0] * 11
    song = sys.stdin.readline().strip()
    #pdb.set_trace()
    num_notes = len(song)
    if num_notes == 0:
        print('0 0 0 0 0 0 0 0 0 0')
        continue
    first = notes[song[0]]
    for button in first:
        counts[button] += 1
    for i in range(num_notes - 1):
        current = notes[song[i]]
        next = notes[song[i+1]]
        new_buttons = next.difference(current)
        for button in new_buttons:
            counts[button] += 1
    for i in range(1, 11):
        print(counts[i], end=' ')
    print()
        
        
