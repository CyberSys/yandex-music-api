import pytest

from yandex_music import Title


@pytest.fixture(scope='class')
def title():
    return Title(TestTitle.title, TestTitle.full_title)


class TestTitle:
    title = None
    full_title = None

    def test_expected_values(self, title):
        assert title.title == self.title
        assert title.full_title == self.full_title

    def test_de_json_required(self, client):
        json_dict = {'title': self.title}
        title = Title.de_json(json_dict, client)

        assert title.title == self.title

    def test_de_json_all(self, client):
        json_dict = {'title': self.title, 'full_title': self.full_title}
        title = Title.de_json(json_dict, client)

        assert title.title == self.title
        assert title.full_title == self.full_title

    def test_equality(self):
        pass
