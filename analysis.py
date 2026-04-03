"""
Analyse croisée des 3 protéines
---------------------------------
Auteur : [À remplir]
Rôle   : Identifier les molécules actives pour 1, 2 ou 3 protéines

Catégories à analyser :
- Actives pour 1 seule protéine
- Actives pour 2 protéines
- Actives pour les 3 protéines
- Jamais actives pour aucune protéine
"""

import pandas as pd
import matplotlib.pyplot as plt


def load_processed_data() -> dict:
    """
    Charge les 3 fichiers CSV traités.

    Returns:
        Dictionnaire {nom_proteine: DataFrame}
    """
    proteins = {
        "ABCB1": "../data/processed/ABCB1_processed.csv",
        "ABCG2": "../data/processed/ABCG2_processed.csv",
        "ABCC1": "../data/processed/ABCC1_processed.csv",
    }

    data = {}
    for name, path in proteins.items():
        # TODO : Charger chaque CSV et stocker dans data
        pass

    return data


def get_active_sids(df: pd.DataFrame) -> set:
    """Retourne les SID des molécules actives."""
    # TODO : Filtrer sur Activity == "Active" et retourner les Substance_SID
    return set()


def cross_analysis(data: dict) -> dict:
    """
    Analyse croisée : combien de protéines chaque molécule inhibe-t-elle ?

    Args:
        data : Dictionnaire {nom_proteine: DataFrame}

    Returns:
        Dictionnaire avec les 4 catégories de molécules
    """
    # TODO : Calculer les intersections et différences entre les sets de SID actifs

    results = {
        "active_1_only": set(),   # Actives pour 1 seule protéine
        "active_2_only": set(),   # Actives pour exactement 2 protéines
        "active_3": set(),        # Actives pour les 3 protéines
        "never_active": set(),    # Jamais actives
    }

    return results


def plot_venn(results: dict):
    """
    Visualise les résultats avec un diagramme de Venn.
    
    TODO : Utiliser matplotlib-venn ou matplotlib pour visualiser
    """
    # TODO : Créer un diagramme de Venn des 3 protéines
    pass


def plot_activity_distribution(data: dict):
    """
    Affiche la distribution Active/Inactive pour chaque protéine.
    """
    # TODO : Barplot ou pie chart par protéine
    pass


if __name__ == "__main__":
    data = load_processed_data()
    results = cross_analysis(data)

    print("=== Analyse croisée ===")
    print(f"Actives pour 1 seule protéine : {len(results['active_1_only'])}")
    print(f"Actives pour 2 protéines      : {len(results['active_2_only'])}")
    print(f"Actives pour les 3 protéines  : {len(results['active_3'])}")
    print(f"Jamais actives                : {len(results['never_active'])}")

    plot_venn(results)
    plot_activity_distribution(data)
