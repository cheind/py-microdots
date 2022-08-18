![](https://github.com/cheind/py-microdots/actions/workflows/python-package.yml/badge.svg)

# py-microdots

This repository provides **py-microdots**, a Python library for encoding and decoding 2D locations based on the [Anoto](https://www.anoto.com/cases/anoto-digital-pen/) dot pattern approach.

<div align="center">
<img src="doc/anoto_pattern.svg" width="80%">
</div>

The Anoto grid pattern encodes a unique 2D position for every possible 6x6 sub-array of dots. Assuming a grid resolution of 0.3 mm, this coding remains unique over the area of Europe and Asia. For clarity, the dots are significantly scaled up and nominal grid lines are shown.

## Literature

The implementation is based on my research on this topic. A detailed report about our findings is available HERE.

## Features

**py-microdots** offers the following features

-   Decoding of position coordinates, section coordinates and pattern rotations.
-   Encoding support including section coordinates
-   Drawing routines
-   Generalized interface that supports tailored coding variants (e.g. 4x4 codes)

## Scope

The focus of this library is depicted best in a diagram shown below

<div align="center">
<img src="doc/pymicrodots-scope.png">
</div>

That is, **py-microdots** focuses on encoding and decoding of bit-matrices. That is, the library does not come with image processing to compute the offset direction of dots.

## Example

```python
# Import the library
import microdots as mdots
import matplotlib.pyplot as plt

# Use the default embodiment with sequence A4 fixed
codec = mdots.anoto_6x6_a4_fixed

# Generate a bit-matrix for section (10,2)
bits = codec.encode_bitmatrix(shape=(9, 16), section=(10, 2))

# Decode a partial matrix
pos = codec.decode_location(bits[3:, 7:])
sec = codec.decode_section(bits[3:, 7:], pos=pos)
rot = codec.decode_rotation(bits[3:, 7:])
print("pos:", pos, "sec:", sec, "rot:", rot)
# > pos: (7, 3) sec: (10, 2) rot: 0

# Render dots
fig, ax = plt.subplots()
mdots.draw_dots(bits, grid_size=1.0, show_grid=True, ax=ax)
fig.savefig("dots.pdf")
plt.close(fig)
```
