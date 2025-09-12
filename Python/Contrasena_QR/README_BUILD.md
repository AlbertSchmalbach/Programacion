Instrucciones para generar un ejecutable (Windows)

Requisitos previos:
- Python 3.8+ instalado y en PATH.
- Visual C++ Redistributable (si PyInstaller lo requiere para dependencias nativas).

Pasos rápidos:
1. Abrir PowerShell en la carpeta del proyecto `Python\Contrasena_QR`.
2. Ejecutar el script:

   .\build_exe.ps1

Notas:
- El script crea un entorno virtual `venv`, instala dependencias desde `requirements.txt` y corre PyInstaller.
- PyInstaller empaqueta la aplicación en `dist\decifrar_contrasena_qr.exe`.
- Si la cámara o codecs de OpenCV faltan, instala las dependencias del sistema adecuadas.

Alternativa manual:

pip install -r requirements.txt
pyinstaller --onefile --noconsole decifrar_contrasena_qr.py

Archivos relevantes:
- `decifrar_contrasena_qr.py` - código fuente principal
- `requirements.txt` - dependencias Python
- `build_exe.ps1` - script automatizado para Windows
