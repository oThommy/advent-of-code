def main():
    measurement_lst = []
    sum_measurement_lst = []
    with open('input.txt', 'r') as file:
        for line in file:
            measurement_lst.append(int(line))
    for offset in range(0, len(measurement_lst) - 3 + 1):
        sum_measurement_lst.append(0)
        for i in range(3):
            sum_measurement_lst[-1] += measurement_lst[offset + i]

    previous_measurement = float('inf')
    current_measurement = float('inf')
    count = 0
    for sum_measurement in sum_measurement_lst:
        previous_measurement = current_measurement
        current_measurement = sum_measurement
        if (current_measurement > previous_measurement):
            count += 1
    print(count)

if __name__ == '__main__':
    main()