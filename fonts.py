def zero( panel ):
    panel[0] += '  000  '
    panel[1] += ' 0   0 '
    panel[2] += ' 0   0 '
    panel[3] += ' 0   0 '
    panel[4] += '  000  '
    panel[5] += '       '

def one( panel ):
    panel[0] += '   1   '
    panel[1] += '   1   '
    panel[2] += '   1   '
    panel[3] += '   1   '
    panel[4] += '   1   '
    panel[5] += '       '

def two( panel ):
    panel[0] += ' 222222 '
    panel[1] += '      2 '
    panel[2] += ' 222222 '
    panel[3] += ' 2      '
    panel[4] += ' 222222 '
    panel[5] += '        '

def blank( panel ):
    panel[0] += '     '
    panel[1] += '     '
    panel[2] += '     '
    panel[3] += '     '
    panel[4] += '|___|'
    panel[5] += '     '

def comma( panel ):
    panel[0] += '      '
    panel[1] += '      '
    panel[2] += '      '
    panel[3] += '+--+  '
    panel[4] += '+-++  '
    panel[5] += '  ++  '

def dot( panel ):
    panel[0] += '      '
    panel[1] += '      '
    panel[2] += '      '
    panel[3] += '+-+   '
    panel[4] += '+-+   '
    panel[5] += '      '

def unknown( panel ):
    panel[0] += ' +----+ '
    panel[1] += ' |????| '
    panel[2] += ' |????| '
    panel[3] += ' |????| '
    panel[4] += ' +----+ '
    panel[5] += '        '
