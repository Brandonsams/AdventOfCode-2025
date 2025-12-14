answer = 0 
day = 1
fname = "example.txt"
fname = "input.txt"
fpath = f"./Day{day:02d}/{fname}"

with open(fpath) as f:
    lines = [line.rstrip("\n") for line in f]

dial_size = 100
position = 50

for line in lines:
    direction = -1 if line[0] == "L" else 1
    amount = int(line[1:])
    
    for i in range(amount):
        position = (position + direction) % dial_size
        if position == 0:
            answer += 1
    

print(answer)
    
