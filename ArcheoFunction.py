
import geopandas as gpd
import pandas as pd
from shapely.geometry import Point
import matplotlib.pyplot as plt
from cartopy.feature import ShapelyFeature
import cartopy.crs as ccrs
import matplotlib.patches as mpatches
import matplotlib.lines as mlines


plt.ion()  # make the plotting interactive
# generate matplotlib handles to create a legend of the features we put in our map.


def generate_handles(labels, colors, edge='k', alpha=1):
    """

    adding labels
    :param labels, colors, edge, alpha
    """
    lc = len(colors)  # get the length of the color list
    handles = []
    for i in range(len(labels)):
        handles.append(mpatches.Rectangle((0, 0), 1, 1, facecolor=colors[i % lc], edgecolor=edge, alpha=alpha))
    return handles
# create a scale bar of length 20 km in the upper right corner of the map
# adapted this question: https://stackoverflow.com/q/32333870
# answered by SO user Siyh: https://stackoverflow.com/a/35705477
def scale_bar(ax, location=(0.92, 0.95)):
    """

    define a scale to plot
    :param ax, location

    """
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

# load the outline of Lebanon and its governorate
    outline = gpd.read_file('C://Assig-egm722//ArcheoFunction//Vector_data//LBN_adm0.shp')
    governorate = gpd.read_file('C://Assig-egm722//ArcheoFunction//Vector_data//LBN_adm1.shp')
    print(outline.head())
    print(governorate.head())
    print(data.head())
    myFig = plt.figure(figsize=(10, 10))  # create a figure of size 10x10 (representing the page size in inches)
    myCRS = ccrs.UTM(37)  # create a Universal Transverse Mercator reference system to transform our data.
    # be sure to fill in XX above with the correct number for the area we're working in.
    ax = plt.axes(projection=ccrs.Mercator())  # finally, create an axes object in the figure, using a Mercator

    # first, we just add the outline and governorate of Lebanon using cartopy's ShapelyFeature
    outline_feature = ShapelyFeature(outline['geometry'], myCRS, edgecolor='k', facecolor='w')
    xmin, ymin, xmax, ymax = outline.total_bounds
    governorate_feature = ShapelyFeature(governorate['geometry'], myCRS, edgecolor='k', facecolor='w')
    xmin, ymin, xmax, ymax = governorate.total_bounds
    ax.add_feature(outline_feature)  # add the features we've created to the map.
    ax.add_feature(governorate_feature)
    # using the boundary of the shapefile features, zoom the map to our area of interest
    ax.set_extent([xmin, xmax, ymin, ymax], crs=myCRS)  # because total_bounds gives output as xmin, ymin, xmax, ymax,
    site = gpd.read_file('C://Assig-egm722//ArcheoFunction//Sites_Location//Sites_1.shp')
    print(site.head())
    site_itm = site.to_crs(epsg=22770)
    print(site_itm.head())
    site_feature = ShapelyFeature(site['geometry'], myCRS, edgecolor='k', facecolor='w')
    xmin, ymin, xmax, ymax = site.total_bounds
    # add the features we've created to the map.
    ax.add_feature(site_feature)
    site_handle = ax.plot(site.geometry.x, site.geometry.y, 's', color='0.5', ms=6, transform=myCRS)

    nice_names = [name.title() for name in site]
    handles = site_handles
    labels = nice_names + ['site']
    leg = ax.legend(handles, labels, title='Legend', title_fontsize=14,
                    fontsize=12, loc='upper left', frameon=True, framealpha=1)

    for i, row in site.iterrows():
        x, y = row.geometry.x, row.geometry.y  # get the x,y location for each town
        plt.text(x, y, row['NAME'].title(), fontsize=8, transform=myCRS)  # use plt.text to place a label at x,y
    myFig.savefig('map.png', bbox_inches='tight', dpi=300)
    outline_itm = outline.to_crs(epsg=22770)
    governorate_itm = governorate.to_crs(epsg=22770)

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

#loading database
df = pd.read_excel('C://Assig-egm722//ArcheoFunction//DataBase_1//Data.xlsx', header=1,skiprows=1)
# converting an excel sheet into shapefile
df.head()
