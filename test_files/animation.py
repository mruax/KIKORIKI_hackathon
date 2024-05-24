from kivy.app import App
from kivy.core.window import Window
from kivy.uix.image import Image
from kivy.animation import Animation


class AnimatedImage(Image):
    def __init__(self, **kwargs):
        super(AnimatedImage, self).__init__(**kwargs)
        self.anim = Animation(pos=(-400, 0), duration=3, transition="in_out_quart")

    def start_animation(self):
        self.anim.start(self)


class MyApp(App):
    def build(self):
        Window.size = (1600, 900)
        img1 = AnimatedImage(source='images\\png\\volna_m.png')
        img1.start_animation()
        return img1


if __name__ == '__main__':
    MyApp().run()

