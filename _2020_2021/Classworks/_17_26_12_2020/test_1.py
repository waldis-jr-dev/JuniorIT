class TestUM:
    def setup_class(cls):
        cls.kek = 234
        print("class setup")

    def teardown_class(cls):
        print("class teardown")

    def setup_method(self, method):
        self.lol = 123
        print("method setup")

    def teardown_method(self, method):
        print("method teardown", f'LOL={self.lol}', f'KEK={self.kek}')

    def test_numbers_5_6(self):
        print("test 5*6")
        assert 5 * 6 == 30

    def test_strings_b_2(self):
        print("test b*2")
        assert 'b' * 2 == 'bb'
