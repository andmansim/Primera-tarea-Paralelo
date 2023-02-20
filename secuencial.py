import random
from time import sleep

url = ['a.com', 'b.com', 'c.com', 'd.com'] #lista de urls

def urlss(urls): #Nos muestra cuando empieza y cuando ha terminado junto con el tiempo que ha tardado de la url. Retorna url y tiempo
    print('Empezando', urls)
    duracion = round(random.random(), 3)
    sleep(duracion)
    print('Terminado', urls, 'tiempo:', duracion, 'segundos')
    return urls, duracion

salida = []
for i in url: #LLamamos a la función con cada url y nos añade en la lista vacía la url con su tiempo
    resultado = urlss(i)
    salida.append(resultado)
