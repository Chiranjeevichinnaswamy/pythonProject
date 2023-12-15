s1={1,2,3+4j,True}
print('type of s1 is',type(s1))

print(dir(s1))

s2=set() ##'''creating empty set'''
print(type(s2))
s3={}
print(type(s3)) ##this will create d

#Methods

#Add Methods
print('before adding s1 values are',s1)
s1.add(4)
print('after adding values s1 will be',s1)

#Clear
s1.clear()##clears all the elements in the set
print('after clear',s1.clear())

#remove
#update
#union
s1={1,2,3,4}
s2={4,5,6,1}
print('union of sets s1 and s2 are',s1.union(s2))
#difference