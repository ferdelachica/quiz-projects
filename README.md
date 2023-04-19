# quiz-projects
### Proyecto de retos semanales para practicar lógica de programación utilizando Java, JavaScript y Python.

## Listado de retos

Aquí encontrarás el listado de retos, su fecha de publicación, dificultad y enunciado del ejercicio. En su directorio podrás consultar las distintas correcciones del ejercicio agrupadas por lenguaje de programación.

* **#0** - [`EL FAMOSO "FIZZ BUZZ"`](./Retos/Reto%20%230%20-%20FIZZ%20BUZZ)
```
/*
 * Escribe un programa que muestre por consola (con un print) los
 * números de 1 a 100 (ambos incluidos y con un salto de línea entre
 * cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
 */
```
* **#1** - [`EL "LENGUAJE HACKER"`](./Retos/Reto%20%231%20-%20LENGUAJE%20HACKER)
```
/*
 * Escribe un programa que reciba un texto y transforme lenguaje natural a
 * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
 *  se caracteriza por sustituir caracteres alfanuméricos.
 * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
 *   con el alfabeto y los números en "leet".
 *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
 */
```
* **#2** - [`EL PARTIDO DE TENIS`](./Retos/Reto%20%232%20-%20EL%20PARTIDO%20DE%20TENIS%20%5BMedia%5D)
```
/*
 * Escribe un programa que muestre cómo transcurre un juego de tenis y quién lo ha ganado.
 * El programa recibirá una secuencia formada por "P1" (Player 1) o "P2" (Player 2), según quien
 * gane cada punto del juego.
 * 
 * - Las puntuaciones de un juego son "Love" (cero), 15, 30, 40, "Deuce" (empate), ventaja.
 * - Ante la secuencia [P1, P1, P2, P2, P1, P2, P1, P1], el programa mostraría lo siguiente:
 *   15 - Love
 *   30 - Love
 *   30 - 15
 *   30 - 30
 *   40 - 30
 *   Deuce
 *   Ventaja P1
 *   Ha ganado el P1
 * - Si quieres, puedes controlar errores en la entrada de datos.   
 * - Consulta las reglas del juego si tienes dudas sobre el sistema de puntos.   
 */
```
* **#3** - [`EL GENERADOR DE CONTRASEÑAS`](./Retos/Reto%20%233%20-%20EL%20GENERADOR%20DE%20CONTRASEÑAS%20%5BMedia%5D)
```
/*
 * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)
 */
```
* **#4** - 23/01/23 | Media | [`PRIMO, FIBONACCI Y PAR`](./Retos/Reto%20%234%20-%20PRIMO,%20FIBONACCI%20Y%20PAR%20%5BMedia%5D)
```
/*
 * Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
 */
```
* **#5** - [`PIEDRA, PAPEL, TIJERA, LAGARTO, SPOCK`](./Retos/Reto%20%236%20-%20PIEDRA,%20PAPEL,%20TIJERA,%20LAGARTO,%20SPOCK%20%5BMedia%5D)
```
/*
 * Crea un programa que calcule quien gana más partidas al piedra,
 * papel, tijera, lagarto, spock.
 * - El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
 * - La función recibe un listado que contiene pares, representando cada jugada.
 * - El par puede contener combinaciones de "🗿" (piedra), "📄" (papel),
 *   "✂️" (tijera), "🦎" (lagarto) o "🖖" (spock).
 * - Ejemplo. Entrada: [("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")]. Resultado: "Player 2".
 * - Debes buscar información sobre cómo se juega con estas 5 posibilidades.
 */
```
* **#6** - [`EL SOMBRERO SELECCIONADOR`](./Retos/Reto%20%237%20-%20EL%20SOMBRERO%20SELECCIONADOR%20%5BMedia%5D)
```
/*
 * Crea un programa que simule el comportamiento del sombrero selccionador del
 * universo mágico de Harry Potter.
 * - De ser posible realizará 5 preguntas (como mínimo) a través de la terminal.
 * - Cada pregunta tendrá 4 respuestas posibles (también a selecciona una a través de terminal).
 * - En función de las respuestas a las 5 preguntas deberás diseñar un algoritmo que
 *   coloque al alumno en una de las 4 casas de Hogwarts (Gryffindor, Slytherin , Hufflepuff y Ravenclaw)
 * - Ten en cuenta los rasgos de cada casa para hacer las preguntas y crear el algoritmo seleccionador.
 *   Por ejemplo, en Slytherin se premia la ambición y la astucia.
 */
```
* **#7** - [`EL GENERADOR PSEUDOALEATORIO`](./Retos/Reto%20%238%20-%20EL%20GENERADOR%20PSEUDOALEATORIO%20%5BMedia%5D)

