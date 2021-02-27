
# Plotly

### Plotly and Plotly Figures
- Plotly graphs can be created with `plotly.express (px)`
- `plotly.graph_objects (go)` for more customization
- `plotly.figure_factory` for specific, advanced figures

### Plotly Figure
- has 3 main components
- `layout` : Dictionary controlling style of the figure
- `data` : list of disctionaries setting graph type and data itself
- data + type =  a trace. There are over 40 types! Can have multiple traces per graph.

### Univariate visualizations
- `plotly.express` : allows quick simple plots to be created by specifying its dataframe and its columns names as arguments
- `graph_objects` `go.X` methods (`go.Bar()`, `go.Scatter()`) allows more customization options but requires more code.
- Univariate plots displays only one variable. Some common univariate plots include `Bar charts, Histograms, Box plots, Density plots`

#### Bar charts with plotly.express
- Core elements are the dataframe containing data & columns for x&y axis.

```python
import plotly.express as px
weekly_temps = pd.DataFrame({'day':['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday'],
'temp':[28, 27, 25, 31, 32, 35, 36]})
fig = px.bar(data_frame=weekly_temps, x='day', y='temp')
fig.show()
```

#### Histograms
- Each column called bin represents a range of values that samples could have for a particular variable. The height of each bar is the count of samples that fall within that range.
- We can choose the no. of bins or have plotly choose the bins for us.
- `orientation` : To orient the plot vertically(v) or horizontally(h)
- `histfunc` : set the bin aggregation (eg. avg, min, max)

```python
fig = px.histogram(data_frame=penguins, x='Body Mass(g)', nbins=10)
fig.show()
```

#### Box plots
- summarizes a variable visually using quartile calculations
- `hover_data` : a list of column names to display an hover, useful to understand outliers.
- `points` : Further specify how to show outliers.

```python
fig = px.box(data_frame=penguins, y="Flipper Length (mm)")
fig.show()
```

### Customizing color
- 




