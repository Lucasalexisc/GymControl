# Índices fijos para cada fila de la matriz
INDICE_NOMBRE_USUARIO ,INDICE_CONTRASENA =0 ,1
SOCIO_NOMBRE ,SOCIO_CODIGO ,SOCIO_EDAD ,SOCIO_TIPO ,SOCIO_TELEFONO =0 ,1 ,2 ,3 ,4
CLASE_CODIGO ,CLASE_NOMBRE ,CLASE_NIVEL ,CLASE_CUPOS =0 ,1 ,2 ,3
INSCRIPCION_CODIGO ,INSCRIPCION_CODIGO_SOCIO ,INSCRIPCION_CODIGO_CLASE ,INSCRIPCION_ASISTENCIAS ,INSCRIPCION_ESTADO =0 ,1 ,2 ,3 ,4

# Estructuras matriciales
usuarios_inicio_sesion =[
["admin","admin1234"],
["recepcion1","recep123"],
["recepcion2","recep456"],
["profeyoga","yoga2026"],
["profebox","boxeo2026"],
["profezumba","zumba2026"],
["coordinador","coord123"],
["ventas1","ventas123"],
["ventas2","ventas456"],
["consulta","consulta123"]
]

socios =[
["Juan Perez",101 ,28 ,1 ,"11-2587-8779"],
["Maria Juana",102 ,32 ,3 ,"11-3456-1028"],
["Rodriguez Pol",103 ,69 ,2 ,"11-4678-2193"],
["Tambussi Fer",104 ,18 ,1 ,"11-5789-3046"],
["Alejandro Esteban",105 ,65 ,2 ,"11-6890-4175"],
["Sofia Diaz",106 ,22 ,1 ,"11-7123-5684"],
["Camila Torres",107 ,45 ,1 ,"11-8234-6795"],
["Joaquin parros",108 ,37 ,1 ,"11-9345-7806"],
["Maria Anjoli",109 ,27 ,3 ,"11-1467-8920"],
["Mateo retil",110 ,22 ,3 ,"11-2578-9031"],
["Lucas Gomez",111 ,19 ,2 ,"11-3689-0142"],
["julio",112 ,32 ,3 ,"11-4790-1253"]
]

clases =[
[201 ,"Yoga",1 ,12 ],
[202 ,"Crossfit",3 ,10 ],
[203 ,"Boxeo",2 ,15 ],
[204 ,"Pilates",1 ,13 ],
[205 ,"Musculacion",2 ,8 ],
[206 ,"Spinning",2 ,12 ],
[207 ,"Funcional",3 ,14 ],
[208 ,"Zumba",1 ,20 ],
[209 ,"Natacion",2 ,16 ],
[210 ,"Stretching",1 ,18 ]
]

inscripciones =[
[301 ,101 ,205 ,8 ,1 ],
[302 ,102 ,204 ,3 ,1 ],
[303 ,103 ,201 ,10 ,2 ],
[304 ,104 ,201 ,2 ,1 ],
[305 ,105 ,201 ,7 ,1 ],
[306 ,106 ,203 ,10 ,2 ],
[307 ,107 ,203 ,10 ,2 ],
[308 ,108 ,203 ,10 ,2 ],
[309 ,109 ,205 ,8 ,1 ],
[310 ,110 ,204 ,5 ,1 ],
[311 ,111 ,201 ,9 ,1 ]
]

def obtener_nombre_nivel (codigo_nivel ):
    """
    Objetivo: obtener el nombre correspondiente a un código de nivel de clase.
    Parámetros: codigo_nivel, código numérico del nivel.
    Salida: nombre del nivel o "Desconocido" si el código no es válido.
    """
    if codigo_nivel ==1 :
        return "Principiante"
    elif codigo_nivel ==2 :
        return "Intermedio"
    elif codigo_nivel ==3 :
        return "Avanzado"
    else :
        return "Desconocido"

def obtener_nombre_tipo (codigo_tipo ):
    """
    Objetivo: obtener el nombre correspondiente a un código de tipo de socio.
    Parámetros: codigo_tipo, código numérico del tipo de socio.
    Salida: nombre del tipo o "Desconocido" si el código no es válido.
    """
    if codigo_tipo ==1 :
        return "Mensual"
    elif codigo_tipo ==2 :
        return "Libre"
    elif codigo_tipo ==3 :
        return "Premium"
    else :
        return "Desconocido"
