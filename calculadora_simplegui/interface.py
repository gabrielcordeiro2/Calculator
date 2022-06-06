# Import Module
from PySimpleGUI import *

class Interface:
    
    def imagem_calculadora():
		
        #GUI Layout
        layout = [[Input(justification="left",default_text= '', size = (10, 3), font = ('Helvetica', 18), text_color = 'black', key = 'input'),ReadFormButton('«'),ReadFormButton('c')],
    		[],
    		[ReadFormButton('7'), ReadFormButton('8'), ReadFormButton('9'), ReadFormButton('/')],
    		[ReadFormButton('4'), ReadFormButton('5'), ReadFormButton('6'), ReadFormButton('*')],
    		[ReadFormButton('1'), ReadFormButton('2'), ReadFormButton('3'), ReadFormButton('-')],
    		[ReadFormButton('.'), ReadFormButton('0'), ReadFormButton('='), ReadFormButton('+')],
    		]
        return layout
    	
    
       

