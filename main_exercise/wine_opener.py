from overrides import override

from gift import Gift


class WineOpener(Gift):
    @override
    def open_gift(self):
        print("Congratulations! you got a new gift! Enjoy!")
