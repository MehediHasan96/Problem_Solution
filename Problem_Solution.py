
lower = 1
upper = 1000000

# Prime number

prime_number_list = []
for i in range(lower, upper + 1):

    if i > 1:
        for j in range(2, i):
            if (i % j) == 0:
                break
        else:
            prime_number_list.append(i)

prime_number_list_length = len(prime_number_list)

# All distances between two consecutive prime numbers

distance_data_list = []
for i in range(0, prime_number_list_length-1):
    value = prime_number_list[i+1] - prime_number_list[i]
    distance_data_list.append(value)


distance_data_list_length = len(distance_data_list)
distance_data_list.sort()

# Mean

add = 0
for i in distance_data_list:
    add += i

mean = add/distance_data_list_length

print("Mean: " + str(mean))

# Median

if distance_data_list_length % 2 == 0:
    median1 = distance_data_list[distance_data_list_length//2]
    median2 = distance_data_list[distance_data_list_length//2 - 1]
    median = (median1 + median2)/2
else:
    median = distance_data_list[distance_data_list_length//2]
print("Median: " + str(median))

# Mode

data = {}
for a in distance_data_list:
    if a not in data:
        data[a] = 1
    else:
        data[a] += 1
mode = [k for k, v in data.items() if v == max(data.values())]
print("Mode: " + ', '.join(map(str, mode)))








