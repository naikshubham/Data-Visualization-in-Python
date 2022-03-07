### Dash
- `dash` : main library
- `dash_core_compenents` : contains the different building blocks to create the app

#### The app layout


- `app = dash.Dash()` # create app object
- set app layout using app.layout, here a single graph. This is done with the dash core compenents `Graph` object, which takes a Plotly figure object and renders it in the app for us.
- figure = The plotly figure to render
- we can also give it and `id` which will be important later when we add interactivity to the dashboard
- Lastly, running the server

```python
if __name__ == '__main__':
    app.run_server(debug=True)
```

### Positioning Dash components
- Dash uses the submodule `dash_html_components` to harness HTML while writing python
- **`Div tags`** : important for structing websites. Can have many different-sized divs with different things inside
- Another tags are **`H tags`** which contain text for titles and are specified as **H1 (larger) to H6 (smaller)** 

#### Using Div and H tags
- Some html code with Overall div (everything inside)

```python
<div>
    <div style="background-color: red; width:250; height:250;"> # div with red background of size 250 by 250
    </div>
    <div style="background-color: lightblue; width:250; height:250;">
    <h1> This box </h1>
    <h2> Another Title </h2>
    </div>
</div>
```

<img src="imgs/div_tags.png" alt="a" width="200"/>

- The first div with a read background that is smaller in size than the screen. The second div with a blue background and the titles inside. This example demonstrates the power of div tags to nest and structure objects.
- Recreating exact example with dash


```python
import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()
app.layout = html.Div(children=[
    html.Div(style={'height':250, 'width':250, 'background-color':'red'}),
    html.Div(children=[
        html.H1("This box"),
        html.H2("Another Title")],
        style={'background-color':'lightblue'})
    ])
```

- HTML tags align to Dash `html.Div() = <div>` & `html.H1() = <h1>`. The overall div and the last div have a `children` argument
- The children argument is a list of objects to go inside. The second div doesn't need this, having no sub-elements. 
- We can put many Dash or HTML components inside a div, such as graph components.

#### Graphs in the layout
- Graphs can be added inside the `children` list of a `html.Div()`. To add a graph to our structure, place a `dcc.Graph()` object inside a children element of an HTML div object
- Create a bar chart of sales by country and create the Dash object

```python
bar_fig_country = px.bar(ecom_sales, x='Total Sales ($)', y='Country', color='Country', color_discrete_map={'United Kingdom':'lightblue', 'Germany':'orange'})
app = dash.Dash()
```

- Then create a layout and insert an H1 title as well as graph

```python
app.layout = html.Div(children=[
    html.H1("Sales Proportion by Country"),
    dcc.Graph(id='bar graph',
              figure= bar_fig_country)])
])
```

### HTML in Dash

#### Structuring tags
- Important structuring tags
- **`.Br()`** = New line break
- **`.Img()`** = Insert an image
- `.Ul()` , `.Ol()` & `.Li()` = Create lists. There is also `UL` for unordered list, like the bullet points 
- `Ol()` for ordered list (numbered - points)
- `.Li()` for each list element

#### Inserting a company logo

```python
app.layout = html.Div(children=[
    html.Img(src='www.website.com/logo.png'),
    html.H1("Our sales dashboard")
])
```

#### Text tags
- We can input and format text with Dash HTML functions. `.P()` or `.Span()` tags are used to insert the plain text. It accepts a children argument (list of text, `.P()` or `.Span()`)
- `.B()` = Bold, `.I()` = Italicize

- set up `span` object with a children argument to include text elements. We can put in strings that use string interpolation since we are writing in python


```python
app.layout = html.Div(children=[
    html.H1("Our Sales Dashboard"),
    html.Span(children=[
        html.H1("Our Sales Dashboard"),
        html.Span(children=[
            f"Prepared: {datetime.now().date()}",
            html.Br(),
            " by ", html.B("Jessie Parker, "),
            html.Br(),
            html.I("Data Scientist")
        ])
    ])
])
```

### CSS Basics in Dash

#### CSS on HTML elements
- CSS can be used on HTML element. Use the `style` property of a tag
- CSS statements in one big string separated by `;`, Statements are `property: value; property: value;`
- Each statement is like a dictionary in python, with the property to set and the value to give it

```python
<h1> Welcome to the website!</h1>
<h2> style="font-size:50px;color:red"> Enjoy your stay!</h2>
```

#### CSS in Dash
- Dash components have a style argument that accepts CSS as a dictionary

