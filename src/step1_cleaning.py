"""
Étape 1 : Nettoyage des données brutes
---------------------------------------
Auteur : [À remplir]
Rôle   : Supprimer les observations ambiguës

Règles :
- Supprimer les lignes où Activity == "Probe"
- Supprimer les lignes Active sans Activity_Value
"""

import pandas as pd


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Nettoie le dataframe brut selon les règles de l'étape 1.

    Args:
        df : DataFrame brut chargé depuis le CSV PubChem

    Returns:
        DataFrame nettoyé
    """
    initial_size = len(df)

    # TODO : Supprimer les lignes où Activity == "Probe"

    # TODO : Supprimer les lignes Active sans valeur dans Activity_Value

    final_size = len(df)
    print(f"[Étape 1] Lignes supprimées : {initial_size - final_size} / {initial_size}")

    return df


if __name__ == "__main__":
    # Test rapide
    df = pd.read_csv("../data/raw/ABCB1_raw.csv")
    df_clean = clean_data(df)
    print(df_clean.head())
