# =============================
# Farm Harvest Calculator
# =============================

# -----Assignment Operrator (=) ------
# Store the harvest in kg  from each of 5 fields 
field1 = 120
field2 = 85
field3 = 150
field4 = 95
field5 = 110

# --- Arithmathic Operator (+, -, *, /) ---
#Calculate total and average harvest
total = field1 + field2 + field3 + field4 + field5
average =total / 5

print("Total harvest   :", total, "kg")
print("Average per field   :", average, "kg" )

#Price per kg is 15 rupees - Calculate total earnings
price_per_kg = 15
earnings = total * price_per_kg
print("Total earnings   :Rs.", earnings)

# --- Floor Division (//) and Modules (%) ---
#Pack the harvest into bags of 25kg each
bags    = total // 25
leftover = total % 25

print("Full bags packed   :", bags)
print("Leftover           :", leftover, "kg")

# --- Comparison Operators (>, <, ==, >=) ---
# Compare This Years harvest with last year
last_year = 500

