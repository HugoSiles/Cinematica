
from vpython import *
BW = 0
if BW==0:
    fgcolor=color.black; bgcolor=color.white
else:
    fgcolor=color.white; bgcolor=color.black

#genera ventana de  objetos 
scene1 = canvas()
scene1.title="                                           DEFINICION DE VECTORES   Por Hugo Siles A."
scene1.width=920
scene1.height=480
scene1.range=(9)
scene1.foreground=fgcolor
scene1.center=vector(0,0.1,0)
scene1.background=(bgcolor) 
#; scene.lights = [vector(0,0.2,0) ]
scene1.ambient = vector(0.7,0.7,0) 
scene1.forward=vector(0.,0,-0.1)
scene1.autoscale = 0
scene1.align = 'left'
#scene.fov=1e-14  # pseudo-orthogonal
def objetos():
    global ventana1, ventana2, ventana3, ventana4
    lineaVert = curve(pos=[(-2.5,-8,0), (-2.5,8,0)],color = vector(0,0,0),radius=0.01)
    eje0_x = curve(pos=[(-1.5,-1,0),(11,-1,0)],radius=0.03, color = vector(0,0,0))
    pointerx = arrow(pos=vector(11,-1,0), axis=vector(0.5,0,0),color = vector(0,0,0),shaftwidth=.07,headwidth=0.14)
    eje0_y = curve(pos=[(2.5,-5,0), (2.5,6,0)],color = vector(0,0,0), radius=0.03)
    pointery = arrow(pos=vector(2.5,6,0), axis=vector(0,0.5,0),color = vector(0,0,0), shaftwidth=.07,headwidth=0.15)
    unitarioX = arrow(pos=vector(2.5,-1,0), axis=vector(1.5,0,0),shaftwidth=0.075,
                      headwidth=.17, color=color.red)
    unitarioY = arrow(pos=vector(2.5,-1,0), axis=vector(0,1.5,0),shaftwidth=0.075,
                      headwidth=.17, color=color.red)
    unitX = label(pos=vector(4.5,-1.6,0),color=color.blue,opacity=0.1,font='sans',
                  text=" vector unitario i ", height=13.5, box=False)
    unitario_i = label(pos=vector(7.,8.6,0),color=color.red,opacity=0.1,font='sans',
                text=" vector unitario i esta definido en la direccion X (horizontal)",
                    height=14, box=True)
    unitario_j = label(pos=vector(7.,7.5,0),color=color.red,opacity=0.1,font='sans',
                text=" vector unitario j esta definido en la direccion Y (vertical)",
                    height=14, box=True)
    unitY= label(pos=vector(4.5,-0.4,0),color=color.blue,font='sans',
                 text=" vector unitario j ",height=13.5, box=False)    
    coordX = label(pos=vector(10.8,-1.5,0),font='sans', text=" x ",height=16, box=False)
    coordY = label(pos=vector(2.,6.5,0), font='sans', text=" y ",height=16, box=False)

objetos()

def texto_vectores():
    
    Titulo= label(pos=vector(-9,8.4,0),color=color.blue,opacity=0.1,font='sans',
                height=19, box=False,text=" VECTORES " )
    Definicion = label(pos=vector(-14.5,7.8,0),color=color.red,opacity=0.1,font='sans',
                height=17, box=False,text=" Definicion: ")
    texto1 = label(pos=vector(-9.5,7.,0),color=color.blue,opacity=0.1, font='sans',
             height=14, box=False,text=" Segmento de recta orientado, referido a un sistema de\n\
    referencia,(Tiene una magnitud, direccion y sentido).\n\
    En fisica las cantidades fisicas que tienen magnitud,\n\
    direccion y sentido se representan por vectores ")
    Componentes = label(pos=vector(-12,4.,0),color=color.red,opacity=0.1,font='sans',
                    height=17, box=False,text="Representacion de vectores: ")
    texto2 = label(pos=vector(-10.,1.,0),color=color.blue,opacity=0.1,font='sans',
                   height=17, box=False,text=" A =     i +     j  =    i      j\n\
   B =     i +     j  =     i       j\n\
   C =     i +     j  =     i       j")
    texto3 = label(pos=vector(-9.5,3.2,0),color=color.blue,opacity=0.1,font='sans',
            height=14, box=False,text="Los vectores pueden representarse en terminos de sus\n\
componentes cartesianas, X e Y, cada componente es\n\
un multiplo del vector unitario respectivo.\n")
    textoA = label(pos=vector(-9.5,1,0),color=color.red,opacity=0.1,font='sans',
                   height=13, box=False,text="Ax        Ay         1    + 2")
    textoB = label(pos=vector(-9.4,0.2,0),color=color.red,opacity=0.1,font='sans',
                   height=13, box=False,text="Bx       By         - 2   +1.5")
    textoC = label(pos=vector(-9.5,-0.6,0),color=color.red,opacity=0.1,font='sans',
                   height=13, box=False,text="Cx       Cy          3     - 1")
    magnitud = label(pos=vector(-12.7,-1.4,0),color=color.red,opacity=0.1,font='sans',
                   height=17, box=False,text="Magnitud de un vector: ")
    textoM = label(pos=vector(-9.5,-2.4,0),color=color.blue,opacity=0.1,font='sans',
                   height=14.5, box=False,text="[A]    = ( Ax  + Ay  )   ")
    textoM1 = label(pos=vector(-8.9,-2.1,0),color=color.blue,opacity=0.1,font='sans',
                   height=11, box=False,text="2                2          2          ")
