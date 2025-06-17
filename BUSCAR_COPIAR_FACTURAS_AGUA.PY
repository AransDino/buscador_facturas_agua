import os
import re
import shutil
import time

# === CONFIGURACIÓN ===
ruta_origen = "H:\\"
ruta_destino = r"C:\Users\Ayoze\Downloads\FACTURAS EJEMPLO\AGUA"
patron = re.compile(r'^D\d{9}\.pdf$', re.IGNORECASE)

# === INICIALIZACIÓN DE VARIABLES ===
os.makedirs(ruta_destino, exist_ok=True)
archivos_encontrados = 0
archivos_copiados = 0
errores = 0
carpetas_escaneadas = 0

# Abrir archivo de errores
ruta_errores = os.path.join(ruta_destino, "errores_copia.txt")
archivo_errores = open(ruta_errores, "w", encoding="utf-8")

print(f"Iniciando búsqueda en: {ruta_origen}")
inicio = time.time()

# === RECORRIDO ===
for carpeta_actual, subcarpetas, archivos in os.walk(ruta_origen):
    carpetas_escaneadas += 1
    print(f"[{carpetas_escaneadas}] Escaneando: {carpeta_actual}")
    for archivo in archivos:
        if patron.match(archivo):
            archivos_encontrados += 1
            ruta_archivo = os.path.join(carpeta_actual, archivo)
            ruta_destino_archivo = os.path.join(ruta_destino, archivo)
            if not os.path.exists(ruta_destino_archivo):
                try:
                    shutil.copy2(ruta_archivo, ruta_destino)
                    archivos_copiados += 1
                    print(f"  ✔ Copiado: {archivo}")
                except Exception as e:
                    errores += 1
                    print(f"  ✖ Error al copiar {archivo}: {e}")
                    archivo_errores.write(f"{ruta_archivo} - {e}\n")
            else:
                print(f"  ⏩ Ya existe: {archivo}")

archivo_errores.close()

# === ESTADÍSTICAS ===
fin = time.time()
print("\n--- RESUMEN ---")
print(f"Carpetas escaneadas:   {carpetas_escaneadas}")
print(f"Archivos encontrados:  {archivos_encontrados}")
print(f"Archivos copiados:     {archivos_copiados}")
print(f"Errores de copia:      {errores}")
print(f"Tiempo total:          {fin - inicio:.2f} segundos")
