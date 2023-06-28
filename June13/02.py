class Calculator:
    color = " "
    model = " "
    weight = 0
    volume = 0
    bottom = True or False
    charge = 0
        
    def __init__(self, color, model, weight):
        self.color = color
        self.model = model
        self.weight = weight
        
    def __repr__(self) -> str:
        msg = "Earphone color: %s, model: %s, weight: %d gramm." % (self.color, self.model, self.weight)
        return msg 