#ventana nueva
def nueva():                
    scene1.visible = False
    for obj in scene1.objects:
        obj.visible = False
    scene1.visible = True                
    objetos()    

def Vectores():
    scene1.visible = False
    for obj in scene1.objects:
        obj.visible = False
    scene1.visible = True
    objetos()
    A = arrow(pos=vector(7,0.5,0), axis=vector(1.5,3,0),shaftwidth=0.05,
              headwidth=.16, color=color.blue)
    vectorA = label(pos=vector(7.2, 2,0), opacity=0.1,font='serif', text=" A ",height=16, box=False)
    Ax = arrow(pos=vector(7.,0.45,0), axis=vector(1.5,0,0),shaftwidth=0.06,
               headwidth=.16, color=color.red)
    vectorAx = label(pos=vector(7.8,0.1,0), opacity=0.01,font='serif', text=" Ax ",height=13, box=False)
    Ay = arrow(pos=vector(8.5,0.5,0), axis=vector(0,3,0),shaftwidth=0.05,
               headwidth=.16, color=color.red)
    vectorAy = label(pos=vector(9,2,0), opacity=0.1,font='serif', text=" Ay ",height=13, box=False)
    B = arrow(pos=vector(1.7,0.8,0), axis=vector(-3,2.25,0),shaftwidth=0.06,
              headwidth=.2, color=color.blue)
    vectorB = label(pos=vector(0.6,2.3,0), opacity=0.1,font='serif',
                    text=" B ",height=17, box=False)
    Bx = arrow(pos=vector(1.7,0.8,0), axis=vector(-3,0,0),shaftwidth=0.06,
               headwidth=.2, color=color.red)
    vectorBx = label(pos=vector(0.5,0.4,0), opacity=0.1,font='serif', text=" Bx ",height=13, box=False)
    By = arrow(pos=vector(-1.26,0.8,0), axis=vector(0,2.25,0),shaftwidth=0.06,
               headwidth=.2, color=color.red)
    vectorBy = label(pos=vector(-1.5,1.8,0), opacity=0.1,font='serif', text=" By ",height=13, box=False)
    C =  arrow(pos=vector(4.5,-2.5,0), axis=vector(4.5,-1.5,0),shaftwidth=0.05,
               headwidth=.16, color=color.blue)
    vectorC = label(pos=vector(6.5,-3.7,0), opacity=0.1,font='serif', text=" C ",height=16, box=False)
    Cx = arrow(pos=vector(4.5,-2.5,0), axis=vector(4.5,0,0),shaftwidth=0.055,
               headwidth=.15, color=color.red)
    vectorCx = label(pos=vector(7.5,-2.1,0), opacity=0.01,font='serif', text=" Cx ",height=13, box=False)
    Cy = arrow(pos=vector(9,-2.5,0), axis=vector(0,-1.5,0),shaftwidth=0.04,
               headwidth=.16, color=color.red)
    vectorCy = label(pos=vector(9.5,-3.2,0), opacity=0.01,font='serif', text=" Cy ",height=13, box=False)
    texto_vectores()
def sumaVec():
    scene1.visible = False
    for obj in scene1.objects:
        obj.visible = False
    scene1.visible = True
    objetos()
    texto_vectores()
    sumaV()
    suma = label(pos=vector(-12.4,-3.2,0),color=color.red,opacity=0.1,font='sans',
                 height=17, box=False,text="Suma y resta de vectores: ")    
    textoS = label(pos=vector(-9.5,-4.2,0),color=color.blue,opacity=0.1,font='sans',
                height=16, box=False,text=" S = A + B = (   i +     j) + (     i +       j)\n\
    =  (    i +      j )")
    textoSN = label(pos=vector(-8.,-4.2,0),color=color.red,opacity=0.1,font='sans',
                    height=16, box=False,text="1      2         - 2      1.5")
    textoSN2 = label(pos=vector(-9.2,-4.9,0),color=color.red,opacity=0.1,font='sans',
                     height=16, box=False,text="  -1     3.5")
