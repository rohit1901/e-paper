from framebuf import FrameBuffer
__version__ = (0, 5, 0)

fast_mode = True  # Does nothing. Kept to avoid breaking code.

class DisplayState():
    def __init__(self):
        self.text_row = 0
        self.text_col = 0

def _get_id(device):
    if not isinstance(device, FrameBuffer):
        raise ValueError('Device must be derived from FrameBuffer.')
    return id(device)