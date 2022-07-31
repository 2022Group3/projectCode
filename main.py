import sys

from DATA import display, extract_images_from_pickle, create_data_csv, devide, statistics
import logging
from logging.handlers import RotatingFileHandler

from GUI import gui
from GUI.gui import app

logging.root.setLevel(logging.INFO)
logging.root.addHandler(RotatingFileHandler("./file.log"))
logging.root.addHandler(logging.StreamHandler())
fmt = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
for h in logging.root.handlers:
    h.setFormatter(fmt)

if __name__ == '__main__':
    logging.info("main")
    gui.window.show()
    sys.exit(app.exec_())
    from DATA import display
    #statistics.stas()
    #extract_images_from_pickle.extract_cifar_data()
    # create_data_csv.cifar10_to_df()
    # create_data_csv.cifar100_to_df()
    #devide.train_validate_test_split()
    # #add_our_img.save_our_img()
    #display.display_img_by_class("dog")
    # try:
    #     #display.displaySampleFromDataset(15)
    # except:
    #     logging.error(Exception)