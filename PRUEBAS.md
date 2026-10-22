# Pruebas técnicas del prototipo

Fecha de ejecución: 22 de octubre de 2026 (America/Lima).
Código base: `dcda76a`. Python 3.13 en Windows.

Se ejecutaron procesos nuevos de `main.py` con entradas controladas,
copias aisladas del programa y datos ficticios. Se comprobó la salida de
consola y el contenido del TXT mediante aserciones; no se usaron ni
modificaron los expedientes personales de la carpeta del proyecto.

| Caso | Resultado esperado y comprobado | Estado |
|---|---|---|
| Archivo inexistente | Buscar y listar indican que no hay registros; no crean el TXT. | Correcto |
| Opciones inválidas y retorno | Se repite el menú apropiado y se puede volver y salir. | Correcto |
| Registro y validaciones | Rechaza vacíos, separador, DNI inválido y tipo inválido; conserva tildes y ceros. | Correcto |
| Cinco tipos y persistencia | Guarda las cuatro categorías y Otro especificado, conservando registros entre ejecuciones. | Correcto |
| Consultas desde TXT | Código completo con minúsculas, DNI con varios trámites y sin coincidencias; archivo intacto. | Correcto |
| Ordenamiento y total | Orden numérico con uno o varios registros, inversos, ordenados y códigos mayores a 9999; TXT intacto. | Correcto |
| Código correlativo | Usa el máximo más uno, aunque las filas estén desordenadas y la última no tenga salto. | Correcto |
| TXT vacío | Búsqueda y listado muestran aviso sin modificar el archivo. | Correcto |
| TXT dañado o códigos duplicados | Informa el error y no añade registros ni modifica el archivo. | Correcto |

Resultado: **9 grupos de pruebas aprobados**. Cada grupo puede incluir varias ejecuciones.

## Prueba manual para la sustentación

1. Ejecutar `py main.py` en una copia destinada a demostración.
2. Registrar dos trámites con el mismo DNI ficticio y tipos distintos.
3. Salir con 4 y volver a ejecutar el programa.
4. Buscar por uno de los códigos completos y comprobar sus datos.
5. Buscar por el DNI ficticio y comprobar que aparecen ambos trámites.
6. Volver al menú principal y listar con 3; comprobar códigos y total.
7. Conservar capturas propias de estas ejecuciones para el informe.

## Alcance pendiente

Estas son pruebas técnicas con datos ficticios, no pruebas de campo.
El equipo debe completar casos basados en el proceso observado y sus
evidencias. No se probaron múltiples instancias simultáneas, cortes de
energía durante escritura, grandes volúmenes ni uso institucional real.
El respaldo automático sigue pendiente si el equipo lo confirma como requisito.
