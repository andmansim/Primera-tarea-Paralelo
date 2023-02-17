import random
from time import sleep

url = ['a.com', 'b.com', 'c.com', 'd.com']

def urlss(urls):
    print('Empezando', urls)
    duracion = round(random.random(), 3)
    sleep(duracion)
    print('Terminado', urls, 'tiempo:', duracion, 'segundos')
    return urls, duracion


