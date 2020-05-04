# 1. Basic
for i in range (151):
    print(i)

# 2. Multiples of 5
for num in range(5,1001,5):
    print(num)

# 3. Counting, the Dojo way

for num in range(1,101):
    if num%10 == 0:
        print("Coding")
    elif num%5 == 0:
        print("Dojo")
    else:
        print(num)

# 4. Whoa. That sucker's huge

count = 0
for num in range(0,500001):
    if num%2 == 1:
        count += num
print(count)

# 5. Countdown by Fours

for num in range(2018,0,-4):
    print(num)

# 6. Flexible Counter

lowNum = 2
highNum = 9
mult = 3
while lowNum <= highNum:
    if lowNum % mult == 0:
        print(lowNum)
    lowNum += 1



