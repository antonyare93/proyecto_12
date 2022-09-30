import time

hora = int(time.ctime()[11:13])
if hora >= 19:
    print('Hora de estar en casa')
else:
    print('Faltan', 19-hora, ' horas para ir a casa')