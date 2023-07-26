import telegram
from environs import Env


env = Env()
env.read_env()


if __name__=='__main__':
    TG_BOT_TOKEN = env('YAMMYCAKE_BOT_TOKEN')
    print(TG_BOT_TOKEN)
