from base_test_case import BaseTestCase
from data.unicode import samples
from selenium.common.exceptions import NoSuchElementException
import pytest


class PostTests(BaseTestCase):
    """A class that contains all of our tests regarding posts.
    """

    def setUp(self):
        super().setUp()
        self.login()

    def _test_make_post(self, message):
        self.make_post(message)
        self.nav_to_post(message)
        self.assert_text(message)  # assert test

    def _test_delete_post(self, message):
        # finding partial match b/c longer posts will have shortened titles
        match_len = 4

        self.delete_post(message)
        self.nav_to_activity_page()

        is_deleted = False
        try:
            self.wait_for_partial_link_text(message[:match_len])
        except NoSuchElementException:
            is_deleted = True

        assert is_deleted, "Post has not been deleted."

    @pytest.mark.first  # to insure that the delete test's dont run before this
    @pytest.mark.dependency(name="test_make_post_thai")
    def test_make_post_thai(self):
        self._test_make_post(samples["thai"])

    @pytest.mark.first
    @pytest.mark.dependency(name="test_make_post_basic_latin")
    def test_make_post_basic_latin(self):
        self._test_make_post(samples["basic_latin"])

    @pytest.mark.first
    @pytest.mark.dependency(name="test_make_post_arrows")
    def test_make_post_arrows(self):
        self._test_make_post(samples["arrows"])

    @pytest.mark.dependency(depends=["test_make_post_thai"])
    def test_delete_post_thai(self):
        self._test_delete_post(samples["thai"])

    @pytest.mark.dependency(depends=["test_make_post_basic_latin"])
    def test_delete_post_basic_latin(self):
        self._test_delete_post(samples["basic_latin"])

    @pytest.mark.dependency(depends=["test_make_post_arrows"])
    def test_delete_post_arrows(self):
        self._test_delete_post(samples["arrows"])
