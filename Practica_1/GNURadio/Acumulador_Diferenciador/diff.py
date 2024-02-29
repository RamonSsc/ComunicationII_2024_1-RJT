"""
Embedded Python Blocks:

Each time this file is saved, GRC will instantiate the first class it finds
to get ports and parameters of your block. The arguments to __init__  will
be the parameters. All of them are required to have default values!
"""

import numpy as np
from gnuradio import gr

class blk (gr.sync_block):
	def __init__ (self): # only default arguments here
		gr.sync_block.__init__ (
			self,
			name ='e_Diff', # will show up in GRC
			in_sig =[np.float32],
			out_sig =[np.float32]			
			
		)
		self.acum_anterior = 0
	def work (self , input_items , output_items ):
		x = input_items[0] # Senial de entrada .
		y0 = output_items[0] # Senial acumulada diferencial
		
		# Perform differentiation logic
		y0[0] = x[0]
		for i in range(1,len(x)):
        		y0[i] = x[i] - y0[i - 1]
		return len(y0)
		
		#y0[:] = self.acum_anterior - np.cumsum(x)
		#self.acum_anterior = y0[-1]
		#y0[:] = diff
		#return len(y0)
