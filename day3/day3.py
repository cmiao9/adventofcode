
data = open("input.txt", "r").read().split("\n")
data = [[int(y) for y in x] for x in data]

# part 1

gamma_rate, epsilon_rate = "", ""

for bit_index in range(len(data[0])):
    most_common_bit = int(sum([x[bit_index] for x in data]) >= len(data) / 2)
    least_common_bit = int(not most_common_bit)

    gamma_rate += str(most_common_bit)
    epsilon_rate += str(least_common_bit)

power_consumption = int(gamma_rate, 2) * int(epsilon_rate, 2)
print(power_consumption)

# part 2

oxygen_generator_rating, co2_scrubber_rating = data[:], data[:]

for bit_index in range(len(data[0])):

    most_common_bit = int(sum([x[bit_index] for x in oxygen_generator_rating]) >= len(oxygen_generator_rating) / 2)
    least_common_bit = int(sum([x[bit_index] for x in co2_scrubber_rating]) < len(co2_scrubber_rating) / 2)

    if len(oxygen_generator_rating) > 1:
        oxygen_generator_rating = list(filter(lambda x: x[bit_index] == most_common_bit, oxygen_generator_rating))
    if len(co2_scrubber_rating) > 1:
        co2_scrubber_rating = list(filter(lambda x: x[bit_index] == least_common_bit, co2_scrubber_rating))

oxygen_generator_rating = int("".join([str(x) for x in oxygen_generator_rating[0]]), 2)
co2_scrubber_rating = int("".join([str(x) for x in co2_scrubber_rating[0]]), 2)

life_support_rating = oxygen_generator_rating * co2_scrubber_rating
print(life_support_rating)
