from parser import *
from app import *
from settings import *

if __name__ == "__main__":
    # get_items()
    # all_products = get_all_products()
    # print(all_products)
    # routers = get_items(url=all_products[0], page_type=1)
    # get_items(url=all_products[0] + "/page/2", page_type=1)  # костыльно, но парсим вторую страницу
    # tvs = get_items(url=all_products[1], page_type=2)
    # cctvs = get_items(url=all_products[2], page_type=3)

    app = QApplication(sys.argv)
    w = MainWindow()

    # w.pemolux("imaqliq-boxfullhd-slide.jpg")


    w.show()
    sys.exit(app.exec())
