from models.item import ItemModel
from models.store import StoreModel

from tests.base_test import BaseTest


class StoreTest(BaseTest):
    def test_create_store_items_empty(self):
        store = StoreModel('test_store')

        self.assertEqual(store.items.all(), [],
                         "the store's items length was not 0 even though no items were added")

    def test_crud(self):
        with self.app_context():
            store = StoreModel('test_store')

            self.assertIsNone(StoreModel.find_by_name('test_store'))

            store.save_to_db()

            self.assertIsNotNone(StoreModel.find_by_name('test_store'))

            store.delete_from_db()

            self.assertIsNone(StoreModel.find_by_name('test_store'))

    def test_store_relation(self):
        with self.app_context():
            store = StoreModel('test_store')
            item = ItemModel('Piano', 19.99, 1)

            store.save_to_db()
            item.save_to_db()

            self.assertEqual(store.items.count(), 1)
            self.assertEqual(store.items.first().name, 'Piano')

    def test_store_json(self):
        store = StoreModel('test_store')
        expected = {
            'id': None,
            'name': 'test_store',
            'items': []
        }

        self.assertDictEqual(store.json(), expected)

    def test_store_json_with_item(self):
        with self.app_context():
            store = StoreModel('test_store')
            item = ItemModel('Piano', 19.99, 1)

            store.save_to_db()
            item.save_to_db()

            expected = {
                'id': 1,
                'name': 'test_store',
                'items': [{'name': 'Piano', 'price': 19.99}]
            }

            self.assertDictEqual(store.json(), expected)
