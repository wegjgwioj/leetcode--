import importlib.util
import pathlib
import unittest


MODULE_PATH = pathlib.Path(__file__).resolve().parents[1] / "1-哈希表" / "202-快乐数.py"
SPEC = importlib.util.spec_from_file_location("happy_number", MODULE_PATH)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(MODULE)


class HappyNumberTests(unittest.TestCase):
    def test_returns_true_for_happy_number(self) -> None:
        self.assertTrue(MODULE.isHappy(19))

    def test_returns_false_for_unhappy_number(self) -> None:
        self.assertFalse(MODULE.isHappy(20))

    def test_returns_false_for_cycle_value(self) -> None:
        self.assertFalse(MODULE.isHappy(37))


if __name__ == "__main__":
    unittest.main()
