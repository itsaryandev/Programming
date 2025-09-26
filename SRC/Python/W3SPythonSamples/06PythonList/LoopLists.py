fruits = [
    "banana", "apple", "date", "elderberry", "cherry",
    "grape", "fig", "honeydew", "lemon", "kiwi",
    "nectarine", "mango", "orange", "quince", "papaya"
]

# for each fruit in fruits list, print the fruit name with its index
for i in range(len(fruits)):    
    if i % 2 == 1:
        print(f"{i}. {fruits[i]} (even index)")
    

# for each fruit in fruits list, print the fruit name
for f1 in fruits:
    print(f1)