```
/*
 * Crea un generador de números pseudoaleatorios entre 0 y 100.
 * - No puedes usar ninguna función "random" (o semejante) del lenguaje de programación seleccionado.
 *
 * Es más complicado de lo que parece...
 */
```
* **#8** - [`HETEROGRAMA, ISOGRAMA Y PANGRAMA`](./Retos/Reto%20%239%20-%20HETEROGRAMA,%20ISOGRAMA%20Y%20PANGRAMA%20%5BFácil%5D)
```
/*
 * Crea 3 funciones, cada una encargada de detectar si una cadena de
 * texto es un heterograma, un isograma o un pangrama.
 * - Debes buscar la definición de cada uno de estos términos.
 */
```
* **#9** - [`LA API`](./Retos/Reto%20%2310%20-%20LA%20API%20%5BMedia%5D)
```
/*
 * Llamar a una API es una de las tareas más comunes en programación.
 *
 * Implementa una llamada HTTP a una API (la que tú quieras) y muestra su
 * resultado a través de la terminal. Por ejemplo: Pokémon, Marvel...
 *
 * Aquí tienes un listado de posibles APIs: 
 * https://github.com/public-apis/public-apis
 */
```
* **#10** - [`URL PARAMS`](./Retos/Reto%20%2311%20-%20URL%20PARAMS%20%5BFácil%5D)
```
/*
 * Dada una URL con parámetros, crea una función que obtenga sus valores.
 * No se pueden usar operaciones del lenguaje que realicen esta tarea directamente.
 *
 * Ejemplo: En la url https://retosdeprogramacion.com?year=2023&challenge=0
 * los parámetros serían ["2023", "0"]
 */
```
* **#11** - [`VIERNES 13`](./Retos/Reto%20%2312%20-%20VIERNES%2013%20%5BFácil%5D)
```
/*
 * Crea una función que sea capaz de detectar si existe un viernes 13 en el mes y el año indicados.
 * - La función recibirá el mes y el año y retornará verdadero o falso.
 */
```
* **#12** - [`ADIVINA LA PALABRA`](./Retos/Reto%20%2313%20-%20ADIVINA%20LA%20PALABRA%20%5BMedia%5D)
```
/*
 * Crea un pequeño juego que consista en adivinar palabras en un número máximo de intentos:
 * - El juego comienza proponiendo una palabra aleatoria incompleta
 *   - Por ejemplo "m_ur_d_v", y el número de intentos que le quedan
 * - El usuario puede introducir únicamente una letra o una palabra (de la misma longitud que
 *   la palabra a adivinar)
 *   - Si escribe una letra y acierta, se muestra esa letra en la palabra. Si falla, se resta
 *     uno al número de intentos
 *   - Si escribe una resolución y acierta, finaliza el juego, en caso contrario, se resta uno
 *     al número de intentos
 *   - Si el contador de intentos llega a 0, el jugador pierde
 * - La palabra debe ocultar de forma aleatoria letras, y nunca puede comenzar ocultando más del 60%
 * - Puedes utilizar las palabras que quieras y el número de intentos que consideres
 */
```
* **#13** - [`OCTAL Y HEXADECIMAL`](./Retos/Reto%20%2314%20-%20OCTAL%20Y%20HEXADECIMAL%20%5BFácil%5D)
```
/*
 * Crea una función que reciba un número decimal y lo trasforme a Octal
 * y Hexadecimal.
 * - No está permitido usar funciones propias del lenguaje de programación que
 * realicen esas operaciones directamente.
 */
```
* **#14** - [`AUREBESH`](./Retos/Reto%20%2315%20-%20AUREBESH%20%5BFácil%5D)
```
/*
 * Crea una función que sea capaz de transformar Español al lenguaje básico del universo
 * Star Wars: el "Aurebesh".
 * - Puedes dejar sin transformar los caracteres que no existan en "Aurebesh".
 * - También tiene que ser capaz de traducir en sentido contrario.
 *  
 * ¿Lo has conseguido? Nómbrame en twitter.com/mouredev y escríbeme algo en Aurebesh.
 *
 * ¡Que la fuerza os acompañe!
 */
```
* **#15** - [`LA ESCALERA`](./Retos/Reto%20%2316%20-%20LA%20ESCALERA%20%5BMedia%5D)
```
/*
 * Crea una función que dibuje una escalera según su número de escalones.
 * - Si el número es positivo, será ascendente de izquiera a derecha.
 * - Si el número es negativo, será descendente de izquiera a derecha.
 * - Si el número es cero, se dibujarán dos guiones bajos (__).
 * 
 * Ejemplo: 4
 *         _
 *       _|       
 *     _|
 *   _|
 * _|
 * 
 */
```