```python
app.layout = html.Div([
    html.H1("Welcome to the website!"),
    html.H2('Text', style={'font-size':'50px', 'color:red'})])
])
```

#### CSS for color
- CSS can be used to set the background color of an object ( `background-color` )
- The text color can be set using the color property. Both accepts strings e.g 'red' or RGB codes e.g 'rgb(0,0,255)' 
- The size of the element can be changed via the width and the height properties

```python
app.layout = html.Div([
    # add & resize the company logo
    html.Img(src=logo_link,
    style={'width':'250px', 'height':'250px'})
])
```

- We can also set the width and height of an element to be a percentage proportion of the parent element, rather than specifying exact pixel sizes.

```python
app.layout = html.Div([
    # add & resize the company logo
    html.Img(src=logo_link,
    style={'width':'50%', 'height':'50%'})
])
```


## Advanced CSS in Dash

#### A border on our app

```python
html.Div(dcc.Graph(figure=ecom_bar),
         style={'width':'500px',
                'height':'450px',
                'border':'5px dotted red'}
```

### CSS spacing
- To set the spacing of an HTML element
- Specify four numbers for each property(padding & margin)
- Clockwise will be top, right, bottom, left
- Alternatively: one number(will be applied to all sides)
- Alternatively: two numbers for top-bottom and left-right

### Centering with auto margin
- `margin : 100px auto`

### CSS for layout
- Elements not aligning? HTML elements can either be inline or block element
- **Inline render on the same line** : have no height or width (or box) properties
- Examples include <|strong|>, <|a|>, <|img|>
    
    
- **Block elements doesn't render side by side** : Block stack on top of one another as they include a line break
- Can't have more than one side-by-side
- Examples include <|h1|> , <|div|>


- There is an intermediatory option of **inline block**
- Can set height/width/box properties
- Can be side-by-side

### Example of Inline-block elements
- We can create some divs that are block and inline-block

```python
<div style='width:50px;height:50px;background-color:blue'></div>
<div style='width:50px;height:50px;background-color:red;display:inline-block'></div>
<div style='width:50px;height:50px;background-color:green;display:inline-block'></div>
```



```python
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
logo_link = 'https://assets.datacamp.com/production/repositories/5893/datasets/fdbe0accd2581a0c505dab4b29ebb66cf72a1803/e-comlogo.png'
ecom_sales = pd.read_csv('/usr/local/share/datasets/ecom_sales.csv')
ecom_line = ecom_sales.groupby('Year-Month')['OrderValue'].agg('sum').reset_index(name='TotalSales')
line_fig = px.line(data_frame=ecom_line, x='Year-Month', y='TotalSales',title='Total Sales by Month')
line_fig.update_layout({'paper_bgcolor':'rgb(224, 255, 252)' }) 
ecom_bar = ecom_sales.groupby('Country')['OrderValue'].agg('sum').reset_index(name='TotalSales')
bar_fig = px.bar(data_frame=ecom_bar, x='TotalSales', y='Country', orientation='h',title='Total Sales by Country')
bar_fig.update_layout({'yaxis':{'dtick':1, 'categoryorder':'total ascending'}, 'paper_bgcolor':'rgb(224, 255, 252)'}) 

app = dash.Dash(__name__)

app.layout = html.Div(children=[
    html.Div(children=[
      html.Img(src=logo_link, 
               # Place the logo side-by-side the H1 with required margin
               style={'display':'inline-block', 'margin':'25px'}),
      html.H1(children=["Sales Figures"],
              # Make the H1 side-by-side with the logos
              style={'display':'inline-block'}), 
      html.Img(src=logo_link,
               # Place the logo side-by-side the H1 with required margin
               style={'display':'inline-block', 'margin':'25px'})]),
    html.Div(
        dcc.Graph(figure=line_fig), 
        # Ensure graphs are correct size, side-by-side with required margin
        style={'width':'500px', 'display':'inline-block', 'margin':'5px'}), 
    html.Div(
      	dcc.Graph(figure=bar_fig),
        # Ensure graphs are correct size, side-by-side with required margin
    	style={'width':'350px', 'display':'inline-block', 'margin':'5px' }), 
    html.H3(f"The largest order quantity was {ecom_sales.Quantity.max()}")
    ],style={'text-align':'center', 'font-size':22, 'background-color':'rgb(224, 255, 252)'})

if __name__ == '__main__':
    app.run_server(debug=True)
```

### Controlling object layout

