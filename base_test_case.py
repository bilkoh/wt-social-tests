from seleniumbase import BaseCase
from data.login_creds import EMAIL, PASSWD


class BaseTestCase(BaseCase):
    """This is the base class our test will inherit from.

        All functions that start with `test_` will be run by pytest.
        Everything else will be ignored by pytest.

        Methods setUp/tearDown are run before and after each test.

        Any other method added to this class should be doing
        something that is or may be used for more than test.
    """

    def setUp(self):
        super().setUp()
        # << Add custom code AFTER the super() line >>

    def tearDown(self):
        self.save_teardown_screenshot()
        # << Add custom code BEFORE the super() line >>
        super(BaseTestCase, self).tearDown()

    def login(self):
        """Log the driver into the website. Many test will require to be in a 
            logged in state."""
        self.open("https://wtsdev.wikitribune.com/login")
        self.click("#email")
        self.type("#email", EMAIL)
        self.click("#password")
        self.type("#password", PASSWD)
        self.click("//button[@type='submit']")
        pass

    def make_post(self, message):
        self.open("https://wtsdev.wikitribune.com/")

        # we're logged in, main page should have "Your feed" section visible
        # if not we'll generate an error
        self.find_element('//*[@id="feed-contents"]/h2')

        # input for post message is in its own iframe, switching to it
        self.switch_to_frame('//iframe[@class="tox-edit-area__iframe"]')
        self.click("#tinymce")
        self.type("#tinymce", message)

        # switching back
        self.driver.switch_to.parent_frame()

        # submit
        self.click('//*[@id="saveArticle"]/span')
        pass

    def nav_to_activity_page(self):
        """Navigate to the page that shows all our posts.
        """
        self.open("https://wtsdev.wikitribune.com/")
        self.click('//*[@id="header-user-url"]')
        self.click('//*[@id="userdd-myactivity"]')
        pass

    def nav_to_post(self, message):
        """Navigate to one of our posts based on the content of post.

        Args:
            message (string): content of our post
        """
        self.nav_to_activity_page()

        # finding partial match b/c longer posts will have shortened titles
        match_len = 4
        self.find_partial_link_text(message[:match_len]).click()
        pass
