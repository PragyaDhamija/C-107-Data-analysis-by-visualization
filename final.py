import pandas as pd 
import plotly.graph_objects as pgo

df = pd.read_csv("data.csv")

#df.loc will help us filter out all the rows with the given student id
studentDF = df.loc[ df["student_id"] == "TRL_zny" ]
print(studentDF.groupby("level")["attempt"].mean())
fig = pgo.Figure(pgo.Bar(
    x = studentDF.groupby("level")["attempt"].mean(),
    y = ["Level 1", "Level 2", "Level 3", "Level 4"],
    orientation = "h"
))
fig.show()