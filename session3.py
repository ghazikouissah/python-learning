import json

capteurs = [{"id": "ESP32-01","temperature": 67.8,"humidite": 45.2,"statut": "actif"},
            {"id": "ESP32-02","temperature": 28.2,"humidite": 24.2,"statut": "actif"},
            {"id": "ESP32-03","temperature": 44.5,"humidite": 69.2,"statut": "inactif"}
            ]

def lire_fichier():
    with open("capteurs.json", "r") as f:
        return json.load(f)

def sauvegarder_fichier(data):
    with open("capteurs.json", "w") as f:
        json.dump(data, f, indent=2)

def capteurs_lire():
    data=lire_fichier()
    for capteur in data:
        print(f"ID: {capteur['id']}, Température: {capteur['temperature']}°C")

def capteurs_a_jour(id_capteur,nouveau_statut):
    data=lire_fichier()
    for capteur in data:
        if capteur["id"] == id_capteur:
            capteur["statut"]=nouveau_statut
            print(f"{id_capteur} nouveau statut : {nouveau_statut}")
    sauvegarder_fichier(data)

def ajouter_capteur(nouveau_capteur):
    data = lire_fichier()
    cles_obligatoires = ["id", "temperature", "humidite", "statut"]
    for cle in cles_obligatoires:
        if cle not in nouveau_capteur:
            print(f"Erreur : champ '{cle}' manquant")
            return
    data.append(nouveau_capteur)
    sauvegarder_fichier(data)
    print(f"{nouveau_capteur['id']} ajouté avec succès")





if __name__ == "__main__":
    sauvegarder_fichier(capteurs)  
    capteurs_a_jour("ESP32-03", "critique")
    ajouter_capteur({"id": "ESP32-05", "temperature": 33.0})
    ajouter_capteur({"id": "ESP32-04", "temperature": 55.0, "humidite": 30.0, "statut": "actif"})
    capteurs_lire()  