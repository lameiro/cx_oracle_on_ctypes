from test_base import TestBase

class Github13(TestBase):
    def test_it(self):
        c = self.get_cursor()
        self.assertEqual(c.execute("""SELECT 'Test\0NameForDesc' from dual""").description[0][0], "'Test\0NameForDesc'".upper())
