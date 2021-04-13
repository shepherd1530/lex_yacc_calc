from rply import ParserGenerator
from ast import *

ENV = {}


class Parser(object):
	"""docstring for Parser"""
	def __init__(self):
		self.pg = ParserGenerator(['EXPONENT', 'INT', 'FLOAT', 'PLUS', 'MINUS',
			'MULTIPLY', 'DIVIDE', 'OPEN_PAREN', 'CLOSE_PAREN',
			'ASSIGN', 'NAME'], precedence=[("left", ["PLUS", "MINUS"]),
			("left", ["MULTIPLY", "DIVIDE"]), ("left", ["ASSIGN"]), ("right", ["EXPONENT"])], cache_id="p_parser")
		
	def parse(self):

		@self.pg.production('program : assignment')
		@self.pg.production('program : expression')
		def program(p):
			return p[0]


		@self.pg.production('assignment : NAME ASSIGN expression')
		def assignment(p):
			global ENV

			left = p[0]
			right = p[2]
			return ASSIGN(left, right, ENV)

		@self.pg.production('expression : expression EXPONENT expression')
		@self.pg.production('expression : expression MULTIPLY expression')
		@self.pg.production('expression : expression DIVIDE expression')
		@self.pg.production('expression : expression PLUS expression')
		@self.pg.production('expression : expression MINUS expression')
		def expression(p):
			global ENV
			
			left = p[0]
			operator = p[1]
			right = p[2]

			if operator.gettokentype() == 'PLUS':
				left = left if isinstance(left, INT) else ENV[left.value]
				return PLUS(left, right)
			elif operator.gettokentype() == 'MINUS':
				return MINUS(left, right)
			elif operator.gettokentype() == 'MULTIPLY':
				return MULTIPLY(left, right)
			elif operator.gettokentype() == 'DIVIDE':
				return DIVIDE(left, right)
			elif operator.gettokentype() == 'EXPONENT':
				return EXPONENT(left, right)



		@self.pg.production('expression : NAME')
		def name(p):
			return NAME(p[0].value)


		@self.pg.production('expression : INT')
		def number(p):
			return INT(p[0].value)


		@self.pg.production('expression : FLOAT')
		def decimal(p):
			return FLOAT(p[0].value)


		@self.pg.error
		def error_handler(p):
			raise ValueError(p)

	def get_parser(self):
		return self.pg.build()