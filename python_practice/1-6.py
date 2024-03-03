"""
d = {'a': 'apple', 'b': 'banana'} 를

d = {'a': 'apple', 'b': 'banana', 'c': 'kiwi', 'd' : 'grape'} 로
업데이트 해주세요~
"""

d = {'a': 'apple', 'b': 'banana'}

a = {'c':'kiwi' , 'd':'grape'}
d.update(a)
print(d)