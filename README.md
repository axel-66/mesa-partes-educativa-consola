# Mesa de partes educativa

Proyecto de Fundamentos de Programación (CIIN1205P).
Aplicación local en Python con consola y almacenamiento en TXT.

## Ejecución

Requiere Python 3.

```powershell
py main.py
```

## Avance actual

Registro de expedientes con campos obligatorios, DNI de 8 dígitos,
código único y fecha automática. Búsqueda por código o DNI desde un mismo
submenú, leyendo el TXT. Por DNI se muestran todos los trámites del solicitante.
Listado ascendente por código mediante ordenamiento por inserción, sin modificar
el TXT. En el menú principal, la opción 3 lista y la opción 4 permite salir.

Tipo de solicitud por opciones: constancia de estudios, certificado de estudios,
constancia de matrícula, libreta u otro (se solicita especificarlo).

## Archivo TXT

Se crea automáticamente `datos/expedientes.txt` al registrar el primer trámite.
Cada línea contiene:

```text
codigo|nombres|apellidos|dni|tipo|asunto|fecha
```

Los registros se conservan al cerrar el programa. Un DNI puede tener varios
expedientes. El archivo con datos personales no se sube a GitHub.

## Documentación

- [Diseño, diagrama y pseudocódigo](DISENO.md)
- [Resultados de pruebas técnicas](PRUEBAS.md)
