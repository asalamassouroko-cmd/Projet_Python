"""
Pipeline principal — Projet Python L3
--------------------------------------
Lance tout le traitement pour les 3 protéines.

Usage : python main.py
"""

import pandas as pd
import os

from step1_cleaning import clean_data
from step2_labeling import apply_threshold, aggregate_molecules
from step3_false_positives import remove_false_positives

# Colonnes finales attendues dans les CSV de sortie
OUTPUT_COLUMNS = [
    "Substance_SID",
    "Compound_CID",
    "Activity",
    "Activity_Type",
    "Activity_Qualifier",
    "Activity_Value",
]

PROTEINS = {
    "ABCB1": "../data/raw/ABCB1_raw.csv",
    "ABCG2": "../data/raw/ABCG2_raw.csv",
    "ABCC1": "../data/raw/ABCC1_raw.csv",
}


def run_pipeline(protein_name: str, input_path: str) -> pd.DataFrame:
    """
    Exécute les 3 étapes de traitement pour une protéine.

    Args:
        protein_name : Nom de la protéine (ex: "ABCB1")
        input_path   : Chemin vers le CSV brut

    Returns:
        DataFrame final traité
    """
    print(f"\n{'='*50}")
    print(f"Traitement : {protein_name}")
    print(f"{'='*50}")

    # Chargement
    df = pd.read_csv(input_path)
    print(f"Données chargées : {len(df)} lignes")

    # Étape 1
    df = clean_data(df)

    # Étape 2
    df = apply_threshold(df)
    df = aggregate_molecules(df)

    # Étape 3
    df = remove_false_positives(df)

    # Garder uniquement les colonnes attendues
    df = df[OUTPUT_COLUMNS]

    print(f"Résultat final : {len(df)} molécules")
    print(df["Activity"].value_counts())

    return df


def main():
    os.makedirs("../data/processed", exist_ok=True)

    for protein_name, input_path in PROTEINS.items():
        if not os.path.exists(input_path):
            print(f"⚠️  Fichier manquant : {input_path} — Passe ce fichier.")
            continue

        df = run_pipeline(protein_name, input_path)

        output_path = f"../data/processed/{protein_name}_processed.csv"
        df.to_csv(output_path, index=False)
        print(f"✅ Sauvegardé : {output_path}")

    print("\n🎉 Pipeline terminé !")


if __name__ == "__main__":
    main()
