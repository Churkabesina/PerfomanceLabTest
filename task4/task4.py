from sys import argv

path = argv[1]

nums = []

with open(path, 'r', encoding='UTF-8') as file_in:
    for i in file_in:
        nums.append(int(i.rstrip('\n')))

nums.sort()
median = nums[len(nums) // 2]
console_out = sum([abs(x - median) for x in nums])
print(console_out)
