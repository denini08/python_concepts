from pydantic import validate_call


@validate_call
def create_user(first_name: str, last_name: str, age: int) -> dict:
    email = f"{first_name.lower()}.{last_name.lower()}@example.com"

    return {
        "first_danme": first_name,
        "last_name": last_name,
        "email": email,
        "age": age,
    }


def main():
    user: dict = create_user("John", "Doe", 38)  # This is OK
    # user: dict = create_user("John", "Doe", "38") # This will pass validation (pydantic will cast)
    # user: dict = create_user("John", "Doe", "thirty-eight") # This will raise a validation error
    print(user)


if __name__ == "__main__":
    main()
