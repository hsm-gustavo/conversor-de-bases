from string import ascii_uppercase

def any_to_dec(number, origin=10):
    number = number.replace(",",".")

    hex = {key:value for key, value in zip(ascii_uppercase, range(10, 36))}
    
    if "." in number:
        integer, decimal = number.split(".")

        new_int = float()
        new_dec = float()
        
        for index, digit in enumerate(integer[::-1]):
            if digit.isalpha():
                digit = hex[digit]
            new_int += int(digit) * (origin ** index)

        for index, digit in enumerate(decimal):
            if digit.isalpha():
                digit = hex[digit]
            new_dec += int(digit) * (origin ** -(index+1))
        
        ans = new_int + new_dec
        return str(ans)
    
    new_num = float()

    for index, digit in enumerate(number[::-1]):
        if digit.isalpha():
            digit = hex[digit]
        new_num += int(digit) * (origin ** index)

    return str(new_num)
    

def dec_to_any(number, destiny=10):
    number = number.replace(",",".")
    
    hex = {key:value for key, value in zip(range(10, 36), ascii_uppercase)}

    if "." in number:
        integer, decimal = number.split(".")

        decimal = float("0."+decimal)

        new_int = str()
        new_dec = str()

        while int(integer) >= 1:
            remainder = int(integer) % destiny
            if remainder > 9:
                remainder = hex[remainder]
            new_int += str(remainder)
            integer = int(integer) // destiny

        places = 0

        while decimal > 0 and places < 12:
            decimal *= destiny
            remainder = int(decimal)
            if remainder > 9:
                remainder = hex[remainder]
            new_dec += str(remainder)
            decimal -= int(decimal)
            places+=1

        return new_int[::-1] + "." + new_dec

    new_number = str()

    while int(number) >= 1:
        remainder = int(number) % destiny
        if remainder > 9:
            remainder = hex[remainder]
        new_number += str(remainder)
        number = int(number) // destiny
    
    return new_number[::-1]


def any_to_any(number, origin, destiny):
    if origin == destiny:
        return number
    dec = any_to_dec(number, origin)
    return dec_to_any(dec, destiny)

def main():

    number = input("What number you wish to convert? (CTRL+C to quit)\n").upper()
    origin = int( input("Type the origin base of the number:\n") )
    destiny = int( input("Type the destiny base of the number:\n") )

    result = any_to_any(number, origin, destiny)

    print(f"Result: {result}")

if __name__ == "__main__":
    try:
        while True:
            main()
    except KeyboardInterrupt:
        print("Goodbye!")
    