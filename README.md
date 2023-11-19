<p align="center">
  <img width=200px height=200px src="https://cdn-icons-png.flaticon.com/512/7439/7439625.png" alt="Logo del Compilador">
</p>

<h3 align="center">Compilador con Análisis Léxico, Sintáctico y Semántico</h3>

<div align="center">

[![Estado](https://img.shields.io/badge/estado-activo-success.svg)]()
[![Plataforma](https://img.shields.io/badge/plataforma-cualquiera-brightgreen.svg)](https://www.tupaginawebdelcompilador.com)
[![GitHub Issues](https://img.shields.io/github/issues/tuusuario/turepo.svg)](https://github.com/tuusuario/turepo/issues)
[![GitHub Pull Requests](https://img.shields.io/github/issues-pr/tuusuario/turepo.svg)](https://github.com/tuusuario/turepo/pulls)
[![Licencia](https://img.shields.io/badge/licencia-MIT-blue.svg)](/LICENSE)

</div>

---

<p align="center"> 🧮 Compilador que realiza análisis léxico, sintáctico y semántico para expresiones matemáticas.
    <br> 
</p>

## 📝 Tabla de Contenidos

- [Acerca del Compilador](#acerca_del_compilador)
- [Estructura del Proyecto](#estructura_del_proyecto)
- [Uso del Compilador](#uso_del_compilador)
- [Ejemplo de Uso](#ejemplo_de_uso)
- [Contribuciones](#contribuciones)
- [Licencia](#licencia)

## 🧐 Acerca del Compilador <a name = "acerca_del_compilador"></a>

Este proyecto presenta un compilador que realiza análisis léxico, sintáctico y semántico para procesar expresiones matemáticas. La aplicación está escrita en Python y consta de tres componentes principales: el analizador léxico, el analizador sintáctico y el analizador semántico.

Este es un compilador simple que permite realizar operaciones matemáticas básicas y funciones trigonométricas. El compilador consta de tres componentes principales: Analizador Léxico, Analizador Sintáctico y Analizador Semántico.

## Estructura del Proyecto <a name = "estructura_del_proyecto"></a>

- **AnalizadorLexico:** Contiene la lógica para el análisis léxico, donde se generan los tokens a partir de la entrada.
  
- **AnalizadorSemantico:** Implementa comprobaciones semánticas adicionales, como división por cero y raíz cuadrada de números negativos.

- **AnalizadorSintactico:** Realiza el análisis sintáctico de la expresión, verificando la estructura gramatical de las operaciones matemáticas.

## Requisitos

- **Python 3.x**

## Instalacion

Clona este repositorio en tu máquina local:
``` 
git clone https://github.com/tu-usuario/compilador-matematico.git
```
Entra al directorio del compilador:
``` 
cd compilador-matematico

```
Ejecuta el script principal:
``` 
python main.py

```

## Uso del Compilador <a name = "uso_del_compilador"></a>

## Menu principal
El programa presenta un menú interactivo con las siguientes opciones:

- **Ejecutar línea:** Permite ingresar una expresión matemática y ver el resultado.
- **Seleccionar archivo:** Lee un archivo de texto con expresiones matemáticas y muestra los resultados.
- **Salir:** Cierra el compilador.

## Ejecutar linea (opcion 1)

- Ingresa una expresión matemática cuando se te solicite y observa el resultado.

## Seleccionar archivo (opcion 2)

- Ingresa el nombre o la ruta del archivo que contiene expresiones matemáticas.
- El compilador procesará cada línea del archivo y mostrará los resultados.

## Ejemplos <a name = "ejemplo_de_uso"></a>
## Opcion 1 (Ejecutar linea)
```python
Entrada
>>> 2 + 3 * 4

Salida
10

```
## Opcion 2 (Seleccionar archivo)
- Crea un archivo de texto (ejemplos.txt) con las siguientes líneas:
```
5 + 8
SEN(45)
```
- Ejecuta la opción "Seleccionar archivo" y proporciona el nombre del archivo (ejemplos.txt).
- Observa los resultados en la consola.


## Como funciona

1. **Entrada de Expresión:** El usuario proporciona una expresión matemática al compilador.

2. **Análisis Léxico:** La expresión se divide en tokens significativos.

3. **Análisis Sintáctico:** Se verifica la estructura gramatical de la expresión.

4. **Análisis Semántico:** Se realizan comprobaciones semánticas adicionales.

5. **Resultado:** El compilador devuelve el resultado de evaluar la expresión.


Este ejemplo muestra cómo instanciar el compilador, proporcionar una expresión matemática y obtener el resultado después de realizar el análisis léxico, sintáctico y semántico.

## Contribuciones <a name = "contribuciones"></a>
¡Las contribuciones son bienvenidas! Si encuentras algún problema o tienes ideas para mejorar el compilador, no dudes en abrir un problema o enviar una solicitud de extracción.

## Licencia <a name = "licencia"></a>
Este proyecto está bajo la Licencia MIT. Consulta el archivo LICENSE para obtener más detalles.

Espero que este compilador sea útil y educativo. ¡Disfruta explorando y experimentando con el código!
