## Data-Visualization-in-using-Matplotlib

### pyplot interface
- The subplots command, when called without any inputs, creates two different objects:a Figure object and Axes object.
- Figure - is the actual plot, and Axes - the canvas on which the plot is drawn.

```python
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
plt.show()
```

#### Adding data to axes

```python
ax.plot(seattle_weather['MONTH'], seattle_weather['MLY-TAVG-NORMAL'])
plt.show()
```

- The plot command is the method of axes object.

### Customizing data appearance
- Data appears to be continuos, but it was actually measured in monthly intervals.A way to indicate this would be to add markers to the plot that show us where the data exists and which parts are just lines that connect between the data points.

#### Adding markers , setting linestyle, choosing color

```python
ax.plot(seattle_weather['MONTH'], seattle_weather['MLY-PRCP-NORMAL'], marker='o', linestyle="--", color="r")
plt.show()
```

#### Eliminating the line
- Pass argument `None` to `linestyle`.

#### Customizing the axes labels

```python
ax.set_xlabel("Time (months)")
ax.set_ylabel("Avg temp")
ax.set_title("Plot")
plt.show()
```

### Small multiples : subplots
- Rows and columns
- ax becomes array of axis object with shape (rows, cols)

```python
fig, ax = plt.subplots(3, 2)
plt.show()
```

#### Subplots with data

```python
fig, ax = plt.subplots(2, 1)
ax[0].plot(seattle_weather['MONTH'], seattle_weather['MLY-PRCP-NORMAL'], marker='o', linestyle="--", color="r")
ax[0].plot(seattle_weather['MONTH'], seattle_weather['MLY-PRCP-25PCTL'], marker='o', linestyle="--", color="r")
ax[0].plot(seattle_weather['MONTH'], seattle_weather['MLY-PRCP-75PCTL'], marker='o', linestyle="--", color="r")

ax[1].plot(austin_weather['MONTH'], austin_weather['MLY-PRCP-NORMAL'], marker='o', linestyle="--", color="r")
ax[1].plot(austin_weather['MONTH'], austin_weather['MLY-PRCP-25PCTL'], marker='o', linestyle="--", color="r")
ax[1].plot(austin_weather['MONTH'], austin_weather['MLY-PRCP-75PCTL'], marker='o', linestyle="--", color="r")

ax[1].set_xlabel("Time (months)")

ax[0].set_ylabel("Precipitation (inches)")
ax[1].set_ylabel("Precipitation (inches)")
plt.show()
```
- The range of yaxis in 2 plots are not exactly the same. This is because the highest and lowest values in the two datasets are not identical.

#### Sharing the y-axis range
- To make sure that all the subplots have the same range of y-axis values, we initialize the figure and its subplots with the key-word argument `sharey=True`.
- This means that both subplots will have the same range of y-axis values, based on the data from both datasets.














