
import sys



dict = {}



def edit_distance_mem(u : str, i : int, v : str, j : int) -> int:
   """
    Argumentos :
        u: str
        i: int
        v: str
        j: int
    Retorna:
        int - La distancia de Levenshtein entre los strings u[0:i] y v[0:j].
        Para el cálculo de esta distancia se usa programación dinámica y
        memorización a través de un diccionario
   """
   if not (i,j) in dict:
       if i == 0:
           dict[(i,j)] = j
       elif j == 0:
           dict[(i,j)] = i
       else:
           r = edit_distance_mem(u,i-1,v,j)
           s = edit_distance_mem(u,i,v,j-1)
           t = edit_distance_mem(u,i-1,v,j-1)
           if u[i-1] == v[j-1]:
               d = 0
           else:
               d = 1
           dict[(i,j)] = min(r+1, s+1, t+d)
   return dict[(i,j)]



def edit_distance(u : str, v : str) -> int:
   """
    Argumentos :
        u: str
        v: str
    Retorna:
        int - La distancia de Levenshtein entre los strings u y v. Para el 
        cálculo de esta distancia invoca a una función que usa programación 
        dinámica y memorización a través de un diccionario 
   """
   dict.clear()
   return edit_distance_mem(u, len(u), v, len(v))



def edit_distance_bottom_up(u : str, v : str) -> int:
   """
    Argumentos :
        u: str
        i: int
        v: str
        j: int
    Retorna:
        int - La distancia de Levenshtein entre los strings u y v.
        Para el cálculo de esta distancia se usa programacion dinámica y
        un enfoque de evaluación bottom-up que evita la recursión
   """
   dict.clear()
   n = len(u)
   m = len(v)
   for i in range(0, n+1):
       dict[(i,0)] = i
   for j in range(0, m+1):
       dict[(0,j)] = j
   for k in range(1, n+1):
       for i in range(k, n+1):
           if u[i-1] == v[k-1]:
               d = 0
           else:
               d = 1
           dict[(i,k)] = min(dict[(i-1,k)]+1, dict[(i,k-1)]+1, dict[(i-1,k-1)]+d) 
       for j in range(k, m+1):
           if u[k-1] == v[j-1]:
               d = 0
           else:
               d = 1
           dict[(k,j)] = min(dict[(k-1,j)]+1, dict[(k,j-1)]+1, dict[(k-1,j-1)]+d) 
   return dict[(n,m)]



if __name__ == "__main__":

    text1 = """These are my principles. If you don’t like them I have others.

Groucho Marx"""
    
    text2 = """An expert is a person who has made all the mistakes that can be made in a very narrow field.

Niels Bohr"""

    print(edit_distance(text1, text2))
    print(edit_distance_bottom_up(text1, text2))
    
    text1 = """LOS HERALDOS NEGROS
Hay golpes en la vida, tan fuertes... ¡Yo no sé!
Golpes como del odio de Dios; como si ante ellos,
la resaca de todo lo sufrido
se empozara en el alma. ¡Yo no sé!

Son pocos; pero son. Abren zanjas oscuras
en el rostro más fiero y en el lomo más fuerte.
Serán tal vez los potros de bárbaros atilas;
o los heraldos negros que nos manda la Muerte.

Son las caídas hondas de los Cristos del alma,
de alguna fe adorable que el Destino blasfema.
Estos golpes sangrientos son las crepitaciones
de algún pan que en la puerta del horno se nos quema.

Y el hombre. Pobre. ¡Pobre! Vuelve los ojos, como
cuando por sobre el hombro nos llama una palmada;
vuelve los ojos locos, y todo lo vivido
se empoza, como charco de culpa, en la mirada.

Hay golpes en la vida, tan fuertes. ¡Yo no sé!

César Vallejo"""

    text2 = """ES OLVIDO
Juro que no recuerdo ni su nombre,
Mas moriré llamándola María,
No por simple capricho de poeta:
Por su aspecto de plaza de provincia.
¡Tiempos aquellos!, yo un espantapájaros,
Ella una joven pálida y sombría.
Al volver una tarde del Liceo
Supe de la su muerte inmerecida,
Nueva que me causó tal desengaño
Que derramé una lágrima al oírla.
Una lágrima, sí, ¡quién lo creyera!
Y eso que soy persona de energía.
Si he de conceder crédito a lo dicho
Por la gente que trajo la noticia
Debo creer, sin vacilar un punto,
Que murió con mi nombre en las pupilas,
Hecho que me sorprende, porque nunca
Fue para mí otra cosa que una amiga.
Nunca tuve con ella más que simples
Relaciones de estricta cortesía,
Nada más que palabras y palabras
Y una que otra mención de golondrinas.
La conocí en mi pueblo (de mi pueblo
Sólo queda un puñado de cenizas),
Pero jamás vi en ella otro destino
Que el de una joven triste y pensativa.
Tanto fue así que hasta llegué a tratarla
Con el celeste nombre de María,
Circunstancia que prueba claramente
La exactitud central de mi doctrina.
Puede ser que una vez la haya besado,
¡Quién es el que no besa a sus amigas!
Pero tened presente que lo hice
Sin darme cuenta bien de lo que hacía.
No negaré, eso sí, que me gustaba
Su inmaterial y vaga compañía
Que era como el espíritu sereno
Que a las flores domésticas anima.
Yo no puedo ocultar de ningún modo
La importancia que tuvo su sonrisa
Ni desvirtuar el favorable influjo
Que hasta en las mismas piedras ejercía.
Agreguemos, aun, que de la noche
Fueron sus ojos fuente fidedigna.
Mas, a pesar de todo, es necesario
Que comprendan que yo no la quería
Sino con ese vago sentimiento
Con que a un pariente enfermo se designa.
Sin embargo sucede, sin embargo,
Lo que a esta fecha aún me maravilla,
Ese inaudito y singular ejemplo
De morir con mi nombre en las pupilas,
Ella, múltiple rosa inmaculada,
Ella que era una lámpara legítima.
Tiene razón, mucha razón, la gente
Que se pasa quejando noche y día
De que el mundo traidor en que vivimos
Vale menos que rueda detenida:
Mucho más honorable es una tumba,
Vale más una hoja enmohecida,
Nada es verdad, aquí nada perdura,
Ni el color del cristal con que se mira.
Hoy es un día azul de primavera,
Creo que moriré de poesía,
De esa famosa joven melancólica
No recuerdo ni el nombre que tenía.
Sólo sé que pasó por este mundo
Como una paloma fugitiva:
La olvidé sin quererlo, lentamente,
Como todas las cosas de la vida.

Nicanor Parra"""

    #Cambio en la profundidad de la recursión para poder ejecutar edit_distance
    sys.setrecursionlimit(3300)

    print(edit_distance(text1, text2))
    print(edit_distance_bottom_up(text1, text2))
