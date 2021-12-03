from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.Qt import *
from panel import Ui_MainWindow
import os
from datetime import datetime
#import calendar
import sqlite3
from pygame import mixer
import webbrowser
from zhon.hanzi import punctuation
from croniter import croniter

from tts import TTS_BAIDU
from conf import Config

date_full = str(datetime.now().strftime('%Y-%m-%d')).split('-')
date_name = 'date'+date_full[0]+date_full[1]+date_full[2]

conn = sqlite3.connect('todo.db')
c = conn.cursor()
# status 0-待执行，1-已执行，2-已停用
c.execute(f'''CREATE TABLE IF NOT EXISTS {date_name}(
            id integer PRIMARY KEY,
            task text,
            status integer,
            time time
         )''')
conn.commit()
# status 0-有效，1-无效
c.execute(f'''CREATE TABLE IF NOT EXISTS crontabtask(
            id integer PRIMARY KEY,
            task text,
            status integer,
            crontab text
         )''')
conn.commit()
# 创建索引
try:
    c.execute(f'CREATE UNIQUE INDEX index_crontabtask ON crontabtask(task)')
    conn.commit()
except Exception as e:
    pass

page_time = 0
number_task = int()
number = 0


class Root(QMainWindow):

    def __init__(self):
        #获取显示器分辨率
        self.desktop = QApplication.desktop()
        self.screenRect = self.desktop.screenGeometry()
        self.screenheight = self.screenRect.height()
        self.screenwidth = self.screenRect.width()
        print("Screen: %sx%s"%(self.screenwidth, self.screenheight))

        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self, self.screenwidth, self.screenheight)

        #self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        #设置支持最大化
        self.showMaximized()
        self.setWindowFlags(Qt.WindowMaximizeButtonHint | Qt.WindowCloseButtonHint | Qt.WindowMinimizeButtonHint)

        self.show()

        self.__initUI()

        # 插入默认待办
        self.__taskDefault()

        self.set_task()

        timer = QTimer(self)
        timer.timeout.connect(self.timer)
        timer.start(1000)

        self.ui.submit.clicked.connect(self.submit)
        self.ui.submit_2.clicked.connect(self.submit2)

        # timer
        self.ui.timer1.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.set_timer))
        self.ui.timer1.clicked.connect(self.active_task1)
        self.ui.timer1.clicked.connect(self.page_clock)
        self.ui.timer2.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.set_timer))
        self.ui.timer2.clicked.connect(self.active_task2)
        self.ui.timer2.clicked.connect(self.page_clock)
        self.ui.timer3.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.set_timer))
        self.ui.timer3.clicked.connect(self.active_task3)
        self.ui.timer3.clicked.connect(self.page_clock)
        self.ui.timer4.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.set_timer))
        self.ui.timer4.clicked.connect(self.active_task4)
        self.ui.timer4.clicked.connect(self.page_clock)
        self.ui.timer5.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.set_timer))
        self.ui.timer5.clicked.connect(self.active_task5)
        self.ui.timer5.clicked.connect(self.page_clock)
        self.ui.timer6.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.set_timer))
        self.ui.timer6.clicked.connect(self.active_task6)
        self.ui.timer6.clicked.connect(self.page_clock)
        self.ui.timer7.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.set_timer))
        self.ui.timer7.clicked.connect(self.active_task7)
        self.ui.timer7.clicked.connect(self.page_clock)
        self.ui.timer8.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.set_timer))
        self.ui.timer8.clicked.connect(self.active_task8)
        self.ui.timer8.clicked.connect(self.page_clock)
        self.ui.timer9.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.set_timer))
        self.ui.timer9.clicked.connect(self.active_task9)
        self.ui.timer9.clicked.connect(self.page_clock)
        self.ui.timer10.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.set_timer))
        self.ui.timer10.clicked.connect(self.active_task10)
        self.ui.timer10.clicked.connect(self.page_clock)

        self.ui.cancel_time.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.day_task))
        self.ui.cancel_time.clicked.connect(self.page_clock_cancel)
        self.ui.sub_time.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.day_task))
        self.ui.sub_time.clicked.connect(self.set_clock)
        self.ui.ok_clock.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.day_task))
        self.ui.ok_clock.clicked.connect(self.stop_clock)

        # pages
        self.ui.comp1.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.completed))
        self.ui.comp1.clicked.connect(self.page_clock)
        self.ui.comp2.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.completed))
        self.ui.comp2.clicked.connect(self.page_clock)
        self.ui.comp4.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.completed))
        self.ui.comp4.clicked.connect(self.page_clock)
        self.ui.comp5.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.completed))
        self.ui.comp5.clicked.connect(self.page_clock)

        self.ui.my_day3.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.day_task))
        self.ui.my_day3.clicked.connect(self.page_clock_cancel)
        self.ui.my_day4.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.day_task))
        self.ui.my_day4.clicked.connect(self.page_clock_cancel)
        self.ui.my_day5.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.day_task))
        self.ui.my_day5.clicked.connect(self.page_clock_cancel)

        self.ui.calender1.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.calender))
        self.ui.calender1.clicked.connect(self.page_clock)
        self.ui.calender2.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.calender))
        self.ui.calender2.clicked.connect(self.page_clock)
        self.ui.calender3.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.calender))
        self.ui.calender3.clicked.connect(self.page_clock)
        self.ui.calender5.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.calender))
        self.ui.calender5.clicked.connect(self.page_clock)

        self.ui.about1.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.about))
        self.ui.about1.clicked.connect(self.page_clock)
        self.ui.about2.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.about))
        self.ui.about2.clicked.connect(self.page_clock)
        self.ui.about3.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.about))
        self.ui.about3.clicked.connect(self.page_clock)
        self.ui.about4.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.about))
        self.ui.about4.clicked.connect(self.page_clock)

        self.ui.search_cal.clicked.connect(self.calender_search)

        # del task
        self.ui.delete1.clicked.connect(self.active_task1)
        self.ui.delete1.clicked.connect(self.remove_task)
        self.ui.delete2.clicked.connect(self.active_task2)
        self.ui.delete2.clicked.connect(self.remove_task)
        self.ui.delete3.clicked.connect(self.active_task3)
        self.ui.delete3.clicked.connect(self.remove_task)
        self.ui.delete4.clicked.connect(self.active_task4)
        self.ui.delete4.clicked.connect(self.remove_task)
        self.ui.delete5.clicked.connect(self.active_task5)
        self.ui.delete5.clicked.connect(self.remove_task)
        self.ui.delete6.clicked.connect(self.active_task6)
        self.ui.delete6.clicked.connect(self.remove_task)
        self.ui.delete7.clicked.connect(self.active_task7)
        self.ui.delete7.clicked.connect(self.remove_task)
        self.ui.delete8.clicked.connect(self.active_task8)
        self.ui.delete8.clicked.connect(self.remove_task)
        self.ui.delete9.clicked.connect(self.active_task9)
        self.ui.delete9.clicked.connect(self.remove_task)
        self.ui.delete10.clicked.connect(self.active_task10)
        self.ui.delete10.clicked.connect(self.remove_task)

        # Completed task
        self.ui.sub1.clicked.connect(self.active_task1)
        self.ui.sub1.clicked.connect(self.sub_task)
        self.ui.sub2.clicked.connect(self.active_task2)
        self.ui.sub2.clicked.connect(self.sub_task)
        self.ui.sub3.clicked.connect(self.active_task3)
        self.ui.sub3.clicked.connect(self.sub_task)
        self.ui.sub4.clicked.connect(self.active_task4)
        self.ui.sub4.clicked.connect(self.sub_task)
        self.ui.sub5.clicked.connect(self.active_task5)
        self.ui.sub5.clicked.connect(self.sub_task)
        self.ui.sub6.clicked.connect(self.active_task6)
        self.ui.sub6.clicked.connect(self.sub_task)
        self.ui.sub7.clicked.connect(self.active_task7)
        self.ui.sub7.clicked.connect(self.sub_task)
        self.ui.sub8.clicked.connect(self.active_task8)
        self.ui.sub8.clicked.connect(self.sub_task)
        self.ui.sub9.clicked.connect(self.active_task9)
        self.ui.sub9.clicked.connect(self.sub_task)
        self.ui.sub10.clicked.connect(self.active_task10)
        self.ui.sub10.clicked.connect(self.sub_task)

        # link contact
        self.ui.contactme.clicked.connect(self.contact)

        # 8项待办事项的ID
        self.__taskIdList = []

        # 当前选中任务的ID
        self.__taskIdActive = -1

        # 是否倒计时
        self.__isCountdown = False

        self.tts = TTS_BAIDU()

    def __initUI(self):
        # 今日待办UI
        self.__ui_task_list = [[self.ui.task1, self.ui.sub1, self.ui.delete1, self.ui.timer1],
                               [self.ui.task2, self.ui.sub2, self.ui.delete2, self.ui.timer2],
                               [self.ui.task3, self.ui.sub3, self.ui.delete3, self.ui.timer3],
                               [self.ui.task4, self.ui.sub4, self.ui.delete4, self.ui.timer4],
                               [self.ui.task5, self.ui.sub5, self.ui.delete5, self.ui.timer5],
                               [self.ui.task6, self.ui.sub6, self.ui.delete6, self.ui.timer6],
                               [self.ui.task7, self.ui.sub7, self.ui.delete7, self.ui.timer7],
                               [self.ui.task8, self.ui.sub8, self.ui.delete8, self.ui.timer8],
                               [self.ui.task9, self.ui.sub9, self.ui.delete9, self.ui.timer9],
                               [self.ui.task10, self.ui.sub10, self.ui.delete10, self.ui.timer10]]

        # 今日办结UI
        self.__ui_completed_list = [self.ui.com1,
                                    self.ui.com2,
                                    self.ui.com3,
                                    self.ui.com4,
                                    self.ui.com5,
                                    self.ui.com6,
                                    self.ui.com7,
                                    self.ui.com8,
                                    self.ui.com9,
                                    self.ui.com10,
                                    self.ui.com11,
                                    self.ui.com12,
                                    self.ui.com13,
                                    self.ui.com14,
                                    self.ui.com15, 
                                    self.ui.com16,
                                    self.ui.com17,
                                    self.ui.com18,
                                    self.ui.com19,
                                    self.ui.com20]

        # 待办查询UI
        self.__ui_calender_com_List = [[self.ui.com1_cal, self.ui.True1],
                                       [self.ui.com2_cal, self.ui.True2],
                                       [self.ui.com3_cal, self.ui.True3],
                                       [self.ui.com4_cal, self.ui.True4],
                                       [self.ui.com5_cal, self.ui.True5],
                                       [self.ui.com6_cal, self.ui.True6],
                                       [self.ui.com7_cal, self.ui.True7],
                                       [self.ui.com8_cal, self.ui.True8],
                                       [self.ui.com9_cal, self.ui.True9],
                                       [self.ui.com10_cal, self.ui.True10]]
        self.__ui_calender_task_List = [[self.ui.task1_cal, self.ui.False1],
                                        [self.ui.task2_cal, self.ui.False2],
                                        [self.ui.task3_cal, self.ui.False3],
                                        [self.ui.task4_cal, self.ui.False4],
                                        [self.ui.task5_cal, self.ui.False5],
                                        [self.ui.task6_cal, self.ui.False6],
                                        [self.ui.task7_cal, self.ui.False7],
                                        [self.ui.task8_cal, self.ui.False8],
                                        [self.ui.task9_cal, self.ui.False9],
                                        [self.ui.task10_cal, self.ui.False10]]

        conf = Config(os.getcwd() + '/conf/conf.ini')
        
        # set APP name
        nameapp = conf.getConfig('APP', 'name')
        if nameapp is not None:
            self.ui.nameapp.setText(nameapp)
            self.ui.nameapp2.setText(nameapp)
            self.ui.nameapp_4.setText(nameapp)
            self.ui.nameapp_5.setText(nameapp)
            self.ui.nameapp_7.setText(nameapp)
            #self.ui.setWindowTitle(nameapp)

        # set username and profile
        user = conf.getConfig('USER', 'name')
        if user is None:
            user = os.getlogin()
        profile = str(user)[0]
        self.ui.nameuser.setText(user)
        self.ui.profile.setText(profile)
        self.ui.nameuser2.setText(user)
        self.ui.profile2.setText(profile)
        self.ui.nameuser2_2.setText(user)
        self.ui.profile2_2.setText(profile)
        self.ui.nameuser2_3.setText(user)
        self.ui.profile2_3.setText(profile)
        self.ui.nameuser5.setText(user)
        self.ui.profile5.setText(profile)

        # set title
        title1 = conf.getConfig('TITLE', 'title1')
        title2 = conf.getConfig('TITLE', 'title2')
        title3 = conf.getConfig('TITLE', 'title3')
        title4 = conf.getConfig('TITLE', 'title4')
        if title1 is not None:
            #self.ui.myday1.setText(title1)
            #self.ui.label_7.setText(title1)
            self.ui.myday_title.setText(title1) # 左侧栏点击“今日待办”后，主窗口显示
            #self.ui.myday2.setText(title1) # 左侧栏“今日待办”
            #self.ui.my_day3.setText(title1) # 左侧栏点击“今日完结”后显示
            #self.ui.my_day4.setText(title1) # 左侧栏点击“待办查询”后显示
            #self.ui.my_day5.setText(title1) # 左侧栏点击“关于”后显示
        if title2 is not None:
            #self.ui.comp1.setText(title2)
            self.ui.completed_title.setText(title2) # 左侧栏点击“今日完结”后，主窗口显示
            #self.ui.comp2.setText(title2) # 左侧栏点击“今日待办”后显示
            #self.ui.comp3.setText(title2) # 左侧栏点击“今日完结”后显示
            #self.ui.comp4.setText(title2) # 左侧栏点击“待办查询”后显示
            #self.ui.comp5.setText(title2) # 左侧栏点击“关于”后显示
        if title3 is not None:
            #self.ui.calender1.setText(title3)
            self.ui.calender_title.setText(title3) # 左侧栏点击“待办查询”后，主窗口显示
            #self.ui.calender2.setText(title3) # 左侧栏点击“今日待办”后显示
            #self.ui.calender3.setText(title3) # 左侧栏点击“今日完结”后显示
            #self.ui.calender4.setText(title3) # 左侧栏点击“待办查询”后显示
            #self.ui.calender5.setText(title3) # 左侧栏点击“关于”后显示
        if title4 is not None:
            #self.ui.about1.setText(title4)
            self.ui.about_title.setText(title4) # 左侧栏点击“关于”后，主窗口显示
            #self.ui.about2.setText(title4) # 左侧栏点击“今日待办”后显示
            #self.ui.about3.setText(title4) # 左侧栏点击“今日完结”后显示
            #self.ui.about4.setText(title4) # 左侧栏点击“待办查询”后显示
            #self.ui.about4_3.setText(title4) # 左侧栏点击“关于”后显示

        #self.ui.addtask.setPlaceholderText("Add a Task")
        self.ui.addtask.setPlaceholderText("添加待办")
        #self.ui.addtask_3.setPlaceholderText("Add a Task")
        self.ui.addtask_3.setPlaceholderText("添加待办")

        now = datetime.now()
        self.ui.date_cal.setPlaceholderText('请输入日期查询：%s'%(now.strftime('%Y/%m/%d')))

        # set date
        date_full2 = str(datetime.now().strftime('%Y-%m-%d'))
        week = {0:'星期一', 1:'星期二', 2:'星期三', 3:'星期四', 4:'星期五', 5:'星期六', 6:'星期日'}
        today = '%s年%s月%s日，%s' % (date_full2[:4], date_full2[5:7], date_full2[8:], week[datetime.now().weekday()])
        self.ui.date.setText(today)
        self.ui.date2.setText(today)
        self.ui.date3.setText(today)

    def mousePressEvent(self, evt):
        self.oldPos = evt.globalPos()

    def mouseMoveEvent(self, evt):
        if not self.windowState() == Qt.WindowFullScreen: # 仅非全屏状态下可以拖动窗口
            delta = QPoint(evt.globalPos() - self.oldPos)
            self.move(self.x() + delta.x(), self.y() + delta.y())
            self.oldPos = evt.globalPos()

    def submit(self):
        global number_task
        text = self.ui.addtask.text()
        self.ui.addtask.clear()
        if len(text) == 0:
            #self.ui.addtask.setPlaceholderText("Please type a Task")
            self.ui.addtask.setPlaceholderText("请输入待办事项")
        else:
            number_task += 1
            self.add_task(number_task, text)

    def submit2(self):
        global number_task
        text = self.ui.addtask_3.text()
        self.ui.addtask_3.clear()
        if len(text) == 0:
            #self.ui.addtask_3.setPlaceholderText("Please type a Task")
            self.ui.addtask_3.setPlaceholderText("请输入待办事项")
        else:
            number_task += 1
            self.add_task(number_task, text)

    def add_task(self, num, txt):
        global c
        global conn
        global date_name

        new_data = ("""INSERT INTO {}(id, task, status, time) VALUES (null,'{}',{},'{}');""".format(date_name, str(txt), 0, '00:00:00'))
        c.execute(new_data)
        conn.commit()
        self.set_task()

    def __taskDefault(self):
        def insert(c, conn, task, crontab):
            new_data = ("""INSERT INTO crontabtask(id, task, status, crontab) VALUES (null,'{}',{},'{}');""".format(task, 0, crontab))
            c.execute(new_data)
            conn.commit()

        global c
        global conn
        global date_name

        rows = c.execute(f'SELECT COUNT(*) FROM crontabtask')
        for row in rows:
            if row[0] > 0:
                return

        # 插入默认任务
        insert(c, conn, '执勤监控安全员同志，请督导前置人员清整卫生。',  '00 07 * * *')
        insert(c, conn, '现在是7点50分，请提醒作战勤务值班员组织交班。', '50 07 * * *')

    def __taskCrontab(self):
        global c
        global conn
        global date_name

        rows = c.execute(f'SELECT task,crontab FROM crontabtask WHERE crontab<>"* * * * *"')
        for row in rows:
            task = row[0]
            crontab = row[1]
            iter = croniter(crontab,datetime.now())
            time = iter.get_next(datetime)
            date = 'date' + time.strftime("%Y%m%d")
            time = time.strftime('%H:%M:%S')
            if date == date_name:
                tmp_rows = c.execute(f'SELECT COUNT(*) FROM {date_name} WHERE task="{task}" AND time="{time}"')
                for tmp_row in tmp_rows:
                    if tmp_row[0] == 0:
                        c.execute("""INSERT INTO {}(id, task, status, time) VALUES (null,'{}',{},'{}');""".format(date_name, task, 0, time))
                        conn.commit()

    def set_task(self):
        global number
        global date_name
        global page_time

        # 根据定时任务，插入下次执行
        self.__taskCrontab()

        number = 0
        rows = c.execute(f'SELECT COUNT(*) FROM {date_name} WHERE status=0')
        for row in rows:
            number = row[0]
            break

        if number == 0 and page_time != 1:
            self.ui.stackedWidget.setCurrentWidget(self.ui.day)

        # 清空任务ID
        self.__taskIdList = []
        count = 0
        tasks = c.execute(f'SELECT * FROM {date_name} WHERE status=0 ORDER BY time ASC')
        #id, task, status, time
        for row in tasks:
            if count == 0:
                if page_time != 1:
                    self.ui.stackedWidget.setCurrentWidget(self.ui.day_task)
            
            if count >= len(self.__ui_task_list):
                break
            self.__ui_task_list[count][0].show()
            self.__ui_task_list[count][0].setText(row[1])
            self.__ui_task_list[count][1].show()
            self.__ui_task_list[count][2].show()
            self.__ui_task_list[count][3].show()
            self.__taskIdList.append(row[0])
            count += 1

        #重新设置number
        number = count

    def set_completed(self):
        global c
        global date_name
        
        count = 0
        tasks = c.execute(f'SELECT * FROM {date_name} WHERE status=1 ORDER BY time ASC')
        for row in tasks:
            if count >= len(self.__ui_completed_list):
                break
            self.__ui_completed_list[count].show()
            self.__ui_completed_list[count].setText(row[1])
            count += 1

    def active_task1(self):
        print('active task 1: %s'%self.ui.task1.text())
        self.__taskIdActive = self.__taskIdList[0]

    def active_task2(self):
        print('active task 2: %s'%self.ui.task2.text())
        self.__taskIdActive = self.__taskIdList[1]

    def active_task3(self):
        print('active task 3: %s'%self.ui.task3.text())
        self.__taskIdActive = self.__taskIdList[2]

    def active_task4(self):
        print('active task 4: %s'%self.ui.task4.text())
        self.__taskIdActive = self.__taskIdList[3]

    def active_task5(self):
        print('active task 5: %s'%self.ui.task5.text())
        self.__taskIdActive = self.__taskIdList[4]

    def active_task6(self):
        print('active task 6: %s'%self.ui.task6.text())
        self.__taskIdActive = self.__taskIdList[5]

    def active_task7(self):
        print('active task 7: %s'%self.ui.task7.text())
        self.__taskIdActive = self.__taskIdList[6]

    def active_task8(self):
        print('active task 8: %s'%self.ui.task8.text())
        self.__taskIdActive = self.__taskIdList[7]

    def active_task9(self):
        print('active task 9: %s'%self.ui.task9.text())
        self.__taskIdActive = self.__taskIdList[8]

    def active_task10(self):
        print('active task 10: %s'%self.ui.task10.text())
        self.__taskIdActive = self.__taskIdList[9]

    def remove_task(self):
        global c
        global conn
        global number
        global date_name

        if self.__taskIdActive > -1:
            c.execute(f'UPDATE {date_name} SET status=2 WHERE id=%s'%(self.__taskIdActive))
            conn.commit()
            self.remover(number)
            self.set_task()

    def remover(self, num):
        for items in self.__ui_task_list:
            items[0].clear()

        self.__ui_task_list[num - 1][0].hide()
        self.__ui_task_list[num - 1][1].hide()
        self.__ui_task_list[num - 1][2].hide()
        self.__ui_task_list[num - 1][3].hide()

    def page_clock(self):
        global page_time
        page_time = 1

        if self.__taskIdActive > -1:
            rows = c.execute(f'SELECT task,time FROM {date_name} WHERE id=%s'%(self.__taskIdActive))
            for row in rows:
                task = row[0]
                time = row[1]
                break
            self.ui.hh.setText(time[:2])
            self.ui.mm.setText(time[3:5])
            self.ui.ss.setText(time[6:])

            crontab = '* * * * *'
            rows = c.execute(f'SELECT crontab FROM crontabtask WHERE task="{task}"')
            for row in rows:
                crontab = row[0]
                break
            self.ui.crontab.setText(crontab)

    def page_clock_cancel(self):
        global page_time
        page_time = 0

    def __play(self, text, loops):
        def punctuationMark(text):
            for i in punctuation:
                text = text.replace(i,'')
            return text
        # 播提示音
        mixer.init()
        mixer.music.load(os.getcwd() + '/alarms/提示音.wav')
        mixer.music.play()
        while mixer.music.get_busy():
            pass
        mixer.music.stop()
        # 播语音
        newtext = punctuationMark(text)
        filename1 = os.getcwd() + '/alarms/' + newtext + '.wav'
        filename2 = os.getcwd() + '/alarms/' + newtext + '.mp3'
        filename = None
        if os.path.exists(filename1):
            filename = filename1
        if os.path.exists(filename2):
            filename = filename2
        
        if filename is not None:
            mixer.init()
            mixer.music.load(filename)
            mixer.music.play(loops = 3) # 循环播放3次
        '''
        filename1 = os.getcwd() + '/alarms/' + newtext + '.wav'
        filename2 = os.getcwd() + '/alarms/' + newtext + '.mp3'
        if os.path.exists(filename1):
            filename = filename1
        else:
            filename = filename2
        if self.tts.TTS(text, filename):
            mixer.init()
            mixer.music.load(filename)
            mixer.music.play(loops = 3)
        '''

    # 日切时清空今日待办、今日完结
    def __clearUI(self):
        # 清空今日待办
        for items in self.__ui_task_list:
            for item in items:
                item.clear()
                item.hide()
        # 清空今日完结
        for item in self.__ui_completed_list:
            item.clear()
            item.hide()

    def timer(self):
        global c
        global conn
        global date_name
        global date_full

        # get time
        currentTime = QTime.currentTime()
        display_text = currentTime.toString('hh:mm:ss')
        #self.ui.now_time.setText(display_text)

        # set date - database
        date_full = str(datetime.now().strftime('%Y-%m-%d')).split('-')
        name = 'date' + date_full[0] + date_full[1] + date_full[2]
        #日切
        if name != date_name:
            date_name = name

            # 刷新界面显示日期
            date_full2 = str(datetime.now().strftime('%Y-%m-%d'))
            week = {0:'星期一', 1:'星期二', 2:'星期三', 3:'星期四', 4:'星期五', 5:'星期六', 6:'星期日'}
            today = '%s年%s月%s日，%s' % (date_full2[:4], date_full2[5:7], date_full2[8:], week[datetime.now().weekday()])
            self.ui.date.setText(today)
            self.ui.date2.setText(today)
            self.ui.date3.setText(today)

            # 清空UI
            self.__clearUI()

            # 切换数据库表
            conn = sqlite3.connect('todo.db')
            c = conn.cursor()
            c.execute(f'''CREATE TABLE IF NOT EXISTS {date_name}(
                        id integer PRIMARY KEY,
                        task text,
                        status integer,
                        time time
                    )''')
            conn.commit()

        # Update task
        self.set_task()
        self.set_completed()

        # clock hh:mm:ss
        conf = Config(os.getcwd() + '/conf/conf.ini')
        # 获取提前提醒时间
        times = conf.getConfig('REMIND', 'time')
        if times is not None and times.isdigit():
            times = int(times)
        else:
            times = 5
        loops = conf.getConfig('REMIND', 'loops')
        if loops is not None and loops.isdigit():
            loops = int(loops)
        else:
            loops = 3
        td1 = datetime(int(date_full[0]), int(date_full[1]), int(date_full[2]), int(display_text[:2]), int(display_text[3:5]), int(display_text[-2:]), 0) - datetime(int(date_full[0]), int(date_full[1]), int(date_full[2]), 0, 0, 0, 0)
        task = c.execute(f'SELECT * FROM {date_name} WHERE status=0')
        # id task status time
        for row in task:
            td2 = datetime(int(date_full[0]), int(date_full[1]), int(date_full[2]), int(row[3][:2]), int(row[3][3:5]), int(row[3][-2:]), 0) - datetime(int(date_full[0]), int(date_full[1]), int(date_full[2]), 0, 0, 0, 0)
            if td2 > td1:
                if (td2 - td1).seconds == times * 60:
                    self.__taskIdActive = row[0]
                    self.ui.tasktime_task.setText(row[1])
                    self.__isCountdown = True
                    self.ui.now_time.setText('00:%02d:00'%(times))
                    self.ui.stackedWidget.setCurrentWidget(self.ui.stop_timer)
                if (td2 - td1).seconds < times * 60 and self.__isCountdown:
                    hour = int((td2 - td1).seconds/60/60)
                    minute = int(((td2 - td1).seconds - hour * 60 * 60)/60)
                    second = (td2 - td1).seconds - hour * 60 * 60 - minute * 60
                    self.ui.now_time.setText('%02d:%02d:%02d'%(hour, minute, second))
            if td2 == td1:
                self.__isCountdown = False
                self.__taskIdActive = row[0]
                self.ui.tasktime_task.setText(row[1])
                self.ui.now_time.setText(row[3])
                self.ui.stackedWidget.setCurrentWidget(self.ui.stop_timer)
                # 播提示音
                self.__play(row[1], loops)

    def set_clock(self):
        def updatetask(c, conn, date_name, id, date, time, number):
            # 将今日任务的执行实现更新为crontab的下次执行时间
            if date == date_name: #下次执行时间为当天的则更新时间
                c.execute("""UPDATE {} SET time="{}" WHERE id={}""".format(date_name, time, id))
                conn.commit()
            else: #下次执行时间为非当天的则删除今日的任务
                c.execute("""DELETE FROM {} WHERE id={}""".format(date_name, id))
                conn.commit()
                self.remover(number)

        global c
        global conn
        global date_name
        global number

        if self.__taskIdActive > -1:
            # 获取task
            rows = c.execute(f'SELECT task FROM %s WHERE id=%s'%(date_name, self.__taskIdActive))
            for row in rows:
                task = row[0]
                break
            crontabInSQL = None
            rows = c.execute(f'SELECT crontab FROM crontabtask WHERE task="{task}"')
            for row in rows:
                crontabInSQL = row[0]
                break

            # 更新定时任务
            try:
                crontab = self.ui.crontab.text()
                iter=croniter(crontab, datetime.now())
                time = iter.get_next(datetime)
                date = 'date' + time.strftime("%Y%m%d")
                time = time.strftime('%H:%M:%S')
                if crontabInSQL is not None:
                    if crontab != crontabInSQL:
                        # 更新定时任务
                        c.execute(f'UPDATE crontabtask SET crontab="{crontab}" WHERE task="{task}"')
                        conn.commit()
                        if crontab != '* * * * *':
                            # 更新下次执行时间
                            updatetask(c, conn, date_name, self.__taskIdActive, date, time, number)
                else:
                    if crontab != '* * * * *':
                        # 插入定时任务
                        c.execute("""INSERT INTO crontabtask(id, task, status, crontab) VALUES (null,'{}',{},'{}');""".format(task, 0, crontab))
                        conn.commit()
                        # 更新下次执行时间
                        updatetask(c, conn, date_name, self.__taskIdActive, date, time, number)
            except Exception as e:
                self.ui.crontab.setText('* * * * *')
                crontab = '* * * * *' #设置为无效

            # 更新今日任务
            if crontab == '* * * * *':
                # 设置时间
                hh = self.ui.hh.text()
                mm = self.ui.mm.text()
                ss = self.ui.ss.text()
                if hh.isdigit() and mm.isdigit() and ss.isdigit() and 0<=int(hh)<=23 and 0<=int(mm)<=60 and 0<=int(ss)<=60:
                    hh = hh if len(hh) == 2 else '0' + hh
                    mm = mm if len(mm) == 2 else '0' + mm
                    ss = ss if len(ss) == 2 else '0' + ss
                    clock = hh+':'+mm+':'+ss
                    c.execute(f'UPDATE %s SET time="%s" WHERE id=%s'%(date_name, clock, self.__taskIdActive))
                    conn.commit()

    def stop_clock(self):
        global c
        global conn
        global date_name
        global date_full
        global number

        # 关闭语音播报
        try:
            mixer.music.stop()
        except Exception as e:
            pass
        
        self.__isCountdown = False
        currentTime = QTime.currentTime()
        display_text = currentTime.toString('hh:mm:ss')
        td1 = datetime(int(date_full[0]), int(date_full[1]), int(date_full[2]), int(display_text[:2]), int(display_text[3:5]), int(display_text[-2:]), 0) - datetime(int(date_full[0]), int(date_full[1]), int(date_full[2]), 0, 0, 0, 0)
        rows = c.execute(f'SELECT * FROM {date_name} WHERE id={self.__taskIdActive} AND status=0')
        # id task status time
        for row in rows:
            td2 = datetime(int(date_full[0]), int(date_full[1]), int(date_full[2]), int(row[3][:2]), int(row[3][3:5]), int(row[3][-2:]), 0) - datetime(int(date_full[0]), int(date_full[1]), int(date_full[2]), 0, 0, 0, 0)
            if td1 < td2: # 定时时间还未到达，不自动设置为完成
                return

        # 定时时间已到达，需更新数据库
        c.execute(f'UPDATE %s SET status=1 WHERE id=%s'%(date_name, self.__taskIdActive))
        conn.commit()

        # 刷新列表
        self.remover(number) 
        self.set_task()
        self.set_completed()

    def sub_task(self):
        global c
        global conn
        global date_name
        global number

        if self.__taskIdActive > -1:
            sql_update_query = """UPDATE {} SET status=1 WHERE id='{}'""".format(date_name, self.__taskIdActive)
            c.execute(sql_update_query)
            conn.commit()
            self.remover(number)
            self.set_task()

    def calender_search(self):
        global c
        global conn
        global date_name

        # 清空当前信息
        for item in self.__ui_calender_com_List:
            item[0].hide()
            item[1].hide()
        for item in self.__ui_calender_task_List:
            item[0].hide()
            item[1].hide()

        if len(self.ui.date_cal.text()) == 0:
            now = datetime.now()
            self.ui.date_cal.setText(now.strftime('%Y/%m/%d'))
        
        try:
            if len(self.ui.date_cal.text()) == 10:
                names = self.ui.date_cal.text().split('/')
                if not (2021 <= int(names[0]) and 1<=int(names[1])<=12 and 1<=int(names[2])<=31):
                    return
                table = 'date'+names[0]+names[1]+names[2]
                c.execute(f'''CREATE TABLE IF NOT EXISTS {table}(
                            id integer PRIMARY KEY,
                            task text,
                            status integer,
                            time time
                        )''')
                conn.commit()
        except Exception as e:
            return

        # 查询今日任务
        tasks = c.execute(f'SELECT * FROM {table}')
        taskList = []
        for task in tasks:
            taskList.append(task)
        # 查询crontab任务
        try:
            if table != date_name:
                rows = c.execute(f'SELECT task,crontab FROM crontabtask WHERE crontab<>"* * * * *"')
                for row in rows:
                    task = row[0]
                    crontab = row[1]
                    iter = croniter(crontab,datetime.now())
                    time = iter.get_next(datetime)
                    date = 'date' + time.strftime("%Y%m%d")
                    time = time.strftime('%H:%M:%S')
                    if date == table:
                        taskList.append((-1, task, 0, time))
        except Exception as e:
            pass
        
        count_com = 0
        count_task = 0
        # id, task, status, time
        for row in taskList:
            if row[2] == 1 and len(row[1]) != 0 and count_com < len(self.__ui_calender_com_List):
                self.__ui_calender_com_List[count_com][0].show()
                self.__ui_calender_com_List[count_com][0].setText(row[1])
                self.__ui_calender_com_List[count_com][1].show()
                count_com += 1
            
            if row[2] == 0 and len(row[1]) != 0 and count_task < len(self.__ui_calender_task_List):
                self.__ui_calender_task_List[count_task][0].show()
                self.__ui_calender_task_List[count_task][0].setText(row[1])
                self.__ui_calender_task_List[count_task][1].show()
                count_task += 1
               
    def contact(self):
        webbrowser.open('https://github.com/217heidai')


if __name__ == '__main__':
    import sys
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)
    root = Root()
    #root.showFullScreen() # 全屏
    sys.exit(app.exec_())
