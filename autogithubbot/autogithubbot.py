from redditreplier import Replier
from parser import parser
from replier import replier
import secret as s

def main():
	bot = Replier(
		parser,
		replier,
		s.user,
		s.password,
		'redditreplier',
		debug=True
	)
	print(bot.start())

if __name__ == '__main__':
	main()