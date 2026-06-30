from abc import ABC, abstractmethod


class IFormat(ABC):
    @abstractmethod
    def play(self, file_path: str) -> None:
        pass


class MusicPlayer(ABC):
    def __init__(self, format: IFormat):
     self.format = format

    @abstractmethod
    def play(self, file_path: str) -> None:
        pass


class DesktopPlayer(MusicPlayer):
    def play(self, file_path: str) -> None:
        print("Using Desktop Player")
        self.format.play(file_path)


class MobilePlayer(MusicPlayer):
    def play(self, file_path: str) -> None:
        print("Using Mobile Player")
        self.format.play(file_path)


class MP3(IFormat):
    def play(self, file_path: str) -> None:
        print(f"Playing MP3 file {file_path}")


class WAV(IFormat):
    def play(self, file_path: str) -> None:
        print(f"Playing WAV file {file_path}")


mp3_format = MP3()
player = DesktopPlayer(mp3_format)
player.play("song.mp3")

wav_format = WAV()
player = MobilePlayer(wav_format)
player.play("song.wav")











