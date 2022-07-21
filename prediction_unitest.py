import unittest
import model_predict
from faker import Faker

class TestUnchangingPrediction(unittest.TestCase):

    def test_picture_predaction(self):
        img='Ship_diagram-numbers.svg.png'
        pred=99.86
        pred1, newPred, pred2, prob2 = model_predict.predict_image(img)
        #newPred=model_predict.predict_image(img)
        newPred=(round(newPred, 2))
        self.assertEqual(pred, newPred)

if __name__ == '__main__':
    unittest.main()
