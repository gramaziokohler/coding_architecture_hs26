# Swiss-city graph

The graph in [example 01](./examples/01-geometry-and-datastructures_hs26.gh) has ten
city nodes and fifteen connections. It demonstrates
`graph.shortest_path(start, destination)`, which minimizes total geometric edge
length in COMPAS 2.15.1. The result is highlighted blue; the preview labels cities.

Use the **Start city** and **Destination city** dropdowns to select endpoints by
city name. Both offer all ten cities. The script matches the selected names to
node keys before calculating the path. Selecting the same city for both returns
that single city.

The default selection is Genève → St. Gallen, giving the path
Genève → Lausanne → Bern → Zürich → St. Gallen. Connections are drawn as straight
graph edges, not actual railway alignments. A code comment mentions
`compas.topology.dijkstra_path` for weighted routing as a possible extension.

## Geographic placement

Positions were derived from station coordinates returned by the public
[Swiss Transport API](https://transport.opendata.ch/docs.html) on 29 October 2026.
A simple local projection preserves a recognisable north-up shape:

- X = (longitude − 6°) × cos(46.8°) × 7.
- Y = (latitude − 45.8°) × 7.
- Z = 0.

These are scaled map units, not metres. The preview adds a display-only gallery
offset. Its border is a simplified version of the
[Natural Earth 1:50m country boundary](https://github.com/nvkelso/natural-earth-vector/blob/master/geojson/ne_50m_admin_0_countries.geojson),
which is [public-domain data](https://www.naturalearthdata.com/about/terms-of-use/).
