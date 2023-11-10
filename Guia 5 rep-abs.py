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


    modulo PlantaImpl implementa Planta {
         var alarmas: Diccionario<Alarma, Conjunto<Sensor>>
         var Sensores: Diccionario<Sensor, Conjunto<Alarma>>
    }


# Se pide:
# a) Escribir formalmente y en castellano el invariante de representación
# b) Escribir la función de abstracción


# Todas las alarmas del conjunto<Alarma> de var sensores, tienen que existir como clave en el diccionario de Alarmas.
# Puede haber una alarma de var alarmas: que tiene por ejemplo <alarma1, s5> donde s5 no pertence a Sensores. y eso cumpliría la especificación
# Me estoy basando en los requiere de la especificación del TAD. No encuentro que en esa especificación
# diga algo que pida que si ((s1,a1) in Sensores => (a1,s1) in alarmas) . 


invRep(pi: PlantaImpl){
     forall a : Alarma :: (a in pi.Sensores[1] ==> a in pi.alarmas)
}


predAbs(){
     
}