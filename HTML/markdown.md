---
marp: true
---


# TUTORIAL MARKDOWN

## 1. ENCABEZADOS

# Titular

Esto es un fregamento de texto.

## Subtitular

Esto es un fragmento mas pequeño.

OtroTitular
===========

otroSubtitular
--------------

---

## 2. FORMATOS

Esto es un ejemplo de **texto en negrita** y otra __forma de hacerlo__.

_texto en cursiva_. Opcionalmente, tambien *asi*.

***texto en negrita y en cursiva***. 

También puedes ~~tachar texto~~.


otroSubtitular
--------------

Frase destacada: ==Texto destacado==

Subscript: H~2~O

Superscript: x^2^

---

## 3. LISTAS

- Primer elemento de una lista
- Segundo elemento de una lista
  - Subelemento uno
  - Subelemento dos

* Primer elemento de una lista
* Segundo elemento de una lista
  * Subelemento uno
  * Subelemento dos

Si quieres escribir un asterisco, utiliza un slash \ antes: \*

---

## 3. ENLACES

[Google](www.google.com)

[Facebook](www.facebook.com)

### Notas a pie

Aquí tienes información sobre el concepto [Dunning-Krugger][1]. Por otro lado,
también tienes información sobre [el principio de Peter][2].

[1]: https://en.wikipedia.org/wiki/Dunning%E2%80%93Kruger_effect
[2]: https://en.wikipedia.org/wiki/Peter_Principle "El principio de Peter"

---

## 4. IMAGENES

![Imagen del artículo sobre Markdown](https://lenguajehtml.com/html/social.jpg)

---

## 5. CITAS

### Cita normal
Esto es un párrafo de texto y a continuación tienes una cita:

> Este es un ejemplo de cita.

Esto es una cita anidada:

### Cita anidada
>> Esto es una cita anidada.


---

# 6. CODIGO

los backticks para indicar código en línea: `console.log("Hola mundo")`

también podemos crear bloques de código:

```js
function log() {
  console.log("Hola!");
}
```

Otro bloque de texto:

    function log() {
      console.log("Hola!");
    }

---

## 7. LINEA

Si queremos añadir una línea horizontal a modo de separación temática, simplemente debemos escribir tres guiones seguidos: (---)

---

## 8. HTML

Esto es un párrafo de texto.

<details>
  <summary>Más información haciendo clic aquí</summary>
  <div>Información adicional.</div>
</details>

---

## 9. TABLAS

### Tabla normal

| Cabecera  | Cabecera  |
|-----------|-----------|
| Celda 1   | Celda 2   |
| Celda 3   | Celda 4   |

### Tabla con alineacion

| Cabecera  | Cabecera  |
|----------:|:---------:|
| Celda 1   | Celda 2   |
| Celda 3   | Celda 4   |

---

## 10. EMOJIS

Hello! :joy:
Quen onda :smile:

---

## 11. FRONTMATTER

/---/
title: "Título del documento"
description: "Esta es una descripción del contenido."
date: 2024-10-20
/---/

## Título del subcontenido

Más contenido **markdown** en el resto del fichero.

