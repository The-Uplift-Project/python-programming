# BASIC
# Given a string representing a stock ticker:
# Write a function that returns the cheapest priced stock symbol

# test_1 = "AAPL 313 GOOG 513 TSLA 58 BBY 22" # BBY
# test_2 = "NBA 12 AAPL 313 GOOG 513 TSLA 58 BBY 222" #NBA
# test_3 = "NBA 11 AAPL 55 GOOG 22 TSLA 44 BBY 22" # NBA

def cheapest_stock(line):
    d = dict()
    d_rev = dict()
    line = line.split()
    for i in range(0, len(line), 2):
        d[line[i]] = line[i+1]
    d_rev = {v: k for (k,v) in d.items()}
    print("Cheapest priced stock: ", d_rev[min(d.values())])

print("Enter Tax percentage: ")
inp = raw_input()
cheapest_stock(inp)
