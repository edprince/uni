class Product():
    def __init__(self, artist, title, price, tracklist):
        self.artist = artist
        self.title = title
        self.price = price
        self.tracklist = tracklist

class CD(Product):
    def __init__(self, artist, title, price, tracklist, shipping_cost):
        self.shipping_cost = shipping_cost
        Product.__init__(self, artist, title, price, tracklist)

class Vinyl(Product):
    def __init__(self, artist, title, price, tracklist, shipping_cost, vinyl_size):
        self.vinyl_size = vinyl_size
        self.shipping_cost = shipping_cost
        Product.__init__(self, artist, title, price, tracklist)

class Download(Product):
    def __init__(self, artist, title, price, tracklist, shipping_cost,
            download_quality, download_size):
        self.download_quality = download_quality
        self.shipping_cost = shipping_cost
        self.download_size = download_size
        Product.__init__(self, artist, title, price, tracklist)

cd1 = Download('Megadeth', 'Hangar 18', 12, ['1. Hangar 18', '2. Sweating Bullets'],
        0, 12, '13MB')

print(cd1.artist, cd1.download_size)
