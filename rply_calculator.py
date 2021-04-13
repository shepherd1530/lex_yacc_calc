from rply import LexerGenerator
from r_ply_parser import Parser

class Lexer(object):
	def __init__(self):
		self.lexer = LexerGenerator()
		self._init_tokens()

	def _init_tokens(self):
		self.lexer.add('PRINT', r'print')
		self.lexer.add('OPEN_PAREN', r'\(')
		self.lexer.add('CLOSE_PAREN', r'\)')
		self.lexer.add('PLUS', r'\+')
		self.lexer.add('MINUS', r'\-')
		self.lexer.add('EXPONENT', r'\*{2}')
		self.lexer.add('MULTIPLY', r'\*')
		self.lexer.add('DIVIDE', r'\/')
		self.lexer.add('FLOAT', r'\d+\.\d+')
		self.lexer.add('INT', r'\d+')
		self.lexer.add('ASSIGN', r'\=')
		self.lexer.add('NAME', r'[a-zA-Z_][a-zA-Z_0-9]*')

		self.lexer.ignore(r'\s+')

	def get_lexer(self):
		return self.lexer.build()




lexer = Lexer().get_lexer()

parser = Parser()
parser.parse()

parser = parser.get_parser()

out = lexer.lex("web = 11")
out2 = lexer.lex("web + 11")


# out = lexer.lex("2 + 2 ** 33 - 22.33")

# for token in out:
# 	print(token)

print(parser.parse(out).eval())
print(parser.parse(out2).eval())