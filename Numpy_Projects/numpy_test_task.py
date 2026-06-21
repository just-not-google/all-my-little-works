import numpy as np
from typing import List, NoReturn

MAX_VALUE = 5

class ScoreCalculator:
    def __init__(self, list_ratings: List[int]) -> NoReturn:
        if len(list_ratings) == MAX_VALUE:
            self.list_ratings = list_ratings
        else:
            self.list_ratings = [0] * 5

    @property
    def array_of_list(self):
        return np.array(self.list_ratings)

    def mean_data(self):
        return np.mean(self.array_of_list)

    def max_data(self):
        return np.max(self.array_of_list)

    def min_data(self):
        return np.min(self.array_of_list)

    def data_more_90(self):
        return self.array_of_list[self.array_of_list > 90]

    def __str__(self) -> str:
        return (f"Array - {self.array_of_list}\n"
                f"Mean - {self.mean_data()}\n"
                f"Max - {self.max_data()}\n"
                f"Min - {self.min_data()}\n"
                f"Data > 90 - {self.data_more_90()}")


if __name__ == "__main__":
    lst_data = []
    print("Enter 5 whole ratings, one at a time:")
    attempt = 0
    added = 0
    while len(lst_data) < 5:
        attempt += 1
        try:
            answer = input(f"(attempt {attempt}; added {added}) >> ")
            if len(answer.split()) != 1:
                raise Exception
            int_answer = int(answer)
            lst_data.append(int_answer)
            added += 1
        except Exception:
            continue
    score_calculator = ScoreCalculator(lst_data)
    print(score_calculator)