```python
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
ecom_sales = pd.read_csv('/usr/local/share/datasets/ecom_sales.csv')
logo_link = 'https://assets.datacamp.com/production/repositories/5893/datasets/fdbe0accd2581a0c505dab4b29ebb66cf72a1803/e-comlogo.png'
ecom_bar_major_cat = ecom_sales.groupby('Major Category')['OrderValue'].agg('sum').reset_index(name='Total Sales ($)')
ecom_bar_minor_cat = ecom_sales.groupby('Minor Category')['OrderValue'].agg('sum').reset_index(name='Total Sales ($)')
bar_fig_major_cat = px.bar(ecom_bar_major_cat, x='Total Sales ($)', y='Major Category', color='Major Category', color_discrete_map={'Clothes':'blue','Kitchen':'red','Garden':'green','Household':'yellow'})
bar_fig_minor_cat = px.bar(ecom_bar_minor_cat, x='Total Sales ($)', y='Minor Category')                       

app = dash.Dash(__name__)

app.layout = html.Div([
  html.Img(src=logo_link,
        # Add margin to the logo
        style={'margin':'30px 0px 0px 0px'}),
  html.H1("Sales breakdowns"),
  html.Div(children=[
      dcc.Graph(
        # Style the graphs to appear side-by-side
        figure=bar_fig_major_cat,
        style={'display':'inline-block'}),
      dcc.Graph(
        figure=bar_fig_minor_cat,
        style={'display':'inline-block'}),
  ]),
  html.H2("Major Category",
        # Style the titles to appear side-by-side with a 2 pixel border
        style={'display':'inline-block', 'border':'2px solid black',
        # Style the titles to have the correct spacings
               'padding':'10px', 'margin':'10px 220px'}),
  html.H2("Minor Category",
        # Style the titles to appear side-by-side with a 2 pixel border
        style={'display':'inline-block', 'border':'2px solid black',
        # Style the titles to have the correct spacings
               'padding':'10px', 'margin':'10px 220px'}),
  
  ], style={'text-align':'center', 'font-size':22})

if __name__ == '__main__':
    app.run_server(debug=True)
```

### Callbacks in Dash

#### What are callbacks?
- Functionality triggered by interaction
- A user interacts with an element -> A Python function is triggered --> something is changed
- This allows us to create interactive user expriences within our app


- Start with the `decorator` function 
- Uses `from dash.dependencies import Input, Output`
- Inside the decorator there are 2 components the Inputs & Outputs.
- **Output** defines which component will be changed using the return value of the triggered function. (where to send the function return)
- Specifically the `component_id` property identifies the component to update. And the `component_property` defines excatly what will be updated on that component.
- **Input** is what triggers the callback. `component_id` is similar & `component_property` is what will be taken from the triggering component to send to the triggered function, placed immediately below the decorator.

```python
@app.callback(
    Output(component_id='my_plot',
           component_property='figure'),
    Input(component_id='my_input',
          component_property='value')    
)
def some_function(data):
    # subset data
    # recreate figure
    return fig
```

### Dropdowns in Dash

```python
dcc.Dropdown(id='title_dd',
             options=[{'label':'Title 1',
                       'value':'Title 1'},
                      {'label':'Title 2',
                       'value':'Title 2'}])
```

- List of label-value dictionaries
- label is what the user sees and value is what is sent to the callbacks


### A dropdown callback
- Example to change the title
- Note that `id='title_dd'` is vital to link to the callback function
- We add the Graph we wish to change to the app layout

```python
app.layout = html.Div(children=[
    dcc.Dropdown(id='title_dd',
                 options=[{'label':'Title 1',
                           'value':'Title 1'},
                          {'label':'Title 2',
                           'value':'Title 2'}]),
    dcc.Graph(id='my_graph')])
@app.callback(
    Output(component_id='my_graph',
           component_property='figure'),
    Input(component_id='title_dd',
          component_property='value')
)

def update_plot(selection):
    title="None Selected"
    if selection:
        title = selection
    bar_fig = px.bar(
        data_frame=ecom_sales,
        title=f"{title}",
        x="Total Sales ($)", y='Country')
    return bar_fig
```



### Dropdown as a filter

```python
#@app.callback()
def update_plot(input_country):
    input_country = 'All Countries'
    sales = ecom_sales.copy(deep=True)
    if input_country:
        sales = sales[sales['Country'] == input_country]
    bar_fig = px.bar(
        data_frame=sales, title=f"Sales in {input_country}",
        x="Total Sales ($)", y='Country')
    return bar_fig
```


```python

```
