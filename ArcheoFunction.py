
import geopandas as gpd
import pandas as pd
from shapely.geometry import Point
import matplotlib.pyplot as plt
from cartopy.feature import ShapelyFeature
import cartopy.crs as ccrs
import matplotlib.patches as mpatches
import matplotlib.lines as mlines

plt.ion() # make the plotting interactive

# generate matplotlib handles to create a legend of the features we put in our map.
def generate_handles(labels, colors, edge='k', alpha=1):
    lc = len(colors)  # get the length of the color list
    handles = []
    for i in range(len(labels)):
        handles.append(mpatches.Rectangle((0, 0), 1, 1, facecolor=colors[i % lc], edgecolor=edge, alpha=alpha))
    return handles

# create a scale bar of length 20 km in the upper right corner of the map
# adapted this question: https://stackoverflow.com/q/32333870
# answered by SO user Siyh: https://stackoverflow.com/a/35705477
def scale_bar(ax, location=(0.92, 0.95)):
    llx0, llx1, lly0, lly1 = ax.get_extent(ccrs.PlateCarree())
    sbllx = (llx1 + llx0) / 2
    sblly = lly0 + (lly1 - lly0) * location[1]

    tmc = ccrs.TransverseMercator(sbllx, sblly)
    x0, x1, y0, y1 = ax.get_extent(tmc)
    sbx = x0 + (x1 - x0) * location[0]
    sby = y0 + (y1 - y0) * location[1]

    plt.plot([sbx, sbx - 20000], [sby, sby], color='k', linewidth=9, transform=tmc)
    plt.plot([sbx, sbx - 10000], [sby, sby], color='k', linewidth=6, transform=tmc)
    plt.plot([sbx-10000, sbx - 20000], [sby, sby], color='w', linewidth=6, transform=tmc)

    plt.text(sbx, sby-4500, '20 km', transform=tmc, fontsize=8)
    plt.text(sbx-12500, sby-4500, '10 km', transform=tmc, fontsize=8)
    plt.text(sbx-24500, sby-4500, '0 km', transform=tmc, fontsize=8)
def archeofunction():
# load the outline of Northern Ireland for a backdrop
    outline = gpd.read_file('C://Assig-egm722//ArcheoFunction//Vector_data//LBN_adm0.shp')
    governorate = gpd.read_file('C://Assig-egm722//ArcheoFunction//Vector_data//LBN_adm1.shp')
    #loading data
df = pd.read_excel('C://Assig-egm722//ArcheoFunction//DataBase_1//Data.xlsx', header=1,
                   skiprows=1)  # converting an excel sheet into shapefile
df.head()
print(outline.head())
print(governorate.head())
print(data.head())

    #create a Universal Transverse Mercator reference system to transform our data
myCRS = crs.UTM(37)
outline_itm = outline.to_crs(epsg=22770)
governorate_itm = governorate.to_crs(epsg=22770)
ax = plt.axes(projection=ccrs.Mercator())  #create an axes object in the figure, using a Mercator
myFig = plt.figure(figsize=(10, 10))  #create a figure of size 10x10 (representing the page size in inches)

    #insert sites
Anfeh = Point(750794.00, 3805582.00)
Tell_arqa = Point(228936.00, 3824965.00)
Roman_temple = Point(229660.32, 3810573.97)
Theater = Point(745098.00, 3793746.00)
Historical_church = Point(744947.00, 3796531.00)
print(Anfeh)
print(Tell_arqa)
print(Theater)
print(Historical_church)
print(Roman_temple)

    # adding buffer zone for sites
Anfeh_buffer = Anfeh.buffer(570)
Tell_arqa_buffer = Tell_arqa.buffer(344)
Roman_temple_buffer = Roman_temple.buffer(685)
Theater_buffer = Theater.buffer(97)
Historical_church_buffer = Historical_church.buffer(1624)

print(type(Anfeh_buffer))
print(type(Tell_arqa_buffer))
print(type(Roman_temple_buffer))
print(type(Theater_buffer))
print(type(Historical_church_buffer))
    

