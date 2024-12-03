

file = open('input.txt')
list1 = []
list2 = []
for line in file:
  nums = line.replace('\n', '').split('   ')
  # print(nums)
  list1.append(int(nums[0]))
  list2.append(int(nums[1]))

list1.sort()
list2.sort()
res = 0
for i in range(len(list1)):
  count = len(list(filter(lambda x: x == list1[i], list2)))
  res += list1[i] * count

print(res)