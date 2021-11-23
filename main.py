from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from panel import Ui_MainWindow
import os
from datetime import datetime
import calendar
import sqlite3
from pygame import mixer
import webbrowser
from tts import TTS_BAIDU
from zhon.hanzi import punctuation
from croniter import croniter

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
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.show()

        self.set_task()

        timer = QTimer(self)
        timer.timeout.connect(self.timer)
        timer.start(1000)

        #self.ui.addtask.setPlaceholderText("Add a Task")
        self.ui.addtask.setPlaceholderText("添加待办")
        #self.ui.addtask_3.setPlaceholderText("Add a Task")
        self.ui.addtask_3.setPlaceholderText("添加待办")

        # set username and profile
        user = os.getlogin()
        if len(user) < 0:
            user = 'Admin'
        abridge = str(os.getlogin())[0]
        self.ui.nameuser.setText(user)
        self.ui.profile.setText(abridge)
        self.ui.nameuser2.setText(user)
        self.ui.profile2.setText(abridge)
        self.ui.nameuser2_2.setText(user)
        self.ui.profile2_2.setText(abridge)
        self.ui.nameuser2_3.setText(user)
        self.ui.profile2_3.setText(abridge)
        self.ui.nameuser5.setText(user)
        self.ui.profile5.setText(abridge)

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

        now = datetime.now()
        self.ui.date_cal.setPlaceholderText('请输入日期查询：%s'%(now.strftime('%Y/%m/%d')))

        # link contact
        self.ui.contactme.clicked.connect(self.contact)

        # 8项待办事项的ID
        self.taskIdList = []

        # 当前选中任务的ID
        self.taskIdActive = -1

        self.tts = TTS_BAIDU()

    def mousePressEvent(self, evt):
        self.oldPos = evt.globalPos()

    def mouseMoveEvent(self, evt):
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

        # 插入默认待办
        self.__taskDefault()

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
        self.taskIdList = []

        count = 0
        tasks = c.execute(f'SELECT * FROM {date_name} WHERE status=0 ORDER BY time ASC')
        #id, task, status, time
        for row in tasks:
            count += 1
            txt = row[1]
            if count == 1:
                if page_time != 1:
                    self.ui.stackedWidget.setCurrentWidget(self.ui.day_task)
                self.ui.task1.show()
                self.ui.task1.setText(txt)
                self.ui.sub1.show()
                self.ui.delete1.show()
                self.ui.timer1.show()
                self.taskIdList.append(row[0])
            elif count == 2:
                self.ui.task2.show()
                self.ui.task2.setText(txt)
                self.ui.sub2.show()
                self.ui.delete2.show()
                self.ui.timer2.show()
                self.taskIdList.append(row[0])
            elif count == 3:
                self.ui.task3.show()
                self.ui.task3.setText(txt)
                self.ui.sub3.show()
                self.ui.delete3.show()
                self.ui.timer3.show()
                self.taskIdList.append(row[0])
            elif count == 4:
                self.ui.task4.show()
                self.ui.task4.setText(txt)
                self.ui.sub4.show()
                self.ui.delete4.show()
                self.ui.timer4.show()
                self.taskIdList.append(row[0])
            elif count == 5:
                self.ui.task5.show()
                self.ui.task5.setText(txt)
                self.ui.sub5.show()
                self.ui.delete5.show()
                self.ui.timer5.show()
                self.taskIdList.append(row[0])
            elif count == 6:
                self.ui.task6.show()
                self.ui.task6.setText(txt)
                self.ui.sub6.show()
                self.ui.delete6.show()
                self.ui.timer6.show()
                self.taskIdList.append(row[0])
            elif count == 7:
                self.ui.task7.show()
                self.ui.task7.setText(txt)
                self.ui.sub7.show()
                self.ui.delete7.show()
                self.ui.timer7.show()
                self.taskIdList.append(row[0])
            elif count == 8:
                self.ui.task8.show()
                self.ui.task8.setText(txt)
                self.ui.sub8.show()
                self.ui.delete8.show()
                self.ui.timer8.show()
                self.taskIdList.append(row[0])
            else:
                break

    def set_completed(self):
        global date_name
        count = 0
        tasks = c.execute(f'SELECT * FROM {date_name} WHERE status=1 ORDER BY time ASC')
        for row in tasks:
            count += 1
            txt = row[1]
            if count == 1:
                self.ui.com1.show()
                self.ui.com1.setText(txt)
            elif count == 2:
                self.ui.com2.show()
                self.ui.com2.setText(txt)
            elif count == 3:
                self.ui.com3.show()
                self.ui.com3.setText(txt)
            elif count == 4:
                self.ui.com4.show()
                self.ui.com4.setText(txt)
            elif count == 5:
                self.ui.com5.show()
                self.ui.com5.setText(txt)
            elif count == 6:
                self.ui.com6.show()
                self.ui.com6.setText(txt)
            elif count == 7:
                self.ui.com7.show()
                self.ui.com7.setText(txt)
            elif count == 8:
                self.ui.com8.show()
                self.ui.com8.setText(txt)
            else:
                break

    def active_task1(self):
        print('active task 1: %s'%self.ui.task1.text())
        self.taskIdActive = self.taskIdList[0]

    def active_task2(self):
        print('active task 2: %s'%self.ui.task2.text())
        self.taskIdActive = self.taskIdList[1]

    def active_task3(self):
        print('active task 3: %s'%self.ui.task3.text())
        self.taskIdActive = self.taskIdList[2]

    def active_task4(self):
        print('active task 4: %s'%self.ui.task4.text())
        self.taskIdActive = self.taskIdList[3]

    def active_task5(self):
        print('active task 5: %s'%self.ui.task5.text())
        self.taskIdActive = self.taskIdList[4]

    def active_task6(self):
        print('active task 6: %s'%self.ui.task6.text())
        self.taskIdActive = self.taskIdList[5]

    def active_task7(self):
        print('active task 7: %s'%self.ui.task7.text())
        self.taskIdActive = self.taskIdList[6]

    def active_task8(self):
        print('active task 8: %s'%self.ui.task8.text())
        self.taskIdActive = self.taskIdList[7]

    def remove_task(self):
        global c
        global conn
        global number
        global date_name

        if self.taskIdActive > -1:
            c.execute(f'UPDATE {date_name} SET status=2 WHERE id=%s'%(self.taskIdActive))
            conn.commit()
            self.remover(number)
            self.set_task()

    def remover(self, num):
        self.ui.task1.clear()
        self.ui.task2.clear()
        self.ui.task3.clear()
        self.ui.task4.clear()
        self.ui.task5.clear()
        self.ui.task6.clear()
        self.ui.task7.clear()
        self.ui.task8.clear()
        if num == 8:
            self.ui.task8.hide()
            self.ui.sub8.hide()
            self.ui.delete8.hide()
            self.ui.timer8.hide()
        elif num == 7:
            self.ui.task7.hide()
            self.ui.sub7.hide()
            self.ui.delete7.hide()
            self.ui.timer7.hide()
        elif num == 6:
            self.ui.task6.hide()
            self.ui.sub6.hide()
            self.ui.delete6.hide()
            self.ui.timer6.hide()
        elif num == 5:
            self.ui.task5.hide()
            self.ui.sub5.hide()
            self.ui.delete5.hide()
            self.ui.timer5.hide()
        elif num == 4:
            self.ui.task4.hide()
            self.ui.sub4.hide()
            self.ui.delete4.hide()
            self.ui.timer4.hide()
        elif num == 3:
            self.ui.task3.hide()
            self.ui.sub3.hide()
            self.ui.delete3.hide()
            self.ui.timer3.hide()
        elif num == 2:
            self.ui.task2.hide()
            self.ui.sub2.hide()
            self.ui.delete2.hide()
            self.ui.timer2.hide()
        elif num == 1:
            self.ui.task1.hide()
            self.ui.sub1.hide()
            self.ui.delete1.hide()
            self.ui.timer1.hide()

    def page_clock(self):
        global page_time
        page_time = 1

        if self.taskIdActive > -1:
            rows = c.execute(f'SELECT task,time FROM {date_name} WHERE id=%s'%(self.taskIdActive))
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

    def __play(self, text):
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
        filename = os.getcwd() + '/alarms/' + newtext + '.wav'
        if os.path.exists(filename):
            mixer.init()
            mixer.music.load(filename)
            mixer.music.play()
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
            mixer.music.play()
        '''


    def timer(self):
        global c
        global conn
        global date_name
        global date_full

        # get time
        currentTime = QTime.currentTime()
        display_text = currentTime.toString('hh:mm:ss')
        self.ui.now_time.setText(display_text)

        # set date
        date_full2 = str(datetime.now().strftime('%Y-%m-%d'))
        week = {0:'星期日', 1:'星期一', 2:'星期二', 3:'星期三', 4:'星期四', 5:'星期五', 6:'星期六'}
        today = '%s年%s月%s日，%s' % (date_full2[:4], date_full2[5:7], date_full2[8:], week[datetime.now().weekday()])
        self.ui.date.setText(today)
        self.ui.date2.setText(today)
        self.ui.date3.setText(today)

        # set date - database
        date_full = str(datetime.now().strftime('%Y-%m-%d')).split('-')
        date_name = 'date' + date_full[0] + date_full[1] + date_full[2]

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

        #conn.commit()

        # clock
        task = c.execute(f'SELECT * FROM {date_name} WHERE status=0')
        # id task status time
        for row in task:
            if str(row[3]) == str(display_text):
                self.taskIdActive = row[0]
                print(row[1])
                self.ui.tasktime_task.setText('%s'%(row[1]))
                # 播提示音
                self.__play(row[1])

                self.ui.stackedWidget.setCurrentWidget(self.ui.stop_timer)

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

        if self.taskIdActive > -1:
            # 获取task
            rows = c.execute(f'SELECT task FROM %s WHERE id=%s'%(date_name, self.taskIdActive))
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
                            updatetask(c, conn, date_name, self.taskIdActive, date, time, number)
                else:
                    if crontab != '* * * * *':
                        # 插入定时任务
                        c.execute("""INSERT INTO crontabtask(id, task, status, crontab) VALUES (null,'{}',{},'{}');""".format(task, 0, crontab))
                        conn.commit()
                        # 更新下次执行时间
                        updatetask(c, conn, date_name, self.taskIdActive, date, time, number)
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
                    c.execute(f'UPDATE %s SET time="%s" WHERE id=%s'%(date_name, clock, self.taskIdActive))
                    conn.commit()

    def stop_clock(self):
        global number
        mixer.music.stop()
        
        # 更新数据库
        c.execute(f'UPDATE %s SET status=1 WHERE id=%s'%(date_name, self.taskIdActive))
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

        if self.taskIdActive > -1:
            sql_update_query = """UPDATE {} SET status=1 WHERE id='{}'""".format(date_name, self.taskIdActive)
            c.execute(sql_update_query)
            conn.commit()
            self.remover(number)
            self.set_task()

    def calender_search(self):
        global c
        global conn
        global date_name
        self.ui.com1_cal.hide()
        self.ui.com2_cal.hide()
        self.ui.com3_cal.hide()
        self.ui.com4_cal.hide()
        self.ui.com5_cal.hide()
        self.ui.com6_cal.hide()
        self.ui.com7_cal.hide()
        self.ui.com8_cal.hide()
        self.ui.task1_cal.hide()
        self.ui.task2_cal.hide()
        self.ui.task3_cal.hide()
        self.ui.task4_cal.hide()
        self.ui.task5_cal.hide()
        self.ui.task6_cal.hide()
        self.ui.task7_cal.hide()
        self.ui.task8_cal.hide()
        self.ui.True1.hide()
        self.ui.True2.hide()
        self.ui.True3.hide()
        self.ui.True4.hide()
        self.ui.True5.hide()
        self.ui.True6.hide()
        self.ui.True7.hide()
        self.ui.True8.hide()
        self.ui.False1.hide()
        self.ui.False2.hide()
        self.ui.False3.hide()
        self.ui.False4.hide()
        self.ui.False5.hide()
        self.ui.False6.hide()
        self.ui.False7.hide()
        self.ui.False8.hide()

        if len(self.ui.date_cal.text()) == 0:
            now = datetime.now()
            self.ui.date_cal.clear()
            self.ui.date_cal.setText(now.strftime('%Y/%m/%d'))
        
        try:
            if len(self.ui.date_cal.text()) == 10:
                names = self.ui.date_cal.text().split('/')
                if not (2021 <= int(names[0]) and 1<=int(names[1])<=12 and 1<=int(names[2])<=31):
                    return
                name = 'date'+names[0]+names[1]+names[2]
                c.execute(f'''CREATE TABLE IF NOT EXISTS {name}(
                            id integer PRIMARY KEY,
                            task text,
                            status integer,
                            time time
                        )''')
                conn.commit()
        except Exception as e:
            return

        # 查询今日任务
        tasks = c.execute(f'SELECT * FROM {name}')
        taskList = []
        for task in tasks:
            taskList.append(task)
        # 查询crontab任务
        try:
            if name != date_name:
                rows = c.execute(f'SELECT task,crontab FROM crontabtask WHERE crontab<>"* * * * *"')
                for row in rows:
                    task = row[0]
                    crontab = row[1]
                    iter = croniter(crontab,datetime.now())
                    time = iter.get_next(datetime)
                    date = 'date' + time.strftime("%Y%m%d")
                    time = time.strftime('%H:%M:%S')
                    if date == name:
                        taskList.append((-1, task, 0, time))
        except Exception as e:
            pass
        
        count_com = 0
        count_task = 0
        # id, task, status, time
        for row in taskList:
            if row[2] == 1 and len(row[1]) != 0:
                count_com += 1
                if count_com == 1:
                    self.ui.com1_cal.show()
                    self.ui.True1.show()
                    self.ui.com1_cal.setText(row[1])
                elif count_com == 2:
                    self.ui.com2_cal.show()
                    self.ui.True2.show()
                    self.ui.com2_cal.setText(row[1])
                elif count_com == 3:
                    self.ui.com3_cal.show()
                    self.ui.True3.show()
                    self.ui.com3_cal.setText(row[1])
                elif count_com == 4:
                    self.ui.com4_cal.show()
                    self.ui.True4.show()
                    self.ui.com4_cal.setText(row[1])
                elif count_com == 5:
                    self.ui.com5_cal.show()
                    self.ui.True5.show()
                    self.ui.com5_cal.setText(row[1])
                elif count_com == 6:
                    self.ui.com6_cal.show()
                    self.ui.True6.show()
                    self.ui.com6_cal.setText(row[1])
                elif count_com == 7:
                    self.ui.com7_cal.show()
                    self.ui.True7.show()
                    self.ui.com7_cal.setText(row[1])
                elif count_com == 8:
                    self.ui.com8_cal.show()
                    self.ui.True8.show()
                    self.ui.com8_cal.setText(row[1])

            elif row[2] == 0 and len(row[1]) != 0:
                count_task += 1
                if count_task == 1:
                    self.ui.task1_cal.show()
                    self.ui.False1.show()
                    self.ui.task1_cal.setText(row[1])
                elif count_task == 2:
                    self.ui.task2_cal.show()
                    self.ui.False2.show()
                    self.ui.task2_cal.setText(row[1])
                elif count_task == 3:
                    self.ui.task3_cal.show()
                    self.ui.False3.show()
                    self.ui.task3_cal.setText(row[1])
                elif count_task == 4:
                    self.ui.task4_cal.show()
                    self.ui.False4.show()
                    self.ui.task4_cal.setText(row[1])
                elif count_task == 5:
                    self.ui.task5_cal.show()
                    self.ui.False5.show()
                    self.ui.task5_cal.setText(row[1])
                elif count_task == 6:
                    self.ui.task6_cal.show()
                    self.ui.False6.show()
                    self.ui.task6_cal.setText(row[1])
                elif count_task == 7:
                    self.ui.task7_cal.show()
                    self.ui.False7.show()
                    self.ui.task7_cal.setText(row[1])
                elif count_task == 8:
                    self.ui.task8_cal.show()
                    self.ui.False8.show()
                    self.ui.task8_cal.setText(row[1])

    def contact(self):
        webbrowser.open('https://github.com/217heidai')


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    root = Root()
    sys.exit(app.exec_())
