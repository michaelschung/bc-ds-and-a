'''
Mr. Chung
HW 8: Randomness
#2: Count Randomness
'''

import random

counts = {}

for i in range(100):
    num = random.randrange(0, 100)
    # If we haven't seen num before
    if num not in counts:
        # Put num in counts with value 1
        counts[num] = 1
    # Otherwise
    else:
        # Bump up the current count by 1
        counts[num] += 1

# Print all values
# for key in sorted(counts):
#     print('{}: {}'.format(key, counts[key]))

# Print all values, including ones that didn't come up
for key in range(100):
    if key in counts:
        print('{}: {}'.format(key, counts[key]))
    else:
        print('{}: 0'.format(key))
