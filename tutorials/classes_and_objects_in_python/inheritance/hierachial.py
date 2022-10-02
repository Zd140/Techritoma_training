class blackandwhitetv:
    def antenna(self):
        print('Channels are telecated from antena')
class colorTV(blackandwhitetv):
    def cableconnection(self):
        print('channels are telecated by in tv through connection')
class wifiledtv(blackandwhitetv):
    def bluthodteethering(self):
        print("Videos can be teethering through output devices,")
class smartTV(blackandwhitetv):
    def andriodapplication(self):
        print("You can watch movies on OTT plateform,")       
        
a1 = colorTV()
a2 = wifiledtv()
a3 = smartTV()
a1.antenna()
a2.antenna()
a3.antenna()     