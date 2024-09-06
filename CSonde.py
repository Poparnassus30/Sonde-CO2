#!/usr/bin/python3 
#coding: UTF-8
import smbus
import time
#import os

import datetime as dt

    
class Sensor(): #module NDIR sur github (version modifié par moi)
    __sonde_gps_point=[]
    __sonde_path_data='/home/pi/SondeCo2-240824/sonde_data.csv'
    __sonde_nombre=0
    
    cmd_measure = [0xFF,0x01,0x9C,0x00,0x00,0x00,0x00,0x00,0x63]
    ppm         = 0
    
    SondeCo2Etat=0

    IOCONTROL   = 0X0E << 3
    FCR         = 0X02 << 3
    LCR         = 0X03 << 3
    DLL         = 0x00 << 3
    DLH         = 0X01 << 3
    THR         = 0X00 << 3
    RHR         = 0x00 << 3
    TXLVL       = 0X08 << 3
    RXLVL       = 0X09 << 3

    def __init__(self, i2c_addr):
        self.i2c_addr = i2c_addr
        self.i2c      = smbus.SMBus(1)
        self.__sonde_nombre=self.__sonde_nombre+1
    def get_i2c_addr(self):
        i2c_addr = self.i2c_addr
        return i2c_addr

    def begin(self):
        try:
            self.write_register(self.IOCONTROL, 0x08)
        except IOError:
            pass

        trial = 10

        while trial > 0:
            trial = trial - 1

            try:
                self.write_register(self.FCR, 0x07)
                self.write_register(self.LCR, 0x83)
                self.write_register(self.DLL, 0x60)
                self.write_register(self.DLH, 0x00)
                self.write_register(self.LCR, 0x03)
                return True
            except IOError:
                pass

        return False

    def measure(self):
        try:
            self.write_register(self.FCR, 0x07)
            self.send(self.cmd_measure)
            time.sleep(0.01)
            self.parse(self.receive())
            return True
        except IOError:
            return False

    def parse(self, response):
        checksum = 0

        if len(response) < 9:
            return

        for i in range (0, 9):
            checksum += response[i]

        if response[0] == 0xFF:
            if response[1] == 0x9C:
                if checksum % 256 == 0xFF:
                    self.ppm = (response[2]<<24) + (response[3]<<16) + (response[4]<<8) + response[5]

    def read_register(self, reg_addr):
        time.sleep(0.001)
        return self.i2c.read_byte_data(self.i2c_addr, reg_addr)

    def write_register(self, reg_addr, val):
        time.sleep(0.001)
        self.i2c.write_byte_data(self.i2c_addr, reg_addr, val)

    def send(self, command):
        if self.read_register(self.TXLVL) >= len(command):
            self.i2c.write_i2c_block_data(self.i2c_addr, self.THR, command)

    def receive(self):
        n     = 9
        buf   = []
        start = time.clock()

        while n > 0:
            rx_level = self.read_register(self.RXLVL)

            if rx_level > n:
                rx_level = n

            buf.extend(self.i2c.read_i2c_block_data(self.i2c_addr, self.RHR, rx_level))
            n = n - rx_level

            if time.clock() - start > 0.2:
                break

        return buf
        
    def SondeCalibration(self):
        #Demarrage calibration
        self.send(0x87)


    
    
   
