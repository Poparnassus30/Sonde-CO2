#!/usr/bin/python3 
#coding: UTF-8
import socket as s 
import smbus
import struct
import sys
import time

class system_control():
    def __init__(self):
        self.sys_name="master"

    def gpio_bilan(self):
        #creer tableau avec taille nombre de GPIO
        #luster les GPIO avec leur statut 
        self.gpio_len = data=[ 'pin01' , 'pin02', 'pin03', 'pin04', 'pin05']

    def gpio_set(self, id, InOut):
        pin=('1','in')
        self.gpio=pin

    def gpio_get(self):
        pin=self.gpio
        return pin

class UPS_battery():
    
    def __init__(self,address,bus_x):
        self.__address=address
        self.bus = smbus.SMBus(bus_x)
        self.readvoltage(self.bus)
        self.readcapacity(self.bus)
        
    def get_voltage(self):
        self.readvoltage(self.bus)
        voltage = self.__voltage
        return voltage
        
    def get_capacity(self):
        self.readcapacity(self.bus)
        capacity = self.__capacity
        return capacity
        
    def get_address(self):
        reg_addr = self.__address
        return reg_addr
    
    def readvoltage(self,reg_addr):
        #retourne un float en Volt du raspi UPS
        read = self.bus.read_word_data(self.__address, 2)
        swapped = struct.unpack("<H", struct.pack(">H" , read)) [0]
        self.__voltage = swapped*1.25 /1000/16

        
    def readcapacity(self,reg_addr):
        #retourne un float 
        read = self.bus.read_word_data(self.__address, 4)
        swapped = struct.unpack("<H", struct.pack(">H", read))[0]
        self.__capacity = swapped/256
           

def data_write(data):
    #ecriture données dans fichier
    sonde_data_path='/home/pi/SondeCo2-240905/Client (id_capteur)/Sonde_Co2_data'
    sonde_data_file='sonde_data.csv'
    with open(sonde_data_path,'a') as f:
        f.write(data)           
        f.write("\n")
    f.close()
    
class MySocket(s.socket):
    __host=''
    __port=''
    __connexion_serveur=''
    
    def __init__(self):
        s.__init__(self)
        
    def send():
        #envoi data
        self.send=1
        
    def set_conf(host,port):
        self.__port=port
        self.__host=host
        
    def socketnew(self): #creer la socket pour se connecter au serveur
        self.__connexion_serveur = s.socket(socket.AF_INET, socket.SOCK_STREAM)
        socketconnection()
        
    def socketconnection(self): # etabli la connection avec le serveur
        self.__connexion_serveur.connect((self.__host, self.__port))
        
    def socketclose(self): # ferme la socket
        self.__connexion_serveur.close()
        
    
