answer = 0
day = 4
fname = "example.txt"
fname = "input.txt"
fpath = f"./Day{day:02d}/{fname}"

with open(fpath) as f:
    grid = [line.rstrip("\n") for line in f]

for l in range(len(grid)):
    grid[l] = "." + grid[l] + "."
grid.insert(0, "." * len(grid[0]))
grid.append("." * len(grid[0]))


def get_accessible_rolls_coords(grid):
    accessible_coords = []
    for row_id, row in zip(range(len(grid)), grid):
        for col_id, col in zip(range(len(row)), row):
            if col == ".":
                continue
            u = 1 if grid[row_id - 1][col_id] == "@" else 0
            d = 1 if grid[row_id + 1][col_id] == "@" else 0
            l = 1 if grid[row_id][col_id - 1] == "@" else 0
            r = 1 if grid[row_id][col_id + 1] == "@" else 0

            ul = 1 if grid[row_id - 1][col_id - 1] == "@" else 0
            ur = 1 if grid[row_id - 1][col_id + 1] == "@" else 0
            dl = 1 if grid[row_id + 1][col_id - 1] == "@" else 0
            dr = 1 if grid[row_id + 1][col_id + 1] == "@" else 0

            adj_count = u + d + l + r + ul + ur + dl + dr
            if adj_count < 4:
                accessible_coords.append((row_id, col_id))
    return accessible_coords

keep_going = True
while keep_going:
    coords = get_accessible_rolls_coords(grid=grid)
    if len(coords) == 0:
        keep_going = False
        continue
    for coord in coords:
        # grid[coord[0]][coord[1]] = "."
        grid[coord[0]] = grid[coord[0]][:coord[1]] + "." + grid[coord[0]][coord[1]+1:]
        answer += 1
    
        # for row in grid:
        #     print(row)

        # print("")
    


print(answer)
