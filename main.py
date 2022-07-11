import extract_images_from_pickle as extract
import params
import add_our_img
import create_data_csv
import devide
import statistics
import display


if __name__ == '__main__':
    extract.extract_cifar_data()
    create_data_csv.cifar10_to_df()
    create_data_csv.cifar100_to_df()
    devide.train_validate_test_split()
    add_our_img.save_our_img()
    display.displayIMGbyClass("dog")
    display.displaySampleFromDataset()
    statistics.show_all_statistics()



