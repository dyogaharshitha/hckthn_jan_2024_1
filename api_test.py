import unittest
import requests

url1 = 'http://127.0.0.1.5000'
url2 = 'http://127.0.0.1.5000/seq?int1=2&int2=3&limit=18&str1=two&str2=three'
class Test(unittest.TestCase):
    url1 = 'http://127.0.0.1.5000'

    # test for connection
    def tst1(self):
        res = requests.get(url1)
        self.assertEqual(res.status_code, 200)
        jsn = res.json()
        print("test  successful")

    # test correct sequence
    def tst2(self):
        res = requests.get(url2)
        self.assertEqual(res.status_code, 200)
        jsn = res.json()



if __name__ == '__main__':
    tstr = Test()
    tstr.tst()