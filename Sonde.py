#!python3

# ceci est une class modifier, la version initial est la NDIR.py développer par xxxxxxx (oublié lol)

import smbus
import os
import GPIO

def new_sensor(*argent,**kwarg):
   new_sonde= sensor()

class sensor():
  __gps_point=None

  def __init__(self):
    self.quantite=self.quantite+1
    
  def sensor_conf(self,point):
     self.__gps_point=point
