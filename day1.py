digit_map = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

for i in range(1, 10):
    key = str(i)
    digit_map[key] = i

ans = 0

with open("day1.txt", "r") as file:
    data = [line.strip() for line in file]

for line in data:
    found_numbers = []

    for key, value in digit_map.items():
        indices = [index for index in range(len(line)) if line.startswith(key, index)]

        for index in indices:
            found_numbers.append((index, value))

            last_index = line.rfind(key)
            if last_index != index:
                found_numbers.append((last_index, value))

    found_numbers.sort(key=lambda x: x[0])

    first_number = found_numbers[0][1]
    last_number = found_numbers[-1][1]
    num = first_number * 10 + last_number

    ans += num

print("Answer:", ans)
