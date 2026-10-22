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
código único y fecha automática. Búsquedas y ordenamiento pendientes.

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
