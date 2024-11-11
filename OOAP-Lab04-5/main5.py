from abc import ABC, abstractmethod


class Phone(ABC):
    @abstractmethod
    def make_call(self):
        pass


class VideoCamera:
    def start_video(self):
        return "Відеокамера: відео-з'єднання встановлено"


class VideoCallAdapter(Phone):
    def __init__(self, camera: VideoCamera):
        self.camera = camera

    def make_call(self):
        return self.camera.start_video()


class Skype:
    def __init__(self, phone: Phone):
        self.phone = phone

    def start_call(self):
        return self.phone.make_call()


if __name__ == "__main__":
    camera = VideoCamera()

    video_call = VideoCallAdapter(camera)

    skype = Skype(video_call)

    print(skype.start_call())
