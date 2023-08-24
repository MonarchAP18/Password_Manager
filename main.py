from cryptography.fernet import Fernet


class PassManager:
    
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
                self.add_pass()
    

    def load_password_f(self,path):
        self.PassFile = path

        with open(path, 'r') as f:
            for line in f:
                site, encrypted = line.split(":")
                self.PassDict[site] = Fernet(self.key).decrypt(encrypted.encode())

    
    def add_pass(self, site, password):
        self.PassDict[site] = password

        if self.password is not None:
            with open(self.PassFile, 'a+') as f:
                encrypted = Fernet(self.key).encrypt(password.encode())
                f.write(site + ":" + encrypted.decode() + "\n")

