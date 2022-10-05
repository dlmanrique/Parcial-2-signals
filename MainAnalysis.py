# -##################################
#             Imports
# -##################################

# from f_Functions import *
# from f_Graphics import *
# -##################################
#       Lectura de datos
# -##################################
#TODO: Realice la lectura de datos, utilice los nombres proporcionados y la ruta del archivo debe ser generalizada.

# str_FileName = # Nombre y dirección del archivo
# m_Data = np.double(st_File['-'])
# s_FsHz = np.double(st_File['-'])

#TODO: Verifique cómo se almacenan sus variables y, si es necesario, modifíquelas.

# -##################################
#                Filtrado
# -##################################
#TODO: Aplique el filtro de respuesta infinita y grafique su señal resultante junto a la original.

# v_Time =    # Vector de tiempo de la señal
# filt_FiltSOS = f_GetIIRFilter(s_FsHz, [Fq1, Fq2], [Fq1Rechazo, Fq2Rechazo])
# v_SigFilt = signal.sosfiltfilt(filt_FiltSOS, m_Data)
# PlotFilteredEEG(m_Data,v_SigFilt,v_Time)

# -##################################
#                RMS
# -##################################

#TODO: Aplique un filtro RMS a su señal, esta no debe modificar la frecuencia de muestreo de la misma.

# -##################################
# Detección y selección de picos
# -##################################

#TODO: Realice una dtección de picos a su señal resultante de RMS y luego seleccione los picos correspondientes a eventos HFO

# threshold = # Umbral de selección de picos
# chanel_peaks, _ = # Función que detecta picos por encima de umbral


# selected_peaks = [] # Picos seleccionados

#TODO: Busque en los articulos que condicion se debe cumplir para seleccionar un pico, luego recorra cada uno de sus picos y dtermine si este debe ser seleccionado.

# -##################################
#        Timepo frecuencia
# -##################################
#TODO: Realice un analisis de tiempo frecuencia solo a una ventana de Xs donde se haya detectado un HFO con una resolucion de 1Hz y 3 ciclos.

# -##################################
#           Visualización
# -##################################

#TODO: Grafique su señal original (Raw), Filtrada, Rms, FFT y Tiempo frecuencia Solo en la ventana de tiempo escogida.