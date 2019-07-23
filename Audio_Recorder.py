import sounddevice as sd

# Establece la frecuencia de sampleo

fs = 44100 # Hercios

duracion = 10.5 # segundos

# Elegir el interfaz con el que se grabara el audio
# Descomentar estas lineas para mas opciones

# sd.default.device
# [5, 5]

# Configurar la latencia por defecto

latencia = sd.default_latency = 'high', 'high'

# No dejar la entrada de audio caer

ever_drop_input = False

# extra_settings = _default_extra_settings = None, None

# extra_settings = default_extra_settings = None, None

# prime_output_buffers_using_stream_callback = False

# sd.check_output_settings(device=None,channels=None,dtype=None,extra_settings=None,samplerate=None)

#sd.sleep() #  mseconds

# sd.get_portaudio_version()

# dither_off = False

# Linea para evitar el efecto Clipping
clip_off = False

# grabacion con optiones_extras 
myrec = sd.rec(int(duracion * fs), samplerate = fs, channels=2, dtype='float64', blocking=True)

# Linea para reproducir la grabacion 
sd.play(myrec)

# Linea para asegurarnos que la grabacion ha finalizado
sd.wait()  

               




