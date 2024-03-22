def decimal_to_binary_hex(decimal):
    if 0 <= decimal <= 255:
        binary = ""
        hexa = ""
        for _ in range(8):
            binary = str(decimal % 2) + binary
            decimal //= 2
        for _ in range(2):
            remainder = decimal % 16
            if remainder < 10:
                hexa = str(remainder) + hexa
            else:
                hexa = chr(remainder + 55) + hexa
            decimal //= 16
        return binary, hexa
    else:
        return "Input out of range (0-255)", "Input out of range (0-255)"


decimal_input = int(input("Enter a decimal number (0-255): "))
binary_output, hex_output = decimal_to_binary_hex(decimal_input)

print(f"Binary: {binary_output}")
print(f"Hexadecimal: {hex_output}")
