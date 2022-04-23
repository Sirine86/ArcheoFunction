import geopandas as gpd
import matplotlib.lines as mlines
import cartopy.crs as ccrs
import matplotlib.patches as mpatches
from shapely.geometry import Point
import sys
print(sys.version) ## define system version of python
plt.ion() # make the plotting interactive

# generate matplotlib handles to create a legend of the features we put in our map.
def generate_handles(labels, colors, edge='k', alpha=1):
    """
    generate handles labels for map
    :param labels, colors, edge, alpha
    return handles label for map
    """
    lc = len(colors)  # get the length of the color list
    handles = []
    for i in range(len(labels)):
        handles.append(mpatches.Rectangle((0, 0), 1, 1, facecolor=colors[i % lc], edgecolor=edge, alpha=alpha))
    return handles

def scale_bar(ax, location=(0.92, 0.95)):
    """
    scale-bar for map
    :param ax, location
    return map
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
    outline = gpd.read_file('C://My DaTa//outline_leb//LBN_adm0.shp')
def archeofunction(condition):
    #load data
    governorate = gpd.read_file('C://My DaTa//Governorate_leb//LBN_adm1.shp')
    data = gpd.read_file('C://Assig-egm722//DB//Data')
    myCRS = ccrs.UTM(22770) #create a Universal Transverse Mercator reference system to transform our data.
    print(outline.head())
    print(governorate.head())
    print(data.head())
    outline_itm = outline.to_crs(epsg=22770)
    governorate_itm = governorate.to_crs(epsg=22770)
    myFig = plt.figure(figsize=(10, 10))  #create a figure of size 10x10 (representing the page size in inches)
    ax = plt.axes(projection=ccrs.Mercator())  #create an axes object in the figure, using a Mercator

