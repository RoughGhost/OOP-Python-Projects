# Dimmer Switch Class

class DimmerSwitch():
    def __init__(self, label):
        self.label = label
        self.isOn = False
        self.brightness = 0

    def turnOn(self):
        self.isOn = True
        # turn the light on at self.brightness

    def turnOff(self):
        self.isOn = False
        # turn the light off

    def raiseLevel(self):
        if self.brightness < 10:
            self.brightness = self.brightness + 1

    def lowerLevel(self):
        if self.brightness > 0:
            self.brightness = self.brightness - 1

    # Extra method for debugging

    def show(self):
        print("Label: ", self.label)
        print("Light is on?", self.isOn)
        print("Brightness is:", self.brightness)
        print()

# Main Code


# Create first DimmerSwitch, turn on and raise level twice
oDimmer1 = DimmerSwitch("Dimmer 1")
oDimmer1.turnOn()
oDimmer1.raiseLevel()
oDimmer1.raiseLevel()

# Create second DimmerSwitch, turn it on and raise the level 3 times
oDimmer2 = DimmerSwitch("Dimmer2")
oDimmer2.turnOn()
oDimmer2.raiseLevel()
oDimmer2.raiseLevel()
oDimmer2.raiseLevel()

# Create thrid dimmer switch using the default settings
oDimmer3 = DimmerSwitch("Dimmer 3")

# Ask each switch to show itself
oDimmer1.show()
oDimmer2.show()
oDimmer3.show()
