# Step 1: ask for a base number and exponent
base = int(input("Enter the base number: "))
exponent = int(input("Enter the exponent: "))

# Step 2: create a running total starting at 1
total = 1

# Step 3: loop exactly 'exponent' times
for i in range(exponent):
    # Step 4: multiply the running total by the base on every repeat
    total = total * base

    # Step 5a: print each step
    print(f"Step {i + 1}: total = {total}")

# Step 5b: print the final answer
print(f"{base} raised to the power of {exponent} = {total}")