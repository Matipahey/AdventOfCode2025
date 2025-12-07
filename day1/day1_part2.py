
def solve():
    current = 50
    count = 0
    with open("adventnumbers.txt", 'r') as file:
        content = file.read()
        lines = [line.strip() for line in content.split()]
        for line in lines:
            if not line: continue

            direction = line[0]
            distance = int(line[1:])

            for i in range(1, distance + 1):
                if direction == 'L' :
                    temp_pos = (current - i) % 100
                else:
                    temp_pos = (current + i) % 100

                if temp_pos == 0:
                    count += 1

            if direction == 'L':
                current = (current - distance) % 100
            else:
                current = (current + distance) % 100
    return count
print(f"Password: {solve()}")

