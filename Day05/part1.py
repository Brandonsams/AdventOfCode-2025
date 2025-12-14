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
    fresh_id_ranges.append((start,end))
        
for id_ingredient in tqdm(id_ingredients):
    id = int(id_ingredient)
    is_fresh = False
    for fresh_id_range in fresh_id_ranges:
        if id >=fresh_id_range[0]:
            if id <=fresh_id_range[1]:
                is_fresh = True
                answer += 1
                break


print(answer)
