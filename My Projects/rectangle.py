class rectangle:
    def __init__(self,width,hight):
        self._width = width
        self._hight = hight

    @property
    def width(self):
        return f"{self._width:.1f}"
    
    @property    
    def hight(self):
        return f"{self._hight:.1f}"
    
    @width.setter
    def width(self,new_width):
        if new_width > 0:
            self._width = new_width
        else:
            print("the width big than 0")
        
    @hight.setter
    def hight(self,new_hight):
        if new_hight > 0:
            self._hight = new_hight
        else:
            print("hight is should be bigger than 0")
        
        

rec1 = rectangle(2,4)
rec1.width = 12
print(rec1.width)