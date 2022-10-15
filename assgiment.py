#1
# num =map(lambda i:i+i+i,[1,2,3])
# print(list(num))

#2
# j=[1,2,3,4,5,6]
# even=[]
# odd =[]
# for i in j:
#     if(i%2==0):
#         even.append(i)
#     else:
#         odd.append(i)
# print("Even List:",even)
# print ("Odd list",odd)

#3
# def lower(str):
#     return str.lower()
# str=map(lower,("Hey","how are you"))
# print(tuple(str))

#4
# def root(i):
#     #p=power
#     p=0.5
#     return i**p
# i=map(root,[4,9,16])
# print(list(i))

#5
# def removeduplicate(str, n):
#     s = set()
#     for i in str:
#         s.add(i)
#     st =""
#     for i in s:
#         st = st+i
#     return st
# str = "Chit Surela"
# n = len(str)
# print(removeduplicate(list(str), n))



# #6
# n = int(input("Enter the number: "))
# for i in range (1, 11):
#     print(n, "x", i, "=", n * i)


#7
# i=[1,2,3]
# j=[4,5,6]
# print(list(i+j))

#8
# num1 = 1116.8
# num2 = 123.999999999999999

# num1 = int(num1)
# num2 = int(num2)

# print(num1, num2, sep = '\n')

#9

# seqtuple = ('A', 'B', 'C', 'D', 'E')
# print(list(reversed(seqtuple)))

# seqrange = range(1, 5)
# print(list(reversed(seqrange)))

#10
devBio = {
  "name": "khushi",
  "name": "janki",
  "name": "drashti",
  "age": 12,
  "language": "Script"
}
print(devBio)
# {'name': 'Goli', 'age': 12, 'language': 'Script'}












