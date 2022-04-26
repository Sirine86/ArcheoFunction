

import pandas as pd
import geopandas as gpd
from shapely.geometry import Point, LineString, Polygon

#adding location of site through UTM
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

#adding buffer zone for sites
Anfeh_buffer = Anfeh.buffer(570)
Tell_arqa_buffer = Tell_arqa.buffer(344)
Roman_temple_buffer = Roman_temple.buffer(685)
Theater_buffer = Theater.buffer(97)
Historical_church_buffer = Historical_church.buffer(1624)

print(type(Anfeh_buffer_buffer))
print(type(Tell_arqa_buffer_buffer))
print(type(Roman_temple_buffer_buffer))
print(type(Theater_buffer_buffer))
print(type(Historical_church_buffer_buffer))
