import telegram
from environs import Env


env = Env()
env.read_env()


if __name__=='__main__':
    print('this is new line!s')
    TG_BOT_TOKEN = env('TG_BOT_TOKEN')
    print(TG_BOT_TOKEN)
