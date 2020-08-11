from base_test_case import BaseTestCase
from data.unicode import samples


class PostTests(BaseTestCase):
    """A class that contains all of our tests regarding posts.
    """

    def setUp(self):
        super().setUp()
        self.login()

    def _test_post(self, message):
        self.make_post(message)
        self.nav_to_post(message)
        self.assert_text(message)  # assert test

    def test_post_thai(self):
        self._test_post(samples["thai"])

    def test_post_basic_latin(self):
        self._test_post(samples["basic_latin"])

    def test_post_arrows(self):
        self._test_post(samples["arrows"])
