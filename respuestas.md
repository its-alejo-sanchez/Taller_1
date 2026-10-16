## Ejercicio 1: Entrada, conversión y control de un ciclo

### 1. Rastreo del programa con las entradas "4", "-2", "6", "fin"
El programa inicia con `total = 0.0` y `cantidad = 0`. El comportamiento paso a paso con cada entrada es:

| Entrada (`texto`) | `valor` | ¿`texto == "fin"`? | ¿`valor >= 0`? | `total` | `cantidad` | Estado / Resultado |
| :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `"4"` | `4.0` | No | Sí | `4.0` | `1` | Se procesa correctamente. |
| `"-2"` | `-2.0` | No | No | `4.0` | `2` | **Error lógico:** No se suma, pero incrementa `cantidad`. |
| `"6"` | `6.0` | No | Sí | `10.0` | `3` | Se procesa correctamente. |
| `"fin"` | *N/A* | *No llega* | *No llega* | `10.0` | `3` | **Lanza `ValueError`** en `float(texto)`. |

* ¿Dónde se interrumpe? Se interrumpe en la línea `valor = float(texto)` al ingresar `"fin"`.
* ¿Llega a imprimir el promedio? No, la excepción `ValueError` detiene el programa por completo antes de la línea del `print`.

### 2. Código Corregido
*El código corregido se encuentra implementado en el archivo `ejercicio_01.py`.*

### 3. Explicación sobre el uso de `eval(texto)`
* Falla con `"fin"`: `eval("fin")` busca una variable llamada `fin` y lanza un `NameError`, por lo que el ciclo seguiría rompiéndose inesperadamente.
* Seguridad (Inyección de código): `eval()` ejecuta cualquier cadena como código vivo de Python. Si un usuario ingresa un comando malicioso, el sistema lo ejecutará.
* Violación de contrato: El contrato especifica una medición numérica individual. `eval()` rompe esto al permitir estructuras complejas (listas, funciones, booleanos).

---



## Ejercicio 2: Colecciones, alias y estado de una función

### 1. Predicción de las tres salidas y análisis de objetos
Al ejecutar el fragmento original del taller, las salidas exactas son:
* `print(datos)` -> `[2, 4]`
* `print(registro)` -> `{'ultima': [3, 4, 8]}`
* `print(salida)` -> `[3, 4, 8]`

Análisis de objetos y alias:
* Objetos distintos: `datos` y `salida` apuntan a listas completamente diferentes en memoria gracias al uso de `.copy()`. Por eso `datos` se mantuvo intacto.
* Nombres que apuntan a la misma lista: El nombre `salida` y la entrada del diccionario `registro["ultima"]` comparten exactamente la misma referencia en memoria. 
* ¿Copiar valores evita todas las modificaciones compartidas? No. El método `.copy()` inicial protegió a la variable `datos`, pero al asignar `registro["ultima"] = copia`, se creó un alias externo. Cualquier mutación posterior sobre `salida` (como `.append(8)`) altera el interior del diccionario porque ambos apuntan al mismo objeto mutado.

### 2. Modificación del registro para aislar el estado
La asignación debe cambiarse a:
```python
registro["ultima"] = copia.copy()
```
Justificación: Al guardar una copia explícita dentro del diccionario, se rompe el enlace de referencia con la lista que la función va a retornar. Como los elementos internos de la lista son números (tipos de datos inmutables), una copia superficial con `.copy()` es 100% suficiente para garantizar que los cambios en `salida` no afecten el historial del registro.

### 3. Entrada como Tupla y solución universal
* Operación que fallaría: Si `datos` fuera `(2, 4)`, la primera operación en fallar sería `copia = valores.copy()`, arrojando un error de tipo `AttributeError: 'tuple' object has no attribute 'copy'` debido a que las tuplas no implementan ese método.
* Cambio propuesto: Reemplazar esa línea por:
```python
copia = list(valores)
```
Esta modificación permite que la función acepte cualquier objeto iterable (sea una lista o una tupla) y genere siempre una lista nueva y mutable sobre la cual operar, preservando intacto el resto de la lógica de la función.



## Ejercicio 3: Primalidad, break y for…else

