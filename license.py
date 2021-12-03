import platform
import uuid
if platform.platform().find('Windows') >= 0:
    import wmi

class Hardware:
    @staticmethod
    def get_cpu_sn():
        """
        获取CPU序列号
        :return: CPU序列号
        """
        if platform.platform().find('Windows') >= 0:
            c = wmi.WMI()
            for cpu in c.Win32_Processor():
                return cpu.ProcessorId.strip()

    @staticmethod
    def get_baseboard_sn():
        """
        获取主板序列号
        :return: 主板序列号
        """
        if platform.platform().find('Windows') >= 0:
            c = wmi.WMI()
            for board_id in c.Win32_BaseBoard():
                return board_id.SerialNumber

    @staticmethod
    def get_bios_sn():
        """
        获取BIOS序列号
        :return: BIOS序列号
        """
        if platform.platform().find('Windows') >= 0:
            c = wmi.WMI()
            for bios_id in c.Win32_BIOS():
                return bios_id.SerialNumber.strip()

    @staticmethod
    def get_disk_sn():
        """
        获取硬盘序列号
        :return: 硬盘序列号列表
        """
        if platform.platform().find('Windows') >= 0:
            c = wmi.WMI()
            disk_sn_list = []
            for physical_disk in c.Win32_DiskDrive():
                disk_sn_list.append(physical_disk.SerialNumber.replace(" ", ""))
            return disk_sn_list
    
    @staticmethod
    def get_mac_address():
        """
        网卡MAC地址，是可以被修改的
        """
        return uuid.UUID(int = uuid.getnode()).hex[-12:]


if __name__ == '__main__':
    print(platform.node())
    print("MAC地址：{}".format(Hardware.get_mac_address()))
    print("CPU序列号：{}".format(Hardware.get_cpu_sn()))
    print("主板序列号：{}".format(Hardware.get_baseboard_sn()))
    print("Bios序列号：{}".format(Hardware.get_bios_sn()))
    print("硬盘序列号：{}".format(Hardware.get_disk_sn()))

