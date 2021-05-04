import unittest

from items import Item


class TestItem(unittest.TestCase):

    def test_return_item_data(self):
        item = Item('Lighter', 'Used for flames', 3)
        self.assertEqual("Lighter, Used for flames, 3", item.display_data())
        return


if __name__ == '__main__':
    unittest.main()
