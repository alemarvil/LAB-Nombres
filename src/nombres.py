from typing import List
from collections import namedtuple,defaultdict
import csv

FrecuenciaNombre = namedtuple('FrecuenciaNombre', 'año,nombre,frecuencia,genero')

def leer_frecuencias_nombres (ruta:str)-> list[FrecuenciaNombre]:
    nombres = []
    with open (ruta,encoding = 'utf-8') as f:
        lector = csv.reader(f)
        next(f)
        for linea in lector:
            año = int(linea[0].strip())
            nombre = linea[1].strip()
            frecuencia = int(linea[2].strip())
            genero = linea[3].strip()

            registro = FrecuenciaNombre(año,nombre,frecuencia,genero)
            nombres.append(registro)

        return nombres


def filtrar_por_genero (nombres:List[FrecuenciaNombre],g:str)->List[FrecuenciaNombre]:
    res = []
    if g != 'Hombre' and g != 'Mujer':
        print("El genero introducido no es correcto.")
    else:
         for c in nombres:
                if g == c[3]:
                    res.append(c)
    return res
        
def calcular_nombres(nombres:List[FrecuenciaNombre],g:str)->set:
    res = set()
    for n in nombres:
        if n.genero == g or g == None:
            res.add(n.nombre)
    return res

def calcular_top_nombres_de_año(nombres:List[FrecuenciaNombre],año:int,limite:int = 10 ,g:str|None = None)->List[tuple[str,int]]:
    f = [c for c in nombres if c.año == año and (c.genero == g or g == None)]
  
    tuplas = [(n.nombre,n.frecuencia) for n in f]

    return sorted(tuplas, key = lambda c:c[1] , reverse = True)[:limite]

def calcular_nombres_ambos_generos(nombres:List[FrecuenciaNombre])-> set[str]:
    mujer = {c.nombre for c in nombres if c.genero == 'Mujer'}
    hombre = {c.nombre for c in nombres if c.genero == 'Hombre'}
    res = mujer & hombre
    return res


def calcular_nombres_compuestos (nombres:List[FrecuenciaNombre],g:str)->set[str]:
    return {c.nombre for c in nombres if ' ' in c.nombre and (g == c.genero or g == None)}

def calcular_frecuencia_media_nombre_años(nombres: List[FrecuenciaNombre],nombre: str,añoi: int,añof: int) -> float:
    nombre = nombre.upper()
    f = [c.frecuencia for c in nombres if c.nombre == nombre and añoi <= c.año < añof]
    if len(f) == 0:
        return 0.0
    else:
        return sum(f) / len(f)


def calcular_nombre_mas_frecuente_año_genero(nombres: List[FrecuenciaNombre],año:int,g: str):
    f = [n for n in nombres if n.año == año and n.genero == g]
    o = sorted(f, key=lambda n:n.frecuencia, reverse =True)
    return o[0].nombre


def calcular_año_mas_frecuencia_nombre(nombres: List[FrecuenciaNombre],nombre: str)->int:
    nombreBuscado = nombre.strip().upper()
    f = [n for n in nombres if n.nombre.strip().upper() == nombreBuscado] # para que escriba el nombre como lo escriba , no de error de que no encuentra
    o = max(f, key = lambda x:x.frecuencia )
    return o.año

def calcular_año_frecuencia_por_nombre(nombres: List[FrecuenciaNombre],g: str)->{str,(int,int)}:
    f = {n.nombre:(n.año,n.frecuencia) for n in nombres if n.genero == g}
    return f

def calcular_nombres_mas_frecuentes(nombres: List[FrecuenciaNombre],g: str,dec: int,n : int = 5)->List[str]:
   añoP= 2000 + dec
   f = defaultdict(int)
   for a in nombres:
        if a.genero == g and añoP <= a.año < añoP + 10:
            f[a.nombre] += a.frecuencia
   o = sorted(f.items(),key=lambda x:x[1] , reverse=True)[:n]
   l = [b[0] for b in o]
   return l




    


        

        
            
        