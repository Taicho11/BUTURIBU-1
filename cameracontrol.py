import RPi.GPIO as GPIO
import time
import cv2
import datetime

GPIO.setmode(GPIO.BCM)
GPIO.setup(14,GPIO.OUT)                             
GPIO.setup(15,GPIO.OUT)
GPIO.setup(21,GPIO.IN,pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(20,GPIO.IN,pull_up_down = GPIO.PUD_DOWN)

count =0
picture_number = -1

while True:
    print('stby')                          #撮影の準備中は’スタンバイモード’であり、赤色のLEDが付く
    GPIO.output(14,1)
    button = GPIO.input(21)
    count = count+1 if button else count+0 #赤色のボタンを押すとスタンバイモード終了
    
    while count:
        print('photo')                     #'フォトモード'に移行
        GPIO.output(14,0)                  #青色のLEDが付く
        GPIO.output(15,1)
        for i in range(3):                 #３回赤がついて、４回目と同時に写真撮影
            GPIO.output(14,1)
            time.sleep(0.5)
            GPIO.output(14,0)
            time.sleep(1)
        picture_number+=1
        GPIO.output(14,1)
        '''
        dt_now = datetime.datetime.now()
        file_name = dt_now.strftime('%Y年%m月%d日%H時%M分%S秒')
        cap = cv2.VideoCapture(0)
        ret,frame = cap.read()
        cv2.imwrite(f'./{picture_number}/{file_name}.jpg',frame)
        cap.release()
        '''
        
        if picture_number == 100:           #１周分撮り終わったらスタンバイモードに戻る
            count = 0
            picture_number = 0
            break
        