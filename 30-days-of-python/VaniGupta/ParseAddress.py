# BASIC
# Lecture Exercise - 1
# Parse an Address 
### Given an address, parse it into it’s discrete pieces and reprint it as a multi-line string.
## 123 Main St., Anytown USA 75777 -> 
## 23 Main St.
## Anytown, USA
## 75777

# 1. Extract the street address 
# 2. Extract the "middle" address city/state/country or state/country
# 3. Extract zipcode 
# 4. Add commas in between city/state/country
# 5. Print in the order street address, then city/state/country, then zipcode

def print_address(input_address):
  split_address = input_address.split(', ')
  street_address = split_address.pop(0)

  print("split_address: ", split_address)
  address = ''.join(split_address)
  print("address: ", address)
  split_address = address.split(' ')
  zipcode = split_address.pop()

  middle_address = ', '.join(split_address)
  print(street_address)
  print(middle_address)
  print(zipcode)
