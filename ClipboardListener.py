import win32clipboard

class ClipboardListener:
    data = None

    def __init__(self):
        print("creating clipboard listener")
        #win32clipboard.OpenClipboard()
        #win32clipboard.EmptyClipboard()
        #win32clipboard.CloseClipboard()

    def getClipboard(self):
        win32clipboard.OpenClipboard()
        self.data = win32clipboard.GetClipboardData()
        win32clipboard.CloseClipboard()
        return self.data