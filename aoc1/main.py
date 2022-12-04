with open('input.txt') as f:
    data = [i for i in f.read().strip().split("\n")]

calorie_count = 0
max_calorie_count = 0
second_calorie_count = 0
third_calorie_count = 0

for item in data:
    if item == '':
        calorie_count = 0
    else:       
        calories = int(item)
        calorie_count += calories
        
    if calorie_count > max_calorie_count:
        third_calorie_count = second_calorie_count
        second_calorie_count = max_calorie_count
        max_calorie_count = calorie_count
    elif calorie_count > second_calorie_count:
        second_calorie_count = calorie_count
    elif calorie_count > third_calorie_count:
        third_calorie_count = calorie_count


print('the maximum amount of calories carried by an elf is:', max_calorie_count)
print('the total amount of calories carried by the top 3 elves is:', max_calorie_count+second_calorie_count+third_calorie_count)
