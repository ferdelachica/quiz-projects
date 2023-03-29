""""
*Escribe un programaque reciba un texto y transforme lenguaje natural a "lenguaje hacker" (leet o 1337).
Este lenguaje se caracteriza por sustituir caracteres alfanuméricos
*Utiliza la tabla https://www.gamehouse.com/blog/leet-speak-cheat-sheet/
*Usa la primera opción de cada transformación
"""


def hackerTranslate(text):
    dicc = {
        'A': "4",
        'B': "l3",
        'C': "[",
        'D': ")",
        'E': "3",
        'F': "|=",
        'G': "&",
        'H': "#",
        'I': "1",
        'J': ",_|",
        'K': ">|",
        'L': "1",
        'M': "/V|",
        'N': "^/",
        'O': "0",
        'P': '|*',
        'Q': "(_,)",
        'R': "12",
        'S': "5",
        'T': "7",
        'U': "(_)",
        'V': "\/",
        'W': "\/\/",
        'X': "><",
        'Y': "j",
        'Z': "2",
    }

    translate_text = ""

    for word in text:
        if word.upper() in dicc.keys():
            translate_text += dicc[word.upper()]
        else:
            translate_text += word

    return translate_text


print(hackerTranslate("Traduce este texto en hacker"))