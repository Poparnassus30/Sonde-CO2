#!/usr/bin/python3 
#coding: UTF-8

import os
import sys
import time as t
from pathlib import Path

#Module personnalisé
import CSonde as s


""" NOTE

I2C = Vérifier la detection du capteur sur le bus i2c, commande pour raspberry

i2cdetect -y 1
     0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f
00:          -- -- -- -- -- -- -- -- -- -- -- -- --
10: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
20: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
30: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
40: -- -- -- -- -- -- -- -- -- -- -- -- -- 4d -- --
50: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
60: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
70: -- -- -- -- -- -- -- --

"""



##################################################################
#Variable global



##################################################################

def main() ->int:

    PRG_count=0
    taux="."
    MaSonde = s.Sensor(0x4D) #On instancie l'objet et lui passe l'adresse du bus i2c en argument 
   
    
    
    while True:
        PRG_count=PRG_count+1
        if MaSonde.begin() == False:
            MaSonde.SondeCo2Etat=0
        else:
                SondeCo2Etat=1
        os.system('clear')
        
        if MaSonde.SondeCo2Etat == 1:
            MaSonde.measure()
            taux_particule = MaSonde.ppm
        
        MaSonde.measure()
        taux_particule = MaSonde.ppm
        SondeValeurCo2PourCent=(taux_particule*100)/100000
        
        data=str(taux_particule)
        s.Sensor_extract(data)
        #date=t.date.today().strftime('%Y-%m-%d %H:%M:%S')
        
        print("######################################################################       PROGRAMME SONDE CO2 " , "TIC::" , "[" , PRG_count, "]" , "     ######################################################################")
        print("# ")
        print("# MaSonde            =","::",MaSonde)
        print("# Sonde état        =",MaSonde.SondeCo2Etat)
        print("# Taux de particule =","[",taux_particule, "ppm]","::","[",SondeValeurCo2PourCent,"%","]")
        print("#")
        print("# IOCONTROL=",MaSonde.IOCONTROL)
        print("# FCR  =",MaSonde.FCR)
        print("# LCR  =",MaSonde.LCR)
        print("# DLL  =",MaSonde.DLL)
        print("# DLH  =",MaSonde.DLH)
        print("# THR  =",MaSonde.THR)
        print("# RHR  =",MaSonde.RHR)
        print("# TXLVL=",MaSonde.TXLVL)
        print("# RXLVL=",MaSonde.RXLVL)
        print("# ")
        print("######################################################################       PROGRAMME SONDE CO2      ######################################################################")
        
        t.sleep(1)
    return 0
    
    
    
if __name__ == '__main__':
    sys.exit(main())
    
