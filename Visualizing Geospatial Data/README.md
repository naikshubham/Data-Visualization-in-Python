# Visualizaing Geospatial Data
- One of the most important tasks of a data scientist is to understand the relationships between their data's physical location and their geographical context
- Plot geospatial points as scatterlots
- Plot geometrics using `geopandas`
- Construct a `GeoDataFrame` from a pandas `DataFrame`
- Spatially join datasets
- Add a street map to our plots
- When and how to create a choropleth

#### Latitude and Longitude
- Longitude are the lines that run north to south, and latitude are the lines that run east to west. We use negative values for latitude south of the Equator and for longitude west of the Greenwich Meridian.
- Style elements like color and marker type helps make our plots visually appealing.
- Longitude is always plotted along the horizontal axis, while latitude is plotted along the vertical axis.

```python
plt.scatter(schools.Longitude,
            schools.Latitude,
            c = 'darkgreen',
            marker = 'p')
plt.show()

plt.scatter(schools.Longitude, schools.Latitude, c='dargreen', marker='p')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.title('Nashville Public Schools')
plt.grid()
plt.show()
```

#### Extracting longitude and latitude
- Datasets won't always have latitude and longitude neatly separated. In this case, we can just pull each value from the location tuple and store it in a new column.

```python
bus_stops['lat'] = [loc[0] for loc in bus_stops.Location]
bus_stops['lng'] = [loc[1] for loc in bus_stops.Location]
bus_stops.head()
```

#### Extracting lng and lat with regex
`Location : MCC - BAY 11\nNashville, TN\n(36.16659, -86.78199)`
- Some times we need to use regex to parse long and lat.

```python
lat_lng_pattern = re.compile(r'\((.*),\s*(.*)\)', flags=re.MULTILINE)

def extract_lat_lng(address):
    try:
        lat_lng_match = lat_lng_pattern.search(address)
        lat = float(lat_lng_match.group(1))
        lng = float(lat_lng_match.group(2))
        return (lat, lng)
    except:
        return (np.NaN, np.NaN)
        
lat_lngs = [extract_lat_lng(location) for location in bus_stops2.loc[:, 'Location']]
bus_stops2['lat'] = [lat for lat, lng in lat_lngs]
bus_stops2['lng'] = [lng for lat, lng in lat_lngs]
```

### Geometries and shapefiles

#### Shapefiles
- We can visualize points data on a map more effectively if we plot meaningful regions to give context to the points. One way to do this is with a shapefile.
- Shapefiles stores a special type of a data known as geometry, that is used to draw a map.
- There are 3 basic kinds of geometry: point (a single longitude/latitude pair), line (two or more lat/long pairs that can be connected to form a continuos segment)  and polygon(made up of 3 or more long/lat pairs that are joined in a specified order to create an enclosed region).

#### Shapefile components
- A shape file can be recognized by its `.shp` extension. The `.shp` file must be in a directory along with `.shx` file and `.dbf` file in order to work.
- These files needs to have a same filename prefix.

```python
my_map.shp (contains the geometry)
my_map.dbf (holds attributes for each geometry)
my_map.shx (links the attributes to the geometry)
```

### Geopandas
- The geopandas package provides a library for working with geospatial data.
- The shape file consists of two polygons - one for the general services district and another for the urban services district.

```python
import geopandas as gpd

geo_df = gpd.read_file('My_Map_Files/my_map.shp')
geo_df.head()
```

#### Viewing a geometry

```python
service_district.loc[0, 'geometry']
```

- Geometry object from the first row in the service districts GeoDataFrame.
- The `loc[]` accessor locates a specific data point when we pass the row name and column name to it, and `iloc[]` accessor locates a specific data point by using the given row index and column index.
- We can print the geometry by wrapping the call to loc or iloc with the print function. Printing the geometry gives us all the long/lat pairs that define the polygon, with each pair separated by comma.

#### Plotting a GeoDataFrame
- Plotting a GeoDataFrame is as easy as calling df.plot()
- We can make it more informative by coloring each region according to some column in the geodataframe.

