import sys


def belly(track, start, end):
  width = 3
  for p in range(end-start+1):
    if track[start+p] == 1:
      return 1
    if track[start+p] == 2:
      width = 2
  return width
ser
lines = sys.stdin.readlines() # or read() to read the whole thing no line separated

N = int(lines[0].split()[0])
T = int(lines[0].split()[1])
LANE = map(int, lines[1].split())

lines = lines[2:] # equivalent to .shift() 2x

for k in range(T):
  i = int(lines[k].split()[0])
  j = int(lines[k].split()[1])

  result = belly(LANE, i, j)
  print result