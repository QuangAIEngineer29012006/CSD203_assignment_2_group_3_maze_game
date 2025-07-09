class Entity:
    def __init__(self,x , y ):
        self.pos_x = x
        self.pos_y = y


    def move(self,dx ,dy):
        self.pos_x += dx
        self.pos_y += dy
        
class Player(Entity):
    def __init__(self, x, y):
        super().__init__(x, y)

class Ghost(Entity):
    def __init__(self, x, y):
        super().__init__(x, y)



        
