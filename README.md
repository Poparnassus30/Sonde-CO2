# Sonde-CO2



Logiciel permettant un relevé de données de dioxyde de carbone, présentation des éléments nécéssaire à la réalisation de la sonde:
  - un capteur CO2 https://sandboxelectronics.com/?product=100000ppm-mh-z16-ndir-co2-sensor-with-i2cuart-5v3-3v-interface-for-arduinoraspeberry-pi&fbclid=IwAR052BKM5tVvsmTGcg-ZWIcFegqh0SS5lfPB8V4pYBOyuSZgU6xBaswT8Is
  - un écran Oled 0,90"
  - 1 raspberry pi0 1V3
  - 1 UPS battery lithium


Pour que le raspberry puisse communiquer avec internet via un pont réeau entre vot-re machine et le raspberry, il est nécessaire d'installer les drivers RPI OTG et d'attribuer au pont reseau une IP, mask, GAteway correspondante  à votre réseau.


====> "Sonde_client.py" 
  L'application "Sonde_serveur.py" sera exécuté sur votre ordinateur par exemple. Les ports de COM doivent être router sur la box.

====> "Sonde_client.py"
  L'application "Sonde_client.py" relève les données toutes les X heures, et les enregistres dans un fichier avec se format :
  [gps;date:heure;valeur en particule par million "ppm";"\n"]

  et affiches le taux de ppm sur l'écran Oled, ainsi que la durée en jour du temps d'exécution du programme)

Une fois la sonde enlevé de son environnement (grottes) , et connecter au réseau , le serveur la détecte et la synchronise.
Il affiche les donnees par onglet (1 capteur / onglet)

** Un module bluetooth sera ajouter plus tard pour synchroniser la sonde directement dans la grotte sans devoir la déplacer.



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
