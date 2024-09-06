#!/usr/bin/python3 
#coding: UTF-8

import os
import sys
import smbus

import time as t
import datetime as dt
from pathlib import Path
#import PIL
#import Adafruit_GPIO.SPI as SPI
#import Adafruit_SSD1306

#Module personnalisé
import CSonde as s #Module NDIR modifié par NP pour  la sonde co2
import CNoyau as n

""" 
##################################################################
# NOTE

Depuis peu les raspberry utilise les adresse ip en IPV6 sauf que elle ne sont pas activer sur la version stresh du pi0


1/ Identifier la version du raspberry
https://windows8facile.fr/identifier-version-raspberry-pi/
https://fr.wikipedia.org/wiki/Raspberry_Pi#Identification_logicielle_des_diff%C3%A9rents_mod%C3%A8les
    root@raspberrypi:/usr/bin# cat /proc/cpuinfo
    processor       : 0
    model name      : ARMv6-compatible processor rev 7 (v6l)
    BogoMIPS        : 697.95
    Features        : half thumb fastmult vfp edsp java tls
    CPU implementer : 0x41
    CPU architecture: 7
    CPU variant     : 0x0
    CPU part        : 0xb76
    CPU revision    : 7

    Hardware        : BCM2835
    Revision        : 900093
    Serial          : 00000000b6151267
    Model           : Raspberry Pi Zero Rev 1.3
    
2.1/ Initialisation du bus i2c
    sudo raspi-config
    

I2C = Vérifier la detection du capteur et de l'écran 
sur le bus i2c, commande pour raspberry

i2cdetect -y 1
    0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f
 00:          -- -- -- -- -- -- -- -- -- -- -- -- --
 10: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
 20: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
 30: -- -- -- -- -- -- -- -- -- -- -- -- 3c -- -- --
 40: -- -- -- -- -- -- -- -- -- -- -- -- -- 4d -- --
 50: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
 60: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
 70: -- -- -- -- -- -- -- --


2.1/ ECRAN EN I2C (0x3C)    
    https://pypi.org/project/Adafruit-SSD1306/
    https://docs.circuitpython.org/projects/ssd1306/en/latest/                                                  #
2.2/ -SONDE EN I2C (0x4D) 
    import NDIR

##################################################################  
"""

##################################################################
#Variable global



##################################################################
"""
def AffichageEcran(arg1):
    #Ecran afficher donner
    var=1
    draw.rectangle((0,0,width,height), outline=0, fill=0)
    Ligne1=(":" + str(SondeMesure()) + "PPM"+ ":" + str(arg1))
    Ligne2=(" ")
    Ligne3=("La Sonde Des Mounjou------")

    draw.text((x,0), str(Ligne1), font=font, fill=255)
    draw.text((x+10), str(Ligne2), font=font, fill=255)
    draw.text((x,20), str(Ligne3), font=font, fill=255)

    image.show()
    disp.image(image)
    disp.display()
    time.sleep(1)
"""

   


def main() ->int:
    
    #Initialisation du capteur de CO2
    taux="."
    MaSonde = s.Sensor(0x4D) #On instancie l'objet et lui passe l'adresse du bus i2c en argument 
    
    #Initialisation de la ocket client de communication
    host='192.168.1.199'
    port='65235'
    """
    #Utilisation de la class MySocket
    MaSocket = n.MySocket()
    MaSocket.set_conf(host,port)
    """
    #initialisation objet UPS_battery
    #bus = smbus.SMBus(1)
    batterie01 = n.UPS_battery(0x36,1) 
    
    PRG_count=0    
    while True:
        #BOUCLE PARAMETRE
        PRG_count=PRG_count+1
        var1=""
        
        #SONDE CO2
        if MaSonde.begin() == False:
            MaSonde.SondeCo2Etat=0
        else:
                SondeCo2Etat=1
               
        if MaSonde.SondeCo2Etat == 1:
            MaSonde.measure()
            taux_particule = MaSonde.ppm
        MaSonde.measure()
        taux_particule = MaSonde.ppm
        SondeValeurCo2PourCent=(taux_particule*100)/1000000
        
        #UPS BATTERY 
        RV = batterie01.get_voltage()
        RC = batterie01.get_capacity()  
        RA = hex(batterie01.get_address())
        
        RA_sonde=hex(MaSonde.get_i2c_addr())
        if RV ==100:
            var1 = "batteri low"
            

        
        #PREPARATION DATA
        date=dt.datetime.now()
        #CONSTRUCTION DE LA DATA
        data1=(str(date)+", ["+str(taux_particule)+"ppm]"+", ["+str(RC)+"%]"+", ["+str(RV)+"V]")
        data=str(taux_particule)
        #EXTRACTION DATA DANS FICHIER 
        n.data_write(data1)

        
        #AFFICHAGE CONSOLE ECRAN(PRG_count) 
        os.system('clear')
        print("\n")        
        print("########################################################################")
        print("# PROGRAMME SONDE CO2 " , "TIC" , "[" , PRG_count, "]"    )                      
        print("########################################################################")
        print("#",date  ) 
        print("# Sonde address [",RA_sonde,"]")
        print("# MaSonde            ",MaSonde                                                                              )
        print("# Sonde état         ",MaSonde.SondeCo2Etat                                                                      )
        print("# Taux de particule  ","[",taux_particule, "ppm]","::","[",SondeValeurCo2PourCent,"%","]"                        )
        """       
        print("#"                                                                                                               )
        print("# IOCONTROL =",MaSonde.IOCONTROL                                                                                 )
        print("# FCR       =",MaSonde.FCR                                                                                       )
        print("# LCR       =",MaSonde.LCR                                                                                       )
        print("# DLL       =",MaSonde.DLL                                                                                       )
        print("# DLH       =",MaSonde.DLH                                                                                       )
        print("# THR       =",MaSonde.THR                                                                                       )
        print("# RHR       =",MaSonde.RHR                                                                                       )
        print("# TXLVL     =",MaSonde.TXLVL                                                                                     )
        print("# RXLVL     =",MaSonde.RXLVL                                                                                     )
        """ 
        print("#")
        print("########################################################################")
        print("# DATA FICHIER:")
        print("#",data1)
        print("#")
        print("########################################################################")
        print("# Socket :"                                                                                                       )
        print("#"                                                                                                               )
        print("#"                                                                                                               )
        print("########################################################################")
        print("# Battery address i2c [", str(RA),"]")
        print("# Battery Tension [", RV,"]")
        print("# Battery Capacity [" , RC,"]")
        print("# ...[", var1 ,"]"                                                                                                         )
        print("########################################################################")
        
        #os.system('pause')
        
        t.sleep(2)
    return 0
    
    
    
if __name__ == '__main__':
    sys.exit(main())
    

    
