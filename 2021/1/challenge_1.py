def main():
    previous_measurement = float('inf')
    current_measurement = float('inf')
    count = 0
    with open('input.txt', 'r') as file:
        for line in file:
            previous_measurement = current_measurement
            current_measurement = int(line)
            if (current_measurement > previous_measurement):
                count += 1
    print(count)

if __name__ == '__main__':
    main()