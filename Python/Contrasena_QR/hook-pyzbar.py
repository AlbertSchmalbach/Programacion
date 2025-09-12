# Hook for PyInstaller to collect dynamic libraries from pyzbar
from PyInstaller.utils.hooks import collect_dynamic_libs

# Collect all dynamic libraries bundled with pyzbar (e.g. libiconv.dll, libzbar.dll)
binaries = collect_dynamic_libs('pyzbar')
