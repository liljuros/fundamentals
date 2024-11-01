### Exercise 1"
#"Given two floats `a` and `b`, and some tolerance `tol`, write an expression that will test whether `a` and `b` are within `tol` of each other."
# a = 2.30
# b = 2.31
# tol = 0.05
# c = a-b
#
# if abs(c) <= tol:
#     print("yes")
# else:
#     print("nope")

### Exercise 2
#"Assume you have some variable `elapsed` that contains elapsed time in seconds."
#"Create three new variables: `hours`, `minutes` and `seconds`, that represent the number of hours, minutes and seconds represented by `elapsed`."
#"For example, if `elapsed = 7835`, then `hours = 2`, `minutes = 10` and `seconds = 35`"

elapsed = int(input("Elapsed time in seconds: "))
hours = int(elapsed/3600)
elapsed %= 3600
minutes = elapsed//60
seconds = elapsed%60

print(f"hours: {hours}, minutes {minutes}, seconds {seconds}")