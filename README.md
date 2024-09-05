# Sonde-CO2


Pour que le raspberry puisse communiquer avec internet via un pont réeau, il est nécessaire d'installer les drivers RPI OTG.

Logiciel permettant un relevé de données de dioxyde de carbone, présentation des éléments nécéssaire à la réalisation de la sonde:
- un capteur MZ 
- un écran Oled 0,90"
- 1 raspberry pi0 1V3
- 1 UPS battery lithium


La sonde CO2 "Sonde_client.py" et l'application Sonde_serveur.py sera exécuté sur une machine.

La sonde (Sonde_client.py) relève les données toutes les X heures, et les enregistres dans un fichier avec se format  (gps;date:heure;valeur en particule par million "ppm";"\n") et affiches le taux de ppm sur l'écran Oled, ainsi que la durée en jour du temps d'exécution du programme)

Une fois la sonde enlevé de son environnement (grottes) , et connecter au réseau , le serveur la détecte et la synchronise.
Il affiche les donnees par onglet (1 capteur / onglet)

** Un module bluetooth sera ajouter plus tard pour synchroniser la sonde directement dans la grotte sans devoir la déplacer.
