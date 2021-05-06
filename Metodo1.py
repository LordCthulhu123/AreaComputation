from dataclasses import dataclass 

@dataclass
class Point:
    x: float 
    y: float

    def __add__(self, b):
        if type(b) == type(self):
            return Point(self.x + b.x, self.y + b.y)
        elif type(b) == float:
            return Point(self.x + b, self.y + b)
        else:
            try:
                self.__add__(float(b))
            except ValueError:
                raise ValueError("Non Implented")

    def __rmul__(self, b):
        if type(b) == float:
            return Point(b * self.x, b * self.y) 


class Grid:
    def __init__(self, x0, x1, y0, y1, num_div_x, num_div_y):
        return 

    def __getitem__(self, key):
        print(key)
        

coiso = Grid(0, 2, 0, 2, 100, 100)
coiso[1, 2]