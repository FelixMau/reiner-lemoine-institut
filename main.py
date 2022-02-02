import os
import pandas as pd

# Todo:
#    1. Importiere die mitgelieferte CSV-Datei in ein Pandas DataFrame, wobei du den Spaltennamen B in „Energiequelle“,
#       den Spaltennamen C in „Leistung in kW“ umbenennst und die Spalte A löschst. In der CSV-Datei entspricht jeder
#       Eintrag einer Erzeugungsanlage.
#    2. Sortiere das DataFrame nach den unterschiedlichen Energiequellen.
#    3. Definiere die Leistung der Einträge, in denen ein „Yes“ eingetragen ist, zu 600 kW.
#    4. Lösche die Einträge, in denen keine Leistung angegeben ist oder etwas anderes steht.
#    5. Speichere die unterschiedlichen Energiequellen jeweils in ein eigenes DataFrame.
#    6. Plotte die Leistung der Energiequelle „gas“ in Abhängigkeit von der Anzahl der Einträge als Graph
#       (z.B. als Balkendiagramm) und speichere sie als jpg/png-Grafik..

##################################################
# Aufgabe 1
with open(os.getcwd() + "/2022-02-02 Data Bewerbungsaufgabe.csv") as f:
    df = pd.read_csv(f, delimiter=";")
df = df.rename(columns={"generator:source": "Energiequelle", "generator:output": "Leistung in kW"})
df.pop("wkt_geom")

##################################################
# Aufgabe 2
df.sort_values(by=["Energiequelle"], inplace=True)

##################################################
# Aufgabe 3
df["Leistung in kW"] = df["Leistung in kW"].replace(to_replace="yes", value="600")

##################################################
# Aufgabe 4
# Remove Nan values:
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

##################################################
# Aufgabe 5
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
