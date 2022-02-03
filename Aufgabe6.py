import os

import pandas as pd
import plotly_express as px


def visualize():
    for i in os.listdir("Energiequellen"):
        with open("Energiequellen/" + i) as f:
            df = pd.read_csv(f, delimiter=";")
        print(df["Energiequelle"])
        fig = px.histogram(df, x='Leistung in kW',
                           # y="Anzahl",
                           barmode="group",
                           title="Anzahl der Einträge von " + df["Energiequelle"][0],
                           text_auto="0.2s",

                           )
        fig.update_yaxes(title={"text": "Anzahl der Einträge"})
        if not os.path.exists("images"):
            os.mkdir("images")
        fig.write_image("images/" + df["Energiequelle"][0] + ".jpeg")
        fig.show()
