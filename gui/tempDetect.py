import cv2
import time
import threading
import serial

def camPreview():       # 단일 함수로 만들기
    previewName = "thermal camera"
    camID = "/dev/video2"
    camFourCC = cv2.VideoWriter.fourcc('Y','1','6',' ')
    cv2.namedWindow(previewName)
    cv2.moveWindow(previewName, 700, 300)
    cam = cv2.VideoCapture(camID)


    
    if cam.isOpened():  # try to get the first frame
        if(camFourCC == cv2.VideoWriter.fourcc('Y','1','6',' ')):
            cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter.fourcc('Y','1','6',' '))
            cam.set(cv2.CAP_PROP_CONVERT_RGB, 0)
        else:
            cam.set(cv2.CAP_PROP_FRAME_WIDTH, 800)      # 여기를 바꿔볼까?
            cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 600)     # 여기도
            cam.set(cv2.CAP_PROP_AUTOFOCUS, 0) # turn the autofocus off

        print('width: {}, height : {}, frame? : {}, ? : {}'.format(cam.get(3), cam.get(4), cam.get(5), cam.get(8)))	# originally 160, 120
    
        rval, frame = cam.read()
    else:
        rval = False
        

    for i in range(150):
        serial_port = serial.Serial(
            port = "/dev/ttyACM1",
            baudrate = 9600,
#        bytesize = serial.EIGHTBITS,
#        parity = serial.PARITY_NONE,
#        stopbits = serial.STOPBITS_ONE
)
        rval, frame = cam.read()
        if(camFourCC == cv2.VideoWriter.fourcc('Y','1','6',' ')):
            temp = frame.max()/100-273
            print("{0}".format(temp))
            if temp >= 50:
                serial_port.write('1'.encode()) # 1 red, 2 green, 3 blank
                time.sleep(5)
                serial_port.write('3'.encode()) # 1 red, 2 green, 3 blank
                return 1
            serial_port.write('2'.encode()) # 1 red, 2 green, 3 blank
            cv2.normalize(frame, frame, 20000, 65535, cv2.NORM_MINMAX) # vivid display 
      
        dst = cv2.resize(frame, dsize=(640, 480), interpolation=cv2.INTER_CUBIC)
        cv2.imshow(previewName, dst)
        
        
        key = cv2.waitKey(20)
        if key == 27:  # exit on ESC
            break

    if cam.isOpened():
        cam.release()
    cv2.destroyWindow(previewName)
    serial_port.write('3'.encode()) # 1 red, 2 green, 3 blank
    
