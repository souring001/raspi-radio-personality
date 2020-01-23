import socket
import RPi.GPIO as GPIO
import asyncore
from threading import Thread
import time
import Adafruit_CharLCD as LCD

BUTTON_PIN = 9
LED_PIN = 17
PORT = 51452
lcd_rs        = 7
lcd_en        = 8
lcd_d4        = 25
lcd_d5        = 24
lcd_d6        = 23
lcd_d7        = 18
lcd_columns = 16
lcd_rows    = 2
status = 0
message = 'Today is GERI.\nHow about you?'
messages = ['I am really GERI\nBUCHUUUUUUUUUUUU',
			'Today is TINK.\nHow about you?',
			'Today is OPPY.\nHow about you?',
			'Today is 0721.\nHow about you?']

class ServerUDP(asyncore.dispatcher):
    data = ""

    def __init__(self, host, port):
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.bind((host, port))
        self.listen(1)
        print("Server listening on port "+str(port))

    def handle_accept(self):
        socket, address = self.accept()
        print('Connected by', address)
        EchoHandler(socket)

class EchoHandler(asyncore.dispatcher_with_send):
    def handle_read(self):
        global message
        global status
        raw_data = self.recv(1024)
        data = str(raw_data.decode())
    	
        if data == 'quit()':
            print("Closing TCP Server...")
            self.out_buffer = "Closing TCP Server".encode()+raw_data
            self.close()
            print("Server closed")
            exit(0)
        elif len(data)>0:
            status = int.from_bytes(raw_data, 'big')
            print("Client << " , status)
            self.out_buffer = "Server >> ".encode()+raw_data #input("intorduzca algo para enviar: ").encode()
            message = messages[status]
            notify()

class Server(Thread):
    def __init__(self):
        Thread.__init__(self)
        print("Starting TCP Server service...")

    def run(self):
        s = ServerUDP('', 51452)
        print("Running TCP Server")
        asyncore.loop()
        
def notify():
	GPIO.output(LED_PIN, GPIO.HIGH)
	time.sleep(1)
	GPIO.output(LED_PIN, GPIO.LOW)

def main():
	global btn
	GPIO.setwarnings(False)
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(BUTTON_PIN,GPIO.IN)
	GPIO.setup(LED_PIN, GPIO.OUT)
	GPIO.add_event_detect(BUTTON_PIN, GPIO.FALLING, callback=callback, bouncetime=300)
	
	lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7,
                       lcd_columns, lcd_rows)
	
	s = Server()
	s.start()
	
	print("tintin")
	
	while True:
		lcd.clear()
		lcd.message(message)
		time.sleep(1)

def callback(channel):
	notify()

if __name__ == "__main__":
    main()


