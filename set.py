# s={2,True,"coding",2.5,2}
# print(type(s))
# print(s)
# print(len(s))
# for i in s:
#     print(i)

# f={"apple","banana","orange","kiwi"}
# l={"apple","pp","gg"}
# d=f.intersection(l)
# print(d)


# f={"apple","banana","orange","kiwi"}
# l={"apple","pp","gg"}
# j=("oo","apple")
# d=f.union(l,j)
# print(d)



# f={"apple","banana","orange","kiwi"}
# l={"apple","pp","gg"}
# j=("oo","apple")
# f.update(l)
# print(f)



# f={"apple","banana","orange","kiwi"}
# l={"apple","pp","gg"}
# j=("oo","apple")
# f.discard("banana")
# print(f)

# s={2,4,2,9,2,11,13}
# # print(sum(s))
# # print(len(s))
# # print(min(s))
# # print(max(s))
# # print(type(s))
# s.difference_update({4,2,9})
# print(s)

def convert(set):
 return sorted(set)
x={1,2,3}
s=set(x)
print(convert(s))