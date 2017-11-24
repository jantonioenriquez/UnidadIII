"""Name: Jose Antonio Enriquez Cabrera.
   Group: GITI9072."""
class House(object): #The class being visited
    def accept(self, visitor):
        """Interface to accept a visitor"""
        #Triggers the visiting operation!
        visitor.visit(self)

    def work_on_hvac(self, hvac_specialist):
        print(self, "worked on by", hvac_specialist) #Note that we now have a reference to the HVAC specialist object in the house object!

    def work_on_electricity(self, electrician):
        #Note that we now have a reference to the electrician object in the house object!
        print(self, "worked on by", electrician) #Note that we now have a reference to the electrician object in the house object!

    def __str__(self):
        """Simply return the class name when the House object is printed"""
        return self.__class__.__name__

class Visitor(object):
    """Abstract visitor"""
    def __str__(self):
        """Simply return the class name when the visitor object is printed"""
        return self.__class__.__name__

class HvacSpecialist(Visitor): #Inherits from the parent class, Visitor
    """Concrete visitor: HVAC specialist"""
    def visit(self, house):
        house.work_on_hvac(self) #Note that the visitor now has reference to the house object

class Electrician(Visitor): #Inherits from the parent class, visitor
    """Concrete visitor: electrician"""
    def visit(self, house):
        house.work_on_electricity(self)#Note that the visitor now has a reference to the house object


#Create an HVAC specialist
hv = HvacSpecialist()
#Create an electrician
e = Electrician()
#Create a house
home = House()
#Let's the house accept the HVAC specialist and work an the house by invoking the visit() method
home.accept(hv)

#Let's the house accept the electrician and work an the house by invoking the visit() method
home.accept(e)