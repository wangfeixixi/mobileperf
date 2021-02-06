import os
import subprocess

from mobileperf.android.globaldata import RuntimeData


def deal_cmd(cmd):
    pi = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)

    # print(pi.stdin.read())
    return pi.stdout.read()


def deal_result():
    result = deal_cmd('adb devices')
    result = result.decode("utf-8")
    if result.startswith('List of devices attached'):
        # 查看连接设备
        result = result.strip().splitlines()
        # 查看连接设备数量
        device_size = len(result)
        if device_size > 1:
            device_list = []
            for i in range(1, device_size):
                device_detail = result[1].split('\t')
                if device_detail[1] == 'device':
                    device_list.append(device_detail[0])
                elif device_detail[1] == 'offline':
                    print(device_detail[0])
                    return False, '连接出现异常，设备无响应'
                elif device_detail[1] == 'unknown':
                    print(device_detail[0])
                    return False, '没有连接设备'
            return True, device_list
        else:
            return False, "没有可用设备"


# print(deal_result())
#
# test = os.getcwd()
# print(test)