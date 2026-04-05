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
import pandas as pd
import sys


def nettoyage_etape1(nom_fichier):
    
    dtf = pd.read_csv(nom_fichier)

    print("Fichier traité :", nom_fichier)
    print("Nombre de lignes au départ :", len(dtf))

    # Suppression des Probe
    dtf = dtf[dtf["Activity"] != "Probe"]

    # Suppression des Active sans Activity_Value
    dtf = dtf[~((dtf["Activity"] == "Active") & (dtf["Activity_Value"].isna()))]

    print("Nombre de lignes après nettoyage :", len(dtf))

    
    nom_sortie = nom_fichier.replace(".csv", "_clean_step1.csv")

    dtf.to_csv(nom_sortie, index=False)

    print("Fichier enregistré :", nom_sortie)

    return dtf



if len(sys.argv) < 2:
    print("Erreur : donner un fichier CSV en argument")
else:
    fichier = sys.argv[1]
    nettoyage_etape1(fichier)

















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
