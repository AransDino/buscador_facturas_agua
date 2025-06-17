# Buscador de Facturas de Agua

Este proyecto está diseñado para buscar y copiar facturas de agua (archivos PDF con nombres que siguen el patrón `D#########.pdf`) desde diferentes ubicaciones del sistema a una carpeta destino. Es útil para centralizar facturas dispersas en varias carpetas o unidades de almacenamiento.

## Descripción de los Scripts

### 1. **BUSCAR_COPIAR_FACTURAS_AGUA.PY**
- Este script busca facturas en una ruta específica (`H:\`) y las copia a una carpeta destino.
- Es ideal para búsquedas en una ubicación concreta.

### 2. **AGUA ALL SYSTEM.PY**
- Escanea todas las unidades del sistema en busca de facturas y las copia a la carpeta destino especificada.
- **Nota importante:** Antes de ejecutar este script, debes modificar la variable `ruta_destino` en el código para indicar la carpeta donde se copiarán las facturas encontradas.

### 3. **AGUA ALL SYSTEM - NO-SYSTEM.PY**
- Similar al anterior, pero excluye carpetas del sistema y otras ubicaciones no deseadas durante la búsqueda.
- **Nota importante:** Antes de ejecutar este script, debes modificar la variable `ruta_destino` en el código para indicar la carpeta donde se copiarán las facturas encontradas.

## Requisitos

- Python 3 instalado en tu sistema.
- Permisos de lectura en las unidades y carpetas que deseas escanear.
- Permisos de escritura en la carpeta destino.

## Configuración

1. **Modificar la variable `ruta_destino`:**
   - En los scripts `AGUA ALL SYSTEM.PY` y `AGUA ALL SYSTEM - NO-SYSTEM.PY`, localiza la variable `ruta_destino` y cámbiala por la ruta de la carpeta donde deseas que se copien las facturas encontradas. Por ejemplo:

     ```python
     ruta_destino = "C:\\ruta\\a\\tu\\carpeta\\destino"
     ```

2. **Opcional:** Si usas el script `BUSCAR_COPIAR_FACTURAS_AGUA.PY`, asegúrate de que la ruta de origen (`H:\`) sea válida en tu sistema.

## Uso

1. Abre una terminal en el directorio del proyecto.
2. Ejecuta el script deseado con el siguiente comando:

   ```sh
   python NOMBRE_DEL_SCRIPT.py
   ```

   Por ejemplo:

   ```sh
   python AGUA ALL SYSTEM.PY
   ```

3. Los archivos encontrados se copiarán a la carpeta destino especificada.
4. Si ocurre algún error durante la copia, se registrará en un archivo llamado `errores_copia.txt` dentro de la carpeta destino.

## Notas

- El patrón de búsqueda está definido para archivos PDF con nombres que comienzan con "D" seguido de 9 dígitos (por ejemplo, `D123456789.pdf`).
- Los scripts que escanean todo el sistema (`AGUA ALL SYSTEM.PY` y `AGUA ALL SYSTEM - NO-SYSTEM.PY`) pueden tardar varios minutos dependiendo del tamaño de tus discos y la cantidad de archivos.
- El script `AGUA ALL SYSTEM - NO-SYSTEM.PY` es más eficiente al evitar carpetas del sistema y otras ubicaciones no deseadas.

## Estructura del Proyecto

```
BUSCADOR DE FACTURAS DE AGUA/
│
├── BUSCAR_COPIAR_FACTURAS_AGUA.PY
├── AGUA ALL SYSTEM.PY
├── AGUA ALL SYSTEM - NO-SYSTEM.PY
└── README.md
```

## Autor

Este proyecto fue desarrollado por **Ayoze**.

## Licencia

Este proyecto no tiene una licencia específica. Puedes usarlo y modificarlo según tus necesidades.
