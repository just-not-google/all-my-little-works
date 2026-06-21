import pynvml
from constants import MIN_COR_GPU, BYTES_TO_GB, DEFAULT_GPU, MW_TO_W
import GPUtil


class AnalyzerGPU:
    '''
    A class for partial analysis of a video card from an NVIDIA computer manufacturer
    (because I didn't have enough strength for a full one, I just didn't care)
    '''
    def __init__(self):
        '''
        All objects required for the class are initialized here.
        '''
        try:
            pynvml.nvmlInit()
        except pynvml.NVMLError as e:
            raise RuntimeError(f"Failed NVML: {str(e)}")

        try:
            self.gpu = GPUtil.getGPUs()
        except Exception as e:
            raise RuntimeError(f"Failed GPUtil: {str(e)}")

        self.is_all_gpu = None

    def driver_version(self) -> str:
        '''
        The function outputs the version of the graphics card driver
        '''
        return pynvml.nvmlSystemGetDriverVersion()

    def nvml_version(self) -> str:
        '''
        The function outputs the NVML version of the graphics card
        '''
        return pynvml.nvmlSystemGetNVMLVersion()

    @property
    def count_device(self) -> int:
        '''
        The function outputs the number of available discrete graphics cards on the computer
        '''
        return pynvml.nvmlDeviceGetCount()

    def analyzing_specific_gpu(self, number_device: int) -> str:
        '''
        A function in which a complete (in my implementation) analysis of one specific video card takes place.
        '''
        try:
            if number_device < MIN_COR_GPU or number_device >= self.count_device:
                number_device = MIN_COR_GPU
        except Exception:
            number_device = MIN_COR_GPU

        lst_stat_gpu = []

        handle = pynvml.nvmlDeviceGetHandleByIndex(number_device)
        gpu_main = self.gpu[number_device]

        name = pynvml.nvmlDeviceGetName(handle)
        uuid = pynvml.nvmlDeviceGetUUID(handle)

        try:
            serial = pynvml.nvmlDeviceGetSerial(handle)
        except pynvml.NVMLError:
            serial = "N/A"

        try:
            memory_info = pynvml.nvmlDeviceGetMemoryInfo(handle)
            m_t = memory_info.total
            m_f = memory_info.free
            m_u = memory_info.used
            memory_str = (f"Total: {m_t / BYTES_TO_GB:.2f} GB\n"
                          f"Free:  {m_f / BYTES_TO_GB:.2f} GB\n"
                          f"Used:  {m_u / BYTES_TO_GB:.2f} GB\n"
                          f"Free Percent: {(m_f / m_t) * 100:.2f}%\n"
                          f"Used Percent: {(m_u / m_t) * 100:.2f}%\n")
        except pynvml.NVMLError:
            memory_str = ("Total: N/A\n"
                          "Free: N/A\n"
                          "Used: N/A\n")

        try:
            temperature = pynvml.nvmlDeviceGetTemperature(handle, pynvml.NVML_TEMPERATURE_GPU)
        except pynvml.NVMLError:
            temperature = "N/A"

        try:
            max_temperature = pynvml.nvmlDeviceGetTemperature(handle, pynvml.NVML_TEMPERATURE_THRESHOLD_SHUTDOWN)
        except pynvml.NVMLError:
            max_temperature = "N/A"

        try:
            fan_speed = pynvml.nvmlDeviceGetFanSpeed(handle)
        except pynvml.NVMLError:
            fan_speed = "N/A"

        try:
            fan_num = pynvml.nvmlDeviceGetNumFans(handle)
        except pynvml.NVMLError:
            fan_num = DEFAULT_GPU

        try:
            clock_speed = gpu_main.clock_speed
        except Exception:
            clock_speed = "N/A"

        try:
            memory_clock = gpu_main.memory_clock
        except Exception:
            memory_clock = "N/A"

        lst_fans = []
        for index_fan in range(fan_num):
            try:
                fan = pynvml.nvmlDeviceGetFanSpeed_v2(handle, index_fan)
                lst_fans.append(f"Fan {index_fan} - {fan} %")
            except pynvml.NVMLError:
                lst_fans.append(f"Fan {index_fan} - N/A")
        fan_str = "\n".join(lst_fans) if lst_fans else "N/A"

        try:
            utilization = pynvml.nvmlDeviceGetUtilizationRates(handle)
            utilization_str = (f"GPU: {utilization.gpu} %\n"
                               f"Memory: {utilization.memory} %\n")
        except pynvml.NVMLError:
            utilization_str = ("GPU: N/A\n"
                               "Memory: N/A\n")

        try:
            power_usage = pynvml.nvmlDeviceGetPowerUsage(handle) / MW_TO_W
        except pynvml.NVMLError:
            power_usage = "N/A"

        try:
            power_limit = pynvml.nvmlDeviceGetPowerManagementLimit(handle) / MW_TO_W
        except pynvml.NVMLError:
            power_limit = "N/A"

        try:
            energy = pynvml.nvmlDeviceGetTotalEnergyConsumption(handle)
        except pynvml.NVMLError:
            energy = "N/A"

        try:
            pci_info = pynvml.nvmlDeviceGetPciInfo(handle)
            pci_str = (f"Bus ID: {pci_info.busId}\n"
                       f"Domain: {pci_info.domain}\n"
                       f"Bus: {pci_info.bus}\n"
                       f"Device: {pci_info.device}\n")
        except pynvml.NVMLError:
            pci_str = ("Bus ID: N/A\n"
                       "Domain: N/A\n"
                       "Bus: N/A\n"
                       "Device: N/A\n")

        lst_stat_gpu.append(f"Statistics GPU - number {number_device}:\n"
                            f"Name: {name}\n"
                            f"UUID: {uuid}\n"
                            f"Serial: {serial}\n"
                            f"{'=' * 20}\n"
                            f"Memory Info:\n{memory_str}"
                            f"{'=' * 20}\n"
                            f"Temperature: {temperature} ℃\n"
                            f"Max Temperature: {max_temperature} ℃\n"
                            f"Fan Speed (legacy): {fan_speed}\n"
                            f"Fan Numbers: {fan_num}\n"
                            f"{'=' * 20}\n"
                            f"Fan List:\n{fan_str}\n"
                            f"{'=' * 20}\n"
                            f"Utilization:\n{utilization_str}"
                            f"{'=' * 20}\n"
                            f"Power Usage: {power_usage} W\n"
                            f"Power Limit: {power_limit} W\n"
                            f"Energy: {energy} mJ\n"
                            f"{'=' * 20}\n"
                            f"PCI:\n{pci_str}"
                            f"{'=' * 20}\n"
                            f"Core Clock Speed: {clock_speed} MHz\n"
                            f"Memory Clock Speed: {memory_clock} MHz\n")

        return "\n".join(lst_stat_gpu)

    def analyzing_all_gpu(self) -> str:
        '''
        A function that serves to ensure that if a specific video card is not selected,
        all available discrete video cards are checked at once
        '''
        lst_answer = []
        for gpu_num in range(self.count_device):
            gpu = self.analyzing_specific_gpu(gpu_num)
            lst_answer.append(gpu)
        text = "\n".join(lst_answer)
        return text

    def __str__(self) -> str:
        '''
        Almost a beautiful conclusion for the end developer who will use this brainchild.
        '''
        return ("GPU STATUS:\n"
                f"{'-' * 20}\n"
                f"Driver Version: {self.driver_version()}\n"
                f"NVML Version: {self.nvml_version()}\n"
                f"Count Device: {self.count_device}\n\n"
                f"GPU STATISTICS:\n"
                f"{'-' * 20}\n"
                f"{self.analyzing_all_gpu()}\n")

    def __del__(self):
        '''
        A function for closing all internal processes of a class after it is deleted.
        '''
        pynvml.nvmlShutdown()


if __name__ == "__main__":
    analys_gpu_test = AnalyzerGPU()
    print(analys_gpu_test)