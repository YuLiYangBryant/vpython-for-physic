from visual import *
scene=display(width=1000,height=800,center=(5,5,5),background=(0.5,0.5,0))

balls = [sphere(pos=(i,j,0),radius=0.1, color=color.red) for i in range(10) for j in range(10)]
spring1 = [helix(pos=(i,j,0), radius = 0.08, thickness = 0.02, axis=vector(1,0,0)) for i in range(9) for j in range(10)]
spring2 = [helix(pos=(i,j,0), radius = 0.08, thickness = 0.02, axis=vector(0,1,0)) for i in range(10) for j in range(9)]
#arr = [arrow(shaftwidth = 0.05, color = color.blue, axis = vector(0,-1,0), pos = ( i, -0.5+(1)**(i), 0.)) for i in range(10) ]

for i in range(10):
    for j in range(10):
       if (i+j) % 2 ==0:
         arr=arrow(pos=(i,j),y=(j-0.35),axis=(0,1),shaftwidth=0.08,headwidth=0.15,color=color.blue,length=0.7)
       else:
         arr=arrow(pos=(i,j),y=(j+0.35),axis=(0,-1),shaftwidth=0.08,headwidth=0.15,color=color.blue,length=0.7)
