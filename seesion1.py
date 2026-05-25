donnees = [23.5, 45.2, 22.1, 67.8, 41.0, 78.3, 19.5, 55.6]
def tout(donnees):
    return (f"tout les donnes {donnees}")


def seuil(donnees):
    anomalies = [t for t in donnees if t > 50]
    return(anomalies)


def moyenne(donnees):
    moy= round(sum(donnees)/len(donnees),2)
    
    if moy>45:
        print("en danger")
    else:
        print("normal")
    return (moy)


if __name__ == "__main__":
    print(tout(donnees))
    print(seuil(donnees))
    print (moyenne(donnees))
