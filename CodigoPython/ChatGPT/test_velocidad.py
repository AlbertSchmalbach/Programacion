import speedtest

def medir_velocidad():
    st = speedtest.Speedtest()
    
    # Realizar una prueba de velocidad
    st.get_best_server()
    download_speed = st.download() / 1024 / 1024  # velocidad de descarga en Mbps
    upload_speed = st.upload() / 1024 / 1024  # velocidad de carga en Mbps
    
    print(f"Velocidad de descarga: {download_speed:.2f} Mbps")
    print(f"Velocidad de carga: {upload_speed:.2f} Mbps")

if __name__ == "__main__":
    medir_velocidad()
