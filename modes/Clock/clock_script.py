import I2C_LCD_driver
import time


mylcd = I2C_LCD_driver.lcd()


while True:
    mylcd.lcd_display_string(time.strftime('%H:%M:%S %a'), 1)
    mylcd.lcd_display_string(time.strftime('%d/%m/%Y'), 2)