```python
school_districts.plot()
plt.show()

school_districts.plot(column = 'district', legend=True)
plt.show()
```

### Scatterplots over polygons
- Combine scatterplot of chicken locations with polygons showing service districts in order to understand where the chickens are w.r.t service district boundaries.

#### Combining scatterplots and polygons
- Maps are created from visual layers, with each layer adding reference points and other cues that enhance the ability to get meaning from the map.

#### Scatterplots over ploygons

```python
school_districts.plot(column='district', legend=True, cmap='Set2')
plt.scatter(schools.lng, schools.lat, marker = 'p', c = 'darkgreen')
plt.title('NashVille schools and School districts')
plt.show()
```

### GeoJSON and plotting with geopandas
- GeoJSON is a newer format for geospatial data. Unlike shapefiles, GeoJSON is a single file, making it easier to work with.

#### Neighbourhoods GeoJSON
- The raw GeoJSON file is easier to interpret than a shape file.
- The geometry is a MultiPolygon. GeoJSON supports multipart geometries, including MultiPoint, MultiLineString and MultiPolygon.

```python
neighborhoods = gpd.read_file('./data/neighborhood_boundaries.geojson')
neighborhoods.head(1)
```

- Reading in the geojson file with geopandas, we can see that the properties of he geojson file(name and geometry) become the columns of the GeoDataFrame.

#### Geopandas dependencies

<img src="data/geopandas.JPG" width="350" title="Geopandas">

- Vector data is type of geospatial data made up of points, lines and polygons. Raster data on the other hand can be thought of as a grid. Topographical maps are example of raster graphics.
- Geopandas makes it easy to work with geospatial data in python. Two supporting libraries that help with this are FIONA and GDAL.
- FIONA provides a bridge from the Open GIS Simple Features Reference(called OGR for short) to python and geopandas. We can leverage the work that OGR and GDAL - the Geospatial Data Abstraction Library - do to translate raster and vector geospatial data formats.

#### Colormaps
- Choosing the right color when plotting our map requires a bit of thought. Matplotlib provides around 100 different colormaps.

#### Plotting with color
- We can also style plot legends by passing a dict of keywords to geopandas.

```python
council_dists.plot(column='district',
                    cmap='Set3',
                    legend=True)
plt.title('Council Districts')
plt.show()

leg_kwds={'title':'District Number',
          'loc':'upper_left',
          'bbox_to_anchor': (1, 1.03),
          'ncol':3}
council_dists.plot(column='district',
                    cmap = 'Set3',
                    legend=True,
                    legend_kwds=leg_kwds)
plt.title('Council Districts')
plt.show()
```

### Projections and Coordinate Reference Systems
- We can construct a GeoDataFrame from a df, as long as we have the required pieces in place: a geometryy column and a cordinate reference system or CRS.

#### Projections
- Before we talk about CRS, its helpful to talk abt projections. Map projections are necessary for projecting the earth in 2-dimensional space.
- The most common projection is the mercator projection. A variation of the mercator projection known as WGS84 (which is short for the world geodetic system 1984 standard) is the projection used in most mapping apps and by the Global Positioning System or GPS.

#### Coordinate Reference Systems
- Setting a coordinate reference systems for a GeoDataFrame tells geopandas how to interpret the longitude and latitude coordinates. Distance units are also dependent on the CRS being used.
- The most common coordinate reference systems are EPSG:4326 and RPSg:3857, both of which use the WGS84 projection. EPSG stands for European Petroleum Survey Group, the entity that developed these systems.
- EPSG:4326 is used with applications like Google Earth, while EPSG:3857 is used in most map applications.
- **Geometry** is a special data structure, and is a required component of GeoDataFrames.

```python
# create a point geometry column

from shapely.geometry import Point
schools['geometry'] = schools.apply(lambda x:Point((x.Longitude, x.Latitude)), axis=1)
schools.head(3)
```

