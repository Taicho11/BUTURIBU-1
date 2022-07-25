import RPi.GPIO as GPIO
import time
import cv2
import datetime

GPIO.setmode(GPIO.BCM)
GPIO.setup(14,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)
GPIO.setup(21,GPIO.IN,pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(20,GPIO.IN,pull_up_down = GPIO.PUD_DOWN)
#スタートボタンが押されたか判別する
count =0
#周回モード時の写真の枚数を代入する。１周するたびにリセット
picture_number = -1

rightwheel = GPIO.PWM(14,50)
leftwheel = GPIO.PWM(15,50)
rightwheel.start(0)
leftwheel.start(0)

while True:
    #ボタンが１瞬でも押されたらループに入る
    button = GPIO.input(21)
    count = count+1 if button else count+0
    print('stby')
    
    while count>=1:
        #円運動しながら連写
        print('circle')
        picture_number+=1
        
        dt_now = datetime.datetime.now()
        file_name = dt_now.strftime('%Y年%m月%d日%H時%M分%S秒')
        cap = cv2.VideoCapture(0)
        ret, frame = cap.read()
        print(ret)
        cv2.imwrite(f'./{picture_number}.taichou/{file_name}.jpg', frame)
        cap.release()
        
        rightwheel.ChangeDutyCycle(100)
        leftwheel.ChangeDutyCycle(50)
        #だいたい１周したらループに入る
        while picture_number >= 1000:
            rightwheel.ChangeDutyCycle(0)
            leftwheel.ChangeDutyCycle(0)
            print('sikosiko')
            dt_now = datetime.datetime.now()
            file_name = dt_now.strftime('%Y年%m月%d日%H時%M分%S秒')
            cap = cv2.VideoCapture(0)
            ret,frame = cap.read()
            cv2.imwrite(f'./shikoshiko/{file_name}.jpg',frame)
            cap.release()
            #フィニッシュボタンを押したらしこしこ終
            if GPIO.input(20):
                count = 0
                picture_number = -1
                break