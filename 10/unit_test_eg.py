"""Unit Test - Example"""
import unittest
import os


def count_line(file_name):
    """Counts number of line in a file"""
    with open(file_name) as f: l = len(f.readlines())
    return l


class SimpleLineCount(unittest.TestCase):
    """Simple file line count function Test"""

    def setUp(self):
        """Setup for Test"""
        print("Setup")
        self._filename = "sample.txt"
        with open(self._filename, 'w') as f:
            f.write("Hello World!")

    def tearDown(self):
        """Test cleanup"""
        print("Cleanup")
        try:
            os.remove(self._filename)
        except:
            pass  # No need to handle issues in cleanup

    def test_dummy(self):
        """Dummy Test"""
        pass

    def test_function_present(self):
        """Test presence of function tested"""
        count_line(self._filename)

    def test_check_line(self):
        """Test functionality"""
        self.assertEqual(count_line(self._filename), 1)

    # def test_failure(self):
    #     """Test failure"""
    #     count_line("Non_Existent_File")

    def test_throw_exception(self):
        """Test function throw correct exception"""
        with self.assertRaises(FileNotFoundError):
            count_line("Non_Existent_File")

    def test_file_deletion(self):
        """Test to validate function does not cleanup file"""
        count_line(self._filename)
        self.assertTrue(os.path.exists(self._filename))


if __name__ == '__main__':
    unittest.main()
