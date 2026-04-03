"""
Étape 3 : Suppression des faux positifs
-----------------------------------------
Auteur : [À remplir]
Rôle   : Éliminer les molécules actives à cause d'interférences expérimentales

Critères d'élimination (molécules étiquetées "Active") :
(i)  Actives dans AID 585 ou AID 485341, MAIS PAS dans AID 584 et AID 485294
(ii) Actives dans AID 411
(iii) Actives dans AID 587, 588, 590, 591, 592, 593 ou 594
"""

import pandas as pd

# Identifiants des bioessais PubChem à récupérer
AID_INTERFERENCE = {
    "luciferase_inhibitors_1": 585,
    "luciferase_inhibitors_2": 485341,
    "luciferase_counter_1": 584,       # Contre-essai (ne pas éliminer si actif ici)
    "luciferase_counter_2": 485294,    # Contre-essai
    "aggregators": 411,
    "autofluorescence": [587, 588, 590, 591, 592, 593, 594],
}


def load_aid_actives(aid: int) -> set:
    """
    Charge la liste des SID actifs pour un AID PubChem donné.
    
    ⚠️ À IMPLÉMENTER :
    Option A — Télécharger manuellement les CSV depuis PubChem et les lire ici
    Option B — Utiliser l'API PubChem pour récupérer automatiquement les données

    Args:
        aid : Identifiant de l'essai biologique

    Returns:
        Set des Substance_SID actifs dans cet essai
    """
    # TODO : Charger les SID actifs pour cet AID
    # Exemple : pd.read_csv(f"../data/raw/AID_{aid}_actives.csv")
    return set()


def remove_false_positives(df: pd.DataFrame) -> pd.DataFrame:
    """
    Supprime les faux positifs selon les 3 critères du sujet.

    Args:
        df : DataFrame après étape 2 (une ligne par molécule)

    Returns:
        DataFrame sans les faux positifs
    """
    active_mask = df["Activity"] == "Active"
    active_sids = set(df.loc[active_mask, "Substance_SID"])

    sids_to_remove = set()

    # TODO : Critère (i) — AID 585 ou 485341 actifs, mais pas AID 584 et 485294

    # TODO : Critère (ii) — AID 411 actifs

    # TODO : Critère (iii) — AID 587, 588, 590, 591, 592, 593 ou 594 actifs

    initial = len(df)
    df = df[~df["Substance_SID"].isin(sids_to_remove)]
    print(f"[Étape 3] Faux positifs supprimés : {initial - len(df)}")

    return df


if __name__ == "__main__":
    df = pd.read_csv("../data/processed/ABCB1_processed.csv")
    df = remove_false_positives(df)
    print(df["Activity"].value_counts())
