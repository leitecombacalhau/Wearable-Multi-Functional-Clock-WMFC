import time
import I2C_LCD_driver

mylcd = I2C_LCD_driver.lcd()


def countdown(t):

    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        mylcd.lcd_display_string(timer, end="\r")
        time.sleep(1)
        t -= 1

    mylcd.lcd_display_string('Time\'s Up!')


countdown(int(30))
