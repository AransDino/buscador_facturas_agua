import os
import re
import shutil
import time
import string
import ctypes

# === CONFIGURACIÓN ===
ruta_destino = r"C:\Users\Ayoze\Downloads\FACTURAS EJEMPLO\AGUA"
patron = re.compile(r'^D\d{9}\.pdf$', re.IGNORECASE)

# === FUNCIONES ===
def obtener_unidades():
    """Devuelve una lista de unidades disponibles en el sistema."""
    unidades = []
    bitmask = ctypes.windll.kernel32.GetLogicalDrives()
    for i in range(26):  # A-Z
        if bitmask & (1 << i):
            unidad = f"{chr(65 + i)}:\\"
            unidades.append(unidad)
    return unidades

# === INICIALIZACIÓN DE VARIABLES ===
os.makedirs(ruta_destino, exist_ok=True)
archivos_encontrados = 0
archivos_copiados = 0
errores = 0
carpetas_escaneadas = 0

# Abrir archivo de errores
ruta_errores = os.path.join(ruta_destino, "errores_copia.txt")
archivo_errores = open(ruta_errores, "w", encoding="utf-8")

print("Iniciando búsqueda en todas las unidades...")
inicio = time.time()

# === RECORRIDO DE UNIDADES ===
for unidad in obtener_unidades():
    print(f"\n>> Escaneando unidad: {unidad}")
    for carpeta_actual, subcarpetas, archivos in os.walk(unidad):
        carpetas_escaneadas += 1
        print(f"[{carpetas_escaneadas}] Carpeta: {carpeta_actual}")
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
print("\n--- RESUMEN FINAL ---")
print(f"Unidades escaneadas:   {len(obtener_unidades())}")
print(f"Carpetas escaneadas:   {carpetas_escaneadas}")
print(f"Archivos encontrados:  {archivos_encontrados}")
print(f"Archivos copiados:     {archivos_copiados}")
print(f"Errores de copia:      {errores}")
print(f"Tiempo total:          {fin - inicio:.2f} segundos")
