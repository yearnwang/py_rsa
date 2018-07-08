import rsa
import base64

from Crypto.Cipher import AES
from Crypto import Random
import random



from hashlib import md5

BS = 16


def unicode_to_utf8(s):
    if isinstance(s, unicode):
        s = s.encode("utf-8")
    return s


def pad(s):
    length = len(s)
    add = BS - length % BS
    byte = chr(BS - length % BS)
    return s + (add * byte)


def unpad(s):
    length = len(s)
    byte = s[length - 1:]
    add = ord(byte)
    return s[:-add]


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


class PUAes(object):
    def __init__(self,_key,_mode = AES.MODE_CBC):

        hash_md5 = md5(_key.encode('utf8'));
        psw_key = hash_md5.hexdigest();

        self.key = psw_key;
        self.mode = _mode;
        self.iv = Random.new().read(AES.block_size);
        pass;

    def encrypt(self,plaintext):
        raw = unicode_to_utf8(plaintext)
        raw = pad(raw)
        cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
        return cipher.encrypt(raw)

        pass;

    def decrypt(self,ciphertext):
        cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
        return unpad(cipher.decrypt(ciphertext))

        pass;




