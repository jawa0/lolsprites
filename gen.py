# Copyright (c) 2013, Jabavu Wolfgang Adams. 
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# 1) Redistributions of source code must retain the above copyright notice, 
# this list of conditions and the following disclaimer. 
# 
# 2) Redistributions in binary form must reproduce the above copyright notice,
# this list of conditions and the following disclaimer in the documentation 
# and/or other materials provided with the distribution. 
#
# 3) Neither the name of Jabavu Wolfgang Adams nor the names of any 
# contributors may be used to endorse or promote products derived from this 
# software without specific prior written permission. 
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.


import cairo
import math

# TODO
#
# * Placeholder screen-shots in standard sizes
# * Placeholder app icons and iTunes Connect art
# * Simple geometric shapes and stars
# * circles with heading indicator (radial line)
# * boxes with arrows (compass directions)
# * capsules
# * rounded rects, dashed, buttons with highlight
# * sprite animations of simple 3d objects spinning
# * animated button gleam/bling
# * scale 9s

# _base_resolutions = {'iPhone': (480, 320), 'iPhone Retina 3.5"': (960, 640), 'iPad': (1024, 768), 
# 	'iPad Retina': (2048, 1536), 'iPhone Retina 4"': (1136, 640), 'Nexus One': (800, 480),
# 	'Nexus S': (800, 480), 'Galaxy Nexus': (1280, 720), 'Nexus 4': (1280, 768),
# 	'Nexus 7': (1280, 800), 'Nexus 10': (2560, 1600)}


# screen_resolutions = {}
# for name, resolution in _base_resolutions.items():
# 	oriented_name = name + ' Landscape'
# 	screen_resolutions[oriented_name] = resolution

# 	oriented_name = name + ' Portrait'
# 	screen_resolutions[oriented_name] = (resolution[1], resolution[0])


rgb_colors = {'black': (0,0,0), 'red': (1,0,0), 'green': (0,1,0), 'blue': (0,0,1),
	'yellow': (1,1,0), 'cyan': (0,1,1), 'magenta': (1,0,1), 'white': (1,1,1)}


def create_filled_square_rgb888(side_pixels, rgb_color = (1,1,1)):
	'''Returns a Cairo surface entirely filled with a square of the desired pixel dimensions, in the
	desired color. The side length is given in pixels as side_pixels. The fill color is given as 
	a 3-tuple of red, green, and blue components (each in the range 0.0 to 1.0) in rgb_color. The 
	returned surface is in 24-bit RGB (FORMAT_RGB24) format, with 8 bits per color channel.'''

	surface = cairo.ImageSurface(cairo.FORMAT_RGB24, side_pixels, side_pixels)
	ctx = cairo.Context(surface)

	apply(ctx.set_source_rgb, rgb_color)
	ctx.rectangle(0, 0, side_pixels, side_pixels)
	ctx.fill()
	return surface


def create_filled_square_with_border_rgb888(side_pixels, border_pixels, rgb_fill = (1,1,1), rgb_border = (0,0,0)):
	surface = cairo.ImageSurface(cairo.FORMAT_RGB24, side_pixels, side_pixels)
	ctx = cairo.Context(surface)

	apply(ctx.set_source_rgb, rgb_fill)
	ctx.rectangle(0, 0, side_pixels, side_pixels)
	ctx.fill()

	apply(ctx.set_source_rgb, rgb_border)

	ctx.set_line_width(border_pixels)
	inset = 0.5 * border_pixels
	ctx.rectangle(inset, inset, side_pixels - 2 * inset, side_pixels - 2 * inset)
	ctx.stroke()

	return surface


def create_filled_circle_with_border_argb8888(radius_pixels, border_pixels, rgb_fill = (1,1,1), rgb_border = (0,0,0)):
	surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, int(2 * radius_pixels), int(2 * radius_pixels))
	ctx = cairo.Context(surface)

	apply(ctx.set_source_rgb, rgb_fill)
	ctx.arc(radius_pixels, radius_pixels, radius_pixels - 0.5 * border_pixels, 0, 2 * math.pi)
	ctx.fill()

	apply(ctx.set_source_rgb, rgb_border)
	ctx.set_line_width(border_pixels)
	ctx.arc(radius_pixels, radius_pixels, radius_pixels - 0.5 * border_pixels, 0, 2 * math.pi)
	ctx.stroke()

	return surface


def create_filled_border_circle_with_radius(radius_pixels, border_pixels, rgb_fill = (1,1,1), rgb_border = (0,0,0)):
	surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, int(2 * radius_pixels), int(2 * radius_pixels))
	ctx = cairo.Context(surface)

	apply(ctx.set_source_rgb, rgb_fill)
	ctx.arc(radius_pixels, radius_pixels, radius_pixels - 0.5 * border_pixels, 0, 2 * math.pi)
	ctx.fill()

	apply(ctx.set_source_rgb, rgb_border)
	ctx.set_line_width(border_pixels)
	ctx.arc(radius_pixels, radius_pixels, radius_pixels - 0.5 * border_pixels, 0, 2 * math.pi)
	ctx.stroke()

	ctx.move_to(radius_pixels, radius_pixels)
	ctx.line_to(2 * radius_pixels - 0.5 * border_pixels, radius_pixels)
	ctx.stroke()

	return surface


