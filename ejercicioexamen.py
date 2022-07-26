class points(object):

    def __init__(self,x,y):
        self.x=x
        self.y=y

    def print_point(self):
        print('x=',self.x,'y=',self.y)

p1=points(1,2)
#p1.print_point()

p2=points(1,2)
p2.x=2
p2.print_point()