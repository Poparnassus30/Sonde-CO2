#!/usr/bin/env python3

import socket
import tkinter as tk
from tkinter import ttk
import threading
import os
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class SondeServeurApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sonde Serveur - Gestion des Capteurs")
        self.root.geometry("1000x600")
        
        # Variables pour l'interface
        self.capteurs = set()  # Ensemble des numéros de série détectés
        self.selected_capteur = tk.StringVar()  # Numéro de série sélectionné pour le graphique
        
        # Création du tableau (Treeview)
        self.columns = ("Numéro de série", "Point GPS", "Date", "Heure", "Minute", "Valeur PPM")
        self.tree = ttk.Treeview(root, columns=self.columns, show="headings")
        
        for col in self.columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100)
        
        self.tree.pack(fill="both", expand=True, side="left")

        # Zone pour le graphique
        self.figure = Figure(figsize=(6, 4), dpi=100)
        self.ax = self.figure.add_subplot(111)
        self.ax.set_title("Graphique des données du capteur")
        self.ax.set_xlabel("Date et Heure")
        self.ax.set_ylabel("Valeur PPM")
        self.canvas = FigureCanvasTkAgg(self.figure, self.root)
        self.canvas.get_tk_widget().pack(fill="both", expand=True, side="right")

        # Liste déroulante pour sélectionner le capteur
        dropdown_frame = tk.Frame(self.root)
        dropdown_frame.pack(fill="x", side="top", pady=5)
        
        tk.Label(dropdown_frame, text="Sélectionnez un capteur :").pack(side="left", padx=5)
        self.dropdown = ttk.Combobox(
            dropdown_frame, textvariable=self.selected_capteur, state="readonly"
        )
        self.dropdown.pack(side="left")
        self.dropdown.bind("<<ComboboxSelected>>", self.plot_capteur_data)

        # Lancer le serveur dans un thread
        self.server_thread = threading.Thread(target=self.start_server, daemon=True)
        self.server_thread.start()

    def start_server(self):
        """
        Démarre le serveur socket pour écouter plusieurs connexions et recevoir des données.
        """
        HOST = "127.0.0.1"  
        PORT = 65432        

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
            server_socket.bind((HOST, PORT))
            server_socket.listen()
            print(f"Serveur en attente de connexions sur {HOST}:{PORT}...")
            
            while True:
                conn, addr = server_socket.accept()
                print(f"Connexion établie avec {addr}")
                client_thread = threading.Thread(target=self.handle_client, args=(conn, addr), daemon=True)
                client_thread.start()

    def handle_client(self, conn, addr):
        numero_serie = None  # Numéro de série du capteur
        with conn:
            while True:
                try:
                    data = conn.recv(1024)
                    if not data:
                        print(f"Client {addr} déconnecté.")
                        break
                    decoded_data = data.decode('utf-8').strip()

                    # Identifier le capteur par son numéro de série
                    if numero_serie is None:
                        numero_serie = decoded_data
                        self.capteurs.add(numero_serie)
                        self.update_dropdown()
                        print(f"Numéro de série détecté : {numero_serie}")
                        continue

                    # Stocker les données dans un fichier et mettre à jour l'interface
                    self.store_data(numero_serie, decoded_data)
                    self.update_table(numero_serie, decoded_data)
                except ConnectionResetError:
                    print(f"Connexion réinitialisée par le client {addr}.")
                    break

    def store_data(self, numero_serie, data):
        """
        Stocke toutes les données dans un fichier unique en ajoutant le numéro de série.
        :param numero_serie: Numéro de série du capteur.
        :param data: Données à stocker.
        """
        filename = "donnees_capteurs.txt"
        with open(filename, "a") as file:
            file.write(f"{numero_serie};{data}\n")

    def update_table(self, numero_serie, data):
        """
        Ajoute une ligne au tableau Treeview.
        :param numero_serie: Numéro de série du capteur.
        :param data: Données reçues sous forme [point_gps;date;heure;minute;valeur_ppm].
        """
        try:
            point_gps, date, heure, minute, valeur_ppm = data.split(';')
            self.tree.insert("", "end", values=(numero_serie, point_gps, date, heure, minute, valeur_ppm))
        except ValueError:
            print(f"Format invalide reçu pour {numero_serie} : {data}")

    def update_dropdown(self):
        """
        Met à jour la liste déroulante des numéros de série.
        """
        self.dropdown['values'] = list(self.capteurs)

    def plot_capteur_data(self, event=None):
        """
        Affiche un graphique des données du capteur sélectionné.
        """
        numero_serie = self.selected_capteur.get()
        if not numero_serie:
            return
        
        filename = "donnees_capteurs.txt"
        if not os.path.exists(filename):
            print(f"Fichier {filename} introuvable.")
            return

        # Lire les données associées au capteur
        dates_heures = []
        valeurs_ppm = []

        with open(filename, "r") as file:
            for line in file:
                parts = line.strip().split(';')
                if len(parts) < 6 or parts[0] != numero_serie:
                    continue
                _, point_gps, date, heure, _, valeur_ppm = parts
                dates_heures.append(f"{date} {heure}")
                valeurs_ppm.append(float(valeur_ppm))

        # Mettre à jour le graphique
        self.ax.clear()
        self.ax.plot(dates_heures, valeurs_ppm, marker="o", label=f"Capteur {numero_serie}")
        self.ax.set_title(f"Données du capteur {numero_serie}")
        self.ax.set_xlabel("Date et Heure")
        self.ax.set_ylabel("Valeur PPM")
        self.ax.legend()
        self.ax.tick_params(axis="x", rotation=45)
        self.canvas.draw()


def main() -> int:
    root = tk.Tk()
    app = SondeServeurApp(root)
    root.mainloop()
    return 0


if __name__ == "__main__":
    import sys
    sys.exit(main())
