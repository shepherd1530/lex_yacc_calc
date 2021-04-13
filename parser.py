from rply import ParserGenerator
from ast import *


class Parser(object):
	"""docstring for Parser"""
	def __init__(self):
		self.pg = ParserGenerator(['INT', 'FLOAT', 'PLUS', 'MINUS',
			'MULTIPLY', 'DIVIDE', 'EXPONENT', 'OPEN_PAREN', 'CLOSE_PAREN',
			'ASSIGN', 'NAME'], precednce=[("left", ["MINUS", "PLUS"])], cache_id="parser")
		
	def parse(self):

		@self.pg.production('expression : INT')
		def number(p):
			return INT(p[0].value)


		@self.pg.production('expression : INT')
		def decimal(p):
			return FLOAT(p[0].value)

		@self.pg.production('program : expression')
		def program(p):
			return p[1]

		@self.pg.production('expression : expression PLUS expression')
		@self.pg.production('expression : expression MINUS expression')
		@self.pg.production('expression : expression MULTIPLY expression')
		@self.pg.production('expression : expression DIVIDE expression')
		@self.pg.production('expression : expression EXPONENT expression')
		def expression(p):
			left = p[0]
			operator = p[1]
			right = p[2]

			if operator.gettokentype() == 'PLUS':
				return PLUS(left, right)
			elif operator.gettokentype() == 'MINUS':
				return MINUS(left, right)
			elif operator.gettokentype() == 'MULTIPLY':
				return MULTIPLY(left, right)
			elif operator.gettokentype() == 'DIVIDE':
				return DIVIDE(left, right)
			elif operator.gettokentype() == 'EXPONENT':
				return EXPONENT(left, right)

		@self.pg.error
		def error_handler():
			pass

	def get_parser(self):
		return self.pg.build()