from nombres import *




if __name__ == "__main__":

    a = leer_frecuencias_nombres('data/frecuencias_nombres.csv')
    #print(a)
    b = filtrar_por_genero(a,'Hombre')
    #print(len(b))
    c = calcular_nombres(a,None)
    #print(c)
    d = calcular_top_nombres_de_año(a,2006,1,'Hombre')
    #print(d)
    e = calcular_nombres_ambos_generos(a)
    f = calcular_nombres_compuestos(a,'Hombre')
    g = calcular_frecuencia_media_nombre_años(a,'Alejandro',2003,2020)
    #print(g)
    h = calcular_nombre_mas_frecuente_año_genero(a,2002,'Mujer')
 
    i = calcular_año_mas_frecuencia_nombre(a,'Alejandro')
    
    j= calcular_año_frecuencia_por_nombre(a,'Hombre')
    k = calcular_nombres_mas_frecuentes(a,'Hombre',0)
    print(k)