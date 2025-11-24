#!/usr/bin/env python3
import argparse
import pandas as pd
from calc_score import calculate

def main():
    parser = argparse.ArgumentParser(description="Ajouter les scores Entry à un CSV de SMILES")
    parser.add_argument("csv_path", type=str, help="Chemin vers le fichier CSV")
    parser.add_argument("smiles_column", type=str, help="Nom de la colonne contenant les SMILES")
    parser.add_argument("--output", type=str, default=None,
                        help="Chemin du fichier CSV de sortie (par défaut écrase le fichier d'entrée)")
    
    args = parser.parse_args()
    
    # Lire le CSV
    df = pd.read_csv(args.csv_path)
    
    if args.smiles_column not in df.columns:
        raise ValueError(f"La colonne '{args.smiles_column}' n'existe pas dans le CSV")
    
    # Calculer les scores avec affichage du nombre d'itérations restantes
    scores = []
    total = len(df)
    for i, s in enumerate(df[args.smiles_column], start=1):
        remaining = total - i
        print(f"Calcul score {i}/{total} | itérations restantes: {remaining}", end='\r')
        scores.append(calculate(s))
    
    df["score_entry"] = scores
    
    # Sauvegarder le CSV
    output_path = args.output or args.csv_path
    df.to_csv(output_path, index=False)
    print(f"\nCSV sauvegardé avec les scores dans '{output_path}'")

if __name__ == "__main__":
    main()
