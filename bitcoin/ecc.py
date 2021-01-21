from unittest import TestCase
from helper import hash160, encode_base58_checksum
from script import Script

class FieldElement:

	def __init__(self, num, prime):

		if num >= prime or num<0:
			error = f"Num {num} not in field range 0 to {prime-1}"
			raise ValueError(error)

		self.num = num
		self.prime = prime


	def __repr__(self):
		
		return f'FieldElement_{self.prime}_({self.num})'


	def __eq__(self, other):
		
		if other is None: return False

		return self.prime == other.prime and self.num == other.num

	def __ne__(self, other):

		return not (self == other)

	def __add__(self, other):

		if self.prime != other.prime:
			error = f"Cannot add two numbers in different fields"
			raise TypeError(error)

		num = (self.num + other.num) % self.prime

		return self.__class__(num, self.prime)

	def __sub__(self, other):

		if self.prime != other.prime:
			error = f"Cannot sub two numbers in different fields"
			raise TypeError(error)

		num = (self.num - other.num) % self.prime
		return self.__class__(num, self.prime)

	def __mul__(self, other):

		if self.prime != other.prime:
			error = f"Cannot mul two numbers in different fields"
			raise TypeError(error)

		num = (self.num * other.num) % self.prime

		return self.__class__(num, self.prime)

	def __pow__(self, exponent):

		n = exponent % (self.prime - 1 )
		num = pow(self.num, n, self.prime)
		return self.__class__(num, self.prime)

	def __truediv__(self, other):

		if self.prime != other.prime:
			error = f"Cannot div two numbers in different fields"
			raise TypeError(error)

		num = (self.num * pow(other.num, self.prime-2, self.prime)) % self.prime

		return self.__class__(num, self.prime)

	def __rmul__(self, coefficient):
		num = (self.num * coefficient) % self.prime
		return self.__class__(num=num, prime=self.prime)


class Point():

	def __init__(self, x, y, a, b):

		self.x = x
		self.y = y
		self.a = a
		self.b = b

		if self.x is None and self.y is None:
			return

		if self.y **2 != self.x**3 + self.a*self.x + self.b:
			raise ValueError(f"({self.x}, {self.y}) is not on the curve")

	def __eq__(self, other):

		return self.x == other.x and self.y == other.y \
		  and self.a == other.a and self.b == other.b

	def __ne__(self, other):

		return not (self == other)

	def __repr__(self):

		if self.x is None:
			return 'Point(infinity)'
		elif isinstance(self.x, FieldElement):
			return 'Point({},{})_{}_{} FieldElement({})'.format(self.x.num, self.y.num, self.a.num, self.b.num, self.x.prime)
		else:
			return 'Point({},{})_{}_{}'.format(self.x, self.y, self.a, self.b)


	def __add__(self, other):

		if self.a != other.a or self.b != other.b:
			raise TypeError(f"Points {self}, {other} are not on the same curve")

		if self.x is None:
			return other
		if other.x is None:
			return self

		if self.x == other.x and self.y != other.y:
			return self.__class__(None, None, self.a, self.b)

		x1, y1, x2, y2 = self.x, self.y, other.x, other.y

		if self == other:
			slope = (3*(x1 ** 2) + self.a) / (2*y1)
			#s = (3 * self.x**2 + self.a) / (2 * self.y)
			x3 = (slope **2) - 2*x1
			y3 = slope*(x1 - x3) - y1

			return self.__class__(x3, y3, self.a, self.b)


		if self.x != other.x :

			slope = (y2 - y1) / (x2 - x1)
			x3 = (slope**2) - x1 - x2
			y3 = slope*(x1-x3) - y1
		
			return self.__class__(x3, y3, self.a, self.b)

		if self == other and self.y == 0 * self.x:
			return self.__class__(None, None, self.a, self.b)

	def __rmul__(self, coefficient):
		coef = coefficient
		current = self
		result = self.__class__(None, None, self.a, self.b)
		while coef:
			if coef & 1:
				result += current
			current += current
			coef >>= 1
		return result

P = 2**256 - 2**32 - 977

