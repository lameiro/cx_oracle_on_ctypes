from test_base import TestBase

class GithubX(TestBase):
    def test_it(self):
        connection = self.get_connection()

        connection.begin()
        cursor = connection.cursor()
        cursor.execute('insert into testnumbers values (42, 42, 42, 42, 42)')
        connection.commit()

        connection.begin()
        cursor = connection.cursor()
        cursor.execute('insert into testnumbers values (43, 43, 43, 43, 43)')
        connection.rollback()

        connection.begin()
        cursor = connection.cursor()
        cursor.execute('select * from testnumbers where (IntCol = 42 and NumberCol = 42) or (IntCol=43 and NumberCol = 43)')
        all_results = cursor.fetchall()
        self.assertEqual([(42, 42.0, 42.0, 42, 42)], all_results)
        connection.rollback()

    def tearDown(self):
        connection = self.get_connection()
        connection.begin()
        cursor = connection.cursor()
        cursor.execute('delete from testnumbers where IntCol = 42 and NumberCol = 42')
        connection.commit()
