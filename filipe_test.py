import machine
#built in blue led, low active
pin2 = machine.Pin(2, machine.Pin.OUT)
# actually, is off
#on state
pin2.on() 
pin2.off()
#off state
pin2.on() 

# D5 port
pinD5 = machine.Pin(12, machine.Pin.OUT) 

# D6 port
pinD6 = machine.Pin(14, machine.Pin.OUT) 
