from calendar import c
import PySimpleGUI as sg

# Layout
sg.theme("DarkGrey3")
layout = [
    [sg.Input("here's the panel",key="panel", size=(23,2)), sg.Button("c", size=(3,1))],
    [sg.Button("m+",key="memory+", size=(3,1)), sg.Button("m-",key="memory-", size=(3,1)), sg.Button("m=",key="memory=", size=(3,1)), sg.Button("x",key="multiply", size=(3,1))],
    [sg.Button("7",key="seven", size=(3,2)), sg.Button("8",key="eight", size=(3,2)), sg.Button("9",key="nine", size=(3,2)), sg.Button("÷",key="divide", size=(3,2))],
    [sg.Button("4",key="four", size=(3,2)), sg.Button("5",key="five", size=(3,2)), sg.Button("6",key="six", size=(3,2)), sg.Button("-",key="minus", size=(3,2))],
    [sg.Button("1",key="one", size=(3,2)), sg.Button("2",key="two", size=(3,2)), sg.Button("3",key="three", size=(3,2)), sg.Button("+",key="add", size=(3,2))],
    [sg.Button("0",key="zero", size=(3,2)), sg.Button(".",key="point", size=(3,2)), sg.Button("=",key="equal", size=(12,2))]
    ]
# Janela
window = sg.Window("Calculator", element_justification="c", resizable=True, margins=(0,0), layout=layout, return_keyboard_events=False)

while True:
    events, values = window.read(timeout=1)    
    if events == sg.WINDOW_CLOSED:
        break











































# import operator

# class Calculator:

        
#     def __init__(self):
#         self.equation = [10,"+",5,"*",2,"-",6,"/",3,"*",5]
#         self.equation2 = []
#         self.memory1 = None
#         self.memory2 = None
#         self.result = []


        
#     def calculate(self):
#         str_operadores = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}
#         operators = ["*", "/", "+", "-"]
#         n = 0
#         nlimit = len(self.equation)

#         while n != nlimit:
#             for item in self.equation:
#                 if item in str_operadores:
#                     print(str_operadores["+"])
#                     item.replace(item, str_operadores[item])
#                     print(item)







#         # while n != nlimit:
#         #     for i in self.equation:
#         #         if i == "*":
#         #             # adiciona a conta no equation2:
#         #             self.equation2.append(self.equation[n-1:n+2])
#         #             #
#         #             conta = self.equation2[0][0:3]
#         #             # executar o calculo da equation2
#         #             calculo = str_operadores[i](self.equation2[0][0], self.equation2[0][2])
#         #             # mover o resultado pra memory2
#         #             self.memory2 = calculo
#         #             # executa o próximo calculo na ordem de prioridade:

#         #             # junta tudo e exibe em result


#                 n += 1

#         print(self.equation)
#         # print(n)
#         # print(self.equation2)
#         # print(conta)













#         # for i in self.equation:
#         #     a = str_operadores[self.symbol](x, y)
#         #     print(a)
        
        
# # a = str_operadores[self.symbol](self.memory1, self.memory2)  
        
        
        
    
# calculadora = Calculator()
# calculadora.calculate()

# var = calculadora.calculate()


    
# input -> "100 / 100 - 100 + 100"    
        
