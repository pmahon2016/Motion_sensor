import RPi.GPIO as GPIO
import time
import smtplib

GPIO.setmode(GPIO.BCM)
PIR_PIN = 21
GPIO.setup(PIR_PIN, GPIO.IN)

def send_email( alerttext):

    # update your settings for your google mail (gmail)  account here
    fromaddr = 'email@gmail.com'  # your from address @gmail.com
    toaddr = 'someemail@domain.com'  # to address
    email_pass = 'passwordhere'  # password
    elogin = 'emaillogin'  # your login ID typically w/o @gmail.com

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login(elogin, email_pass)
        server.sendmail(fromaddr, toaddr, alerttext)
        server.close()
        print("email sent successfully")
    except:
        print("Your email was not sent")


def MOTION(PIR_PIN):
    print("Motion Detected!")
    send_email("Motion in Dining Room")

print("PIR Module Test (CTRL+C to exit)")
time.sleep(2)
print("Ready")


try:
    GPIO.add_event_detect(PIR_PIN, GPIO.RISING, callback=MOTION)
    while 1:
        time.sleep(100)
except KeyboardInterrupt:   
    print(" Quit")
 
GPIO.cleanup()
