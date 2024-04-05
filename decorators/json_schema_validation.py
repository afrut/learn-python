# JSON schema reference: https://json-schema.org/understanding-json-schema/reference
import sys
from functools import wraps
from typing import Callable, Dict

from jsonschema import validate

# The specified schema to validate
schema_insert_transaction = {
    "type": "object",
    "properties": {
        "date": {"type": "string", "format": "date"},
        "description": {"type": "string"},
        "amount": {"type": "number"},
    },
}


# A decorator to validate the schema of a function's argument
def validate_schema(
    name_of_argument_to_validate: str, schema: Dict | None = None
) -> Callable:
    def validate_func(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            instance = kwargs[name_of_argument_to_validate]
            # Compute default schema to evaluate. This module must adhere to
            # defining schemas in variable names of the format schema_function_name
            # so that the appropriate schema can be inferred.
            nonlocal schema
            if schema is None:
                # Infer variable name that contains schema and get its value
                var_name_that_contains_schema = "schema_" + func.__name__
                schema = getattr(sys.modules[__name__], var_name_that_contains_schema)
            validate(instance=instance, schema=schema)
            ret = func(*args, **kwargs)
            return ret

        return wrapper

    return validate_func


# Validate the schema of the input of this function
# *, in function arguments denote keyword-only argument sto simplify the decorator
@validate_schema(name_of_argument_to_validate="transaction")
def insert_transaction(*, transaction: Dict):
    print(f"Inserted transaction {transaction}")


# validate(instance=transaction, schema=schema)

if __name__ == "__main__":
    insert_transaction(
        transaction={
            "date": "2023-01-27",
            "description": "Bought some takeout",
            "amount": -23.1,
        }
    )
    insert_transaction(
        transaction={
            "date": "2023-01-27",
            "description": "Bought some takeout",
            "amount": "-23.1",
        }
    )
