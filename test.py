import RPi.GPIO as gpio
import time
import glob ,os
gpio.setwarnings(False)
gpio.setmode(gpio.BCM)
gpio.setup(17 , gpio.OUT )  #for led 
gpio.setup(26 , gpio.IN)    #for COS
gpio.setup(27 , gpio.OUT)   # for PTT
gpio.output(27, 0)
gpio.output(17 , 0 )
c=0
stopflag=int(input('>>> INPUT YOUR STOP FLAG : '))
while True :
    if gpio.input(26) == True:
        gpio.output(17 , 1 )
    elif gpio.input(26) == False:
        gpio.output(17 , 0) 
        if gpio.input(26) == False :
            gpio.output(17 , 0 )
            print('recording is start')
            os.system('arecord -d 5 test_recording_'+str(c)+'.wav -D sysdefault:CARD=1')
            print('end')
            c+=1
    if int(time.asctime().split()[3].split(':')[1]) == stopflag :
        r_list=glob.glob(r'/home/pi/*.wav')
        print(' recorded wav file is readdy to play......')
        for i in r_list:
            play='aplay ' + i
            print('>>>  RTS PTT ON....... ')
            gpio.output(27 , 1)
            t=os.system(play)
            print(t)
        gpio.cleanup()
        print('cleanup..........!!!')
        break 
    


