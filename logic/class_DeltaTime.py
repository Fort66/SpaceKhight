

class DeltaTime:
    __delta_time = {'dt': 0.0}
    
    def __init__(self):
        self.__dict__ = self.__delta_time
        
    def __setattribute__(self, value):
        self.dt = value
        return self.dt


dt = DeltaTime()
dt = 250
print(dt.__dict__)