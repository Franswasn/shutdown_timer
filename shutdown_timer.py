import time
import subprocess
shutdowntime = input('Enter shutdown time (hr:min:sec):')
while True:

    time_only= time.asctime()
    times= time_only.split(' ')
    x = times[4]
    if x == shutdowntime:
        print('helloo shutdown')
        subprocess.call(["shutdown","/s","/t", "5"])