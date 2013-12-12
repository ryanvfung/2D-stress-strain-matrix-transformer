2D Stress / Strain Matrix Transformer
=====================================

Introduction
------------

Transforms a 2D Stress or Strain matrix by a specific angle (in degrees), using the following equation:

	/ xx' \   /   cos²θ      sin²θ       2cosθsinθ  \   / xx \
	| yy' | = |   sin²θ      cos²θ      -2cosθsinθ  | × | yy |
	\ xy' /   \ -cosθsinθ   cosθsinθ    cos²θ-sin²θ /   \ xy /

**Author**: Ryan Fung

**Created**: 2013-12-06

**Last Modified**: 2013-12-12


Upcoming Features to be Implemented
-----------------------------------
None


Change log
----------
### 2013-12-06 Version 0.1
* Initial release

**2013-12-12**
* Minor modifications to comments