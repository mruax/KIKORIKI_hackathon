from kivy.animation import Animation
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.clock import Clock


class ProductWidget(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.label1 = Label()
        self.add_widget(self.label1)
        self.label2 = Label()
        self.add_widget(self.label2)
        self.image = Image()
        self.add_widget(self.image)

    def fade_out(self):
        # anim_label1 = Animation(opacity=0, duration=1)
        anim_label2 = Animation(opacity=0, duration=1)
        anim_image = Animation(opacity=0, duration=1,x=self.image.x - 100, y=self.image.y - 100)

        # anim_label1.start(self.label1)
        anim_label2.start(self.label2)
        anim_image.start(self.image)


    def fade_in(self):
        # anim_label1 = Animation(opacity=1, duration=1)
        anim_label2 = Animation(opacity=1, duration=1)
        anim_image = Animation(opacity=1, duration=1, x=self.image.x + 100, y=self.image.y + 100)

        # anim_label1.start(self.label1)
        anim_label2.start(self.label2)
        anim_image.start(self.image)


class ProductSlider(App):
    def build(self):
        self.root = BoxLayout(orientation='vertical')
        self.product_widgets = []
        for i in range(2):  # создаем 2 виджета для товаров
            pw = ProductWidget()
            self.product_widgets.append(pw)
        self.root.add_widget(self.product_widgets[0])
        self.current_product = 0
        self.animate_product()
        return self.root

    def animate_product(self, *args):
        # анимация смещения товара за экран
        self.product_widgets[self.current_product].fade_out()
        # планируем следующую анимацию через 5 секунд
        Clock.schedule_once(self.show_next_product, 5)

    def show_next_product(self, *args):
        # переключаем на следующий товар
        self.current_product = (self.current_product + 1) % 2
        self.root.clear_widgets()
        self.root.add_widget(self.product_widgets[self.current_product])
        self.product_widgets[self.current_product].image.source = 'closed.png'
        self.product_widgets[self.current_product].label1.text = f'Product {self.current_product + 1} label 1'
        self.product_widgets[self.current_product].label2.text = f'Product {self.current_product + 1} label 2'
        # анимация появления товара
        self.product_widgets[self.current_product].fade_in()
        # планируем следующую анимацию через 5 секунд
        Clock.schedule_once(self.animate_product, 5)


if __name__ == '__main__':
    ProductSlider().run()
