class soemthing:
    name = ''
    # def __init__(self, name) :
    #     self.name = name
    # def __str__(self):
    #     return self.name
    @property
    def pro(self):
        return "here"

b = soemthing()
print(b)
print(b.pro)
