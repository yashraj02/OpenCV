dilate
to
get
rid
of
text
median
blur
to
further
surpass
any
text & get
image
with shadows and discoloration
    calculate
abs
diff
between
orignal & the
background(just
obtained) if image:
    the
bits
that
are
identical(i.e
white
paper) will
have
0(black)
Difference & bits
that
are
non - identical
will
have
high
difference(i.e
Black
text(on
orignal
img) vs
white
text(on
background
img)).
this
will
give
us
black
background & white
text.So
we
invert
it
for black text & white background.
Now
to
even
further
remove
gray
patches
on
white
portion
do
thresholding & again
normalize
