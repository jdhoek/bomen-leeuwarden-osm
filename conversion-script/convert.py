#!/usr/bin/env python3

import sys
import json

from lxml import etree

species_found = {}
species_known = {}
species_lookup = {}
needleleaved = []

def show_help():
    print("{} INPUT > OUTPUT".format(sys.argv[0]))


def parse_command():
    if len(sys.argv) < 2:
        show_help()
        sys.exit(0)

    read_species_known()
    read_species_lookup()
    read_needleleaved()

    convert(
        sys.argv[1]
    )

def read_needleleaved():
    with open("needleleaved.json", "r") as read_file:
        needleleaved.extend(json.load(read_file))

def read_species_known():
    with open("species.json", "r") as read_file:
        data = json.load(read_file)
        for tree in data['data']:
            species_known[tree['value']] = tree['count']

def read_species_lookup():
    with open("lookup.json", "r") as read_file:
        data = json.load(read_file)
        for (species, tags) in data.items():
            species_lookup[species] = tags

def convert(file_name):
    with open(file_name) as input_file:
        tree = etree.parse(input_file)
        root = tree.getroot()
        for element in root:
            # Node.
            for tag in element:
                key = tag.get('k')
                if key in ('X', 'Y'):
                    element.remove(tag)
                elif key == 'PLANTJAAR':
                    year = tag.get('v').replace('.0', '')
                    tag.attrib['k'] = 'start_date'
                    tag.attrib['v'] = year
                    None
                elif key == 'OPMERKINGE':
                    tag.attrib['k'] = 'note'
                elif key == 'ELEMENTNR':
                    ref = tag.get('v').replace('.0', '')
                    tag.attrib['k'] = 'ref:boomnummer'
                    tag.attrib['v'] = ref
                elif key == 'BOOMSOORT':
                    soort = tag.get('v').replace("\"", "'")
                    genus_or_species = 'species'
                    if soort in species_found:
                        species_found[soort]['count'] += 1
                    else:
                        species_found[soort] = {}
                        species_found[soort]['count'] = 1
                    if soort in species_known:
                        species_found[soort]['known'] = True
                    else:
                        species_found[soort]['known'] = False
                        if soort in species_lookup:
                            (genus_or_species, soort) = next(iter(species_lookup[soort].items()))
                        else:
                            print('Missing species from lookup table: ' + soort)
                            sys.exit(1)

                    tag.attrib['k'] = genus_or_species
                    tag.attrib['v'] = soort
                    if soort in needleleaved:
                        is_needleleaved = etree.Element("tag", attrib={'k':'leaf_type', 'v':'needleleaved'})
                        element.append(is_needleleaved)
                    else:
                        is_broadleaved = etree.Element("tag", attrib={'k':'leaf_type', 'v':'broadleaved'})
                        element.append(is_broadleaved)

                elif key == 'STATUS':
                    if tag.get('v') == 'monumentale boom':
                        is_monumental = etree.Element("tag", attrib={'k':'denotation', 'v':'natural_monument'})
                        element.append(is_monumental)
                    element.remove(tag)

            is_a_tree = etree.Element("tag", attrib={'k':'natural', 'v':'tree'})
            element.append(is_a_tree)

            source = etree.Element("tag", attrib={'k':'source', 'v':'Monumentale en Gedenkbomen dataset gemeente Leeuwarden'})
            element.append(source)

            source_date = etree.Element("tag", attrib={'k':'source:date', 'v':'2015-08-26'})
            element.append(source_date)



        xml = etree.tostring(tree,
                             encoding="utf8",
                             xml_declaration=True,
                             pretty_print=True)
        print(bytes.decode(xml))
        #species_list = []
        #for s in species_found.items():
        #    species_list.append((s[0], s[1]['known'], s[1]['count']))
        #species_list.sort(key=lambda x: (x[1], x[2], x[0]))
        #print("{")
        #for e in species_list:
        #    if e[1] == False:
        #        escaped = e[0].replace("\"", "'")
        #        print("  \"%s\":{\"species\":\"%s\"}," % (escaped, escaped))
        #print("}")
    

if __name__ == '__main__':
    parse_command()
