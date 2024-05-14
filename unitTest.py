import unittest
from bs4 import BeautifulSoup

class TestHTMLStructure(unittest.TestCase):

    def setUp(self):
        with open("index.html", "r", encoding="utf-8") as file:
            self.html_content = file.read()

        with open("chatbot.html", "r", encoding="utf-8") as file:
            self.chatbot_html_content = file.read()

        with open("faq.html", "r", encoding="utf-8") as file:
            self.faq_html_content = file.read()

    #Index.html tests
    def test_get_started_button(self):
        soup = BeautifulSoup(self.html_content, 'html.parser')
        button = soup.find('button', string='Get Started')
        self.assertIsNotNone(button, "The 'Get Started' button should be present on the webpage.")
  
        parent_anchor = button.find_parent('a')
        self.assertIsNotNone(parent_anchor, "The 'Get Started' button should be wrapped in an anchor tag.")
        self.assertEqual(parent_anchor['href'], "chatbot.html", "The anchor tag should link to 'chatbot.html'.")

    def test_welcome_text(self):
        soup = BeautifulSoup(self.html_content, 'html.parser')
        welcome_text = soup.find('h1', string='Welcome to UoS AI Advisor')
        self.assertIsNotNone(welcome_text, "The welcome text should be present on the webpage.")

    #chatbot.html tests
    def test_faq_button(self):
        soup = BeautifulSoup(self.chatbot_html_content, 'html.parser')
        faq_link = soup.find('h1').find('a', string='FAQ')
        self.assertIsNotNone(faq_link, "The 'FAQ' link should be present on the webpage within an anchor tag.")

        self.assertEqual(faq_link['href'], "faq.html", "The anchor tag should link to 'faq.html'.")


    def test_slider_menu(self):
        soup = BeautifulSoup(self.chatbot_html_content, 'html.parser')
        menu_toggle = soup.find('img', id='menuToggle')
        self.assertIsNotNone(menu_toggle, "The menu toggle image should be present on the webpage.")
      
        side_menu = soup.find('div', id='sideMenu')
        self.assertIsNotNone(side_menu, "The side menu div should be present on the webpage.")
        
        close_menu = soup.find('button', id='closeMenu')
        self.assertIsNotNone(close_menu, "The close menu button should be present on the webpage.")
        
    #FAQ.html tests
    def test_welcome_text_faq(self):
        soup = BeautifulSoup(self.faq_html_content, 'html.parser')
        welcome_text = soup.find('h1', string=' Frequently Asked Questions ')
        self.assertIsNotNone(welcome_text, "The welcome text should be present on the faq webpage.")


    def tearDownClass():
        print("All tests ran successfully!")

if __name__ == "__main__":
    unittest.main()
