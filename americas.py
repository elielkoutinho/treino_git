from pygal.maps.world import World


wm = World()
wm.title = 'Américas do Norte, Central e Sul'
wm.add('América do Norte',['ca','mx','us'])
wm.add('América Central',['bz', 'cr', 'gt', 'hn', 'ni', 'pa', 'sv'])
wm.add('América do Sul', ['ar', 'bo', 'br', 'cl', 'co', 'ec', 'gf',    'gy', 'pe', 'py', 'sr', 'uy', 've'])

wm.render_to_file('arquivos/americas33.svg')