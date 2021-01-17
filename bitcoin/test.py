from ecc import PrivateKey, Signature
from helper import hash256, encode_base58, little_endian_to_int, int_to_little_endian
# e = int.from_bytes(hash256(b'my secret'), 'big')  # <1>
# z = int.from_bytes(hash256(b'my message'), 'big')  # <2>
# k = 1234567890  # <3>
# r = (k*G).x.num  # <4>
# k_inv = pow(k, N-2, N)
# s = (z+r*e) * k_inv % N  # <5>



#e = int.from_bytes(hash256(b'xxx'), 'big')  # <1>
#priv = PrivateKey(e)

#print(priv.point.address(compressed = True, testnet=True))


print(int_to_little_endian(1, 4).hex())