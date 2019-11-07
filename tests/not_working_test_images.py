from yandex_music import Images


class TestImages:
    _208x208 = None
    _300x300 = None

    def test_expected_values(self, images):
        assert images._208x208 == self._208x208
        assert images._300x300 == self._300x300

    def test_de_json_required(self, client):
        json_dict = {}
        images = Images.de_json(json_dict, client)

    def test_de_json_all(self, client):
        json_dict = {'_208x208': self._208x208, '_300x300': self._300x300}
        images = Images.de_json(json_dict, client)

        assert images._208x208 == self._208x208
        assert images._300x300 == self._300x300

    def test_equality(self):
        pass
