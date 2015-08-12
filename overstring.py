class sstr(str):
    def __init__(self, string):
        super().__init__()
        self.string = string
        self.len = len(string)
    
    def __lshift__(self, count):
        count = count % self.len
        if count > 0:
            self._string = self.string[count:]
            self._string += self.string[:count]
            return sstr(self._string)
            
        return sstr(self.string)
        
    
    def __rshift__(self,count):
        count = count % self.len
        if count > 0:
            self._string = self.string[-count:]
            self._string += self.string[:(self.len-count)]
            return sstr(self._string)
            
        return sstr(self.string)
