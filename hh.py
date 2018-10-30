import machine
button = machine.Pin(15, machine.Pin.IN, machine.Pin.PULL_UP)
pin1 = machine.Pin(27, machine.Pin.OUT)
pin2 = machine.Pin(32, machine.Pin.OUT)
pin3 = machine.Pin(12, machine.Pin.OUT)
counter = 1
pin1.value(1)
held = False
while True:
    if not(held):
        if  button.value() == 0:
            counter += 1
            if counter == 1:
                pin2.value(0)
                pin3.value(0)
                pin1.value(1)

            elif counter == 2:
                pin1.value(0)
                pin3.value(0)
                pin2.value(1)

            elif counter == 3:
                pin1.value(0)
                pin2.value(0)
                pin3.value(1)
                counter = 0
        time.sleep(0.1)
        if button.value() == 0:
            held = True
        if button.value() == 1:
            held = False
    elif held:
        pass

