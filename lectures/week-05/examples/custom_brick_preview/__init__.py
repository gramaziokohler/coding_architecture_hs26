"""Experimental batch previews for COMPAS geometry in Rhino 8 Python 3."""

from pathlib import Path

__all__ = ["bricks_to_rhino_mesh"]
_brick_builder = None


def bricks_to_rhino_mesh(bricks):
    """Return one mesh from bricks with center, dimensions, and Z rotation.

    Accepts a custom class with center, xsize, ysize, zsize, and angle attributes.
    Does not modify the input. Empty input returns None. This is a preview of
    separate brick shells, not a Boolean union; rotations are about world Z.
    """
    import clr
    import System

    global _brick_builder
    if _brick_builder is None:
        dll = Path(__file__).with_name("CustomBrickPreview.dll")
        if not dll.is_file():
            raise ImportError(
                "Build CustomBrickPreview.dll with build_in_rhino.py first."
            )
        clr.AddReference(str(dll))
        from CustomBrickPreview import BrickMeshBuilder

        _brick_builder = BrickMeshBuilder

    values = []
    for brick in bricks:
        values.extend(brick.center)
        values.extend((brick.xsize, brick.ysize, brick.zsize, brick.angle))
    if not values:
        return None
    return _brick_builder.Build(System.Array[System.Double](values))
