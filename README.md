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
