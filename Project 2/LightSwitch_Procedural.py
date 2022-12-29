# Procedural Light Switch

def turnOn():
    global switchIsOn
    # turn the light on
    switchIsOn = True


def turnOff():
    global switchIsOff
    # turn the light off
    switchIsOff = False


# Main Code
switchIsOn = False  # a global Boolean Variable

# Test Code
print(switchIsOn)
turnOn()
print(switchIsOn)
turnOff()
print(switchIsOn)
turnOn()
print(switchIsOn)
