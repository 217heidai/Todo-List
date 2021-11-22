import os
from aip import AipSpeech


class TTS_BAIDU(object):
    def __init__(self):
        self.__APP_ID = '25204844'
        self.__APP_KEY = 'b9lE7chWHxGBTzR7DZRXuOx0'
        self.__SECRET_KEY = 'GpN3Hl8QTL6wVOxI6LKXMfFCvKKLiX8W'
        self.__client = AipSpeech(self.__APP_ID, self.__APP_KEY, self.__SECRET_KEY)

    def TTS(self, text, filename):
        if os.path.exists(filename):
            return True
        result  = self.__client.synthesis(text*20, 'zh', 1, {'spd': 5, 'vol': 5, 'per': 1})
        # 识别正确返回语音二进制 错误则返回dict 参照下面错误码
        if not isinstance(result, dict):
            #if os.path.exists(filename):
            #    os.remove(filename)
            with open(filename, 'wb') as f:
                f.write(result)
                return True
        return False



if __name__ == '__main__':
    from pygame import mixer
    def test(text, filename):
        baidu = TTS_BAIDU()
        baidu.TTS(text, filename)
        mixer.init()
        mixer.music.load(filename)
        mixer.music.play()
        while mixer.music.get_busy():
            pass
        mixer.music.stop()
        
    text = '现在是7点50分，请提醒作战勤务值班员组织交班。'
    filename = os.getcwd() + '/alarms/现在是7点50分，请提醒作战勤务值班员组织交班。.wav'
    test(text, filename)

        