def TextoSumaVec():
    suma = label(pos=vector(-12.4,-3.2,0),color=color.red,opacity=0.1,font='sans',
                 height=17, box=False,text="Suma y resta de vectores: ")    
    textoS = label(pos=vector(-9.5,-4.2,0),color=color.blue,opacity=0.1,font='sans',
                height=16, box=False,text=" S = A + B = (   i +     j) + (     i +       j)\n\
    =  (    i +      j )")
    textoSN = label(pos=vector(-8,-4.2,0),color=color.red,opacity=0.1,font='sans',
                    height=16, box=False,text="1      2         - 2      1.5")
    textoSN2 = label(pos=vector(-9.2,-4.9,0),color=color.red,opacity=0.1,font='sans',
                     height=16, box=False,text="  -1     3.5")
    
def restaVec():
    scene1.visible = False
    for obj in scene1.objects:
        obj.visible = False
    scene1.visible = True
    objetos()
    texto_vectores()
    restaV()
    TextoSumaVec()
    textoR = label(pos=vector(-9.5,-6,0),color=color.blue,opacity=0.1,font='sans',
                   height=16, box=False,text=" D = C - A = (    i      j) - (    i +     j)\n\
          =  (    i      j)")
    textoRN = label(pos=vector(-8.1,-6.,0),color=color.red,opacity=0.1,font='sans',
                    height=16, box=False,text=" 3   - 1        1       2")
    textoSN2 = label(pos=vector(-8.9,-6.75,0),color=color.red,opacity=0.1,font='sans',
                    height=16, box=False,text="     2   - 3")    

def sumaV():
    A = arrow(pos=vector(8,0.3,0), axis=vector(1.5,3,0),shaftwidth=0.05,
              headwidth=.15,color=color.blue)
    vectorA = label(pos=vector(9.2,1.8,0), opacity=0.1,font='serif', text=" A ",
                    height=16, box=False)
    B = arrow(pos=vector(9.5,3.3,0), axis=vector(-3,2.25,0),shaftwidth=0.05,
              headwidth=.15, color=color.blue)
    vectorB = label(pos=vector(8.5,4.5,0), opacity=0.1,font='serif', text=" B ",
                height=16, box=False)
    S = arrow(pos=vector(8,0.3,0), axis=vector(-1.5,5.25,0),shaftwidth=0.05,
              headwidth=.14, color=color.red)
    vectorS = label(pos=vector(7.,2.4,0), opacity=0.1,font='serif', text=" S ",
                height=16, box=False)
    Sy = arrow(pos=vector(6.5,0.3,0), axis=vector(0,5.25,0),shaftwidth=0.05,
               headwidth=.15, color=color.green)
    Sx = arrow(pos=vector(8,0.3,0), axis=vector(-1.5,0,0),shaftwidth=0.06,
               headwidth=0.16, color=color.green)
    textoSx = label(pos=vector(7.4,-0.1,0), opacity=0.01,font='serif',
                text=" Sx ",height=15, box=False)
    textoSy = label(pos=vector(6,3.,0), opacity=0.01,font='serif',
                text=" Sy ",height=15, box=False)
def restaV():
    C =  arrow(pos=vector(5,4.8,0), axis=vector(4.5,-1.5,0),shaftwidth=0.05,
               headwidth=.15, color=color.blue)
    vectorC = label(pos=vector(7.5,4.5,0), opacity=0.1,font='serif', text=" C ",
                    height=16, box=False)
    A = arrow(pos=vector(9.5,3.3,0), axis=vector(-1.5,-3,0),shaftwidth=0.05,
              headwidth=.15, color=color.blue)
    vectorA = label(pos=vector(9.2,1.8 ,0), opacity=0.1,font='serif',
                text=" - A ",height=16, box=False)
    D = arrow(pos=vector(5.,4.8,0), axis=vector(3,-4.5,0),shaftwidth=0.05,
              headwidth=.15, color=color.red)
    vectorD = label(pos=vector(7.,2.5,0), opacity=0.1,font='serif',
                text=" D ",height=16, box=False)
    Dy = arrow(pos=vector(5.,4.8,0), axis=vector(0,-4.5,0),shaftwidth=0.05,
               headwidth=.15, color=color.green)
    Dx = arrow(pos=vector(5.,0.3,0), axis=vector(3,0.,0),shaftwidth=0.05,
               headwidth=.15, color=color.green)
    textoDx = label(pos=vector(7.5,-0.18,0), opacity=0.01,font='serif',
                    text=" Dx ",height=15, box=False)
    textoDy = label(pos=vector(4.5,2.2,0), opacity=0.01,font='serif',
                    text=" Dy ",height=15, box=False)

scene1.caption = '\n\n\n\n\n                    CONTROLES \n\n\n'
scene1.append_to_caption('     ')
button(text="Ventana Nueva",align='right', bind=nueva)
scene1.append_to_caption('        ')
button(text="Vectores",align='right', bind=Vectores)

scene1.append_to_caption('\n\n\n\n    ')
button(text="Suma_vectores",align='right', bind=sumaVec)
scene1.append_to_caption('    ')
button(text="Resta_vectores",align='right', bind=restaVec)



