from decimal import Decimal

def cic2():
    pmt = int(input("What is your monthly contribution?:"))
    p = int(input("What is your lump sum investment?:"))
    r = float(input("What is the interest rate in percentage?:"))
    n = int(input("How many times is the interest compounded each year?:"))
    t = int(input("How many years will you be investing for?:"))
    
    part0 = p * (1 + (r/100)/n) ** (n * t)
    part1 = ((1 + (r/100)/n) ** (n * t)) - 1
    part2 = (r/100) / n
    formula = Decimal(part0 + (pmt * (part1 / part2)) * (1 + part2))
    output = round(formula, 2)
    print("You should have", output, "after", t, "years")

cic2()
