import time
import unittest


def time_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Час виконання функції {func.__name__}: {elapsed_time} секунд")
        return result

    return wrapper


@time_decorator
def example_function(x, y):
    time.sleep(2)
    return x + y


class TestTimeDecorator(unittest.TestCase):
    def test_time_decorator(self):
        with self.assertLogs() as logs:
            result = example_function(10, 20)
            self.assertIn("Час виконання функції example_function:", logs.output[0])

        self.assertEqual(result, 30)


if __name__ == '__main__':
    unittest.main()
