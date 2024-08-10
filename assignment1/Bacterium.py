class Bacterium:
    # Complete the class

    def __init__(self, x, y, size, shape, figure, species, environment):
        self.x = x
        self.y = y
        self.size = size
        self.shape = shape
        self.figure = figure
        self.species = species
        self.environment = environment

# Create 3 instances
Bacilli = Bacterium(1, 2, 8,"rod","plasma","Dictyoglomota","soil"  )
Cocci = Bacterium(2, 3, 7, "sphere","capsule ","Deinococcota","underwater" )
Spirilli = Bacterium(3, 4, 6, "spiral","flagella","Deferribacterota","radioactive waste")
