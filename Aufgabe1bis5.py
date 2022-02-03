import os

import pandas as pd


##################################################
# Aufgabe 1

def import_ajustments():
    with open(os.getcwd() + "/2022-02-02 Data Bewerbungsaufgabe.csv") as f:
        df = pd.read_csv(f, delimiter=";")
    df = df.rename(columns={"generator:source": "Energiequelle", "generator:output": "Leistung in kW"})
    df.pop("wkt_geom")
    return df


##################################################
# Aufgabe 2

def sort(df: pd.DataFrame):
    df.sort_values(by=["Energiequelle"], inplace=True)
    return df


##################################################
# Aufgabe 3
# In der Aufgabenstellung steht alle "Yes" sollen ersetzt werden. Im Datensatz gibt es aber nur Einträge mit "yes"
# Hier wurden Einträge mit "yes" ersetzt
def yes_to_value(df: pd.DataFrame):
    df["Leistung in kW"] = df["Leistung in kW"].replace(to_replace="yes", value="600")
    return df


##################################################
# Aufgabe 4
# Remove Nan values:
def remove_nan_and_invalid(df: pd.DataFrame):
    drop_arr = df[df["Leistung in kW"].isna()]
    df = df.drop(drop_arr.index)

    # Remove "non figure values"
    drop_arr = []
    for i in df.index:
        try:
            float(df["Leistung in kW"][i])
        except ValueError:
            drop_arr.append(i)
    df = df.drop(drop_arr)
    return df


##################################################
# Aufgabe 5
def split_dataframe_by_source_and_save(df: pd.DataFrame):
    try:
        os.makedirs("Energiequellen")
    except FileExistsError:
        pass

    for i in df.groupby(["Energiequelle"]):
        for k in i:
            if type(k) == pd.DataFrame:
                k = k.reset_index()
                k.pop("index")
                k.to_csv("Energiequellen/" + i[0] + ".csv", index=False, sep=";")
