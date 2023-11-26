-------------------------------------------------------------------------------------------------------------


#Ejercicio 4 - Planta industrial:
 # Considere la siguiente  especificación de una relación uno/muchos entre alarmas y sensores de una planta industrial 
 # Un sensor puede estar asociado a muchas alarmas, y una alarma puede tener muchos sensores asociados




 TAD Planta{
    obs alarmas: conj<Alarma>                 # ejemplo {alarma1,alarma2,alarma3,..}
    obs sensores: conj<tupla<Sensor,Alarma>>  # ejemplo {(sensor1, alarma1),(sensor2,alarma2)}

    proc nuevaPlanta(): Planta          # Constructor
        asegura res.alarmas == {}       # Ambos observadores deben ser seteados en cada proc
        asegura res.sensores == {}     

    proc agregarAlarma(input p: Planta, in a: Alarma)   # Recibe una planta y agrega una alarma al conjunto de alarmas
        requiere !(a in p.alarmas)                      # Requiere que esa alarma no esté previamente en las alarmas de la planta
        asegura p.alarmas == old(p).alarmas + {a}  
        asegura p.sensores == old(p).sensores


    proc agregarSensor(inout p:Planta, in a: Alarma, in s:Sensor)
        requiere a in p.alarmas                         # Requiere que la alarma esté en el conjunto de alarmas de la planta
        requiere !(<s,a> in p.sensores)
        asegura p.alarmas == old(p).alarmas            
        asegura p.sensores == old(p.sensores) + {<s,a>} # agrego una tupla a los sensores

 } # Ojo porque segun este TAD, para agregar un sensor si o si tiene que haber una alarma, pero para agregar una alarma no es necesario que haya un sensor






# Se decidió usar la siguiente estructura como representación, que permite consultar fácilmente tanto
# en una dirección (sensores de una alarma) como en la contraria (alarmas de un sensor).







# Se pide:
# a) Escribir formalmente y en castellano el invariante de representación
# b) Escribir la función de abstracción


# 1) Todas las alarmas del conjunto<Alarma> de var sensores, tienen que existir como clave en el diccionario de Alarmas
# 2) Para todo sensor de var Sensores, su Conjunto<Alarma> no tiene que ser conjunto vacío
# 3)todos los elementos del Conjunto<Sensor> de alarmas, tienen que existir en las claves de Sensores
# 4) Para cada alarma del var alarmas, que tiene un sensor en el conjunto sensores, luego ese sensor va a estar como clave en 
# var Sensores, y esa alarma va a pertenecer al Conjunto<Alarma> del valor     

# 5) Para cada sensor del var sensores, que tiene una alarma en el conjunto alarmas, luego esa alarma
# va a estar como clave en var Alarmas, y ese sensor va a pertenecer al Conjunto<Sensor> del valor

(En la estructura Inv y Rep , es correcto poner algunos mas, en el tad no). El tad no tiene que ser redundante y ser minimal

 modulo PlantaImpl implementa Planta {
         var alarmas: Diccionario<Alarma, Conjunto<Sensor>>
         var Sensores: Diccionario<Sensor, Conjunto<Alarma>>
    } 

invRep(pi: PlantaImpl){
     1) forall s: Sensor :: (s in pi.Sensores =>L (forall a: Alarma :: (a in pi.Sensores[s] =>L a in pi.Alarma) )   # Se podria borrar porque el 4 y 5 lo cubren
     2) forall s: Sensor :: (s in pi.Sensores =>L |pi.Sensores[s]| > 0 ) # (alarmas si puede estar vacío )
     3) forall a: Alarma :: (a in pi.Alarmas =>L (forall s: Sensor :: ( s in pi.Alarmas[a] =>L s in pi.Sensores) )  # Se podria borrar porque el 4 y 5 lo cubren
     4) forall a: Alarma :: (a in pi.Alarmas =>L (forall s: Sensor :: ( s in pi.Alarmas[a] =>L s in pi.Sensores && a in pi.Sensores[s] ) ) )
     5) forall s: Sensor :: (s in pi.Sensores =>L (forall a: Alarma :: ( a in pi.Sensores[s] =>L a in pi.Alarmas && s in pi.Alarmas[a] ) ) )
}




