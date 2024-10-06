from kivy.app import App
from kivy.uix.widget import Widget


# Quais são as funçoes para 'plotar' o objeto e renderizar o contexto? 
from kivy.graphics import Funcao1, Funcao2, Rotate 

from kivy.clock import Clock
from kivy.graphics.transformation import Matrix


class Objeto3D(Widget):
    def __init__(self, **kwargs):
        
        super(Objeto3D, self).__init__(**kwargs)    
        self.canvas = RenderContext()

        self.canvas.shader.source = 'shaders.glsl'
        
        # qual é a função criada dentro da classe Objeto3D para rotacionar o objeto?
        Clock.schedule_interval(self.XX,1/60)

        with self.canvas:
            self.desenhaObjeto()
    
    def desenhaObjeto(self):
        asp = self.width / self.height

        proj = Matrix().view_clip(-asp, asp, -1, 1, 1, 100, 1)
        
        self.canvas['projection_mat'] = proj
        
        vertices = [
                    # implemente tres pontos sendo que cada um possui 
                    # x,y,z, vetor normal, textura e cloração em rgb

                    Primeiro ponto,   0,0,-1,  0,0, Coloração,  
                    Segundo  ponto,   0,0,-1,  0,0, Coloração,  
                    Terceiro ponto,   0,0,-1,  0,0, Coloração
        ]

        vertex_format = [(b'v_pos',3,'float'),
                         (b'v_normal',3,'float'),
                         (b'v_tc0',2,'float'),
                         (b'color',3,'float')]
        
        self.rot = Rotate(angle=30,origin = (-1,1,-6,),axis=(0,1,1))      
       
        Mesh(vertices=vertices, 
             indices = [0,1,2], 
             fmt = vertex_format,
             mode='triangles')

    def rotate(self, *args):
        # Implemente um soma de qualquer valor ao angulo utilizado em Rotate
        

class Game3D(App):
    def build(self):
        return Objeto3D()
    
Game3D().run()
