import RPi.GPIO as sk 
import time

ledblue_rhand =7
ledblue_lhand =24
ledblue_rleg =18
ledblue_lleg =23
ledred =12
ledgreen =8

try:
	sk.setmode(sk.BOARD)
	sk.setup(ledblue_rhand,sk.OUT)	
	sk.setup(ledblue_lhand,sk.OUT)
	sk.setup(ledblue_rleg,sk.OUT)
	sk.setup(ledblue_lleg,sk.OUT)

	sk.setup(ledred,sk.OUT)
	sk.setup(ledgreen,sk.OUT)
except RuntimeError:
	print("Use SUDO!")

def sk_blink(s,t):
      for  i in range(s):
        print("LED turning on")
        sk.output(ledblue_rhand,sk.HIGH)
        sk.output(ledblue_lhand,sk.HIGH)
        sk.output(ledblue_rleg,sk.HIGH)
        sk.output(ledblue_lleg,sk.HIGH)
        sk.output(ledred,sk.HIGH)
        sk.output(ledgreen,sk.HIGH)
        time.sleep(t)
        print("LED turning off")
        sk.output(ledblue_rhand,sk.LOW)
        sk.output(ledblue_lhand,sk.LOW)
        sk.output(ledblue_rleg,sk.LOW)
        sk.output(ledblue_lleg,sk.LOW)
        sk.output(ledred,sk.LOW)
        sk.output(ledgreen,sk.LOW)
        time.sleep(t)
def sk_glow(s,t):
    for  i in range(s):
        print("LED turning on glow function-(suite)")
        sk.output(ledblue_rhand,sk.HIGH)
        sk.output(ledblue_lhand,sk.HIGH)
        sk.output(ledblue_rleg,sk.HIGH)
        sk.output(ledblue_lleg,sk.HIGH)
        sk.output(ledred,sk.HIGH)
        sk.output(ledgreen,sk.HIGH)
        time.sleep(t)
def sk_dim(s,t):
    for  i in range(s):
        print("LED turning on dim function-(suite)")
        sk.output(ledblue_rhand,sk.LOW)
        sk.output(ledblue_lhand,sk.LOW)
        sk.output(ledblue_rleg,sk.LOW)
        sk.output(ledblue_lleg,sk.LOW)
        sk.output(ledred,sk.LOW)
        sk.output(ledgreen,sk.LOW)
        time.sleep(t)
def shirt_glow(s,t):
    for  i in range(s):
        print("LED turning on shirt_glow function-(suite)")
        sk.output(ledblue_rhand,sk.HIGH)
        sk.output(ledblue_lhand,sk.HIGH)
        time.sleep(t)

def pant_glow(s,t):
    for  i in range(s):
        print("LED turning on pant_glow function-(suite)")
        sk.output(ledblue_rleg,sk.HIGH)
        sk.output(ledblue_lleg,sk.HIGH)
        time.sleep(t)
        
def sk_santhosh(channel):


  
                                                                                                       
  
  sk_blink(4,0.5)
  for  i in range(1):
        print("LED turning on left hand")
	sk.output(ledblue_rhand,sk.LOW)
        sk.output(ledblue_rleg,sk.LOW)
        sk.output(ledblue_lleg,sk.LOW)
        sk.output(ledred,sk.LOW)
        sk.output(ledgreen,sk.LOW)
        sk.output(ledblue_lhand,sk.HIGH)
        time.sleep(2)
        print("LED turning right hand")
        sk.output(ledblue_rleg,sk.LOW)
        sk.output(ledblue_lleg,sk.LOW)
        sk.output(ledred,sk.LOW)
        sk.output(ledgreen,sk.LOW)
        sk.output(ledblue_lhand,sk.LOW)    
        sk.output(ledblue_rhand,sk.HIGH)
        time.sleep(4)

  sk_glow(1,32)
  sk_glow(1,5)
  sk_blink(50,0.1)
  sk_glow(1,5)
  sk_blink(25,0.2)
  sk_glow(1,35)
  sk_glow(1,7)
  sk_glow(1,86)
  sk_blink(20,0.5)
  sk_glow(1,5)
  sk_glow(1,40)
  sk_blink(1,5)
  sk_glow(1,6)
  sk_blink(1,5)
  sk_glow(1,22)
  sk_blink(100,0.1)
  sk_glow(50,0.2)
  pant_glow(1,1.5)
  shirt_glow(1,1.5) 

  sk_glow(1,20)
  sk_blink(3000,0.2)
    
 
    
sk.setwarnings(False) 
sk.setmode(sk.BOARD)
sk.setup(10, sk.IN, pull_up_down=sk.PUD_DOWN) 
sk.add_event_detect(10,sk.RISING,callback=sk_santhosh) 
message = input("Waiting for Switch \n Press enter to quit\n\n") 
sk.cleanup()

