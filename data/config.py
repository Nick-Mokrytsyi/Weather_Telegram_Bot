from environs import Env

env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")
OMW_TOKEN = env.str("OMW_TOKEN")
ADMINS = env.list("ADMINS")
OMW_URL = "https://api.openweathermap.org/data/2.5/weather?q={city}&appid={OMW_TOKEN}"

GOOGLE_API = env.str("GOOGLE_API")
GOOGLE_URL = "https://maps.googleapis.com/maps/api/timezone/json?location=39.6034810%2C-119.6822510&timestamp" \
             "=1331766000" \
             "&language=en&" \
             f"key={GOOGLE_API}"
