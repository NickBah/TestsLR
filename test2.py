
def createDict(k, v):
    res = {}
    if (type(k) != list):
        raise Exception('First_Argument_Not_List_Exception')
    if (type(v) != list):
        raise Exception('Second_Argument_Not_List_Exception')

    for i in range(len(k)):
        try:
            res.update({k[i]: v[i]})
        except IndexError:
            res.update({k[i]: None})
    return res

if __name__ == '__main__':
    import unittest

    a = ['key1', 'key2', 'key3', 'key4', 'key5']
    b = [15, 25, 35]

    c = ['key6', 'key7', 'key8']
    d = [45, 55, 65]

    class TestCreationMethods(unittest.TestCase):

        def test_normal_values(self):
            self.assertEqual(createDict(a,b), {'key1': 15, 'key2': 25, 'key3': 35, 'key4': None, 'key5': None})
            self.assertEqual(createDict(c,d), {'key6': 45, 'key7': 55, 'key8': 65})


        def test_notlist_type(self):
            self.assertTrue(createDict(2,[1,2,3,4]) is None)
            self.assertTrue(createDict(['a','b','c'],'abc') is None)

    unittest.main(verbosity=2)