def rounded_rect(side_pixels, border_pixels, bevel_radius_percentage = 0.2, rgb_fill = (1,1,1), rgb_border = (0,0,0)):
	# TODO: cleanup copypasta

	surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, side_pixels, side_pixels)
	ctx = cairo.Context(surface)

	bevel_pixels = side_pixels * bevel_radius_percentage

	apply(ctx.set_source_rgb, rgb_fill)

	ctx.arc(side_pixels - bevel_pixels, bevel_pixels, bevel_pixels - 0.5 * border_pixels, 1.5 * math.pi, 0)
	ctx.arc(side_pixels - bevel_pixels, side_pixels - bevel_pixels, bevel_pixels - 0.5 * border_pixels, 0, 0.5 * math.pi)
	ctx.arc(bevel_pixels, side_pixels - bevel_pixels, bevel_pixels - 0.5 * border_pixels, 0.5 * math.pi, math.pi)
	ctx.arc(bevel_pixels, bevel_pixels, bevel_pixels - 0.5 * border_pixels, math.pi, 1.5 * math.pi)
	ctx.line_to(side_pixels - bevel_pixels, 0.5 * border_pixels)
	ctx.fill()


	# apply(ctx.set_source_rgb, rgb_fill)
	# ctx.arc(radius_pixels, radius_pixels, radius_pixels - 0.5 * border_pixels, 0, 2 * math.pi)
	# ctx.fill()

	apply(ctx.set_source_rgb, rgb_border)

	ctx.set_line_width(border_pixels)

	ctx.arc(side_pixels - bevel_pixels, bevel_pixels, bevel_pixels - 0.5 * border_pixels, 1.5 * math.pi, 0)
	ctx.arc(side_pixels - bevel_pixels, side_pixels - bevel_pixels, bevel_pixels - 0.5 * border_pixels, 0, 0.5 * math.pi)
	ctx.arc(bevel_pixels, side_pixels - bevel_pixels, bevel_pixels - 0.5 * border_pixels, 0.5 * math.pi, math.pi)
	ctx.arc(bevel_pixels, bevel_pixels, bevel_pixels - 0.5 * border_pixels, math.pi, 1.5 * math.pi)
	ctx.line_to(side_pixels - bevel_pixels, 0.5 * border_pixels)

	ctx.stroke()
	return surface


def filename_from_options(kind, size, border, fill_color, border_color, bevel = None):
	return ''


if __name__ == '__main__':
	square_sizes = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]
	border_widths = [1, 2, 4, 8, 16, 32, 64]
	bevel_percentages = [0.1, 0.15, 0.2, 0.25, 0.4]

	for sz in square_sizes:
		surface = create_filled_square_rgb888(sz, (1,1,1))
		surface.write_to_png('images/square_%s_%04d.png' % ('white', sz))

		surface = create_filled_square_rgb888(sz, (0,0,0))
		surface.write_to_png('images/square_%s_%04d.png' % ('black', sz))

		for bw in border_widths:
			if bw >= sz / 2:	# Skip if border is too thick for small image
				continue

			surface = create_filled_square_with_border_rgb888(sz, bw)
			surface.write_to_png('images/square_%s_%04d_border_%s_%02d.png' % ('white', sz, 'black', bw))

			surface = create_filled_square_with_border_rgb888(sz, bw, (0,0,0), (1,1,1))
			surface.write_to_png('images/square_%s_%04d_border_%s_%02d.png' % ('black', sz, 'white', bw))

			surface = create_filled_circle_with_border_argb8888(0.5 * sz, bw)
			surface.write_to_png('images/circle_%s_%04d_border_%s_%02d.png' % ('white', sz, 'black', bw))

			surface = create_filled_circle_with_border_argb8888(0.5 * sz, bw, (0,0,0), (1,1,1))
			surface.write_to_png('images/circle_%s_%04d_border_%s_%02d.png' % ('black', sz, 'white', bw))

			surface = create_filled_border_circle_with_radius(0.5 * sz, bw, (0,0,0), (1,1,1))
			surface.write_to_png('images/circle_rad_%s_%04d_border_%s_%02d.png' % ('black', sz, 'white', bw))

			surface = create_filled_border_circle_with_radius(0.5 * sz, bw)
			surface.write_to_png('images/circle_rad_%s_%04d_border_%s_%02d.png' % ('white', sz, 'black', bw))

			for bevel in bevel_percentages:
				bevel_pix = bevel * sz
				if bevel_pix < 3:	# Don't draw really tiny bevels
					continue

				if bevel_pix < 2 * bw:	# Or we won't see a curve
					continue

				surface = rounded_rect(sz, bw, bevel, (1,1,1), (0,0,0))
				surface.write_to_png('images/square_%s_%04d_border_%s_%02d_bevel_%04d.png' % ('white', sz, 'black', bw, bevel_pix))

				surface = rounded_rect(sz, bw, bevel, (0,0,0), (1,1,1))
				surface.write_to_png('images/square_%s_%04d_border_%s_%02d_bevel_%04d.png' % ('black', sz, 'white', bw, bevel_pix))
