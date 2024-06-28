from decimal import Decimal

def cic2():
    pmt = int(input("What is your monthly contribution?:"))
    p = int(input("What is your lump sum investment?:"))
    r = float(input("What is the interest rate in percentage?:"))
    n = int(input("How many times is the interest compounded each year?:"))
    t = int(input("How many years will you be investing for?:"))
    
    part_0 = p * (1 + (r/100)/n) ** (n * t)
    part_1 = ((1 + (r/100)/n) ** (n * t)) - 1
    part_2 = (r/100) / n
    formula = Decimal(part_0 + (pmt * (part_1 / part_2)) * (1 + part_2))
    output = round(formula, 2)
    print("You should have", output, "after", t, "years")

cic2()