### 1. Retorno y comportamiento para 1, 2 y 9
* Para `n = 1`: Devuelve `True`. El ciclo `range(2, 1)` está vacío, por lo que no se ejecuta ninguna iteración. Al no interrumpirse con un `break`, el flujo entra directamente al bloque `else` del ciclo, asignando `resultado = True`.
* Para `n = 2`: Devuelve `True`. El ciclo `range(2, 2)` está vacío, por lo que no se ejecuta ninguna iteración. Pasa directamente al bloque `else` del ciclo, asignando `resultado = True`.
* Para `n = 9`: Devuelve `False`. El ciclo se ejecuta y **se prueba el divisor 3** (ya que 9 % 2 != 0, pero 9 % 3 == 0). Al cumplirse la condición, se ejecuta el `break` e interrumpe el ciclo, por lo que no se alcanza el bloque else.

### 3. Refutación de la interpretación del `for...else`
La afirmación *"el else significa que el último if fue falso"* es falsa. 
Si tomamos como contraejemplo el caso de `n = 1` o `n = 2`, el ciclo ni siquiera llega a evaluar la condición del `if` porque el rango está vacío. Sin embargo, el programa entra al `else`. En Python, el bloque `else` asociado a un ciclo `for` significa estrictamente: *"el ciclo terminó de recorrerse de forma completa y natural sin haber sido interrumpido por un `break`"*.




## Ejercicio 4: Recursividad: contrato, caso base y progreso

### 1. Secuencia de llamadas para euclides(84, 30)
La secuencia de ejecuciones recursivas es la siguiente:
1. `euclides(84, 30)` -> Calcula `84 % 30 = 24`, llama a `euclides(30, 24)`
2. `euclides(30, 24)` -> Calcula `30 % 24 = 6`, llama a `euclides(24, 6)`
3. `euclides(24, 6)`  -> Calcula `24 % 6 = 0`, llama a `euclides(6, 0)`
4. `euclides(6, 0)`   -> Caso base activo (`b == 0`). **Retorna 6**.

¿Qué cantidad disminuye y por qué termina?
La cantidad que disminuye de forma estrictamente decreciente en cada paso es el segundo argumento `b` (que pasa a tomar el valor de `a % b`). Debido a las propiedades matemáticas de la división entera, el residuo `a % b` siempre es un entero estrictamente menor que el divisor `b` y mayor o igual a cero (\(0 \le r < b\)). Como los enteros no pueden disminuir infinitamente hacia el cero sin alcanzarlo, el algoritmo tiene garantizado terminar en un número finito de pasos cuando el residuo sea exactamente `0`.

### 2. Insuficiencia de los casos de prueba 0 y 4
Probar únicamente con `0` y `4` no es suficiente para verificar el contrato porque estos valores son positivos o cero. El contrato exige explícitamente validar el comportamiento para un entero no negativo. Al no evaluar cómo reacciona el código ante un número negativo (como `-1` o `-5`), se oculta un fallo crítico: el programa entraría en una recursión infinita (superando el límite de llamadas del sistema) ya que la condición `n <= 1` se cumpliría de inmediato en la primera llamada de `factorial(-1)` devolviendo `1`, lo cual es matemáticamente incorrecto.

### 3. Factorial(4): Llegar al caso base frente a terminar toda la ejecución
Cuando la recursión llega a su caso base más profundo (`n = 1`), la función no ha terminado de calcular el resultado; apenas ha completado la fase de bajada. Las multiplicaciones quedan "en espera" acumuladas en la pila de llamadas del sistema. 

Al alcanzarse el caso base, las multiplicaciones pendientes por resolverse en la fase de subida son:
\[\text{Resultado} = 4 \times (3 \times (2 \times 1))\]




## Ejercicio 5: Contratos con *args, **kwargs y zip

### 1. Peligro de usar `zip` sin verificar longitudes
Utilizar la función incorporada `zip` de Python sin validar previamente que las colecciones midan lo mismo puede ocultar un error grave de consistencia en los datos. Por defecto, `zip` detiene la generación de tuplas en el momento en que la colección más corta se agota, ignorando silenciosamente los elementos sobrantes de la colección más larga. Esto provocaría que el programa ignore mediciones o intervalos faltantes sin alertar al usuario mediante un error.

### 2. Comportamiento ante argumentos mal formateados o errores ortográficos
* Si se usa `pares` sin asterisco (`*`): La función recibiría la lista de tuplas completa como un único elemento posicional dentro de la tupla `pares` (es decir, `pares` sería `([(1, 7), (8, 0)],)`). Al intentar desempaquetar o iterar con la expectativa de que cada elemento sea un par individual, el programa arrojará errores de longitud o de emparejamiento.
* Si se escribe mal la opción (`esacala`): El bloque de validación de la función detectará que `"esacala"` no forma parte de las palabras clave permitidas en las opciones y lanzará inmediatamente un `ValueError` debido a la presencia de una clave desconocida.




