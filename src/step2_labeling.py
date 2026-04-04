"""
Étape 2 : Reclassification et label global par molécule
---------------------------------------------------------
Auteur : [À remplir]
Rôle   : Appliquer le seuil 10 µM et résoudre les conflits

Règles :
- Si Activity_Value <= 10 µM → Active
- Si Activity_Value >  10 µM → Inactive
- Gérer les molécules avec plusieurs observations (moyenne, écart-type, majorité)
"""

import pandas as pd
import numpy as np

THRESHOLD = 10.0  # µM


def apply_threshold(df: pd.DataFrame) -> pd.DataFrame:
    """
    Reclasse chaque observation selon le seuil de 10 µM.

    Args:
        df : DataFrame nettoyé (après étape 1)

    Returns:
        DataFrame avec Activity mise à jour
    """
    # TODO : Appliquer le seuil sur Activity_Value
    # - Si Activity_Value <= THRESHOLD → "Active"
    # - Si Activity_Value >  THRESHOLD → "Inactive"
    # - Si pas de Activity_Value → conserver la valeur actuelle

    return df


def resolve_conflicts(group: pd.DataFrame) -> pd.Series:
    """
    Résout les conflits quand une molécule a plusieurs observations.

    Args:
        group : Groupe de lignes correspondant à un même Substance_SID

    Returns:
        Série avec les colonnes finales de la molécule, ou None si à supprimer
    """
    labels = group["Activity"].unique()

    # TODO : Cas 1 — tous les labels sont identiques
    # → garder le label, moyenne des Activity_Value

    # TODO : Cas 2a — labels contradictoires, toutes les valeurs sont disponibles
    # → calculer moyenne et écart-type
    # → si moyenne > écart-type : garder (label selon seuil)
    # → sinon : supprimer la molécule (return None)

    # TODO : Cas 2b — labels contradictoires, certaines valeurs manquantes
    # → label majoritaire
    # → si pas de majorité : supprimer
    # → si majorité Active : moyenne des valeurs dispo
    # → si majorité Inactive : pas de valeur

    pass


def aggregate_molecules(df: pd.DataFrame) -> pd.DataFrame:
    """
    Applique resolve_conflicts à chaque molécule (groupé par Substance_SID).

    Args:
        df : DataFrame après apply_threshold

    Returns:
        DataFrame avec une ligne par molécule
    """
    # TODO : Grouper par Substance_SID et appliquer resolve_conflicts

    return df


if __name__ == "__main__":
    df = pd.read_csv("../data/raw/ABCB1_raw.csv")
    df = apply_threshold(df)
    df = aggregate_molecules(df)
    print(df.head())
