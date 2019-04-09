# Monumentale en gedenkwaardige bomen in de gemeente Leeuwarden

Deze dataset voor de OpenStreetMap editor [JOSM](https://josm.openstreetmap.de/) is een afgeleide
van de *Monumentale en gedenkwaardige bomen dataset* die door de gemeente Leeuwarden gepubliceerd is.

Het doel van `bomen.osm` is om OpenStreetMap-mappers in Leeuwarden de mogelijkheid te geven bijzondere en
beeldbepalende bomen eenvoudig aan de kaart toe te voegen met de juiste tags en locatie.

## Gebruik van de data

De data is vrij om te gebruiken. De brondata is onder de 
[CC0-licentie](https://creativecommons.org/share-your-work/public-domain/cc0/) vrijgegeven. Dit
betekent dat het gebruik ervan vrij is. Deze afgeleide dataset is onder dezelfde licentie geplaatst.

## OpenStreetMap tags

Bij de conversie van de brondata zijn de volgende tags aangemaakt.

* `genus`, en soms `species` of `taxon` (afhankelijk van de waarde van `BOOMSOORT` in de brondata)
* `start_date` (plantjaar, uit `PLANTJAAR`)
* `leaf_type` (afgeleid van `BOOMSOORT`) 
* `leaf_cycle` (afgeleid van `BOOMSOORT`) 
* `denotation=natural_monument` (voor monumentale bomen)
* `natural=tree` (🌲)
* `source=Monumentale en Gedenkbomen dataset gemeente Leeuwarden`
* `source:date` (datum van publicatie van de brondata)
* `ref:lwdtrees` (referentienummer uit veld `ELEMENTNR`)

## Toepassen in OpenStreetMap

Laad `bomen.osm` in JOSM in, en kopieer de bomen die in het gebied staan naar de laag waarin je de
kaart aan het bewerken bent. Gebruik de *Paste at source Position* functie, zodat de bomen op
precies dezelfde plek staan.

Sommige bomen hebben in de oorspronkelijke data een opmerking; beoordeel of je deze wil behouden, of
dat deze niet in OpenStreetMap hoort.

**Neem alleen bomen uit deze dataset over waarvan je bevestigd hebt dat ze er ook daadwerkelijk nog
staan.**

Het is niet de bedoeling dat deze dataset in een keer geïmporteerd wordt in OpenStreetMap.

## Wijzigingen ten opzichte van de brondata

Op basis van de tags die in OpenStreetMap al in gebruik zijn voor de soortnamen van bomen, zijn
spelfouten en kleine afwijkingen in de brondata gecorrigeerd. Deze fouten zijn bij de gemeente
gemeld, en worden in een toekomstige versie hopelijk meegenomen.

Verder is de soortnaam gebruikt om in ieder geval de `genus`-tag te vullen, en meestal ook
`species`. Bij boomsoorten waar er sprake is van een *cultivar* is de volledige naam in de
`taxon`-tag opgenomen, en bevat `species` de soortnaam zonder cultivar.

Bomen die in de brondata de status van 'monumentale boom' hebben, zijn in `bomen.osm` met
[`denotation=natural_monument`](https://wiki.openstreetmap.org/wiki/Key:denotation) gemarkeerd.

Omdat in de brondata referentienummers niet uniek zijn, bestaat de `source:ref`-tag steeds uit een
voorloopnummer (oplopend vanaf 0) gevolgd door het referentienummer (in de vorm
`voorloopnummer:referentienummer`).

## Coördinaten

Voor de conversie van de coördinaten in de brondata naar de voor JOSM geschikte WGS84 coördinaten is
deze Proj.4 parameter gebruikt:

```
+towgs84=565.417,50.3319,465.552,-0.398957,0.343988,-1.8774,4.0725
```

De volledige Proj.4 string op basis van de `.prj` uit de brondata staat in het conversiescript.

## Toekomst

In de loop van 2019 komt waarschijnlijk een update beschikbaar van de gemeente. Deze dataset kan dan
ook een update krijgen.
