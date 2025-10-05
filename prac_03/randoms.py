import random

print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3

# What did you see on line 1?
# 18
#
# What was the smallest number you could have seen, what was the largest?
# The smallest number is 5, the largest number is 20.
#
# What did you see on line 2?
# 3
#
# What was the smallest number you could have seen, what was the largest?
# The smallest number is 3, the largest number is 9.
#
# Could line 2 have produced a 4?
# No, because the step is 2.
#
# What did you see on line 3?
# 4.5238887149214895
#
# What was the smallest number you could have seen, what was the largest?
# The smallest number is 2.5, the largest number is 5.5.

# Write code, not a comment, to produce a random number between 1 and 100 inclusive.
random_number = random.randint(1, 100)
print(random_number)