class S256Field(FieldElement):

	def __init__(self, num, prime=None):
		super().__init__(num = num, prime = P)

	def __repr__(self):
		return f'{x.zfill(64)}'

	def sqrt(self):
		return self**((P+1) // 4)

A = 0
B = 7
N = 0xfffffffffffffffffffffffffffffffebaaedce6af48a03bbfd25e8cd0364141

class S256Point(Point):

	def __init__(self, x, y, a=None, b=None):
		a, b = S256Field(A), S256Field(B)
		if type(x) == int:
			super().__init__(x = S256Field(x), y = S256Field(y), a = a, b = b)
		else:
			super().__init__(x = x, y = y, a = a, b = b)

	def __rmul__(self, coefficient):
		coef = coefficient % N
		return super().__rmul__(coef)

	def hash160(self, compressed = True):
		return hash160(self.sec(compressed = compressed))

	def address(self, compressed = True, testnet = False):
		'''returns the address string'''
		h160 = self.hash160(compressed = compressed)
		if testnet:
			prefix = b'\x6f'
		else:
			prefix = b'\x00'
		return encode_base58_checksum(prefix + h160)

	def verify(self, z, sig):
		s_inv = pow(sig.s, N -2, N)
		u = z * s_inv % N
		v = sig.r * s_inv % N
		total = u * G + v * self
		return total.x.num ==sig.r

	def sec(self, compressed = True):
		'''returns the binary version of the SEC format'''
		if compressed:
			if self.y.num % 2 ==0:
				return b'\x02' + self.x.num.to_bytes(32, 'big')
			else:
				return b'\x03' + self.x.num.to_bytes(32, 'big')
		else:
			return b'\x04' + self.x.num.to_bytes(32, 'big') + self.y.num.to_bytes(32, 'big')

	@classmethod
	def parse(self, sec_bin):
		'''returns a Point object from a SEC binary (not hex)'''
		if sec_bin[0] == 4:
			x = int.from_bytes(sec_bin[1:33], 'big')
			y = int.from_bytes(sec_bin[33:65], 'big')
			return S256Point(x=x, y=y)

		is_even = sec_bin[0] == 2

		x = S256Field(int.from_bytes(sec_bin[1:], 'big'))
		#right side of the equation y**2 = x**3 + 7
		alpha = x**3 + S256Field(B)
		#solve left side
		beta = alpha.sqrt()
		if beta.num % 2 == 0:
			even_beta = beta
			odd_beta = S256Field(P- beta.num)
		else:
			even_beta = S256Field(P- beta.num)
			odd_beta = beta
		if is_even:
			return S256Point(x, even_beta)
		else:
			return S256Point(x, odd_beta)




G = S256Point(0x79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798,0x483ada7726a3c4655da4fbfc0e1108a8fd17b448a68554199c47d08ffb10d4b8)

class Signature():

	def __init__(self, r, s):
		self.r = r
		self.s = s

	def __repr__(self):
		return f'Signature({self.r},{self.s})'

	def der(self):
		rbin = self.r.to_bytes(32, 'big')
		#remove all null bytes at the beginning
		rbin = rbin.lstrip(b'\x00')
		#if rbin has a high bit, add a x\00
		if rbin[0] & 0x80:
			rbin = b'\x00' + rbin
		result = bytes([2, len(rbin)]) + rbin

		sbin = self.s.to_bytes(32, 'big')
		#remove all null bytes at the beginning
		sbin = sbin.lstrip(b'\x00')
		#if sbin has a high bit, add a x\00
		if sbin[0] & 0x80:
			sbin = b'\x00' + sbin
		result += bytes([2, len(sbin)]) + sbin

		return bytes([0x30, len(result)]) + result


class PrivateKey():

	def __init__(self, secret):
		self.secret = secret
		self.point = secret * G

	def hex(self):
		return f'{self.secret.zfill(64)}'

	def sign(self, z):
		k = self.deterministic_k(z)
		r = (k*G).x.num
		k_inv = pow(k, N-2, N)
		s = (z + r*self.secret) * k_inv % N
		if s > N/2:
			s = N - s
		return Signature(r, s)

	def deterministic_k(self, z):
		k = b'\x00' * 32
		v = b'\x01' * 32
		if z > N:
			z -= N
		z_bytes = z.to_bytes(32, 'big')
		secret_bytes = self.secret.to_bytes(32, 'big')
		s256 = hashlib.sha256
		k = hmac.new(k, v + b'\x00' + secret_bytes + z_bytes, s256).digest()
		v = hmac.new(k, v, s256).digest()
		k = hmac.new(k, v + b'\x01' + secret_bytes + z_bytes, s256).digest()
		v = hmac.new(k, v, s256).digest()
		while True:
			v = hmac.new(k, v, s256).digest()
			candidate = int.from_bytes(v, 'big')
			if candidate >= 1 and candidate < N:
				return candidate  # <2>
			k = hmac.new(k, v + b'\x00', s256).digest()
			v = hmac.new(k, v, s256).digest()

	def wif(self, compressed = True, testnet = False):
		secret_bytes = self.secret.to_bytes(32, 'big')
		if testnet:
			prefix = b'\xef'
		else:
			prefix = b'\x80'

		if compressed:
			suffix = b'\x01'
		else:
			suffix = b''
		return encode_base58_checksum(prefix + secret_bytes + suffix)

class Tx:

	def __init__(self, version, tx_ins, tx_outs, locktime, testnet = False):

		self.version = version
		self.tx_ins = tx_ins
		self.tx_outs = tx_outs
		self.locktime = locktime
		self.testnet = testnet

	def __repr__(self):
		tx_ins = ''
		for tx_in in self.tx_ins:
			tx_ins += tx_in.__repr__() + '\n'
		tx_outs = ''
		for tx_out in self.tx_outs:
			tx_outs += tx_out.__repr__() + '\n'
		return f'tx: {self.id()}\nversion: {self.version}\ntx_ins:\n{tx_ins}tx_outs:\n{tx_outs}locktime: {self.locktime}'

	def id(self):
		'''Human-readable hexadecimal of the transaction hash'''
		return self.hash().hex()

	def hash(self):
		'''Binary hash of the legacy serialization'''
		return hash256(self.serialize())[::-1]

	@classmethod
	def parse(cls, s):
		serialized_version = s.read(4)
		version = int_to_little_endian(serialized_version, 4).hex()
		num_inputs = read_varint(s)
		inputs = []
		for _ in range(num_inputs):
			inputs.append(TxIn.parse(s))
		num_outputs = read_varint(s)
		outputs = []
		for _ in range(num_outputs):
			outputs.append(Txout.parse(s))
		locktime = int_to_little_endian(s.read(4))

		return cls(version, inputs, outputs, locktime, testnet=testnet)


class Txin:
	
	def __init__(self, prev_tx, prev_index, script_sig=None, sequence=0xffffffff):
		self.prev_tx = prev_tx
		self.prev_index = prev_index
		if script_sig is None:
			self.script_sig = Script()
		else:
			self.script_sig = script_sig
		self.sequence = sequence

	def __repr__(self):
		return f'{self.prev_tx.hex()}:{self.prev_index}'

	@classmethod
	def parse(cls, s):
		'''Takes a byte stream and parses the tx_input at the start.
		Returns a TxIn object.
		'''

		prev_tx = s.read(32)[::-1]
		prev_index = little_endian_to_int(s.read(4))
		script_sig = Script.parse(s)
		sequence = little_endian_to_int(s.read(4))
		return cls(prev_tx, prev_index, script_sig, sequence)	

class Txout:

	def __init__(self, amount, script_pubkey):
		self.amount = amount
		self.script_pubkey = script_pubkey

	def __repr__(self):
		return f"{self.amount}:{self.script_pubkey}"


	@classmethod
	def parse(cls, s):
		amount = little_endian_to_int(s.read(8))
		script_pubkey = Script.parse(s)
		return cls(amount, script_pubkey)
			
class ECCTest(TestCase):

	def test_on_curve(self):
		prime = 223
		a = FieldElement(0, prime)
		b = FieldElement(7, prime)
		valid_points = ((192,105),(17,56),(1,193))
		invalid_points = ((200,119),(42,99))

		for x_raw, y_raw in valid_points:
			x = FieldElement(x_raw, prime)
			y = FieldElement(y_raw, prime)
			Point(x, y, a, b)
		for x_raw, y_raw in invalid_points:
			x = FieldElement(x_raw, prime)
			y = FieldElement(y_raw, prime)
			with self.assertRaises(ValueError):
				Point(x, y, a, b)

	def test_add(self):

		prime = 223
		a = FieldElement(0, prime)
		b = FieldElement(7, prime)

		valid_points = ((170,142,60,139,220,181),(47,71,17,56,215,68),(143,98,76,66,47,71))

		for x_raw_1, y_raw_1, x_raw_2, y_raw_2, x_raw_3, y_raw_3 in valid_points:
			a = FieldElement(num=0, prime=prime)
			b = FieldElement(num=7, prime=prime)
			x1 = FieldElement(num=x_raw_1, prime=prime)
			y1 = FieldElement(num=y_raw_1, prime=prime)
			x2 = FieldElement(num=x_raw_2, prime=prime)
			y2 = FieldElement(num=y_raw_2, prime=prime)
			x3 = FieldElement(num=x_raw_3, prime=prime)
			y3 = FieldElement(num=y_raw_3, prime=prime)
			p1 = Point(x1, y1, a, b)
			p2 = Point(x2, y2, a, b)
			p3 = Point(x3, y3, a, b)
			p1 + p2 == p3