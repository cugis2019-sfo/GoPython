import pandas as pd
import plotly
import plotly.graph_objs as go 
from plotly.offline import plot

# we read the data into a dataset or data frame called df
df = pd.read_excel("GISdata.xlsx", sheet_name = "cancercases")
print(df)

# we use the bar graph option of the graph_objs function from the plotly library 
cancercases = go.Bar(x=df["CancerType"], y=df["Number"],
                     
                #we add color to the graph using the jet scale
                marker = {"color": df["Number"], "colorscale" : "Portland"}
                 )

#Greens", "YlOrRd", "Bluered", "RdBu", "Reds", "Blues", "Picnic", "Rainbow", "Portland", "Jet", "Hot",
       #"Blackbody", "Earth", "Electric", "Viridis", "Cividis

# we use the layout option of the graph_objs function from the plotly library 
titles = go.Layout(
                    #define title of the graph
                    title = "Number of Cancer cases by types within women",
                    
                    #define title for x-axis
                    xaxis=go.layout.XAxis(
                            title=go.layout.xaxis.Title(
                            text="Types of Cancer",
                        )
                    ),
                    
                    #define title for y-axis
                    yaxis=go.layout.YAxis(
                            title=go.layout.yaxis.Title(
                            text="Numbers of Cases",
                            )
                      )
                    )

# we use figure option of the graph_objs function from the plotly library 
fig = go.Figure(data=[cancercases], layout = titles)

# we call the plot function from the plotly.offline library
plot(fig)

