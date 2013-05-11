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