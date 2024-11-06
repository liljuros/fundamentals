#"Given a variable `a` (containing any value), re-assign the value `"N/A"` if `a` is `None`, and leave `a` unchanged otherwise.
# Use an `if...else...` statement."

# a = input("Give a value: ")
# if a == "None":
#     a = "N/A"
#
# print(a)


#"Do the same thing as Question 1, but this time use a ternary operator."
# b = input("Give a value: ")
# a = "N/A" if b == "None" else b
# print(a)



#  "Given an credit score `score`, assign a string value to another variable `rating` based on the following scale:\n",
#     "\n",
#     "- [0, 580) --> Poor\n",
#     "- [580, 670) --> Fair\n",
#     "- [670, 740) --> Good\n",
#     "- [740, 800) --> Very Good\n",
#     "- [800, 850] --> Excellent\n"
#    ]
# score = int(input("Give me a score: "))
# rating = ""
#
# if 0 <= score < 580:
#     rating = "Poor"
# elif 580 <= score < 670:
#     rating = "Fair"
# elif 670 <= score < 740:
#     rating = "Good"
# elif 740 <= score < 800:
#     rating = "Very good"
# elif 800 <= score <= 850:
#     rating = "Excellent"
# else:
#     rating = "Wrong input"
#
# print(rating)

# "Given an `elapsed` time (in seconds), write code to set a variable `magnitude` based on the following conditions:\n",
# "\n",
# "- if elapsed time is less than 1 minute, `magnitude` --> `'seconds'`\n",
# "- if elapsed time is more than 1 minute, but less than 1 hour, `magnitude` --> `'minutes'`\n",
# "- if elapsed time is more than 1 hour, but less than 1 day, `magnitude` --> `'hours'`\n",
# "- if elapsed time is more than 1 day, but less than 1 week: `magnitude` --> `'days'`\n",
# "- if elapsed time is more than 1 week, `magnitude` --> '`weeks'`"
# ]
# }
# ],
elapsed = int(input("Give me the amount of time in seconds: "))
beginning = elapsed
hours = int(elapsed/3600)
elapsed %= 3600
minutes = elapsed//60
seconds = elapsed%60
magnitude = ""

if beginning / 60 < 1:
    magnitude = "seconds"
elif hours <= 0:
    magnitude = "minutes"
elif 1 <= hours <= 23:
    magnitude = "hours"
elif 24 <= hours <= 167:
    magnitude = "days"
else:
    magnitude = "weeks"

print(magnitude)

