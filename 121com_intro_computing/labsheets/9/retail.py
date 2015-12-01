class Product():
    def __init__(self, title, price):
        self.title = title
        self.price = price

class Music(Product):
    def __init__(self, title, price, tracklist, artist):
        self.tracklist = tracklist
        self.artist = artist
        Product.__init__(self, title, price)

class Movie(Product):
    def __init__self(self, title, price, director, run_time):
        self.director = director
        self.run_time = run_time
        Product.__init__(self, title, price)

class CD(Music):
    def __init__(self, artist, title, price, tracklist, shipping_cost):
        self.shipping_cost = shipping_cost
        Product.__init__(self, title, price)

class Vinyl(Music):
    def __init__(self, artist, title, price, tracklist, shipping_cost, vinyl_size):
        self.vinyl_size = vinyl_size
        self.shipping_cost = shipping_cost
        Product.__init__(self, title, price)

class Download(Music):
    def __init__(self, artist, title, price, tracklist, shipping_cost,
            download_quality, download_size):
        self.download_quality = download_quality
        self.shipping_cost = shipping_cost
        self.download_size = download_size
        Product.__init__(self, title, price)

class Dvd(Movie):
    def __init__(self, title, price, director, run_time):
        Movie.__init__(self, title, price, director, run_time)

class Download(Movie):
    def __init__(self, title, price, director, run_time, file_size, quality):
        self.file_size = file_size
        self.quality = quality
        Movie.__init__(self, title, price, director, run_time)

#cd1 = Download('Megadeth', 'Hangar 18', 12, ['1. Hangar 18', '2. Sweating Bullets'],
#        0, 12, '13MB')
shawshank = Download('The Shawshank Redemption', 5, 'Frank Darabont', '2hr 22',
        '1.2GB', '480p')
print(shawshank.run_time)
#print(cd1.artist, cd1.download_size)
