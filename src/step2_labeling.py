"""
Étape 2 : Reclassification et label global par molécule
---------------------------------------------------------
Auteur : ASSOUROKO Abdul salam
Rôle   : Appliquer le seuil 10 µM et résoudre les conflits

Règles :
- Si Activity_Value <= 10 µM → Active
- Si Activity_Value >  10 µM → Inactive
- Gérer les molécules avec plusieurs observations (moyenne, écart-type, majorité)
"""

import pandas as pd
import numpy as np

THRESHOLD = 10.0

def apply_threshold(df):
    for i, row in df.iterrows():
        if pd.notna(row["Activity_Value"]):
            if row["Activity_Value"] <= THRESHOLD:
                df.at[i, "Activity"] = "Active"
            else:
                df.at[i, "Activity"] = "Inactive"
    return df


def resolve_conflicts(group):
    labels = group["Activity"].unique()

    # Cas 1 : tous pareils
    if len(labels) == 1:
        return {
            "Activity": labels[0],
            "Activity_Value": group["Activity_Value"].mean()
        }

    # Cas 2a : toutes les valeurs dispo
    if group["Activity_Value"].notna().all():
        mean = group["Activity_Value"].mean()
        std  = group["Activity_Value"].std()
        if mean > std:
            label = "Active" if mean <= THRESHOLD else "Inactive"
            return {"Activity": label, "Activity_Value": mean}
        else:
            return None  # supprimée

    # Cas 2b : valeurs partiellement manquantes
    counts = group["Activity"].value_counts()
    if len(counts) > 1 and counts.iloc[0] == counts.iloc[1]:
        return None  # égalité → supprimée

    majority = counts.idxmax()
    if majority == "Active":
        return {"Activity": "Active", "Activity_Value": group["Activity_Value"].mean()}
    else:
        return {"Activity": "Inactive", "Activity_Value": np.nan}


def aggregate_molecules(df):
    rows = []
    for sid, group in df.groupby("Substance_SID"):
        result = resolve_conflicts(group)
        if result is not None:
            # Garder les autres colonnes de la première ligne
            base = group.iloc[0][["Substance_SID", "Compound_CID", "Activity_Type", "Activity_Qualifier"]].to_dict()
            base.update(result)
            rows.append(base)
    return pd.DataFrame(rows)


if __name__ == "__main__":
    df = pd.read_csv("../data/raw/ABCB1_raw.csv")
    df = apply_threshold(df)
    df = aggregate_molecules(df)
    # Garder seulement les colonnes demandées dans le bon ordre
    cols = ["Substance_SID", "Compound_CID", "Activity", "Activity_Type", "Activity_Qualifier", "Activity_Value"]
    df = df[cols]
    df.to_csv("../data/processed/ABCB1_step2.csv", index=False)
    print(df.head())
    print(df["Activity"].value_counts())
