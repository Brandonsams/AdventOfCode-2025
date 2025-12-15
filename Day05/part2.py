from tqdm import tqdm

answer = 0
day = 5
fname = "example.txt"
fname = "input.txt"
fpath = f"./Day{day:02d}/{fname}"

with open(fpath) as f:
    db = f.read()

id_ranges, id_ingredients = db.split("\n\n")
id_ranges = id_ranges.split("\n")
id_ingredients = id_ingredients.split("\n")

fresh_id_ranges = []
for id_range in tqdm(id_ranges):
    start, end = map(int, id_range.split("-"))
    fresh_id_ranges.append((start, end))

fresh_id_ranges.sort(key=lambda x: x[0])

merged = []
for start, end in fresh_id_ranges:
    if not merged or start > merged[-1][1]:  # no overlap
        merged.append([start, end])
    else:  # overlap
        merged[-1][1] = max(merged[-1][1], end)
answer = sum(end - start + 1 for start, end in merged)        

print(answer)
