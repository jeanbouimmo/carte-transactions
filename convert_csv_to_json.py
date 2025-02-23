import pandas as pd
import glob
import os

pd.set_option('future.no_silent_downcasting', True)

# Pattern mis à jour pour trouver les fichiers optimisés
fichiers = glob.glob("*_st_maur_optimized.csv")
print("Fichiers trouvés :", fichiers)

liste_df = []

for fichier in fichiers:
    df = pd.read_csv(fichier, dtype=str)
    liste_df.append(df)
    print(f"Fichier traité : {fichier}")

if liste_df:
    df_combiné = pd.concat(liste_df, ignore_index=True)
    output_file = "combined_optimized.json"
    df_combiné.to_json(output_file, orient='records', indent=2, force_ascii=False)
    print(f"Fichier JSON combiné sauvegardé : {output_file}")
else:
    print("Aucun fichier CSV trouvé.")
