from PyInstaller.utils.hooks import collect_dynamic_libs, collect_data_files

# Ensure PyInstaller includes pyzbar's compiled extensions and any bundled DLLs/data
binaries = collect_dynamic_libs('pyzbar')
datas = collect_data_files('pyzbar')
