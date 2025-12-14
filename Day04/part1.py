answer = 0
day = 4
fname = "example.txt"
fname = "input.txt"
fpath = f"./Day{day:02d}/{fname}"

with open(fpath) as f:
    lines = [line.rstrip("\n") for line in f]

for l in range(len(lines)):
    lines[l] = "." + lines[l] + "."
lines.insert(0, "." * len(lines[0]))
lines.append("." * len(lines[0]))

for r, row in zip(range(len(lines)), lines):
    for c, col in zip(range(len(row)), row):
        if col == ".":
            continue
        u = 1 if lines[r - 1][c] == "@" else 0
        d = 1 if lines[r + 1][c] == "@" else 0
        l = 1 if lines[r][c - 1] == "@" else 0
        right = 1 if lines[r][c + 1] == "@" else 0

        ul = 1 if lines[r - 1][c - 1] == "@" else 0
        ur = 1 if lines[r - 1][c + 1] == "@" else 0
        dl = 1 if lines[r + 1][c - 1] == "@" else 0
        dr = 1 if lines[r + 1][c + 1] == "@" else 0

        adj_count = u + d + l + right + ul + ur + dl + dr
        if adj_count < 4:
            answer += 1


print(answer)
