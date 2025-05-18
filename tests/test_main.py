import unittest
import json
from jsonschema import validate, ValidationError
from src.main import get_user


class TestMain(unittest.TestCase):
    def setUp(self):
        with open("schemas/user.schema.json", encoding="utf-8") as f:
            self.schema = json.load(f)

    def test_get_user_validates_against_schema(self):
        user = get_user()

        try:
            validate(instance=user, schema=self.schema)
        except ValidationError as e:
            self.fail(f"Validation failed: {e}")


if __name__ == "__main__":
    unittest.main()
