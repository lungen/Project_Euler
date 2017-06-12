with open("13_BigNumber.txt", "r") as f:
    data = f.read()

nums = []
for line in data.strip().split("\n"):
    nums.append(line)

s = sum(int(i) for i in (nums))
print(s)
