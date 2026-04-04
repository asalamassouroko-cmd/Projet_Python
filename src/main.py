"""
Pipeline principal — Projet Python L3
Lance tout le traitement pour les 3 protéines.
Usage : python main.py
"""
import pandas as pd
import os
from step1_cleaning import clean_data
from step2_labeling import apply_threshold, aggregate_molecules
from step3_false_positives import remove_false_positives

OUTPUT_COLUMNS = [
    "Substance_SID", "Compound_CID", "Activity",
    "Activity_Type", "Activity_Qualifier", "Activity_Value",
]

PROTEINS = {
    "ABCB1": "../data/raw/ABCB1_raw.csv",
    "ABCG2": "../data/raw/ABCG2_raw.csv",
    "ABCC1": "../data/raw/ABCC1_raw.csv",
}

def run_pipeline(protein_name, input_path):
    print(f"\n{'='*40}\nTraitement : {protein_name}\n{'='*40}")

    df = pd.read_csv(input_path)
    print(f"Chargé : {len(df)} lignes")

    df = clean_data(df)
    print(f"Après étape 1 : {len(df)} lignes")

    df = apply_threshold(df)
    df = aggregate_molecules(df)
    print(f"Après étape 2 : {len(df)} molécules")

    df = remove_false_positives(df)
    print(f"Après étape 3 : {len(df)} molécules")

    df = df[OUTPUT_COLUMNS]
    print(df["Activity"].value_counts())
    return df


def main():
    os.makedirs("../data/processed", exist_ok=True)

    for protein_name, input_path in PROTEINS.items():
        if not os.path.exists(input_path):
            print(f"Fichier manquant : {input_path}, ignoré.")
            continue

        df = run_pipeline(protein_name, input_path)

        output_path = f"../data/processed/{protein_name}_processed.csv"
        df.to_csv(output_path, index=False)
        print(f"Sauvegardé : {output_path}")

    print("\nPipeline terminé !")


if __name__ == "__main__":
    main()
