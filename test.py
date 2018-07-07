import PUSafe
import binascii

public_key_str = """-----BEGIN RSA PUBLIC KEY-----
MIGJAoGBAJ6m+aWR00650XWRNzAcy2ywCS5UAyPC4RVhlAP0BOtjegv5rHFgs/Wg
C+lHUCwQ6/vnS9uebcnlSCjldMQRqGLoCyHdvuN0USWBRsJkCsYXWNEuoiwZ3RUQ
EJuhGBjhy7bAN80SqTIUoPgMSfHCe1ymi3ppuskAOTfOR3KjhvlFAgMBAAE=
-----END RSA PUBLIC KEY-----"""

private_key_str = """-----BEGIN RSA PRIVATE KEY-----
MIICYQIBAAKBgQCepvmlkdNOudF1kTcwHMtssAkuVAMjwuEVYZQD9ATrY3oL+axx
YLP1oAvpR1AsEOv750vbnm3J5Ugo5XTEEahi6Ash3b7jdFElgUbCZArGF1jRLqIs
Gd0VEBCboRgY4cu2wDfNEqkyFKD4DEnxwntcpot6abrJADk3zkdyo4b5RQIDAQAB
AoGAHQciEEgxKGtZRrCOL3BlS/qdg2t9s5JZiobzBRIlwEfQMda51XjDFIL3CvSw
V4+1Db8RIxrGrbUU0d7Bsj2r9l31jCcZvf3ohqRklcWZ/OF7ndL1pHq1yOR3jqVY
JcVie7OZmAt6dqT7FqzbapdxoU5tMmILI9hQBhwhC+puXPUCRQCrD6APLQvgioTK
kkh3iaMBgH/sU2aRk50q7kQhS8XIs1G3tJihBxveXKkflllW/Nxr6EDKBDgmvzEr
SVeNOZGdXZ13lwI9AO1uAp+QopQ6nmsYCApCihnVCJ8hcvERokm9Wgcadfr/fW9d
HwDdCB/YKDwNHTObExhyERBeo1TMo0RRgwJEP5PxI3LUpUIWlMvFz1gCk75UzVs6
FgVNNvWTsORewHeVebfPupnPy9eYrDrPPbuBmUGbQvpKfGw3NCVwOvcYnep7akUC
PQCSb1sm1qmvCkhSfMvYqBlMvVtH6fVeQSX6nNI9t1A0sgbG/IP2oFw2Z7bI8r2j
6mzoktF7ayMJVf0MUckCRQCJPNzi+INd9rXghnDIpx49gMML719k8fkLlpwOD2Se
8PKB5W18W0u8ECrHS906JZFESKLqVYWqmM2jgBVTOp7XzdjWfA==
-----END RSA PRIVATE KEY-----"""


def main():
    fuzz_str = 'A' * 1024;
    msg = fuzz_str;

    myrsa = PUSafe.PURsa(public_key_str, private_key_str);

    encrypt_str = myrsa.encrypt(msg);
    print binascii.b2a_hex(encrypt_str);

    decrpyt_str = myrsa.decrypt(encrypt_str)
    print decrpyt_str;


main();
