import random
from multiprocessing import Pool #libreria para hacerlo paralelo
from time import sleep

url = ['a.com', 'b.com', 'c.com', 'd.com', 'e.com'] #añadimos uno

def urlss(urls): #Nos muesra cuando empieza y cuando a terminado junto con el tiempo tardado de la url. Retorna url y tiempo
    print('Empezando', urls)
    duracion = round(random.random(), 3)
    sleep(duracion)
    print('Terminado', urls, 'tiempo:', duracion, 'segundos')
    return urls, duracion

if __name__ == '__main__':
    pool = Pool(processes=4) #coge 4 procesos en paralelo 
    datos = pool.map(urlss, url) #alamacena aquí todo lo que nos devuelve la función
    pool.close() #cerramos los procedientos

    print()

    salida = []
    for i in datos: #printeamos todo
        print(i)

