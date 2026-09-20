# Q4_fruit_sets.py

fruits = {
    "Apple",
    "Mango",
    "Orange",
    "Banana",
    "Pineapple",
    "Grapes",
    "Watermelon",
    "Guava",
    "Litchi",
    "Papaya"
}

summer_fruits = {
    "Mango",
    "Watermelon",
    "Litchi",
    "Papaya",
    "Pineapple"
}

winter_fruits = {
    "Orange",
    "Apple",
    "Guava",
    "Grapes",
    "Pineapple"
}

# 1. Print all fruits
print("All Fruits:")
print(fruits)

print("\nSummer Fruits:")
print(summer_fruits)

print("\nWinter Fruits:")
print(winter_fruits)

# 2. Fruits present in both summer and winter
print("\nFruits present in both summer and winter:")
print(summer_fruits & winter_fruits)

# 3. Summer fruits but not in fruits
print("\nSummer fruits but not in fruits:")
print(summer_fruits - fruits)

# 4. Fruits present in both summer and winter but not in fruits
print("\nCommon summer and winter fruits but not in fruits:")
print((summer_fruits & winter_fruits) - fruits)

# 5. Check Orange
if "Orange" in fruits:
    print("\nOrange is present in fruits set.")
else:
    print("\nOrange is not present in fruits set.")

# 6. Find which set contains Pineapple
print("\nPineapple is present in:")

if "Pineapple" in fruits:
    print("Fruits set")

if "Pineapple" in summer_fruits:
    print("Summer fruits set")

if "Pineapple" in winter_fruits:
    print("Winter fruits set")
