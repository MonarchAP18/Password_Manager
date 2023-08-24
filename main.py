from cryptography.fernet import Fernet


class Manager:
    
    def __init__(self):
        self.key = None
        self.PassFile = None
        self.PassDict = {}
    

    def Create(self, path):
        self.key = Fernet.generate_key()
        with open(path, 'wb') as f:
            f.write(self.key)

    def Loader(self,path):
        with open(path, 'rb') as f:
            self.key = f.read()
    
    def Create_File(self, path, initial_values = None):
        self.PassFile = path
        
        if initial_values is not None:
            for key, values in initial_values.items():
                pass 