## Ejercicio 6: Paquetes, importaciones y rutas

### 1. Predicción de líneas impresas y disponibilidad
Al ejecutar desde `curso/` en un proceso nuevo, se imprimen las siguientes líneas:
```text
Demostración 5.0
4.0
```
Explicación de la disponibilidad:
El script `principal.py` añade la carpeta `biblioteca` al inicio de `sys.path`. Al hacer `import Libreria`, Python busca la carpeta `Libreria` dentro de `biblioteca` y ejecuta su `__init__.py`. Este archivo realiza una importación relativa (`from .cinematica import velocidad`), la cual a su vez ejecuta `cinematica/__init__.py`. Este último importa `velocidad` desde el archivo `codigo.py` (`from .codigo import velocidad`). De esta manera, la función se propaga en cascada y queda expuesta directamente como un atributo del paquete principal bajo el nombre `Libreria.velocidad`.

### 2. Problemas de las rutas relativas y reescritura
Si el comando se lanza como `python curso/principal.py` desde el directorio superior:
* Problema con `sys.path.insert(0, "biblioteca")`: Python buscará una carpeta llamada `biblioteca` en el directorio actual (la raíz superior), lo cual provocará un error de tipo `ModuleNotFoundError` debido a que `biblioteca` se encuentra realmente adentro de la carpeta `curso/`.
* Problema con `Path("datos/mediciones.csv")`: Buscará el archivo dentro de una carpeta `datos/` situada en la raíz superior en lugar de buscar dentro de `curso/datos/`, rompiendo la carga de información.

### 3. Diferencia entre sys.path y Libreria.__file__
* `sys.path`: Es una lista de cadenas de texto que definen todos los directorios del sistema donde Python buscará módulos y paquetes al usar la instrucción `import`.
* `Libreria.__file__`: Es una propiedad específica del objeto módulo que contiene la ruta absoluta o relativa del archivo físico (`__init__.py`) que fue cargado en memoria para ese paquete.




## Ejercicio 7: Revisar un lector que oculta datos defectuosos

### 1. Comportamiento original e información perdida
Al procesar el archivo de ejemplo proporcionado, la función original devuelve únicamente:
`[(0.0, 2.0)]`

Información que se pierde:
El lector descarta por completo y de forma silenciosa la línea 3 (`1, error`) y la línea 4 (`2, 8, extra`). No le informa al usuario que existieron datos defectuosos ni especifica en qué parte del documento ocurrieron las fallas (la conversión de texto a número falló en la línea 3 por la palabra "error", y en la línea 4 se produjo un desbordamiento de índice o lectura errónea según cómo opere el corte por comas).

### 3. Archivos de prueba y justificación del manejo de errores
Para validar y contrastar el comportamiento entre ambas versiones, se proponen estos dos archivos:

* Archivo A (`vacio.csv`): Contiene únicamente la cabecera `tiempo_s,posicion_m` y ninguna fila de datos.
  * *Original:* Devuelve `[]`.
  * *Corregida:* Lanza un `ValueError` indicando la ausencia total de mediciones en el archivo.
* Archivo B (`defectuoso.csv`): Contiene datos correctos mezclados con un campo mal estructurado (ej. `1.5, texto_invalido`).
  * *Original:* Omite la fila defectuosa de manera silenciosa y devuelve solo los datos limpios.
  * *Corregida:* Interrumpe inmediatamente la ejecución lanzando una excepción detallada que especifica el número exacto de la fila que causó el fallo.

Justificación: Devolver una lista vacía `[]` ante cualquier eventualidad impediría diferenciar entre un archivo perfectamente válido que simplemente no contiene registros, un archivo con un encabezado corrupto o un archivo que falló a mitad de la lectura por culpa de una cadena de caracteres mal formateada. Detener el programa con una excepción descriptiva asegura la integridad de los análisis de datos posteriores.




## Ejercicio 8: Algoritmo de puntos medios: corregir a partir de una especificación

### 1. Cálculo manual para a=0, b=2, n=2
* Datos iniciales: `ancho = (2 - 0) / 2 = 1.0`. Los dos subintervalos son `[0, 1]` (para `i=0`) y `[1, 2]` (para `i=1`).

