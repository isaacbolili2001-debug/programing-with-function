"""
When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your heart’s maximum rate.
"""

age = int(input("Enter your age: "))
max_heart_rate = 220 - age
lower_bound = max_heart_rate * 0.65
upper_bound = max_heart_rate * 0.85

print(f"Your maximum heart rate is {max_heart_rate} beats per minute.")
print(f"Your target heart rate range is {lower_bound:.0f} to {upper_bound:.0f} beats per minute.")

"""
named argument
"""

a="isaac"
b="bolili"
c="bakambala"

print(a,b,c, sep="|", flush=True)