import pandas as pd 
import plotly.express as px 

df_trio = pd.read_csv("data/PFC_TRIO_cellcounts.csv")

fig = px.scatter_3d(df_trio, x="AP", y="ML", z="DV", color="color", opacity=0.5)
fig["layout"].update(width=1200, height=800, autosize=False)
fig.update_traces(marker_size=3)

fig.show()