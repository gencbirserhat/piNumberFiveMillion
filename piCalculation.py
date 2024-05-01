from mpmath import mp

# Number of digits to be computed
number_of_digits = 5000000

# Calculation adjusted to the desired precision
mp.dps = number_of_digits

# Calculate the value of pi
pi = mp.pi

# Write to file
with open("pi5mn.txt", "w") as file:
    file.write(str(pi))
