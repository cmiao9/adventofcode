data = open("input.txt", "r").read().split("\n")
data = [x.split(" ") for x in data]
data = [(direction, int(magnitude)) for (direction, magnitude) in data]

# part 1

horizontal_position, depth = 0, 0

for direction, magnitude in data:
    if direction == "forward":
        horizontal_position += magnitude
    elif direction == "up":
        depth -= magnitude
    elif direction == "down":
        depth += magnitude

print(horizontal_position * depth)

# part 2

horizontal_position, depth, aim = 0, 0, 0

for direction, magnitude in data:
    if direction == "forward":
        horizontal_position += magnitude
        depth += aim * magnitude
    elif direction == "up":
        aim -= magnitude
    elif direction == "down":
        aim += magnitude

print(horizontal_position * depth)