- To create a geometry column, first build a representation of the geometry and then use a specific constructor from the geometry module in the shapely package.
- Shapely is a python package that provides methods for creating and working with points, lines and polygons.
- We can create a Point geometry from Longitude and Latitude, by applying a lambda function that combines longitude and latitude to create a tuple and constructs a Point geometry from that tuple.
- Now the schools data has a geometry column and is ready to be used to build a GeoDataFrame.

#### Creating a GeoDataFrame from a DataFrame
- To construct a GeoDataFrame from the schools DataFrame, use the GeoDataFrame constructor, passing it - the schools DataFrame, the crs to use, and the geometry to use.
- Below we have created an object called `school_crs`, and set it to use the `epsg:4326` Coordinate Reference System.
- We specify the geometry column we just created as the new GeoDataFrame's geometry.
- schools_geo is identical to schools data. Only the datatype has changed from a DataFrame to a GeoDataFrame.

```python
import geopandas as pd

schools_crs = {'init':'epsg:4326'}
schools_geo = gpd.DataFrame(schools,
                            crs = schools_crs,
                            geometry = schools.geometry)
```

#### Changing from one CRS to another
- Notice that the schools `geo_geometry` uses `degrees` to measure distance from the reference points: the Prime Meridian and the Equator.
- We can convert the **geometry to measure distance in meters**, using the `to_crs()` method.
- Here we convert the geometry column of schools_geo to **EPSG:3857**. The resulting measurements are in meters.
- The original Long and Lat columns remain in decimal degress units. **`to_crs()`** only changes the geometry column.
 
### Spatial Joins

#### The .sjoin() op argument
- Geopandas has a spatial join method called **`sjoin()`**. sjoin() takes an argument - op, short for operation, which specifies the type of spatial join.
- op is one of 3 types : **intersects, contains, or within**

```python
import geopandas as gpd

gpd.sjoin(blue_region_gdf, black_point_gdf, op = <opeartion>)
```

#### Using .sjoin(), op = 'intersects'
- `intersects` returns all observations where the blue region intersects points.
- `contains` returns observations where the blue_region completely contains points.
- `within` there are no cases where the blue region is within a point.

```python
gpd.sjoin(blue_region_gdf, black_point_gdf, op='intersects')
gpd.sjoin(blue_region_gdf, black_point_gdf, op='contains')
gpd.sjoin(blue_region_gdf, black_point_gdf, op='within')
```

#### The .sjoin() op argument - within

```python
# find council districts within school districts

within_gdf = gpd.sjoin(council_districts, school_districts, op='within')
print("Council districts within school districts:", within_gdf.shape[0])
```

#### The .sjoin() op argument - contains

```python
# find school districts that contain council districts

contains_gdf = pd.sjoin(school_districts, council_districts, op='contains')
print("school districts contain council districts:", contains_gdf.shape[0])
```

#### The .sjoin() op argument - intersects

```python
# find council districts that intersects with school districts

intersects_gdf = gpd.sjoin(council_districts, school_districts, op='intersects')
print("Council districts intersects school districts:", intersect.shape[0])
```

```python
within_gdf.district_left = council_district
within_gdf.district_right = school_district
within_gdf[['council_district', 'school_district']].
            groupby('school_district').agg('count').sort_values('council_district'), ascending=False)
```

### GeoSeries attributes and methods

#### Shapely attributes and methods
- We can think of a GeoSeries as the geometry column of a GeoDataFrame. Geopandas inherits a number of useful methods and attributes from the Shapely package.

```python
# the geometry column in a GeoSeries
type(school_districts.geometry)
```

- **Geoseries.area** : The area attribute returns the calculated area of a geometry.
- **GeoSeries.centroid** : The centroid attribute returns the center point of a geometry.
- **GeoSeries.distance** : The distance method gives the minimum distance from a geometry to a location specified using the `other` argument.

#### GeoSeries.area
- returns the area of each geometry in a GeoSeries. The units for area depend on the distance units for the coordinate reference system that the GeoSeries is using.

