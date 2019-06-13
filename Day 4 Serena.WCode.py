import pandas
import plotly

# numbers don't always need quote

studentlist = [["Steve",32,"male"],["Lia",28,"female"],["Vin",45,"male"],["Katie",38,"female"]]
print(studentlist)

studentlistdf = pandas.DataFrame(studentlist, columns = ["name","age","gender"],index=["1","2","3","4"])
print(studentlistdf)


# graph our data 
# short form is call alias
dir(plotly)
from plotly.offline import plot
import plotly.graph_objs as go

agename = go.Bar(x=studentlistdf["name"], y=studentlistdf["age"])

plot([agename])