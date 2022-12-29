# OO LightSwitch

class LightSwitch():
    def __init__(self):
        self.switchIsOn = False

    def turnOn(self):
        # turn the switch on
        self.switchIsOn = True

    def turnOff(self):
        # turn the switch off
        self.switchIsOn = False

    def show(self):
        print(self.switchIsOn)

# Main Code


oLightSwitch1 = LightSwitch()  # Create LightSwitch Object
oLightSwitch2 = LightSwitch()  # Create another LightSwitch

# Test Code
oLightSwitch1.show()
oLightSwitch2.show()
oLightSwitch1.turnOn()  # Turn switch 1 on
# Switch 2 should be off at a start, but this makes it clearer
oLightSwitch2.turnOff()
oLightSwitch1.show()
oLightSwitch2.show()
