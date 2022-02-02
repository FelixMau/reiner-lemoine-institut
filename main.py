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

import Aufgabe1bis5
import Aufgabe6

def main():
    df = Aufgabe1bis5.import_ajustments()
    df = Aufgabe1bis5.sort(df)
    df = Aufgabe1bis5.yes_to_value(df)
    df = Aufgabe1bis5.remove_nan_and_invalid(df)
    Aufgabe1bis5.split_dataframe_by_source_and_save(df)
    Aufgabe6.visualize()


if __name__ == '__main__':
    main()
