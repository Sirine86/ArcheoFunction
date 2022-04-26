%matplotlib notebook

import pandas as pd
import geopandas as gpd
from shapely.geometry import Point, LineString, Polygon

Anfeh = point(750794.00, 3805582.00)
Tell_arqa = point(228936.00, 3824965.00)
Roman_temple = point(229660.32, 3810573.97)
Theater = point(745098.00, 3793746.00)
Historical_church = point(744947.00, 3796531.00)

print(Anfeh)
print(Tell_arqa)
print(Theater)
print(Historical_church)
print(Roman_temple)

## adding buffer zone for sites
Anfeh_buffer = Anfeh.buffer(570)
Tell_arqa_buffer = Tell_arqa.buffer(344)
Roman_temple_buffer = Roman_temple.buffer(685)
Theater_buffer = Theater.buffer(97)
Historical_church_buffer = Historical_church.buffer(1624)