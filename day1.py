with open("day1.txt") as file:
    data = [i for i in file.read().strip().split("\n")]
# now we have all the strings in a list called data
"""
next loop through data 
first and last 
"""
# part 1
k = []
for i in data:
    nums = [int(j) for j in i if j.isdigit()]
    f = nums[0]
    l = nums[-1]
    k.append(int(str(f) + str(l)))

n = sum(k)
print(n)


