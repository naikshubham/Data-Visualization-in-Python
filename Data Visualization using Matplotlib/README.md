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

