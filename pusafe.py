import rsa
import base64

class PURsa(object):

    def __init__(self,_public_key_str,_private_key_str):
        self.private_key = rsa.PrivateKey.load_pkcs1(_private_key_str);
        self.public_key = rsa.PublicKey.load_pkcs1(_public_key_str);
        pass;

    def encrypt(self,buffer,length=100):
        res = []
        for i in range(0, len(buffer), length):
            res.append(rsa.encrypt(buffer[i:i + length],self.public_key))
        return "".join(res)
        pass;

    def decrypt(self,buffer,length=128):
        res = []
        for i in range(0, len(buffer), length):
            res.append(rsa.decrypt(buffer[i:i + length], self.private_key))
        return "".join(res)
        pass;

    def encrypt_file(self):
        pass;

    def decrypt_file(self):
        pass;





