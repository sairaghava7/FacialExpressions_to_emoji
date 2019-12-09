class pet:
    number_of_legs=0
    
    def sleep(self):
        print('bizz')
    
    def count_legs(self):
        print("I have %i legs"% self.number_of_legs)

class dog(pet):
    def sound(self):
        print('bow bow!!!')

labrador = pet()
labrador.number_of_legs=4
labrador.count_legs()


gm= dog()
gm.sound()
