"""
Ejercicio: Bloque para hallar promedios
"""

import numpy as np
from gnuradio import gr


class blk(gr.basic_block):

    def __init__(self):  # only default arguments here
        gr.sync_block.__init__(
            self,
            name='Promedios de tiempos',   # will show up in GRC
            in_sig=[np.float32],
            out_sig=[np.float32,np.float32,np.float32,np.float32,np.float32]
            )
            
            # Se definen las entradas y salidas del bloque (GUI)
        
        # Básicamente acá se definen variables de operación para 
        # reinicializar
        
        self.acum_anterior = 0 
        self.Ntotales = 0
        self.acum_anterior1 = 0
        self.acum_anterior2 = 0

    def work(self, input_items, output_items):
    
    # Se definen las entradas y salidas funcionales
    
        x = input_items[0] # Señal de entrada
        y0 = output_items[0] # Promedio de la entrada
        y1 = output_items[1] # Media de la señal
        y2 = output_items[2] # RMS de la señal
        y3 = output_items[3] # Potencia promedio de la señal
        y4 = output_items[4] # Desviación estandar de la señal
        
        # Calculo del promedio
        N = len(x)
        self.Ntotales = self.Ntotales + N
        acumulado = self.acum_anterior + np.cumsum(x)
        self.acum_anterior = acumulado[N-1]
        y0[:] = acumulado/self.Ntotales
        
        # Calculo de la media cuadratica
       	x2 = np.multiply(x,x)
       	acumulado1 = self.acum_anterior1 + np.cumsum(x2)
       	self.acum_anterior1 = acumulado1[N-1]
       	y1[:] = acumulado1/self.Ntotales
       	
       	# Calculo de la RMS
       	y2[:] = np.sqrt(y1)
       	
       	# Calculo de la potencia promedio
       	y3[:] = np.multiply(y2,y2)
       	
       	# Calculo de la desviación estandar
       	x3 = np.multiply(x-y0,x-y0)
       	acumulado2 = self.acum_anterior2 + np.cumsum(x3)
       	self.acum_anterior2 = acumulado2[N-1]    	
       	y4[:] = np.sqrt(acumulado2/self.Ntotales) 
       	
       	return len(x)
      
