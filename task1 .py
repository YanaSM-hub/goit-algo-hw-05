import re
from typing import Callable, Generator

def generator_numbers(text: str) -> Generator[float, None, None]:

    pattern = r"\b\d+(?:\.\d+)?\b"
    for match in re.finditer(pattern, text):
        yield float(match.group())


def sum_profit(text: str, func: Callable[[str], Generator[float, None, None]]) -> float:
    return sum(func(text))



if __name__ == "__main__":
    sample_text = "Our revenue this month is 1200.50 from sales and 800 from services."
    total = sum_profit(sample_text, generator_numbers)
    print(f"Total profit: {total}")

  
