# value 다 더해주세요(sum)

d = {'a': 15, 'b': 634, 'c': 124, 'd': -436, 'e': -235, 'f': 856, 'g': 23, 'h': 523}



# sum()함수 사용

# total = sum(d.values())
# print(total)


# total = sum(d[x] for x in d)
# print(total)



# lambda식 사용

# from functools import reduce

# total = reduce(lambda x, y:x+y, d.values())
# print(total) 