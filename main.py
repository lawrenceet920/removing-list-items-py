# Ethan Lawrence
# Oct 30 2024
# Removing list items

import random
import time

# Favorites
favorites = ['Alpha', 'Beta', 'Charly', 'Delta', 'Foxtrot', 'Echo', 'Golf']
print (favorites)
# Pop
favorites.pop()
favorites.pop(-2)
print (favorites)
# Remove
favorites.remove('Beta')
print (favorites)
# Del
del favorites[0]
print (favorites)

time.sleep(1)
# Part 2

# Changing Guest list
guests = ['Alpha', 'Beta', 'Charly', 'Delta', 'Foxtrot']
for guest in guests:
    print(f'Hello {guest}, I would like to formally invite you to a dinner party!')
missing = random.randrange(0, len(guests))
print(f'{guests[missing]} is unable to make it to the party.')
guests.remove(guests[missing])

for guest in guests:
    print(f'Hello {guest}, I would like to formally invite you to a dinner party!')

time.sleep(1)
# Shrinking Guest list
print('I will only have space for 2 guests.')
for guest in guests:
    if len(guests) == 2:
        continue
    removed_guest = guests.pop(random.randrange(0, len(guests)))
    print(f'Sorry {removed_guest}, but I cannot invite you to dinner')

print(guests[0] + ' You are still invited to the dinner party')
del guests[0]
print(guests[0] + ' You are still invited to the dinner party')
del guests[0]

print(guests)