```python
# area of first polygon in districts
print(districts.geometry[0].area)

# calculate area of each school district
district_area = school_districts.geometry.area
# print the area and crs used
print(district_area.sort_values(ascending=False))
print(school_districts.crs)
```

- We can change the CRS to one that uses meters for distance and then convert meters squared to kilometers squared.

```python
# create a copy of school_districts that uses EPSG:3857
school_districts_3857 = school_districts.to_crs(epsg=3857)

# define a variable for m**2 and km**2 and get area in km squared
sqm_to_sqkm = 10**6
district_area_km = school_districts_3857.geometry.area / sqkm_to_sqm
print(district_area_km.sort_values(ascending=False))
print(school_districts_3857.crs)
```

#### GeoSeries.centroid

```python
districts.geometry.centroid[0]
```

#### GeoSeries.distance()
- GeoSeries.distance(other) - returns minimum distance to other

```python
# distance from red_pt to centroid
cen = districts.geometry.centroid[0]
print(red_pt.distance(other=cen)
```

#### Distance between two points

```python
district_one = school_districts.loc[school_districts.district == '1']

# create geometry in schools
schools['geometry'] = schools.apply(lambda x:Point((x.lng, x.lat)), axis=1)

# construct schools GeoDataFrame
schools_geo = gpd.GeoDataFrame(schools, crs=district_one.crs, geometry=schools.geometry)

# spatial join schools within dist 1
schools_in_dist1 = gpd.sjoin(schools_geo, district_one, op='within')
```

- Calculate the distance between each school and the center_point of school_district_one.

```python
import pprint

distances = {}
for row in schools_in_dist1.iterrows():
    vals = row[1]
    key = vals['name']
    ctr = vals['center']
    distances[key] = vals['geometry'].distance(ctr)
pprint.pprint(distances)
```

### Street maps with folium
- Folium is a python package for interactive maps built upon Leaflet.js

#### folium.Map()
- To create a map with folium, we pass our starting coordinate pair as `location` to the folium Map constructor to create a map object. Use `display()` to show the map.
- `display` is part of ipython notebooks.
- Below we have used the latitude and longitude that describe the point location of the Eiffel Tower in Paris, France.
- **Folium always wants coordinates as an array, with the latitude first.**

```python
import folium

# construct a map centered at the Eiffel Tower
eiffel_tower = folium.Map(location=[48.8583736, 2.2922926])

# display the map
display(eiffel_tower)
```

#### Setting the zoom level
- We can set an initial zoom level when we construct a map with the zoom_start argument. The higher the number, the closer the map will zoom into the starting coordinate pair.
- Here we have set zoom_start to 12, which will get us nice and close.

```python
import folium

# construct a map centered at the Eiffel Tower
eiffel_tower = folium.Map(location=[48.8583736, 2.2922926], zoom_start = 12)

# display the map
display(eiffel_tower)
```

#### Folium location from centroid
- We want to use the point in the center column of district_one as the starting coordinate of a folium map called district_one map.
- Remember that we need to reverse the order of the coordinate pair for folium so that latitude is first. 
- The `center` column is a GeoSeries and the value stored in that column is a Point geometry. Will save that Point geometry to a variables called `center_point`.

```python
center_point = district_one.center[0]
type(center_point)

# reverse the order for folium location array
district_center = [center_point.y, center_point.x]

# print center point and district_center
print(center_point)
print(district_center)
```

- We'll use the district center array as the location for a folium map

#### Adding a polygon to a folium map
- Here, we create a map object called `district1_map` using `district_center` for the location.
- Next we pass the polygon for district_one to the folium GeoJson constructor in order to draw the shape of school district one.
- We use the `add_to()` method to add the polygon to the district_one map.

```python
# create a folium map centered on district 1
district1_map = folium.Map(location = district_center)

# add the outline of district one
folium.GeoJson(district_one.geometry).add_to(district1_map)

# display the resulting map
display(district1_map)
```




















































































































































































