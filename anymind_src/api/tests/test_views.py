from ddt import data, ddt
from django.test import TestCase

from api.tests.test_response import TEST_TEXT as ttext
from api.views import remove_tags, scrab_tweets

PAGES_SIZES = (1, 3, 6, 8, 9, 11, 13, 16, 19, 20)


@ddt
class APITestCase(TestCase):

    def test_scrab_tweets_parse_text(self):
        expected_data_0 = {
            'account': {
                'fullname': 'Elizabeth Stewart',
                'href': '/eerstewart1'
            },
            'date': 'Aug 31',
            'hashtags': [],
            'text': 'Currently expanding my'
        }
        expected_data_length = 20
        data = scrab_tweets(ttext)
        self.assertEqual(expected_data_length, len(data))
        self.assertEqual(expected_data_0, data[0])

    def test_scrab_tweets_pages_size_gt_defaul(self):
        expected_data_length = 20
        data = scrab_tweets(ttext, pages_size=100)
        self.assertEqual(expected_data_length, len(data))

    @data('a', -12, None, 0)
    def test_scrab_tweets_pages_size_not_positive_number(self, page_size):
        expected_data_length = 20
        data = scrab_tweets(ttext, pages_size=page_size)
        self.assertEqual(expected_data_length, len(data))

    @data(*PAGES_SIZES)
    def test_scrab_tweets_pages_size_lt_default(self, pages_size):
        data = scrab_tweets(ttext, pages_size=pages_size)
        self.assertEqual(pages_size, len(data))

    def test_remove_tags(self):
        array = ttext.split('<td class')
        result_array = remove_tags(array)
        for item_list in result_array:
            for item in item_list:
                self.assertEqual(item.find('<'), -1)
                self.assertEqual(item.find('>'), -1)
