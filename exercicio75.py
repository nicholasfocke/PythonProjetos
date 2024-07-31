def create_multiplier (multiplier):
    def multiply(number):
        return multiplier * number 
    return multiply

duplicate = create_multiplier(2)
triple = create_multiplier(3)
quadruple= create_multiplier(4)
 
print(duplicate(2))
print(triple(3))
print(quadruple(4))
 