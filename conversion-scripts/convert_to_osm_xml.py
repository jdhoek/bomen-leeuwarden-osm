#!/usr/bin/env python3

import sys
import shapefile

from lxml import etree
from pyproj import Proj

projection = None 

def show_help():
    print("{} INPUT > OUTPUT".format(sys.argv[0]))


def parse_command():
    if len(sys.argv) < 2:
        show_help()
        sys.exit(0)

    convert(
        sys.argv[1]
    )


def convert(file_name):
    root = etree.Element('osm', attrib={'version':'0.6', 'generator':'bomentool'})
    sf = shapefile.Reader(file_name)
    projection = Proj('+proj=sterea +lat_0=52.15616055555555 +lon_0=5.38763888888889 +k=0.9999079 +x_0=155000 +y_0=463000 +ellps=bessel +towgs84=565.417,50.3319,465.552,-0.398957,0.343988,-1.8774,4.0725 +units=m +no_defs')

    shapeRecs = sf.shapeRecords()

    element_id = 0

    for sr in shapeRecs:
        node_id = -1 - element_id
        x, y = sr.shape.points[0]
        lon, lat = projection(x, y, inverse=True)
        node = etree.Element('node', attrib={'id': str(node_id), 
            'lat': '%9.7f' % lat, 'lon': '%11.7f' % lon})
        
        for tag_name in ['BOOMSOORT', 'PLANTJAAR', 'STATUS', 'OPMERKINGE']:
            try:
                value = sr.record[tag_name]
                if value:
                    tag = etree.Element('tag', attrib={'k': tag_name, 'v': str(value)})
                    node.append(tag)
            except:
                pass

        element_nr = '%d:%s' % (element_id, sr.record['ELEMENTNR'])
        ref_tag = etree.Element('tag', attrib={'k': 'ELEMENTNR', 'v': element_nr})
        node.append(ref_tag)

        x_tag = etree.Element('tag', attrib={'k': 'X', 'v': str(x)})
        y_tag = etree.Element('tag', attrib={'k': 'Y', 'v': str(y)})
        node.append(x_tag)
        node.append(y_tag)
        
        root.append(node)
        element_id += 1

    xml = etree.tostring(root,
                         encoding="utf8",
                         xml_declaration=True,
                         pretty_print=True)
    print(bytes.decode(xml))
    

if __name__ == '__main__':
    parse_command()
