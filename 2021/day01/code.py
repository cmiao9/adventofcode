data = open("input.txt", "r").read().split("\n")
data = [int(x) for x in data]

# part 1

is_increase = [data[i] < data[i + 1] for i in range(len(data) - 1)]
print(sum(is_increase))

# part 2

is_increase_3 = [
    sum(data[i : i + 3]) < sum(data[i + 1 : i + 4]) for i in range(len(data) - 1)
]
print(sum(is_increase_3))
