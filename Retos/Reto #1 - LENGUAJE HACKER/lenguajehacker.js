/*
Escribe un programaque reciba un texto y transforme lenguaje natural a "lenguaje hacker" (leet o 1337).
Este lenguaje se caracteriza por sustituir caracteres alfanuméricos
*Utiliza la tabla https://www.gamehouse.com/blog/leet-speak-cheat-sheet/
*Usa la primera opción de cada transformación
*/

function hackerTranslate (frase){

    //Diccionario para la traducción

    const dicHacker = {
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
    //Crea la variable translate_text donde estará la frase a traducir
    let translate_text = '';

    //Recorre la frase
    for (let i = 0; i < frase.length; i++) {
        const letra = frase.charAt(i).toUpperCase();

        translate_text += dicHacker[letra] || letra;
    }

    console.log(translate_text)
}
hackerTranslate("Estoy traduciendo a hacker")