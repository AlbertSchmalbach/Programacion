Packaging notes — including pyzbar DLLs for Windows

1) Preferred: use a PyInstaller hook (provided in this folder) so PyInstaller automatically bundles pyzbar dynamic libraries.

   From this folder run:

   ```bash
   pyinstaller --onefile --additional-hooks-dir=. decifrar_contrasena_qr.py
   ```

   The `hook-pyzbar.py` will collect pyzbar's `.pyd` / DLL files and data files.

2) If you still get a missing dynlib/dll error, locate pyzbar package files and add them manually.

   Find the pyzbar package folder from Python:

   ```bash
   python -c "import pyzbar, os; print(os.path.dirname(pyzbar.__file__))"
   ```

   Look for files like `pyzbar*.pyd` or `libzbar-0.dll` inside that folder. Then run PyInstaller adding them explicitly, for example (Windows):

   ```bash
   pyinstaller --onefile \
     --add-binary "C:\path\to\pyzbar\pyzbar.cp310-win_amd64.pyd;pyzbar" \
     --add-binary "C:\path\to\pyzbar\libzbar-0.dll;." \
     decifrar_contrasena_qr.py
   ```

   Replace paths/filenames above with the actual files you found.

3) Ensure runtime zbar is present if your pyzbar installation requires a separately-installed zbar runtime. On Windows you can install a zbar binary or use a pyzbar wheel that bundles the DLL.

4) Dependencies

   Create a `requirements.txt` and install into a clean virtualenv before packaging:

   ```bash
   pip install -r requirements.txt
   ```
