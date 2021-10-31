from environs import Env

env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")
OMW_TOKEN = env.str("OMW_TOKEN")
ADMINS = env.list("ADMINS")
OMW_URL = "http://api.openweathermap.org/data/2.5/weather?q={city}&appid={OMW_TOKEN}"
