import wmi

# Nueva función: Crear un punto de restauración
def crear_punto_de_restauracion():
    try:
        c = wmi.WMI()
        restore_point = c.Win32_SystemRestore.CreateRestorePoint(
            "Punto de restauración generado por script", 0, 100)
        mensaje = "Punto de restauración creado exitosamente."
        print(f"[INFO] {mensaje}")
        escribir_reporte("Crear punto de restauración", mensaje)
    except Exception as e:
        mensaje = f"No se pudo crear el punto de restauración: {e}"
        print(f"[ERROR] {mensaje}")
        escribir_reporte("Crear punto de restauración", mensaje)

# Nueva función: Desinstalar un programa
def desinstalar_programa():
    programa = input("Ingrese el nombre del programa que desea desinstalar: ")
    confirmacion = input(
        f"¿Está seguro que desea desinstalar {programa}? Esto no se puede deshacer (S/N): ").strip().lower()
    if confirmacion == 's':
        try:
            subprocess.run(f"wmic product where name=\"{programa}\" call uninstall",
                           shell=True, check=True)
            mensaje = f"El programa {programa} fue desinstalado correctamente."
            print(f"[INFO] {mensaje}")
            escribir_reporte("Desinstalar programa", mensaje)
        except Exception as e:
            mensaje = f"No se pudo desinstalar el programa {programa}: {e}"
            print(f"[ERROR] {mensaje}")
            escribir_reporte("Desinstalar programa", mensaje)
    else:
        print("Desinstalación cancelada.")

# Nueva función: Listar y formatear unidades de disco
def listar_y_formatear_unidades():
    print("=== Listado de unidades de disco ===")
    unidades = [disk.device for disk in psutil.disk_partitions()]
    sistema = os.environ.get("SystemDrive", "C:")  # Unidad del sistema (por defecto C:)
    
    for unidad in unidades:
        try:
            uso = shutil.disk_usage(unidad)
            print(f"Unidad: {unidad} | Total: {uso.total // (1024**3)} GB | Libre: {uso.free // (1024**3)} GB")
        except Exception:
            print(f"Unidad: {unidad} (Error al obtener información)")

    print("\n=== Formatear unidades USB ===")
    for disk in psutil.disk_partitions(all=False):
        if "removable" in disk.opts.lower():
            print(f"Unidad USB detectada: {disk.device}")

    unidad_formatear = input("\nIngrese la letra de la unidad USB que desea formatear (ejemplo: D:\\): ").strip().upper()
    
    if unidad_formatear == sistema:
        print("[ERROR] No puede formatear la unidad del sistema.")
        return
    
    if not any(unidad_formatear in disk.device for disk in psutil.disk_partitions(all=False) if "removable" in disk.opts.lower()):
        print("[ERROR] La unidad seleccionada no es una unidad USB o no existe.")
        return

    confirmacion = input(f"¿Está seguro que desea formatear la unidad {unidad_formatear}? (S/N): ").strip().lower()
    if confirmacion == 's':
        try:
            subprocess.run(["format", unidad_formatear, "/FS:NTFS", "/Q", "/Y"], check=True, shell=True)
            print(f"[INFO] Unidad {unidad_formatear} formateada correctamente.")
            escribir_reporte("Formatear unidad USB", f"Unidad {unidad_formatear} formateada.")
        except Exception as e:
            print(f"[ERROR] No se pudo formatear la unidad: {e}")
            escribir_reporte("Formatear unidad USB", f"Error al formatear unidad {unidad_formatear}: {e}")
    else:
        print("Operación cancelada.")
        
# Nueva función: Restaurar a valores de fábrica
def restaurar_valores_fabrica():
    print("Este proceso restaurará el sistema a sus valores de fábrica.")
    print("Se recomienda crear un punto de restauración antes de continuar.")
    crear_punto = input("¿Desea crear un punto de restauración ahora? (S/N): ").strip().lower()
    if crear_punto == 's':
        crear_punto_de_restauracion()
    confirmacion = input(
        "¿Está seguro que desea restaurar el sistema a los valores de fábrica? Esto no se puede deshacer (S/N): ").strip().lower()
    if confirmacion == 's':
        try:
            subprocess.run("systemreset -factoryreset", shell=True)
            mensaje = "El sistema fue restaurado a sus valores de fábrica."
            print(f"[INFO] {mensaje}")
            escribir_reporte("Restaurar valores de fábrica", mensaje)
        except Exception as e:
            mensaje = f"No se pudo restaurar el sistema: {e}"
            print(f"[ERROR] {mensaje}")
            escribir_reporte("Restaurar valores de fábrica", mensaje)
    else:
        print("Restauración cancelada.")

# Actualización del menú
def menu():
    while True:
        print("\n=== OPTIMIZADOR DE PC ===")
        print("1. Eliminar archivos temporales")
        print("2. Vaciar papelera de reciclaje")
        print("3. Reorganizar archivos")
        print("4. Liberar espacio en disco")
        print("5. Borrar datos de navegación")
        print("6. Ver información del sistema")
        print("7. Realizar test de velocidad de Internet")
        print("8. Crear un punto de restauración")
        print("9. Desinstalar un programa")
        print("10. Listar y formatear unidades de disco")
        print("11. Restaurar sistema a valores de fábrica")
        print("12. Salir")
        opcion = input("Seleccione una opción: ")
        print()

        if opcion == '1':
            eliminar_archivos_temporales()
        elif opcion == '2':
            vaciar_papelera_reciclaje()
        elif opcion == '3':
            reorganizar_archivos()
        elif opcion == '4':
            liberar_espacio_disco()
        elif opcion == '5':
            borrar_datos_navegacion()
        elif opcion == '6':
            ver_informacion_sistema()
        elif opcion == '7':
            realizar_test_velocidad()
        elif opcion == '8':
            crear_punto_de_restauracion()
        elif opcion == '9':
            desinstalar_programa()
        elif opcion == '10':
            listar_y_formatear_unidad()
        elif opcion == '11':
            restaurar_valores_fabrica()
        elif opcion == '12':
            print("Saliendo del programa. ¡Adiós!")
            break
        else:
            print("[ERROR] Opción inválida. Intente de nuevo.")
