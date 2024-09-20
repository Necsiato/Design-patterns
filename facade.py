class Amplifier:
    def on(self):
        print("Amplifier on")

    def set_volume(self, level):
        print(f"Amplifier setting volume to {level}")


class Tuner:
    def on(self):
        print("Tuner on")


class DVDPlayer:
    def on(self):
        print("DVD Player on")

    def play(self, movie):
        print(f"DVD Player playing {movie}")

class HomeTheaterFacade:
    def __init__(self, amp, tuner, dvd):
        self.amp = amp
        self.tuner = tuner
        self.dvd = dvd

    def watch_movie(self, movie):
        print("Get ready to watch a movie...")
        self.amp.on()
        self.amp.set_volume(10)
        self.tuner.on()
        self.dvd.on()
        self.dvd.play(movie)

    def end_movie(self):
        print("Shutting down the movie theater...")

if __name__ == "__main__":
    amp = Amplifier()
    tuner = Tuner()
    dvd = DVDPlayer()
    home_theater = HomeTheaterFacade(amp, tuner, dvd)

    home_theater.watch_movie("Inception")
    home_theater.end_movie()
