import eapi.hw
import paho.mqtt.client as mqtt


class MqttModul():
    def __init__(self, server="iot.eclipse.org", port=1883):
        self.num = 1
        self.client = mqtt.Client()
        self.client.connect(server, port, keepalive=60)
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.client.connect(server, port, keepalive=60)

        self.eamodul = eapi.hw.EAModul()
        self.eamodul.taster_event_registrieren(0, self.taster_gedrueckt)

    def taster_gedrueckt(self, pin):
        print("[publish]", self.num)
        self.client.publish("eamodul/taster0/pressed/", 1)

    def on_connect(self, client, userdata, flags, rc):
        print("[connected]")
        self.client.subscribe("eamodul/taster0/pressed/")

    def on_message(self, client, userdata, msg):
        print("[msg reveived] topic:", msg.topic, "payload:", msg.payload)

        # turn off all LED rot, gelb, grün
        self.eamodul.schalte_leds(False, False, False)

        if self.num % 3 == 0 or self.num % 5 == 0:
            if self.num % 3 == 0:
                self.eamodul.schalte_led(eapi.hw.EAModul.LED_GELB, True)
            if self.num % 5 == 0:
                self.eamodul.schalte_led(eapi.hw.EAModul.LED_ROT, True)
        else:
            self.eamodul.schalte_led(eapi.hw.EAModul.LED_GRUEN, True)

        self.num += 1

    def start(self):
        self.client.loop_forever()


def main():
    mqttmod = MqttModul()
    mqttmod.start()

if __name__ == "__main__":
    main()

