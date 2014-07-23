from redditreplier import Replier
from parser import Parser
import secret as s
import warnings

def main():
    bot = Replier(
        Parser(),
        s.user,
        s.password,
        'all',
        debug=True
    )
    bot.start()

if __name__ == '__main__':
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        main()