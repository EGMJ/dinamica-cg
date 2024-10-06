---VERTEX SHADER-------------------------------------------------------

// desenhar o objeto e possibilitar a rotação
uniform mat4 projection_mat;
uniform mat4 modelview_mat;

// atributo de posição de cada vertice
attribute vec3  v_pos;


// atributo de cor de cada vertice 
attribute vec3 color;

// variaçao de cores entre os vertices
// implemente a variaçao de cor como vec3


void main(void){
    gl_Position = projection_mat * modelview_mat * vec4(v_pos,1.0);    

// implemente o atributo cor a variaçao

}

---FRAGMENT SHADER-----------------------------------------------------

// implemente a variaçao de cor como vec3 (a mesma que a anterior)

void main (void){

// estamos atribuindo a variaçao de cor ao gl_FragColor como vec4, apenas complete

    gl_FragColor = vec4(xxx,1);
}
