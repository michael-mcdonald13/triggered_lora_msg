

#Script to send LoRa message when rising is detected on set pin

from machine import Pin, Timer


button = Pin(21, Pin.IN, Pin.PULL_DOWN) # select free GPIO pin on microcontroller
counter = 0  # Initialize the button press count
debounce_timer = None

def button_pressed(pin):
    global counter, debounce_timer  # Declare variables as global

    if debounce_timer is None:
        counter += 1
        # Start a timer for debounce period (e.g., 200 milliseconds)
        debounce_timer = Timer()
        debounce_timer.init(mode=Timer.ONE_SHOT, period=200, callback=debounce_callback)
        send_msg_out(counter)

def debounce_callback(timer):
    global debounce_timer
    debounce_timer = None
    
def send_msg_out(count):
    
    print(f'Trap triggered:{count}')
    #add actions here

# Attach the interrupt to the button's rising edge
button.irq(trigger=Pin.IRQ_RISING, handler=button_pressed)

def main():
    
    print("Waiting for trigger condition to be met...")
    
    
    
if __name__ == '__main__':

    try:
        main()
    except Exception as e:
        sys.print_exception(e) 
    except KeyboardInterrupt:
        print('Program Interrupted by the user')


