# TV class with test code

class TV():
    def __init__(self, brand, location):
        self.brand = brand
        self.location = location
        self.isOn = False
        self.isMuted = False
        # Some default list of channels
        self.channelList = [2, 4, 5, 7, 9, 11, 20, 36, 44, 54, 65]
        self.nChannels = len(self.channelList)
        self.channelIndex = 0
        self.VOLUME_MINIMUM = 0  # constant
        self.VOLUME_MAXIMUM = 10  # constant
        self.volume = self.VOLUME_MAXIMUM // 2  # integer divide

    def power(self):
        self.isOn = not self.isOn   # toggle

    def volumeUp(self):
        if not self.isOn:
            return
        if self.isMuted:
            self.isMuted = False  # changing the volume while isMuted, unmutes the sound
        if self.volume < self.VOLUME_MAXIMUM:
            self.volume = self.volume + 1

    def volumeDown(self):
        if not self.isOn:
            return
        if self.isMuted:
            self.isMuted = False  # changing the volume while muted, unmutes the sound
        if self.volume > self.VOLUME_MINIMUM:
            self.volume = self.volume - 1

    def channelUp(self):
        if not self.isOn:
            return
        self.channelIndex = self.channelIndex + 1
        if self.channelIndex == self.nChannels:
            self.channelIndex = 0  # wrap around to the first channel

    def channelDown(self):
        if not self.isOn:
            return
        self.channelIndex = self.channelIndex - 1
        if self.channelIndex < 0:
            self.channelIndex = self.nChannels - 1    # wrap around to the top channel

    def mute(self):
        if not self.isOn:
            return
        self.isMuted = not self.isMuted

    def setChannel(self, newChannel):
        if newChannel in self.channelList:
            self.channelIndex = self.channelList.index(newChannel)
        # if the newChannel is not in our list of channels, don't do anything

    def showInfo(self):
        print()
        print('TV Status: ', self.brand)
        print("Location: ", self.location)
        if self.isOn:
            print('    TV is: On')
            print('    Channel is:', self.channelList[self.channelIndex])
            if self.isMuted:
                print('    Volume is:', self.volume, '(sound is muted)')
            else:
                print('    Volume is:', self.volume)
        else:
            print('    TV is: Off')


# Main Code
oTV1 = TV("Samsung", "Family Hall")
oTV2 = TV("Apple", "Bedroom")

# Turn both Tvs On
oTV1.power()
oTV2.power()

# Raise the volume of tv1
oTV1.volumeUp()
oTV1.volumeUp()

# Raise the volume of tv2
oTV2.volumeUp()
oTV2.volumeUp()
oTV2.volumeUp()
oTV2.volumeUp()
oTV2.volumeUp()

# Change TV's Channel, then mute it
oTV2.setChannel(44)
oTV2.mute()

# Now display both Tvs
oTV1.showInfo()
oTV2.showInfo()
