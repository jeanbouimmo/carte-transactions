import pandas as pd
import glob
import os

# Liste des colonnes à supprimer
colonnes_a_supprimer = [
    "id_mutation",
    "numero_disposition",
    "adresse_code_voie",
    "code_commune",
    "ancien_code_commune",
    "ancien_nom_commune",
    "id_parcelle",
    "ancien_id_parcelle",
    "numero_volume"
]

# Parcourir tous les fichiers correspondant au pattern *_st_maur.csv
for fichier in glob.glob("*_st_maur.csv"):
    # Chargement du fichier en forçant la lecture en type chaîne pour mieux traiter les cellules vides
    df = pd.read_csv(fichier, dtype=str)
    
    # Remplacer les chaînes vides ou composées uniquement d'espaces par NaN
    df = df.replace(r'^\s*$', pd.NA, regex=True)
    
    # Supprimer les colonnes si elles existent dans le DataFrame
    colonnes_existantes = [col for col in colonnes_a_supprimer if col in df.columns]
    df.drop(columns=colonnes_existantes, inplace=True)
    
    # Supprimer les lignes entièrement vides
    df.dropna(how='all', inplace=True)
    
    # Supprimer les colonnes entièrement vides (optionnel)
    df.dropna(axis=1, how='all', inplace=True)
    
    # Enregistrer le fichier optimisé (ici, on ajoute le suffixe _optimized)
    nom_fichier, ext = os.path.splitext(fichier)
    output_file = f"{nom_fichier}_optimized{ext}"
    df.to_csv(output_file, index=False)
    print(f"Fichier optimisé sauvegardé : {output_file}")
