import csv
import json

# Fichiers source et destination
csv_file = "transactions.csv"
json_file = "transactions.json"

transactions = []

with open(csv_file, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=',')  # Change à ';' si besoin

    for row in reader:
        try:
            # Extraire l'année depuis date_mutation
            annee = row["date_mutation"].split("-")[0]  # Prend l'année uniquement
            
            # Vérifier que les coordonnées sont valides
            if row["latitude"] and row["longitude"]:
                lat = float(row["latitude"])
                lon = float(row["longitude"])
            else:
                continue  # Sauter les lignes sans coordonnées

            # Récupérer les autres informations
            transactions.append({
                "annee": int(annee),
                "rue": row["adresse_nom_voie"].strip(),
                "num": row["adresse_numero"].strip() if row["adresse_numero"] else "N/A",
                "prix": int(float(row["valeur_fonciere"])) if row["valeur_fonciere"] else 0,
                "surface": int(float(row["surface_reelle_bati"])) if row["surface_reelle_bati"] else 0,
                "type": row["type_local"].strip(),
                "lat": lat,
                "lon": lon
            })
        except ValueError as e:
            print(f"Erreur de conversion sur la ligne : {row}, {e}")

# Sauvegarde du JSON
with open(json_file, "w", encoding="utf-8") as jsonfile:
    json.dump(transactions, jsonfile, indent=4, ensure_ascii=False)

print(f"✅ Conversion terminée ! {len(transactions)} transactions enregistrées.")
