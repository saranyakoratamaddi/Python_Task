#12. Smart Home Devices (Multiple Inheritance) 
#A smart home device may have both WiFi connectivity and Voice control features. Create classes WiFiDevice and VoiceAssistant, and a class SmartSpeaker that 
#inherits from both using multiple inheritance.




class WifiDevice:
    def __init__(self,network):
        self.network=network
    def connect_wifi(self):
        print(f"Connected to WiFi Network {self.network}")
class VoiceAssistant:
    def __init__(self,assistant_name):
        self.assistant_name=assistant_name
    def listen_command(self):
        print(f"{self.assistant_name} listening to your command")
class SmartSpeaker(WifiDevice,VoiceAssistant):
    def __init__(self,device_name,network,assistant_name):
        WifiDevice.__init__(self,network)
        VoiceAssistant.__init__(self,assistant_name)
        self.device_name=device_name
    def play_music(self,song):
        print(f"{self.device_name} is playing {self.song}")
speaker=SmartSpeaker("Living Room","Airtel","Alexa")
speaker.connect_wifi()
speaker.listen_command()
speaker.play_music("classic")
                     