* Código Defectuoso Original:
  * `i = 0`: `centro = 0 + 0 * 1 = 0`. Contribución: `0**2 * 1 = 0`. El acumulador pasa a ser `0`.
  * `i = 1`: `centro = 0 + 1 * 1 = 1`. Contribución: `1**2 * 1 = 1`. El acumulador se sobreescribe y pasa a ser `1`.
  * Resultado devuelto por el código original: `1.0`

* Algoritmo Especificado Correcto (Puntos Medios):
  * `i = 0`: `centro = 0 + (0 + 0.5) * 1 = 0.5`. Contribución: `0.5**2 * 1 = 0.25`.
  * `i = 1`: `centro = 0 + (1 + 0.5) * 1 = 1.5`. Contribución: `1.5**2 * 1 = 2.25`.
  * Resultado que debe devolver la especificación: `0.25 + 2.25 = 2.5`

### 2. Identificación de errores y justificación de la corrección
Arreglar únicamente la ecuación del punto medio no basta porque el código original presenta tres fallas críticas adicionales:
1. Validación tardía: Calcula el `ancho` antes de validar si `n` o el intervalo son correctos. Si `n <= 0`, ocurrirá un error destructivo de división por cero (`ZeroDivisionError`) antes de poder lanzar la excepción `ValueError`.
2. Sobreescritura del acumulador: En la línea `acumulado = centro**2 * ancho`, se utiliza el operador de asignación simple `=` en lugar del operador de adición `+=`. Esto descarta los cálculos de todas las iteraciones previas y provoca que la función solo retorne el área del último subintervalo calculado.
3. Inicialización ineficiente: Aunque no es un error fatal, la validación debe ocurrir al puro inicio para proteger la integridad del flujo antes de gastar recursos en operaciones aritméticas.




## Ejercicio 9: Entorno, terminal y Git: diagnóstico de una secuencia

### 1. Explicación de comandos de entorno virtual y borrado
* `python3 -m venv .venv`: Crea una carpeta oculta llamada `.venv` en el directorio actual. Dentro de ella instala una copia aislada del ejecutable de Python, la herramienta `pip` y una estructura limpia de bibliotecas.
* `source .venv/bin/activate`: Modifica temporalmente las variables de entorno de tu terminal activa (especialmente la variable `$PATH`) para que al escribir el comando `python`, el sistema use el ejecutable aislado de la carpeta `.venv` en lugar del Python global de la computadora.
* `python programa.py`: Ejecuta el script utilizando el intérprete de Python del entorno virtual que acabas de activar.

¿Crear equivale a activar? No. Crear solo genera los archivos físicos en el disco duro. Activar es el paso necesario para indicarle a la terminal que debe empezar a utilizar esos archivos aislados.
¿Borrar `.venv` borra tu código? No, no lo borra. El script `programa.py` se encuentra en la carpeta raíz del proyecto, de forma paralela y externa a `.venv`. Como la carpeta del entorno virtual solo almacena binarios y librerías descargadas, eliminarla no altera tus archivos de código fuente.

### 2. Control de cambios en Git (Ciclo de vida del archivo)
Al ejecutar `git commit -m "Respuestas"`, la versión que entra en el commit es la primera versión (la que existía en el instante exacto en que ejecutaste `git add respuestas.md`). Las modificaciones posteriores se consideran cambios fuera del área de preparación (*staging area*).

Para incluir las modificaciones posteriores en un nuevo commit, debes ejecutar los siguientes comandos en tu terminal de Bash:
```bash
git add respuestas.md
git commit -m "Incluye modificaciones posteriores de las respuestas"
```

### 3. Guardar, Crear Commit y Subir a GitHub
* Guardar un archivo: Operación local del editor (VS Code) que escribe los cambios en el disco duro de tu máquina. Git aún no realiza ningún seguimiento de este paso.
* Crear un commit: Registra una foto fija (*snapshot*) de los cambios que estaban en el área de preparación dentro de la base de datos local de Git en tu computadora.
* Subir a GitHub (`push`): Copia y transfiere todos los commits registrados en tu historial local hacia los servidores remotos de GitHub para que estén disponibles en la nube.

Comandos para la terminal:
* Ver cambios pendientes: `git status`
* Enviar los commits al repositorio remoto: `git push`
