

class MusicPlayer:
    def __init__(self, format):
     self.format = format

    def play(self, file_path):
        raise NotImplementedError("Not implemented")


class DesktopPlayer(MusicPlayer):
    def play(self, file_path):
        print("Using Desktop Player")
        self.format.play(file_path)


class MobilePlayer(MusicPlayer):
    def play(self, file_path):
        print("Using Mobile Player")
        self.format.play(file_path)


class MP3:
    def play(self, file_path):
        print(f"Playing MP3 file {file_path}")


class WAV:
    def play(self, file_path):
        print(f"Playing WAV file {file_path}")


mp3_format = MP3()
player = DesktopPlayer(mp3_format)
player.play("song.mp3")

wav_format = WAV()
player = MobilePlayer(wav_format)
player.play("song.wav")

