

class DVDPlayer:
    def on(self):
        print("DVD Player turned on")

    def play_movie(self, movie):
        print(f"Playing movie '{movie}'")

    def off(self):
        print("DVD Player turned off")


class Proyector:
    def on(self):
        print("Proyector turned on")

    def off(self):
        print("Proyector turned off")


class Speakers:
    def on(self):
        print("Speaker turned on")

    def off(self):
        print("Speaker turned off")


class HomeTheaterFacade:
    def __init__(self, dvd_player, proyector, speakers):
        self.dvd_player = dvd_player
        self.proyector = proyector
        self.speakers = speakers

    def watch_movie(self, movie):
        print(f"Get ready to watch a movie...")
        self.dvd_player.on()
        self.proyector.on()
        self.speakers.on()
        self.dvd_player.play_movie(movie)

    def end_movie(self):
        print(f"Shutting down movie...")
        self.dvd_player.off()
        self.proyector.off()
        self.speakers.off()


dvd_player = DVDPlayer()
proyector = Proyector()
speakers = Speakers()

home_theater = HomeTheaterFacade(dvd_player, proyector, speakers)
home_theater.watch_movie("Star Wars")

print("Wait two hours...")

home_theater.end_movie()

