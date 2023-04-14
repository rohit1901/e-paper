from uctypes import bytearray_at, addressof
from framebuf import FrameBuffer
# Writer for colour displays.
class CWriter(Writer):


    def __init__(self, device, font, fgcolor=None, bgcolor=None, verbose=True):
        if not hasattr(device, 'palette'):
            raise OSError('Incompatible device driver.')
        if implementation[1] < (1, 17, 0):
            raise OSError('Firmware must be >= 1.17.')

        super().__init__(device, font, verbose)
        if bgcolor is not None:  # Assume monochrome.
            self.bgcolor = bgcolor
        if fgcolor is not None:
            self.fgcolor = fgcolor
        self.def_bgcolor = self.bgcolor
        self.def_fgcolor = self.fgcolor

    def _printchar(self, char, invert=False, recurse=False):
        s = self._getstate()
        self._get_char(char, recurse)
        if self.glyph is None:
            return  # All done
        buf = bytearray_at(addressof(self.glyph), len(self.glyph))
        fbc = FrameBuffer(buf, self.clip_width, self.char_height, self.map)
        palette = self.device.palette
        palette.bg(self.fgcolor if invert else self.bgcolor)
        palette.fg(self.bgcolor if invert else self.fgcolor)
        self.device.blit(fbc, s.text_col, s.text_row, -1, palette)
        s.text_col += self.char_width
        self.cpos += 1

    def setcolor(self, fgcolor=None, bgcolor=None):
        if fgcolor is None and bgcolor is None:
            self.fgcolor = self.def_fgcolor
            self.bgcolor = self.def_bgcolor
        else:
            if fgcolor is not None:
                self.fgcolor = fgcolor
            if bgcolor is not None:
                self.bgcolor = bgcolor
        return self.fgcolor, self.bgcolor