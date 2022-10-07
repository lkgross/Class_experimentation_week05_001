mountains = ['Mount Kilimanjaro', 'Mount Kenya', 'Mount Stanley', 'Mount Meru']
print(['Mount Kilimanjaro', 'Mount Kenya', 'Mount Stanley', 'Mount Meru'])
print(mountains)
print(len(mountains))
len("Derek")
print(len("Derek"))
sorted(mountains)
# Use the function to directly print something.
print(sorted(mountains))
print(mountains)
sorted(mountains, reverse=True)
print(sorted(mountains, reverse=True))
# The method will change something in the list.
# Lists are mutable.
mountains.append('Mount Meru')
print(mountains)
mountains.insert(3, 'Mount Speke')
print(mountains)
del mountains[3]
print(mountains)
mountains.remove('Mount Meru')
print(mountains)
print(f"Let's pop this element off the list: {mountains.pop()}")
print(mountains)
print(f"The tallest mountain in Africa is: {mountains.pop(0)}")
print(mountains)
print(f"The next tallest mountain in Africa is: {mountains.pop(0)}")
# You can index on strings, as well as lists.
print("Sunny"[0])
mountains.reverse()
print(mountains)
"Sunny".lower()
print("Sunny".lower())
name = "SUNNY"
name.lower()
print(name)
print(name.lower())
print(name)
print(mountains)
mountains.append('Mount Kenya')
mountains.append('Mount Stanley')
mountains.append('Mount Meru')
print(mountains)
heights = [5895, 5199, 5109, 4562]
for height in heights:
    print(height)
print()
for i in range(4):
    print(heights[i])
print()
for i in range(len(heights)):
    print(heights[i])
facts = []
for i in range(len(mountains)):
    facts.append(f'The height of {mountains[i]} is {heights[i]} meters.')
print(facts)

mountains = ['Mount Stanley', 'Mount Kenya', 'Mount Stanley', 'Mount Meru']
print(mountains)
mountains[3] = 'Mount Speke'
print(mountains)

# You can call functions min, max, and sum on lists of numbers.
heights = [5895, 5199, 5109, 4562]
print(heights)
print(min(heights))
print(max(heights))
# We can call the sum function to get the total height of all four mountains,
# although this number is not particularly meaningful in a practical sense.
print(sum(heights))

