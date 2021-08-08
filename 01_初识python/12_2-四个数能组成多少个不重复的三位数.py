# 有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
'''
	1. 可填在百位、十位、个位的数字有哪些？
	2. 不考虑重复的情况，这四个数字能组成多少个三位数？
	3. 去重复的条件是什么？
'''

count = 0
for i in range(1,5): # 可填在百位的数字：1、2、3、4
	for j in range(1,5): # 可填在十位的数字：1、2、3、4
		for k in range(1,5): # 可填在个位的数字：1、2、3、4
			if i != j and i != k and j != k: # 常规处理方式，条件判断去重
				print(i,j,k)
				count = count + 1

			# lst = [i,j,k] # 使用列表存数据
			# if len(set(lst)) == 3: # 利用set集合去重
			# 	print(lst)
			# 	count += 1
print(f'能组成的三位数的个数是：{count}')