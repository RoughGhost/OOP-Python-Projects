# Dimmer Switch class

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
        print('Label:', self.label)
        print('Light is on?', self.isOn)
        print('Brightness is:', self.brightness)
        print()


# Create two DimmerSwitch Objects
oDimmer1 = DimmerSwitch("Dimmer 1")
oDimmer2 = DimmerSwitch("Dimmer 2")

# Tell oDimmer1 to raise its level
oDimmer1.raiseLevel()

# Tell oDimmer2 to raise to level
oDimmer2.raiseLevel()
