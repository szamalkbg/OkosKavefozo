#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, TouchSensor, ColorSensor, InfraredSensor
from pybricks.parameters import Port, Stop
from pybricks.tools import wait
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

class Kavefozo():
    def __init__(self):
        # tégla (brick)
        self.ev3 = EV3Brick()
        # szenzor (sensor)
        self.isz = InfraredSensor(Port.S4)

    def indul(self):
        self.ev3.speaker.set_volume(40)

        while True:
            gombok = self.isz.buttons(1)
            if gombok:
                print("megnyomva")
                self.ev3.speaker.play_file('bekapcs.wav')
                wait(400)
                self.ev3.speaker.play_file('piroskek.wav')
                wait(300)
                if self.isz.buttons(1):
                    self.ev3.speaker.play_file('elindul.wav')
                    wait(1000)
                    self.ev3.speaker.play_file('coffee.wav')
                    wait(1000)
                    self.ev3.speaker.play_file('keszkave.wav')
