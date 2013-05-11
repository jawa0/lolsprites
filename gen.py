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


_base_resolutions = {'iPhone': (480, 320), 'iPhone Retina 3.5"': (960, 640), 'iPad': (1024, 768), 
	'iPad Retina': (2048, 1536), 'iPhone Retina 4"': (1136, 640), 'Nexus One': (800, 480),
	'Nexus S': (800, 480), 'Galaxy Nexus': (1280, 720), 'Nexus 4': (1280, 768),
	'Nexus 7': (1280, 800), 'Nexus 10': (2560, 1600)}


screen_resolutions = {}
for name, resolution in _base_resolutions.items():
	oriented_name = name + ' Landscape'
	screen_resolutions[oriented_name] = resolution

	oriented_name = name + ' Portrait'
	screen_resolutions[oriented_name] = (resolution[1], resolution[0])


if __name__ == '__main__':
	width_pixels = 64
	height_pixels = 64

	surface = cairo.ImageSurface(cairo.FORMAT_RGB24, width_pixels, height_pixels)
	ctx = cairo.Context(surface)

	ctx.set_source_rgb(1, 1, 1)
	ctx.rectangle(0, 0, width_pixels, height_pixels)
	ctx.fill()

	surface.write_to_png('square_white_%04d.png' % (width_pixels,))