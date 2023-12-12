# for i in ['foo', 'bar', 'baz', 'qux']:
#     if 'b' in i:
#         print(i)
#     else:
#         print('I Practice Law of Attraction')
#

# #now lets see with the dictionaries
#
#
# # Initialize a counter to keep track of the current key's position
# count = 0
#
# # Iterate through the keys of the dictionary
# for k in d:
#     # Increment the counter
#     count += 1
#
#     # Check if the current key's position is in the list of positions to access
#     if count in positions_to_access:
#         # Print the key
#         print(k)
#
#     # If you've accessed all the desired keys, you can break out of the loop
#     if count >= max(positions_to_access):
#         break

# check for the second character of the keys

d = {'foo': 1, 'bar': 2, 'baz': 3, 'Chinnu': 4, 'Vibhav': 5}

# Iterate through the keys of the dictionary
for k in d:
    # Check if the key has at least two characters
    if len(k) >= 2:
        # Print the second character of the key (index 1)
        print(k[1])


