# Decimal to Binary and Hexadecimal Converter (0-255)

def decimal_to_binary_hex(decimal):
    if 0 <= decimal <= 255:
        binary_representation = bin(decimal)[2:].zfill(8)  # Ensure 8 bits representation
        hexadecimal_representation = hex(decimal)[2:].upper()
        return binary_representation, hexadecimal_representation
    else:
        return "Input out of range (0-255)", "Input out of range (0-255)"

# Example usage
decimal_input = int(input("Enter a decimal number (0-255): "))
binary_output, hex_output = decimal_to_binary_hex(decimal_input)

print(f"Binary: {binary_output}")
print(f"Hexadecimal: {hex_output}")

