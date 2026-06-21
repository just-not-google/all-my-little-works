import numpy as np

class Simulation:
    def __init__(self):
        self._incomes = np.random.randint(100, 501, 30)
        self._expenses = np.random.randint(50, 301, 30)
        self._days = np.arange(1, 31)

    @property
    def balance(self):
        try:
            return self._incomes - self._expenses
        except Exception:
            return False

    @property
    def mean_balance(self):
        try:
            return np.mean(self.balance)
        except Exception:
            return False

    @property
    def _boolean_arr(self):
        try:
            return self.balance > 0
        except Exception:
            return False

    @property
    def _filtered_balance(self):
        try:
            return self.balance[self._boolean_arr]
        except Exception:
            return False

    @property
    def _filtered_days(self):
        try:
            return self._days[self._boolean_arr]
        except Exception:
            return False

    def full_final_version(self):
        try:
            return np.column_stack((self._filtered_days, self._filtered_balance))
        except Exception:
            return False

    def __str__(self):
        return (f"Balance:\n"
                f"{self.balance}\n"
                f"=================\n"
                f"Mean Balance:\n"
                f"{self.mean_balance}\n"
                f"=================\n"
                f"Filtered Balance:\n"
                f"{self.full_final_version()}\n"
                f"=================\n")

    def __del__(self):
        print("The Simulation class has ceased to exist")


if __name__ == "__main__":
    simulation_1 = Simulation()
    print(simulation_1)


