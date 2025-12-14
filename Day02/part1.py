from tqdm import tqdm

answer = 0
day = 2
fname = "example.txt"
fname = "input.txt"
fpath = f"./Day{day:02d}/{fname}"

with open(fpath) as f:
    line = f.readline().rstrip("\n")

ids = []
id_ranges = line.split(",")
for id_range in id_ranges:
    start, end = map(int, id_range.split("-"))
    for id in range(start, end + 1):
        ids.append(id)

for id in tqdm(ids):
    sid = str(id)
    if len(sid) % 2 == 1:
        continue
    l = sid[0:int(len(sid)/2)]
    r = sid[int(len(sid)/2):]
    if l == r:
        answer += id




print(answer)
