import Adafruit_CharLCD as LCD
# ピンの設定. GPIO番号を入れる　
lcd_rs        = 7
lcd_en        = 8
lcd_d4        = 25
lcd_d5        = 24
lcd_d6        = 23
lcd_d7        = 18
#
# 16x2桁.
lcd_columns = 16
lcd_rows    = 2
#
#
lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7,
                       lcd_columns, lcd_rows)
# 液晶クリア.
lcd.clear()
# メッセージ表示.
lcd.message('Hello World!16x2\nQiita.com/mt08/')
# カーソル表示して、ブリンク
lcd.blink(True)
