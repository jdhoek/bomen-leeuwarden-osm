#!/usr/bin/env python3

import sys
import json

from lxml import etree

species_found = {}

def show_help():
    print("{} INPUT > OUTPUT".format(sys.argv[0]))


def parse_command():
    if len(sys.argv) < 2:
        show_help()
        sys.exit(0)

    scan(
        sys.argv[1]
    )

def scan(file_name):
    with open(file_name) as input_file:
        tree = etree.parse(input_file)
        root = tree.getroot()
        for element in root:
            # Node.
            for tag in element:
                key = tag.get('k')
                if key == 'BOOMSOORT':
                    soort = tag.get('v').replace("\"", "'")
                    if soort in species_found:
                        species_found[soort]['count'] += 1
                    else:
                        species_found[soort] = {}
                        species_found[soort]['count'] = 1

        print(json.dumps(species_found))
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
