MIN_IP_LENGTH = 7
MAX_IP_LENGTH = 15
OCTET_COUNT = 4
BITS_IN_OCTET = 8
MAX_OCTET_VALUE = 255
MIN_OCTET_VALUE = 0

# ====== Валидный ли введённый IP-адрес? ======
def is_valid_ip_address(ip_address: str) -> bool:
    try:
        if len(ip_address) < MIN_IP_LENGTH or len(ip_address) > MAX_IP_LENGTH:
            return False
        else:
            x_1 = ip_address.split(".")
            if len(x_1) == OCTET_COUNT:
                for i in x_1:
                    if int(i) < MIN_OCTET_VALUE or int(i) > MAX_OCTET_VALUE:
                        return False
                return True
    except ValueError:
        return False

# ====== Бинарное педставление введённого IP-адреса ======
def bin_ip_address(ip_address: str) -> str:
    if not is_valid_ip_address(ip_address):
        return "Неверный формат IP-адреса!"

    try:
        x_1 = ip_address.split(".")
        y = []
        for i in x_1:
            y.append(bin(int(i))[2:])

        y_1 = []
        for g in y:
            if len(g) < BITS_IN_OCTET:
                len_g = BITS_IN_OCTET - len(g)
                y_1.append("0" * len_g + g)
            elif len(g) == BITS_IN_OCTET:
                y_1.append(g)
        return ".".join(y_1)
    except Exception as e:
        return f"Неизвеастная ошибка - {e}"

# ====== Класс введённого IP-адреса ======
def class_ip_address(ip_address: str) -> str:
    if not is_valid_ip_address(ip_address):
        return "Неверный формат IP-адреса!"

    try:
        x_1 = ip_address.split(".")
        y = int(x_1[0])
        if 1 <= y <= 126:
            return "A"
        elif 128 <= y <= 191:
            return "B"
        elif 192 <= y <= 223:
            return "C"
        elif 224 <= y <= 239:
            return "D"
        elif 240 <= y <= 255:
            return "E"
        else:
            return "Неопределенный класс"
    except Exception as e:
        return f"Неизвеастная ошибка - {e}"

# ====== Тип введённого IP-адреса ======
def private_ip_address(ip_address: str) -> str:
    if not is_valid_ip_address(ip_address):
        return "Неверный формат IP-адреса!"

    try:
        x_1 = ip_address.split(".")
        if int(x_1[0]) == 10:
            return f"Приватный"
        elif int(x_1[0]) == 172 and 16 <= int(x_1[1]) <= 31:
            return f"Приватный"
        elif int(x_1[0]) == 192 and int(x_1[1]) == 168:
            return f"Приватный"
        else:
            return f"Открытый"
    except Exception as e:
        return f"Неизвеастная ошибка - {e}"

# ====== Маска по умолчанию для введённого IP-адреса ======
def default_mask(ip_address: str) -> str:
    if not is_valid_ip_address(ip_address):
        return "Неверный формат IP-адреса!"

    try:
        class_ip_adr = class_ip_address(ip_address)
        if class_ip_adr == "A":
            return "255.0.0.0"
        elif class_ip_adr == "B":
            return "255.255.0.0"
        elif class_ip_adr == "C":
            return "255.255.255.0"
        elif class_ip_adr == "D":
            return "Не имеет маски по умолчанию"
        elif class_ip_adr == "E":
            return "Не имеет маски по умолчанию"
        else:
            return "Неопределенная маска - класс не найден"
    except Exception as e:
        return f"Неизвеастная ошибка - {e}"

# ====== Бинарное представление маски по умолчанию ======
def bin_default_mask(ip_address: str) -> str:
    ip_address = default_mask(ip_address)
    if not is_valid_ip_address(ip_address):
        return "Неверный формат IP-адреса!"

    try:
        y_1 = ip_address.split(".")
        x_1 = []
        for i in y_1:
            x_1.append(bin(int(i))[2:])

        y_2 = []
        for g in x_1:
            if len(g) < BITS_IN_OCTET:
                len_g = BITS_IN_OCTET - len(g)
                y_2.append("0" * len_g + g)
            elif len(g) == BITS_IN_OCTET:
                y_2.append(g)
        h = ".".join(y_2)
        return h
    except Exception as e:
        return f"Неизвеастная ошибка - {e}"

# ====== Номер сети для введённого IP-адреса ======
def net_id(ip_address: str) -> str:
    try:
        if not is_valid_ip_address(ip_address):
            return "Неверный формат IP-адреса!"

        mask = default_mask(ip_address)
        if not is_valid_ip_address(mask):
            return "Не имеет маски по умолчанию"

        ip_octets = [int(x) for x in ip_address.split(".")]
        mask_octets = [int(x) for x in mask.split(".")]

        net_octets = []
        for ip_octet, mask_octet in zip(ip_octets, mask_octets):
            net_octets.append(str(ip_octet & mask_octet))  # Побитовое И

        return ".".join(net_octets)

    except Exception as e:
        return f"Неизвестная ошибка - {e}"

# ====== Номер сети и номер узла для введённого IP-адреса ======
def net_id_host_id(ip_address: str) -> str:
    if not is_valid_ip_address(ip_address):
        return "Неверный формат IP-адреса!"

    try:
        mask = default_mask(ip_address)
        if not is_valid_ip_address(mask):
            return "Не имеет маски по умолчанию"
        mask_octets = mask.split(".")
        template = []
        for octet in mask_octets:
            if octet == "255":
                template.append("N")
            elif octet == "0":
                template.append("H")
            else:
                template.append("X")
        return ".".join(template)
    except Exception as e:
        return f"Неизвестная ошибка - {e}"


def read_file_txt(file_name):
    try:
        y_1 = []
        with open(f"{file_name}", "r", encoding="utf-8") as file:
            lines = file.readlines()
            for line in lines:
                y_1.append(line.strip())
            return y_1
    except Exception as e:
        return f"Неизвестная ошибка - {e}"


if __name__ == "__main__":
    y = read_file_txt("ip_address.txt")
    for i in y:
        result = bin_ip_address(i)
        result_1 = class_ip_address(i)
        result_2 = private_ip_address(i)
        result_3 = default_mask(i)
        result_4 = bin_default_mask(i)
        result_5 = net_id_host_id(i)
        result_6 = net_id(i)
        print(f"IP-адрес: {i}")
        print(f"Бинарное представление IP-адреса: {result}")
        print(f"Класс IP-адреса: {result_1}")
        print(f"Тип IP-адрес: {result_2}")
        print(f"Маска по умолчанию: {result_3}")
        print(f"Бинарное представление маски по умолчанию: {result_4}")
        print(f"Номер сети и номер узла: {result_5}")
        print(f"Номер сети: {result_6}")
        print("\n")