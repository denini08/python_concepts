from typing import NewType

type User = dict[str, str | int | None]

# Basic syntax
# type RGB = tuple[int, int, int]
# type HSL = tuple[int, int, int]

# With NewType
RGB = NewType("RGB", tuple[int, int, int])
HSL = NewType("HSL", tuple[int, int, int])


def create_user(
    first_name: str,
    last_name: str,
    age: int | None = None,
    fav_color: RGB | None = None,
) -> dict:
    email = f"{first_name.lower()}.{last_name.lower()}@example.com"

    return {
        "first_danme": first_name,
        "last_name": last_name,
        "email": email,
        "age": age,
        "fav_color": fav_color,
    }


def main():
    user: dict = create_user("John", "Doe", 38, RGB((123, 211, 377)))
    # With basic syntax, using aliases like this doesn't help with
    # 'accidently passing HSL instead of RGB', as they are both just 3-tuples of ints
    # user: dict = create_user("John", "Doe", 38, HSL((211, 123, 377)))
    print(user)


if __name__ == "__main__":
    main()
