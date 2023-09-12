number = 90
string_number = str(number)
sum_nums = 0
for i in range(0, len(string_number)):
    sum_nums += int(string_number[i]) ** (i+1)
if sum_nums == number:
    special = True
    print(special)
else:
    special = False
    print(special)

