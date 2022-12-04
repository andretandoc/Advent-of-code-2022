with open('input.txt') as f:
    data = [i for i in f.read().strip().split("\n")]

calorie_count = 0
max_calorie_count = 0
for item in data:
    if item == '':
        count = 0
    else:       
        calories = int(item)
        calorie_count += calories
        

    if calorie_count > max_calorie_count:
        max_calorie_count = calorie_count

print('The max is:', max_calorie_count)

