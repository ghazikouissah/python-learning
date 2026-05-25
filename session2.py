capteurs = [{"id": "ESP32-01","temperature": 67.8,"humidite": 45.2,"statut": "actif"},
            {"id": "ESP32-02","temperature": 28.2,"humidite": 24.2,"statut": "actif"},
            {"id": "ESP32-03","temperature": 44.5,"humidite": 69.2,"statut": "inactif"}
            ]
def afficher_capteurs(capteurs):
    for capteur in capteurs:
        print(f"ID: {capteur['id']}, Température: {capteur['temperature']}°C")

def capteurs_seuils(capteurs):
    for capteur in capteurs:
        if capteur["statut"] == "actif" and capteur["temperature"] > 50:
            print(f"ID: {capteur['id']} est actif et a une température élevée de {capteur['temperature']}°C")

def changer_statut (capteurs,id_capteur,nouveau_statut):
    for capteur in capteurs:
        if capteur["id"] == id_capteur:
            capteur["statut"]=nouveau_statut
            print(f"ESP32-03 nouveau statut : {capteurs[2]['statut']}")

def capteur_actifs(capteurs):
    compteur =0
    for capteur in capteurs:
        if capteur["statut"]=="actif":
            compteur +=1
    return compteur   

if __name__ == "__main__":
    afficher_capteurs(capteurs)
    capteurs_seuils(capteurs)
    changer_statut(capteurs, "ESP32-03", "critique")
    print(f"le nombre de capteurs actifs est {capteur_actifs(capteurs)}")