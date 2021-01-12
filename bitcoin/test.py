from ecc import S256Point, G, N
from helper import hash256
e = int.from_bytes(hash256(b'my secret'), 'big')  # <1>
z = int.from_bytes(hash256(b'my message'), 'big')  # <2>
k = 1234567890  # <3>
r = (k*G).x.num  # <4>
k_inv = pow(k, N-2, N)
s = (z+r*e) * k_inv % N  # <5>
point = e*G  # <6>
print(point)
S256Point(028d003eab2e428d11983f3e97c3fa0addf3b42740df0d211795ffb3be2f6c52, \
0ae987b9ec6ea159c78cb2a937ed89096fb218d9e7594f02b547526d8cd309e2)
print(hex(z))
print(hex(r))
print(hex(s))
