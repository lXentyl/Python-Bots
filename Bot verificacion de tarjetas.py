def luhn_algorithm(card_number):
    # Convertir el número de tarjeta en una lista de enteros
    digits = [int(digit) for digit in str(card_number)]
    
    # Duplicar los dígitos en posiciones pares contando desde la derecha
    for i in range(len(digits) - 2, -1, -2):
        digits[i] *= 2
        if digits[i] > 9:
            digits[i] -= 9

    # Sumar todos los dígitos
    total_sum = sum(digits)

    # Si el total es divisible por 10, es un número válido según Luhn
    return total_sum % 10 == 0

# Ejemplo de uso
card_number = "4532015112830366"  # Este es un número de tarjeta ficticio
if luhn_algorithm(card_number):
    print("El número de tarjeta es válido según Luhn.")
else:
    print("El número de tarjeta no es válido.")
