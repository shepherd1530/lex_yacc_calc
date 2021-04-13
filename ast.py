
class INT:
	def __init__(self, value):
		self.value = value

	def eval(self):
		return int(self.value)

class NAME:
	def __init__(self, value):
		self.value = value

	def eval(self):
		return str(self.value)


class FLOAT:
	def __init__(self, value):
		self.value = value

	def eval(self):
		return float(self.value)


class BinaryOp:
	def __init__(self, left, right, ENV=None):
		self.left = left
		self.right = right
		self.ENV = ENV


class PLUS(BinaryOp):
	def eval(self):
		return self.left.eval() + self.right.eval()


class MINUS(BinaryOp):
	def eval(self):
		return self.left.eval() - self.right.eval()


class MULTIPLY(BinaryOp):
	def eval(self):
		return self.left.eval() * self.right.eval()


class DIVIDE(BinaryOp):
	def eval(self):
		return self.left.eval() / self.right.eval()


class EXPONENT(BinaryOp):
	def eval(self):
		return self.left.eval() ** self.right.eval()

class ASSIGN(BinaryOp):
	def eval(self):
		val = self.right
		self.ENV[self.left.value] = val
		return val
