# Building-grid conventions for HS26

Use the same outward face winding from week 07 through slabs, façades, and the final project. No reversal is needed when moving to the next exercise.

## Box vertices and faces

For a box built with `Box.from_corner_corner_height(Point(0, 0, 0), Point(xsize, ysize, 0), zsize)`, with positive sizes, `box.compute_vertices()` returns the following order in COMPAS 2.15.1:

| Label | Index | Coordinates |
|---|---:|---|
| a | 0 |                   (0, 0, 0) |
| b | 1 | (0, ysize, 0) |
| c | 2 | (xsize, ysize, 0) |
| d | 3 | (xsize, 0, 0) |
| e | 4 | (0, 0, zsize) |
| f | 5 | (xsize, 0, zsize) |
| g | 6 | (xsize, ysize, zsize) |
| h | 7 | (0, ysize, zsize) |

After adding these vertices to a VolMesh, use their **vertex keys**, in the same order, to construct the cell:

```python
faces = [
    [a, b, c, d],  # bottom: -Z
    [a, d, f, e],  # front:  -Y
    [a, e, h, b],  # left:   -X
    [b, h, g, c],  # back:   +Y
    [c, g, f, d],  # right:  +X
    [e, f, g, h],  # top:    +Z
]
volmesh.add_cell(faces)
```

The face vertices run counterclockwise when viewed from outside the cell. `add_cell` preserves the supplied winding; it does not repair reversed faces automatically. A cyclic shift of a face list preserves its normal, while reversing the order flips its normal.

Do not mix this vertex order with another box constructor or a hand-written vertex list without checking the coordinates. `Box(xsize, ysize, zsize)` uses local X, Y, Z dimensions; `Box.from_width_height_depth(width, height, depth)` maps those arguments to local X, Z, Y respectively. A box's frame origin is its **centre**, not its lower corner.

## Shared vertices and half-faces

Neighbouring cells must reuse the same vertex keys. The course builders use `TOL.geometric_key(point)` to identify coincident corners, and add each distinct vertex only once. Merely putting different vertices at identical coordinates does not establish cell adjacency.

Each cell owns its oriented half-faces. On a shared face, the two neighbouring cells have opposite outward normals. `volmesh.halffaces()` visits both sides; `volmesh.faces()` visits one representative per geometric face. Use `faces()` when generating one slab per face, to avoid duplicate internal slabs. The representative normal of an internal face depends on which half-face is visited; its sign alone cannot classify a slab.

## Slab classification

First select horizontal faces. Their unit normals are parallel to positive or negative Z. For the axis-aligned grids used here, `abs(normal.dot(Vector.Zaxis())) == 1` selects them. Use a tolerance for more general calculated geometry.

Then classify each selected face:

| Condition | Category |
|---|---|
| `volmesh.halfface_opposite_cell(hf) is not None` | `floor_slab` |
| Boundary face, normal dot Z < 0 | `bottom_slab` |
| Boundary face, normal dot Z > 0 | `roof` |

Cell key `0` is a valid neighbour. Testing `if opposite_cell:` incorrectly treats that cell as absent. Always test `is not None`.

Slab geometry in the supplied solution extends below the face level. Its placement is independent of whether the face normal points up or down; changing the winding is not a way to move the slab.

## Façade frames

Generate façade panels only on boundary faces whose normals are perpendicular to Z. The supplied frame construction is:

```python
xaxis = face_normal.cross(Vector.Zaxis())
yaxis = face_normal.cross(xaxis)
frame = Frame(centroid, xaxis, yaxis)
```

For these vertical faces, the local Y axis points downward and the frame normal points outward. This is a valid right-handed frame. The panel's local X is its horizontal span, local Y is its vertical span, and local Z is its thickness.

The HS26 exercises use a north-up plan convention, with +Z upward and
**North = +Y, East = +X, South = −Y, West = −X**. This matches
[Rhino's default model North](https://docs.mcneel.com/rhino/8/help/en-us/commands/sun.htm).
Classify a façade by its outward normal:

| Outward normal | Orientation |
|---|---|
| +Y | North (`N`) |
| +X | East (`E`) |
| −Y | South (`S`) |
| −X | West (`W`) |

The South-only attractor exercise therefore changes the **−Y façade**. Use this mapping consistently when completing the student template; do not reverse face winding to assign compass labels.

These are the tutorial's modelling directions. A site's geographic North may differ, especially after placing the building on a plot; transform or redefine the reference directions explicitly when needed.

## Quick checks

For a regular 2 × 2 × 2 grid with every cell included, expect:

| Item | Count |
|---|---:|
| Cells | 8 |
| Shared vertices | 27 |
| Unique faces | 36 |
| Half-faces | 48 |
| Boundary faces | 24 |
| Columns | 18 |
| Main beams | 36 |
| Slabs | 12: 4 bottom, 4 internal, 4 roof |
| Façade panels | 16 |

For each convex box cell, `face_normal.dot(face_centroid - cell_centroid)` must be positive. Regenerating beams, columns, slabs, or façades must replace the previous list rather than append duplicates.
