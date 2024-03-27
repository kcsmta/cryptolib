import random

class Khanh_simple_encryption():

    def __init__(self, modulus=7) -> None:
        self.modulus = modulus

    
    def KeyGen(self):
        self.sk = random.randint(0, (self.modulus))


    def Encrypt(self, message):    
        assert isinstance(message, int) and 0 < message < self.modulus

        return (message+self.sk)%self.modulus
    

    def Decrypt(self, ciphertext):
        assert isinstance(ciphertext, int) and 0 < ciphertext < self.modulus

        return (ciphertext - self.sk)%self.modulus

