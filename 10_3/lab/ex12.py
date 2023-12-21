# Exercise 1.2. Write Python code to evaluate these expressions.
# The answers can be stored in a name, or evaluated in a print statement

# 1. How many seconds are there in 42 minutes 42 seconds?

sec_per_min = 60
min = 42
sec = 42

total_seconds = min*sec_per_min+sec

print(total_seconds)


# 2. How many miles are there in 10 kilometers? Hint: there are 1.61
# kilometers in a mile.

kilometer = 1.61
mile = 1
m_per_km = mile/kilometer
miles_per_10_km = m_per_km * 10

print(miles_per_10_km)


# 3. If you run a 10 kilometer race in 42 minutes 42 seconds, what is your
# average pace (time per mile in minutes and seconds)? What is your average
# speed in miles per hour?

km_time_in_seconds = total_seconds/10
km_time_in_min = km_time_in_seconds/60

average_mph = km_time_in_min * m_per_km

print(average_mph)