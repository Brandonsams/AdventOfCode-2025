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
    len_sid = len(sid)
    for part_length in range(1, len_sid):
        if len_sid % part_length != 0:
            continue
        chunks = set([sid[i : i + part_length] for i in range(0, len_sid, part_length)])
        if len(chunks) == 1:
            answer += id
            break


print(answer)
