answer = 0
day = 3
fname = "example.txt"
fname = "input.txt"
fpath = f"./Day{day:02d}/{fname}"

with open(fpath) as f:
    banks = [line.rstrip("\n") for line in f]

joltage_length = 12
for bank in banks:
    sub_bank_start = 0
    largest_joltage = ""
    for j in range(joltage_length):
        sub_bank = bank[
            sub_bank_start : (
                len(bank)
                if -1 * (joltage_length - j) == -1
                else -1 * (joltage_length - j) + 1
            )
        ]
        sub_bank_max = 0
        sub_bank_max_index = 0
        for i, sb in zip(range(len(sub_bank)), sub_bank):
            if int(sb) > sub_bank_max:
                sub_bank_max = int(sb)
                sub_bank_max_index = i
        sub_bank_start = sub_bank_start + sub_bank_max_index + 1
        largest_joltage += str(sub_bank_max)
    answer += int(largest_joltage)

print(answer)
