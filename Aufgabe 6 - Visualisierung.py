import pandas as pd
import os
import numpy as np
import plotly_express as px


for i in os.listdir("Energiequellen"):
    with open("Energiequellen/"+i) as f:
        df = pd.read_csv(f, delimiter=";")
    print(df["Energiequelle"])
    fig = px.histogram(df, x='Leistung in kW',
                       #y="Anzahl",
                       barmode="group",
                       title="Anzahl der Einträge von "+df["Energiequelle"][0],
                       text_auto="0.2s",

                       )
    fig.update_yaxes(title={"text":"Anzahl der Einträge"})
    fig.to_image(format="jpg")
    fig.show()