predAbs(pi: PlantaImpl, p: Planta){         # Recibe el módulo y el TAD . Tiene que conectar las estructuras del módulo con los obs del TAD
     p.alarmas == pi.alarmas  # Los conjuntos deben ser iguales (doble inclusión)
 &&  forall t : tupla<Sensor,Alarma> :: (t in p.sensores =>L t[0] in pi.Sensores && t[1] in pi.alarmas && t[1] in pi.Sensores[t[0]] )
 &&  forall s : Sensor :: (s in pi.sensores =>L (forall a: Alarma :: (a in pi.Sensores[s] =>L <s,a> in p.sensores ) ) )

}
-------------------------------------------------------------------------------------------------------------
Ejercicio 5 Planilla de actividades (Está la resolución en pdf en clase de rep y abs)

Un consultor independiente desea mantener una planilla con las actividades que realiza cada mes
en cada uno de los proyectos en los que participa. 
La planilla que desea mantener se describe con el siguiente TAD.

TAD Planilla { 
 obs actividades: conj<Actividad> 
 obs proyectoDe: dict<Actividad, Proyecto> 
 obs mesDe: dict<Actividad, int> 
 obs horaDe: dict<Actividad, int>

proc nuevaPlanilla(): Planilla
proc totProyxMes(in p: Planilla, in m: Mes, in r: Proyecto): int
proc agregar( inout p: Planilla, in a: Actividad, in r: Proyecto, in mes: int, in horas: int )
}
Actividad es string Proyecto es string

Se propone la siguiente estructura para representar dicho TAD

modulo PlanillaImpl implementa Planilla { 
 var detalle: Diccionario<  
                          Actividad, struct<proy: Proyecto, mes: int, horas: int>   -- Ejemplo: { "Actividad1" : <proyecto="Proy1", mes = 12, horas = 15>,
                          >                                                                       "Actividad2" : <proyecto="Proy1", mes = 08, horas = 09> }
var horasPorMes: Diccionario<proyecto, Array<int>>                                  -- Ejemplo: { "Proy2":[3,5,7,9,12,07,09,11,09,11,7,15],  # La posicion i del array, representa la suma de horas de todas las actividades de ese proyecto dentro del mismo mes
                                                                                                  "Proy1":[3,5,7,9,12,07,09,11,09,11,7,15], }                    
}

Se pide:
a) Escribir formalmente y en castellano el invariante de representacion.
b) Escribir la funcion de abstraccion.


Invariante de representación:

El numero de mes de cada actividad tiene que ser un entero entre 1 y 12 (Mejor entre 0 y 11 para que coincida con los indices del array de horasPorMes
La longitud de los array de horasPorMes debe ser 12 (Un indice para cada mes)
Todos los proyectos de detalle.proyecto tienen que estar dentro de horasPormes y viceversa
horasPormes[proyecto][i] tiene que ser igual a la suma de todas las detalle[proyecto].horas donde detalle[proyecto].mes = i

invRep(p : PlanillaImpl){
forall a : Actividad :: ( a in p.detalle =>L (0<= p.detalle[a].mes < 12))      &&

forall pro: Proyecto :: ( pro in p.horasPorMes =>L p.horasPorMes[pro].length == 12

forall pro: Proyecto, m: int :: (pro in p.horasPorMes =>L p.horasPorMes[pro][m] 

forall a: Actividad :: ( a in p.detalle =>L p.detalle[a].proyecto in p.horasPorMes )  &&
forall pro: Proyecto :: ( pro in p.horasPorMes =>L ( exists a: Actividad :: p.detalle[a].Proyecto == pro ) ) &&


forall pro: Proyecto, m:int, a: Actividad :: (pro in p.horasPorMes =>L ( p.horasPorMes[pro] ==          # Ver si está correcto que m:int y a:Actividad esten ahi
                                                    sum (if a in p.detalle &&L p.detalle[a].proy== pro && p.detalle[a].mes == m 
                                                         then p.detalle[a].horas
                                                         else 0 fi ))

}

Predicado de abstracción:
Establece la equivalencia entre un TAD y su implementación

predAbs(pi: PlanillaImpl, p: Planilla){
    forall a: Actividad :: (
    a in pi.detalle <==> a in p.actividades        &&L
    pi.detalle[a].proy == p.proyectoDe[a]          &&
    pi.detalle[a].mes == p.mesDe[a]                &&
    pi.detalle[a].horas == p.horaDe[a]
     
}



Actividad es string Proyecto es string




-------------------------------------------------------------------------------------------------------------
Ejercicio 6 Alta fiesta



TAD AltaFiesta {
obs invitados: conj<Persona>
obs pendientes: conj<Persona>
obs grupoDe: dict<Persona, Grupo>
obs regaloDe: dict<Persona, Regalo>
proc iniciarFiesta(in personas: Conjunto<Persona>): AltaFiesta

proc lleganInvitados(
inout a: AltaFiesta,
in c: Conjunto<Persona>,
in g: Grupo,
in r: Regalo
)
}



modulo AltaFiestaImpl implementa AltaFiesta {
var invitados: Conjunto<Persona>
var presentes: Conjunto<Persona>
var grupoDe: Diccionario<Grupo, Conjunto<Persona>>
var regaloDeGrupo: Diccionario<Grupo, Regalo>
}
Persona es string
Grupo es string
Regalo es string


# Invariante de representación

# Invitados y presentes no parecen tener una restricción por si mismos (tendrán con el resto)
# 1) todo Grupo que esté en la fiesta, tiene por lo menos una persona
# 2) no puede haber una persona que pertenezca a 2 o mas grupos distintos

# Ahora interconectamos las estructuras

# 3) todas las personas presentes tienen que pertenecer al conjunto invitados
# 4) todas las personas de cada grupo tienen que pertenecer al conjunto presentes
# 5) los grupos que trajeron regalos deben ser los mismos grupos que existen en grupoDe


invRep(afi : AltaFiestaImpl){
   1) forall g: grupo :: (g in afi.grupoDe =>L |afi.grupoDe[g]| > 0 ) 
   2) forall g,h: grupo :: (g in afi.grupoDe && h in afi.grupoDe && g!=h =>L afi.grupoDe[g] * afi.grupoDe[h] = {} ) 
   3) forall p: persona :: (p in afi.presentes =>L p in afi.invitados) 
   4) forall g: grupo :: (g in afi.grupoDe =>L (forall  p: Persona :: (p in afi.grupoDe[g] =>L p in presentes) )
   5) afi.grupoDe == afi.regaloDeGrupo   #Igualdad de conjuntos de claves

}

TAD AltaFiesta {
obs invitados: conj<Persona>
obs pendientes: conj<Persona>
obs grupoDe: dict<Persona, Grupo>
obs regaloDe: dict<Persona, Regalo>


predAbs( afi: AltaFiestaImpl, af: AltaFiesta){
 afi.invitados == af.invitados
 
 forall p: Persona :: ( p in af.pendientes <=> p in af.invitados && !(p in afi.presentes) # podria ser af.pendientes = af.invitados - afi.presentes
 
 forall p: Persona :: ( p in af.grupoDe =>L af.grupoDe[p] in afi.grupoDe && p in afi.grupoDe[af.grupoDe[p]] )
 forall g: Grupo :: ( g in afi.grupoDe =>L (forall p: Persona :: (p in afi.grupoDe[g] =>L p in af.grupoDe && af.grupoDe[p] == g )
  
 forall p: Persona :: ( p in af.regaloDe =>L (exists g: Grupo :: (g in afi.grupoDe && p in afi.grupoDe[g] &&L afi.regaloDeGrupo[g] == af.regaloDe[p]
 forall g: Grupo :: (g in afi.regaloDeGrupo =>L forall p: Persona :: ( p in afi.grupoDe[g] =>L p in af.regaloDe && af.regaloDe[p] == afi.regaloDeGrupo[p]

}


-------------------------------------------------------------------------------------------------------------












