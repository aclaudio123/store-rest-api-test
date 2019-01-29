"""
Integration test

In this module we look at how to test
 foreign key constrains, store relationships


"""
from models.item import ItemModel
from models.store import StoreModel
from tests.base_test import BaseTest


class ItemTest(BaseTest):
    def test_crud(self):
        with self.app_context():
            StoreModel('Piano').save_to_db()
            item = ItemModel('Piano', 19.99, 1)

            self.assertIsNone(ItemModel.find_by_name('Piano'),
                              "Found an item with name {}, but expected not to.".format(item.name))

            item.save_to_db()

            self.assertIsNotNone(ItemModel.find_by_name('Piano'))

            item.delete_from_db()

            self.assertIsNone(ItemModel.find_by_name('Piano'))

    # test store relationship
    def test_store_relationship(self):
        with self.app_context():
            store = StoreModel('test_store')
            item = ItemModel('Piano', 19.99, 1)

            store.save_to_db()
            item.save_to_db()

            self.assertEqual(item.store.name, 'test_store')

