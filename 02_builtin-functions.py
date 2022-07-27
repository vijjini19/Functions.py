'''pre defined functions'''

'''sorted()'''
# a=[1,8,4,7,6,9]
# a.sort(reverse=True)
# print(a)
# print(sorted([1,7,3,5,9,8]))
# print(sorted((1,7,3,5,9,8)))

'''all()'''
# print(all([True,1,2]))
# print(all([True,'',1,2]))
# print(all([True,' ',1,2]))
# print(all([True,False,1,2]))
# print(all([True,1,2,0]))
# print(all([True,1,2,None]))

'''any()'''
# print(any([True,False,23]))
# print(any([True,False,False,23]))
# print(any([True,False,0]))
# print(any([True,True,0]))
# print(any([False,False,None]))

'''bool()'''
# print(bool(True))
# print(bool(False))
# print(bool(0))
# print(bool(1))
# print(bool(None))
# print(bool('hi'))

'''eval()'''
# print('eval=',eval('5+6.8-1'))
# a=eval('5+6-1')
# b=eval('4+3.8-1')
# print(a,type(a))
# print(b,type(b))

'''sum()'''
# print('sum=',sum([1,3,7,9]))
# print('sum=',sum([1,3, 99,9]))

'''reversed()-list'''
# for i in reversed([3,6,4,8]):
#     print(i,end=' ')

'''reversed()-tuple'''
# for i in reversed((3,6,4,8)):
#     print(i)

'''enumerate()'''
# a=['bread','ball','board']
# b=enumerate(a)
# print(type(b))
# print(list(b))
# print(tuple(b))
# print(dict(b))

# a=['bread','ball','board']
# c=enumerate(a,11)
# print(list(c))
