
# Time Handler
import datetime

# Timezone Handler
from pytz import timezone

def getCurrentTime(tz='America/Sao_Paulo'):
    utc = datetime.datetime.now(datetime.timezone.utc)
    BRSP = timezone(tz)
    timeNow = utc.astimezone(BRSP)

    return timeNow

if __name__ == '__main__':
    print('main run')