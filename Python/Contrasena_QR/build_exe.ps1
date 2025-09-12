# Script PowerShell para crear un ejecutable de la aplicación decifrar_contrasena_qr
# Pasos:
# 1. Crear y activar un entorno virtual
# 2. Instalar dependencias desde requirements.txt
# 3. Ejecutar PyInstaller para generar un ejecutable

$env:VENV_DIR = "venv"

# 1. Crear entorno virtual
python -m venv $env:VENV_DIR

# 2. Activar entorno virtual
& "$env:VENV_DIR\Scripts\Activate.ps1"

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Ejecutar PyInstaller (ventana única para Tkinter)
# Usamos la carpeta actual como fuente de hooks para incluir hook-pyzbar.py
pyinstaller --onefile --noconsole --additional-hooks-dir=. decifrar_contrasena_qr.py

Write-Host "Generación completada. Revisa la carpeta 'dist' para el ejecutable."
Write-Host "Si PyInstaller sigue fallando por DLLs faltantes, intenta ejecutar PyInstaller con opciones adicionales:"
Write-Host "pyinstaller --onefile --noconsole --add-binary \"path\\to\\pyzbar\\libiconv.dll;pyzbar\" decifrar_contrasena_qr.py"
