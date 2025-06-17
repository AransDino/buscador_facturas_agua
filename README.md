# Buscador de Facturas de Agua

Este proyecto contiene varios scripts en Python para buscar y copiar facturas de agua (archivos PDF con nombre `D#########.pdf`) desde diferentes ubicaciones del sistema a una carpeta destino.

## Scripts incluidos

- **BUSCAR_COPIAR_FACTURAS_AGUA.PY**  
  Busca facturas en una ruta específica (`H:\`) y las copia a una carpeta destino.

- **AGUA ALL SYSTEM.PY**  
  Escanea todas las unidades del sistema en busca de facturas y las copia a la carpeta destino especificada.

- **AGUA ALL SYSTEM - NO-SYSTEM.PY**  
  Similar al anterior, pero excluye carpetas del sistema y otras ubicaciones no deseadas durante la búsqueda.

## Uso

1. Asegúrate de tener Python 3 instalado en tu sistema.
2. Modifica las rutas de origen y destino en los scripts según tus necesidades.
3. Ejecuta el script deseado desde la terminal:

   ```sh
   python NOMBRE_DEL_SCRIPT.py
   ```

4. Los archivos encontrados se copiarán a la carpeta destino. Los errores se registran en un archivo `errores_copia.txt` dentro de la carpeta destino.

## Notas

- Los scripts requieren permisos de lectura en las unidades y carpetas a escanear.
- El patrón de búsqueda está definido para archivos PDF con nombres que empiezan por "D" seguido de 9 dígitos.
- Si ejecutas los scripts que escanean todo el sistema, pueden tardar varios minutos dependiendo del tamaño de tus discos.

## Autor
