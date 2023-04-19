import random
import string

#Incluimos las opciones mayúsculas, números y símbolos para luego seleccionar si activarlas o no con un True/False
def g_password(length: int, include_uppercase: bool, include_numbers: bool, include_symbols: bool) -> str:
    char = ''

    #Establecemos como valores mínimo y máximo de entre 8 y 16 caracteres
    if length < 8 or length > 16:
        raise ValueError('Número de caracteres incorrecto (8-16)')
    
    #Si las opciones son True añadirá en la contraseña lo seleccionado
    if include_uppercase:
        char += string.ascii_uppercase
    if include_numbers:
        char += string.digits
    if include_symbols:
        char += string.punctuation
    #En el caso de que no se seleccione nada la contraseña por defecto incluirá letras y símbolos
    if not char:
        char = string.ascii_letters + string.digits + string.punctuation

    #Añadimos al campo passw la contraseña uniendo de forma aleatoria los caracteres
    passw = ''.join(random.sample(char, length))
    return passw

print(g_password(14, True, True, True))
