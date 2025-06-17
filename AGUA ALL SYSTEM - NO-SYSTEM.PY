import os
import re
import shutil
import time
import ctypes

# === CONFIGURACIÓN ===
ruta_destino = r"C:\Users\yasla\Downloads\ayoze\buscador_facturas_agua\FACTURAS LOCALIZADAS"
patron = re.compile(r'^D\d{9}\.pdf$', re.IGNORECASE)

# Nombres de carpetas a evitar (no rutas completas, para cortar recursión)
nombres_excluidos = ['windows', 'program files', 'program files (x86)', 'appdata',
                     'system volume information', '$recycle.bin', 'videos', 'onedrive']

def obtener_unidades():
    unidades = []
    bitmask = ctypes.windll.kernel32.GetLogicalDrives()
    for i in range(26):
        if bitmask & (1 << i):
            unidades.append(f"{chr(65 + i)}:\\")
    return unidades

# === INICIALIZACIÓN ===
os.makedirs(ruta_destino, exist_ok=True)
archivos_encontrados = 0
archivos_copiados = 0
errores = 0
carpetas_escaneadas = 0
ruta_errores = os.path.join(ruta_destino, "errores_copia.txt")
archivo_errores = open(ruta_errores, "w", encoding="utf-8")

inicio = time.time()
print("Iniciando búsqueda...")

for unidad in obtener_unidades():
    print(f"\n>> Escaneando unidad: {unidad}")
    for carpeta_actual, subcarpetas, archivos in os.walk(unidad, topdown=True):
        # Modificar subcarpetas en vivo para excluir
        subcarpetas[:] = [d for d in subcarpetas if d.lower() not in nombres_excluidos]

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
fin = time.time()

# === RESUMEN ===
print("\n--- RESUMEN ---")
print(f"Unidades escaneadas:   {len(obtener_unidades())}")
print(f"Carpetas escaneadas:   {carpetas_escaneadas}")
print(f"Archivos encontrados:  {archivos_encontrados}")
print(f"Archivos copiados:     {archivos_copiados}")
print(f"Errores de copia:      {errores}")
print(f"Tiempo total:          {fin - inicio:.2f} segundos")

input("\nPresiona ENTER para salir...")

