from tqdm import tqdm
import pandas as pd
import math

answer = 0
day = 6
fname = "example.txt"
fname = "input.txt"
fpath = f"./Day{day:02d}/{fname}"

df = pd.read_csv(fpath, sep=r"\s+", header=None)

last_row = df.iloc[-1].squeeze()
df = df.iloc[:-1]
df = df.astype(int)


for op, (col_name, col_data) in tqdm(zip(list(last_row),df.items())):
    col = col_data.tolist()
    result = None
    if op == "*":
        result = math.prod(col)
    else:
        result = sum(col)
    answer += result



print(answer)
