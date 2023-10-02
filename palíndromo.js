// function esPalindromoConFuncion(palabra) {
//     let invertida = palabra.split("").reverse().join("");
//     return (invertida === palabra);
// }

function esPalindromo(palabra) {
    // dividir la cadena en un array en letras
    let letras = [];

    for (let i = 0; i < palabra.length; i++){
        letras.push(palabra[i]);
    }

    // invertir en array con un bucle
    let letrasInvertidas = [];
    for(let i = letras.length - 1; i >= 0; i--) {
       letrasInvertidas.push(letras[i]);
    }

    // unir todas las letras del array con un bucle y guardado resultado
    // en una variable
    let palabraInvertida = "";
    for (let i = 0; i < letrasInvertidas.length; i++){
        palabraInvertida += letrasInvertidas[i]
    }

    // devolver resultado
    return (palabra === palabraInvertida);
}

console.log(esPalindromo("otto"))
console.log(esPalindromo("Victor"))

