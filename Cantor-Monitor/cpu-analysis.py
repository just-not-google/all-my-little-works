import psutil
from typing import Union


class AnalyzerCPU:
    '''
    A class for partial analysis of the computer processor
    (because I didn't have enough strength for a full one, I just didn't care)
    '''
    def number_logical_processors(self) -> int:
        '''
        The function outputs the number of logical processor cores
        '''
        return psutil.cpu_count()

    def number_physical_processors(self) -> int:
        '''
        The function outputs the number of physical processor cores
        '''
        return psutil.cpu_count(logical=False)

    @property
    def all_cpu_times(self):
        '''
        A function for accessing a tuple of all possible CPU time options (for Windows in my case).
        '''
        try:
            cpu_times = psutil.cpu_times()
            return cpu_times
        except Exception:
            return None

    def user_times(self) -> Union[int, str]:
        '''
        Well, it's clear from the name of the function.
        '''
        if self.all_cpu_times is None:
            return "N/A"
        return self.all_cpu_times.user

    def system_times(self) -> Union[int, str]:
        '''
        Well, it's clear from the name of the function.
        '''
        if self.all_cpu_times is None:
            return "N/A"
        return self.all_cpu_times.system

    def idle_times(self) -> Union[int, str]:
        '''
        Well, it's clear from the name of the function.
        '''
        if self.all_cpu_times is None:
            return "N/A"
        return self.all_cpu_times.idle

    def __str__(self):
        '''
        Almost a beautiful conclusion for the end developer who will use this brainchild.
        '''
        return (f"Number Logical Processors: {self.number_logical_processors()}\n"
                f"Number Physical Processors: {self.number_physical_processors()}\n"
                f"{'=' * 20}\n"
                f"Total CPU time in various modes:\n"
                f"User Time: {self.user_times()}\n"
                f"System Time: {self.system_times()}\n"
                f"Idle Time: {self.idle_times()}\n"
                f"{'=' * 20}\n")


if __name__ == "__main__":
    analys_cpu_test = AnalyzerCPU()
    print(analys_cpu_test)