d={}
print(type(d))


d2={1:"Ramesh",2:"Rahul",3:"Chiranjeevi"}
print("The values in the dictionary d2 are",d2)
print("Methods available for the dictionary d2 are ",dir(d2))
#Keys and values
print("the keys available in d2 are",d2.keys())#keys are similar to columns
print("the values available in d2 are",d2.values())#valuea are  similar to rows
print("the items available in d2 are",d2.items())

#we cannot have duplicate keys but can have dupicate values
d3={1:"Maruthi",2:"Zen",3:"Maruthi",1:"Suzuki"}#
print("the values of the dictionary d3 are",d3)

#Adding new values into the dictionary

d4={1:"Ram",2:"Shiva",3:"Chetana"}
print("Before adding 4'th key the values are ",d4)
d4.update({4:"Sureka"})
print("After adding the key4 the values are ",d4)
d4[3]="Indumathi"#another way of adding/update values
print(d4)

##Accessing the values from the dictionary
print("3rd value in the dictionary d3 are",d3.get(3))
print("the d4[2] value is",d4[2])

##removing the elements from the dictionary
d3={1:"Maruthi",2:"Zen",3:"Maruthi",1:"Suzuki",4:"Yamaha"}

print("before pop dictionary d3 is",d3)
print("d3",d3.pop(1))
print("after pop dictionary d3 is",d3)

d3={1:"Maruthi",2:"Zen",3:"Maruthi",1:"Suzuki",4:"Yamaha"}
print("before pop item the elements in d3 are",d3)
print("d3 popitem",d3.popitem())#popitem removes the last element from the dictionary
print("after pop item the elements in d3 are",d3)

