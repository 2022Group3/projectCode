import unittest
from MODEL import model_predict

class TestUnchangingPrediction(unittest.TestCase):

    def test_picture_predaction(self):
        img_path = r"C:\Users\user1\Downloads\automobile2.png"
        img = model_predict.load_image(img_path)
        pred = "automobile"
        prob = 99
        pred1, prob1, pred2, prob2,_,_ = model_predict.predict_image(img)
        self.assertEqual(pred1, pred)
        self.assertLessEqual(prob,prob1)


if __name__ == '__main__':
    unittest.main()