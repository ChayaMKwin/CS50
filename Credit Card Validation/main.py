def main():
    # Get card number
    cn = int(input("Number: "))
    
    # Count length
    i = 0
    cc = cn
    while cc > 0:
        cc = cc // 10
        i += 1
        
    # is length is valid?
    if i != 13 and i != 15 and i != 16:
        print("INVALID")
        return

    # Calculate checksum
    sum1 = 0
    sum2 = 0
    x = cn
    total = 0
    while x > 0:
        # Remove last digit and add to sum1
        mod1 = x % 10
        x = x // 10
        sum1 += mod1
        # Remove second last digit
        mod2 = x % 10
        x = x // 10
        # Double second last digit and add digits to sum2
        mod2 *= 2
        d1 = mod2 % 10
        d2 = mod2 // 10
        sum2 += d1 + d2
    
    total = sum1 + sum2

    # Next check Luhn Algorithm
    if total % 10 != 0:
        print("INVALID")
        return

    # Get starting digits
    start = cn
    while start > 100:
        start = start // 10

    # Next check starting digits for card type
    if start // 10 == 5 and 0 < start % 10 < 6:
        print("MASTERCARD")
    elif start // 10 == 3 and (start % 10 == 4 or start % 10 == 7):
        print("AMEX")
    elif start // 10 == 4:
        print("VISA")
    else:
        print("INVALID")

if __name__ == "__main__":
    main()