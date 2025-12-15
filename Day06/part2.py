from tqdm import tqdm
import pandas as pd
import math

answer = 0
day = 6
fname = "example.txt"
fname = "input.txt"
fpath = f"./Day{day:02d}/{fname}"

with open(fpath) as f:
    lines = [line.rstrip("\n") for line in f]

op = ""
vals = []
for l in list(zip(*lines)):
    if len(set(list(l))) == 1:
        # calculate result
        result = None
        if op == "*":
            result = math.prod(vals)
        else:
            result = sum(vals)
        answer += result
        op = ""
        vals = []
        continue

    op = op if l[-1] == " " else l[-1]
    val = int("".join(list(l)[0:-1]).replace(" ", ""))
    vals.append(val)

# calculate FINAL result
result = None
if op == "*":
    result = math.prod(vals)
else:
    result = sum(vals)
answer += result

print(answer)
