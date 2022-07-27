from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from PyQt5 import uic
import asyncio

# FL
import sys
sys.path.append('.')
from flwr import *
from fl_client import *

# edge consensus learning
from ecl_run_mnist import Kings
from time import sleep
import json

# cl
from cl_run_mnist import Queens


# Logging
import logging
from io import StringIO

fl_logger = logging.getLogger('FL')
#fl_formatter = '%(asctime)s [FL] %(levelname)s :  %(message)s'
#fl_logger.setFormatter(fl_logger)
fl_logger.setLevel(logging.INFO)

ecl_logger = logging.getLogger('ECL')
#ecl_formatter = '%(asctime)s [ECL] %(levelname)s :  %(message)s'
#ecl_logger.setFormatter(ecl_logger)
ecl_logger.setLevel(logging.INFO)

cl_logger = logging.getLogger('CL')
#cl_formatter = '%(asctime)s [CL] %(levelname)s :  %(message)s'
#cl_logger.setFormatter(cl_logger)
cl_logger.setLevel(logging.INFO)



# graph
from pyqtgraph import PlotWidget, plot

import pyqtgraph as pg

class QPlainTextEditLoggerFL(logging.Handler):
    def __init__(self, parent1, parent2, acc0, acc1,acc2,acc3,acc4,acc5,acc6,acc7,acc8,acc9):
        super(QPlainTextEditLoggerFL,self).__init__()

        self.widget = parent1 #QPlainTextEdit(parent1)
        #self.widget.resize(500,190)
        #self.widget.setReadOnly(True)


        self.graph = parent2
        self.graph.setBackground('w')
        self.graph.showGrid(x=True, y=True)
        #self.graph.plot([1,2],[3,4])

        self.loss_epoch = 0
        self.loss_list =""

        self.acc0 = acc0
        self.acc1 = acc1
        self.acc2 = acc2
        self.acc3 = acc3
        self.acc4 = acc4
        self.acc5 = acc5
        self.acc6 = acc6
        self.acc7 = acc7
        self.acc8 = acc8
        self.acc9 = acc9

    def emit(self, record):
        msg = self.format(record)

        msg_str = str(msg)
        if "train_loss:" in msg_str:
            msg_loss = msg_str.split(' ',-1)[2]

            self.loss_list += msg_loss
            self.loss_list += " "
            self.loss_epoch +=1
            x_range = list(range(self.loss_epoch))
            y_range = [float(x) for x in self.loss_list.split()]

            bargraph = pg.BarGraphItem(x=x_range, height = y_range, width=0.2, brush='r')

            self.graph.addItem(bargraph)

            #print(x_range,y_range)
            #self.graph.plot(x_range, y_range)

        if "accuracy:" in msg_str:
            msg_digit = msg_str.split(' ', -1)[1]
            msg_acc = msg_str.split(' ', -1)[3]
            if msg_digit == '0':
                if int(msg_acc) > 0:
                   self.acc0.setStyleSheet("Color : green")
                self.acc0.setText(msg_acc +"%")
            elif msg_digit == '1':
                if int(msg_acc) > 0:
                    self.acc1.setStyleSheet("Color : green")
                self.acc1.setText(msg_acc +"%")
            elif msg_digit == '2':
                if int(msg_acc) > 0:
                    self.acc2.setStyleSheet("Color : green")
                self.acc2.setText(msg_acc +"%")
            elif msg_digit == '3':
                if int(msg_acc) > 0:
                    self.acc3.setStyleSheet("Color : green")
                self.acc3.setText(msg_acc +"%")
            elif msg_digit == '4':
                if int(msg_acc) > 0:
                    self.acc4.setStyleSheet("Color : green")
                self.acc4.setText(msg_acc +"%")
            elif msg_digit == '5':
                if int(msg_acc) > 0:
                    self.acc5.setStyleSheet("Color : green")
                self.acc5.setText(msg_acc +"%")
            elif msg_digit == '6':
                if int(msg_acc) > 0:
                    self.acc6.setStyleSheet("Color : green")
                self.acc6.setText(msg_acc +"%")
            elif msg_digit == '7':
                if int(msg_acc) > 0:
                    self.acc7.setStyleSheet("Color : green")
                self.acc7.setText(msg_acc +"%")
            elif msg_digit == '8':
                if int(msg_acc) > 0:
                    self.acc8.setStyleSheet("Color : green")
                self.acc8.setText(msg_acc +"%")
            elif msg_digit == '9':
                if int(msg_acc) > 0:
                    self.acc9.setStyleSheet("Color : green")
                self.acc9.setText(msg_acc +"%")
            else:
                print('...')

        self.widget.append(msg) #appendPlainText(msg)
        self.widget.moveCursor(QTextCursor.End)

    def write(self, m):
        pass

class QPlainTextEditLoggerCL(logging.Handler):
    def __init__(self, parent1, parent2):
        super(QPlainTextEditLoggerCL,self).__init__()

        self.widget = parent1 # QPlainTextEdit(parent1)
        #self.widget.resize(500,190)
        #self.widget.setReadOnly(True)


class QPlainTextEditLoggerECL(logging.Handler):
    def __init__(self, parent1, parent2, acc0, acc1,acc2,acc3,acc4,acc5,acc6,acc7,acc8,acc9):
        super(QPlainTextEditLoggerECL,self).__init__()

        self.widget = parent1 #QPlainTextEdit(parent1)
        #self.widget.resize(500,190)
        #self.widget.setReadOnly(True)


        self.graph = parent2
        self.graph.setBackground('w')
        self.graph.showGrid(x=True, y=True)
        #self.graph.plot([1,2],[3,4])

        self.loss_epoch = 0
        self.loss_list =""

        self.acc0 = acc0
        self.acc1 = acc1
        self.acc2 = acc2
        self.acc3 = acc3
        self.acc4 = acc4
        self.acc5 = acc5
        self.acc6 = acc6
        self.acc7 = acc7
        self.acc8 = acc8
        self.acc9 = acc9

    def emit(self, record):
        msg = self.format(record)

        msg_str = str(msg)
        if "loss:" in msg_str:
            msg_loss = msg_str.split(' ',-1)[2]

            self.loss_list += msg_loss
            self.loss_list += " "
            self.loss_epoch +=1
            x_range = list(range(self.loss_epoch))
            y_range = [float(x) for x in self.loss_list.split()]

            bargraph = pg.BarGraphItem(x=x_range, height = y_range, width=0.2, brush='r')

            self.graph.addItem(bargraph)

            #print(x_range,y_range)
            #self.graph.plot(x_range, y_range)

        if "accuracy:" in msg_str:
            msg_digit = msg_str.split(' ', -1)[3]
            msg_acc = msg_str.split(' ', -1)[5]
            if msg_digit == '0':
                if int(msg_acc) > 0:
                   self.acc0.setStyleSheet("Color : green")
                self.acc0.setText(msg_acc +"%")
            elif msg_digit == '1':
                if int(msg_acc) > 0:
                    self.acc1.setStyleSheet("Color : green")
                self.acc1.setText(msg_acc +"%")
            elif msg_digit == '2':
                if int(msg_acc) > 0:
                    self.acc2.setStyleSheet("Color : green")
                self.acc2.setText(msg_acc +"%")
            elif msg_digit == '3':
                if int(msg_acc) > 0:
                    self.acc3.setStyleSheet("Color : green")
                self.acc3.setText(msg_acc +"%")
            elif msg_digit == '4':
                if int(msg_acc) > 0:
                    self.acc4.setStyleSheet("Color : green")
                self.acc4.setText(msg_acc +"%")
            elif msg_digit == '5':
                if int(msg_acc) > 0:
                    self.acc5.setStyleSheet("Color : green")
                self.acc5.setText(msg_acc +"%")
            elif msg_digit == '6':
                if int(msg_acc) > 0:
                   self.acc6.setStyleSheet("Color : green")
                self.acc6.setText(msg_acc +"%")
            elif msg_digit == '7':
                if int(msg_acc) > 0:
                    self.acc7.setStyleSheet("Color : green")
                self.acc7.setText(msg_acc +"%")
            elif msg_digit == '8':
                if int(msg_acc) > 0:
                    self.acc8.setStyleSheet("Color : green")
                self.acc8.setText(msg_acc +"%")
            elif msg_digit == '9':
                if int(msg_acc) > 0:
                    self.acc9.setStyleSheet("Color : green")
                self.acc9.setText(msg_acc +"%")
            else:
                print('...')

        self.widget.append(msg) #appendPlainText(msg)
        self.widget.moveCursor(QTextCursor.End)

    def write(self, m):
        pass

class QPlainTextEditLoggerCL(logging.Handler):
    def __init__(self, parent1, parent2, acc0, acc1,acc2,acc3,acc4,acc5,acc6,acc7,acc8,acc9):
        super(QPlainTextEditLoggerCL,self).__init__()

        self.widget = parent1 # QPlainTextEdit(parent1)
        #self.widget.resize(500,190)
        #self.widget.setReadOnly(True)


        self.graph = parent2
        self.graph.setBackground('w')
        self.graph.showGrid(x=True, y=True)
        #self.graph.plot([1,2],[3,4])


        self.loss_epoch = 0
        self.loss_list =""

        self.acc0 = acc0
        self.acc1 = acc1
        self.acc2 = acc2
        self.acc3 = acc3
        self.acc4 = acc4
        self.acc5 = acc5
        self.acc6 = acc6
        self.acc7 = acc7
        self.acc8 = acc8
        self.acc9 = acc9

    def emit(self, record):
        msg = self.format(record)

        msg_str = str(msg)
        if "Loss:" in msg_str:
            msg_loss = msg_str.split(' ',-1)[7]
            print(msg_loss)

            self.loss_list += msg_loss
            self.loss_list += " "
            self.loss_epoch +=1
            x_range = list(range(self.loss_epoch))
            y_range = [float(x) for x in self.loss_list.split()]

            bargraph = pg.BarGraphItem(x=x_range, height = y_range, width=0.2, brush='r')

            self.graph.addItem(bargraph)

            #print(x_range,y_range)
            #self.graph.plot(x_range, y_range)

        if "accuracy:" in msg_str:
            msg_digit = msg_str.split(' ', -1)[3]
            msg_acc = msg_str.split(' ', -1)[5]
            if msg_digit == '0':
                if int(msg_acc) > 0:
                   self.acc0.setStyleSheet("Color : green")
                self.acc0.setText(msg_acc +"%")
            elif msg_digit == '1':
                if int(msg_acc) > 0:
                    self.acc1.setStyleSheet("Color : green")
                self.acc1.setText(msg_acc +"%")
            elif msg_digit == '2':
                if int(msg_acc) > 0:
                    self.acc2.setStyleSheet("Color : green")
                self.acc2.setText(msg_acc +"%")
            elif msg_digit == '3':
                if int(msg_acc) > 0:
                    self.acc3.setStyleSheet("Color : green")
                self.acc3.setText(msg_acc +"%")
            elif msg_digit == '4':
                if int(msg_acc) > 0:
                    self.acc4.setStyleSheet("Color : green")
                self.acc4.setText(msg_acc +"%")
            elif msg_digit == '5':
                if int(msg_acc) > 0:
                    self.acc5.setStyleSheet("Color : green")
                self.acc5.setText(msg_acc +"%")
            elif msg_digit == '6':
                if int(msg_acc) > 0:
                   self.acc6.setStyleSheet("Color : green")
                self.acc6.setText(msg_acc +"%")
            elif msg_digit == '7':
                if int(msg_acc) > 0:
                    self.acc7.setStyleSheet("Color : green")
                self.acc7.setText(msg_acc +"%")
            elif msg_digit == '8':
                if int(msg_acc) > 0:
                    self.acc8.setStyleSheet("Color : green")
                self.acc8.setText(msg_acc +"%")
            elif msg_digit == '9':
                if int(msg_acc) > 0:
                    self.acc9.setStyleSheet("Color : green")
                self.acc9.setText(msg_acc +"%")
            else:
                print('...')

        self.widget.append(msg) #appendPlainText(msg)
        self.widget.moveCursor(QTextCursor.End)

    def write(self, m):
        pass


#  Step 1: Create a worker class
class WorkerFL(QObject):
    finished = pyqtSignal()
    progress = pyqtSignal(int)

    def run(self):
        """Long-running task."""
        client = FlowerClient(fl_logger)
        client.run(client)

        self.finished.emit()

class WorkerECL(QObject):
    finished = pyqtSignal()
    progress = pyqtSignal(int)

    def run(self):
        """Long-running task."""
        args_conf = 'ecl/conf/BALTHASAR.json'
        args_nodes = 'ecl/conf/node_list.json'
        args_algorithm = 'admm'


        with open(args_conf) as f:
            conf = json.load(f)
            name = conf["name"]
            interval = conf["interval"]
            offset = conf["offset"]
            device = conf["device"]

        with open(args_nodes) as f:
            conf = json.load(f)
            nodes = conf["nodes"]

        #for i in range(5):
        #    sleep(1)
        #    self.progress.emit(i + 1)

        #king = Kings(name, nodes, args_algorithm, device, 100, interval, offset, "log/")
        king = Kings(ecl_logger, name, nodes, args_algorithm, device,  interval, offset, "log/")
        king.train()

        self.finished.emit()

class WorkerCL(QObject):
    finished = pyqtSignal()
    progress = pyqtSignal(int)

    def run(self):
        """Long-running task."""
        args_conf = 'cl.yaml'

        queen = Queens(cl_logger)
        queen.experiment(args_conf)

        self.finished.emit()

form_class = uic.loadUiType("LearningUI.ui")[0]

class MyApp(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        #self.labelECLtopo.resize(1200,300)
        #self.labelECLtopo.setPixmap(QPixmap("ecl/ecl_topology.png").scaled(420,240, Qt.KeepAspectRatio))
        #self.labelECLtopo.show()

        self.labelFL0.setPixmap(QPixmap("data/digit/0_img.png").scaled(50,50, Qt.KeepAspectRatio))
        self.labelFL1.setPixmap(QPixmap("data/digit/1_img.png").scaled(50,50, Qt.KeepAspectRatio))
        self.labelFL2.setPixmap(QPixmap("data/digit/2_img.png").scaled(50,50, Qt.KeepAspectRatio))
        self.labelFL3.setPixmap(QPixmap("data/digit/3_img.png").scaled(50,50, Qt.KeepAspectRatio))
        self.labelFL4.setPixmap(QPixmap("data/digit/4_img.png").scaled(50,50, Qt.KeepAspectRatio))
        self.labelFL5.setPixmap(QPixmap("data/digit/5_img.png").scaled(50,50, Qt.KeepAspectRatio))
        self.labelFL6.setPixmap(QPixmap("data/digit/6_img.png").scaled(50,50, Qt.KeepAspectRatio))
        self.labelFL7.setPixmap(QPixmap("data/digit/7_img.png").scaled(50,50, Qt.KeepAspectRatio))
        self.labelFL8.setPixmap(QPixmap("data/digit/8_img.png").scaled(50,50, Qt.KeepAspectRatio))
        self.labelFL9.setPixmap(QPixmap("data/digit/9_img.png").scaled(50,50, Qt.KeepAspectRatio))
        self.labelFL0.show()
        self.labelFL1.show()
        self.labelFL2.show()
        self.labelFL3.show()
        self.labelFL4.show()
        self.labelFL5.show()
        self.labelFL6.show()
        self.labelFL7.show()
        self.labelFL8.show()
        self.labelFL9.show()
        self.labelFL0ACC.setText("0%")
        self.labelFL1ACC.setText("0%")
        self.labelFL2ACC.setText("0%")
        self.labelFL3ACC.setText("0%")
        self.labelFL4ACC.setText("0%")
        self.labelFL5ACC.setText("0%")
        self.labelFL6ACC.setText("0%")
        self.labelFL7ACC.setText("0%")
        self.labelFL8ACC.setText("0%")
        self.labelFL9ACC.setText("0%")

        self.labelCL0.setPixmap(QPixmap("data/digit/0_img.png").scaled(50,50, Qt.KeepAspectRatio))
        self.labelCL1.setPixmap(QPixmap("data/digit/1_img.png").scaled(50,50, Qt.KeepAspectRatio))
        self.labelCL2.setPixmap(QPixmap("data/digit/2_img.png").scaled(50,50, Qt.KeepAspectRatio))
        self.labelCL3.setPixmap(QPixmap("data/digit/3_img.png").scaled(50,50, Qt.KeepAspectRatio))
        self.labelCL4.setPixmap(QPixmap("data/digit/4_img.png").scaled(50,50, Qt.KeepAspectRatio))
        self.labelCL5.setPixmap(QPixmap("data/digit/5_img.png").scaled(50,50, Qt.KeepAspectRatio))
        self.labelCL6.setPixmap(QPixmap("data/digit/6_img.png").scaled(50,50, Qt.KeepAspectRatio))
        self.labelCL7.setPixmap(QPixmap("data/digit/7_img.png").scaled(50,50, Qt.KeepAspectRatio))
        self.labelCL8.setPixmap(QPixmap("data/digit/8_img.png").scaled(50,50, Qt.KeepAspectRatio))
        self.labelCL9.setPixmap(QPixmap("data/digit/9_img.png").scaled(50,50, Qt.KeepAspectRatio))
        self.labelCL0.show()
        self.labelCL1.show()
        self.labelCL2.show()
        self.labelCL3.show()
        self.labelCL4.show()
        self.labelCL5.show()
        self.labelCL6.show()
        self.labelCL7.show()
        self.labelCL8.show()
        self.labelCL9.show()
        self.labelCL0ACC.setText("0%")
        self.labelCL1ACC.setText("0%")
        self.labelCL2ACC.setText("0%")
        self.labelCL3ACC.setText("0%")
        self.labelCL4ACC.setText("0%")
        self.labelCL5ACC.setText("0%")
        self.labelCL6ACC.setText("0%")
        self.labelCL7ACC.setText("0%")
        self.labelCL8ACC.setText("0%")
        self.labelCL9ACC.setText("0%")

        self.labelECL0.setPixmap(QPixmap("data/digit/0_img.png").scaled(50,50, Qt.KeepAspectRatio))
        self.labelECL1.setPixmap(QPixmap("data/digit/1_img.png").scaled(50,50, Qt.KeepAspectRatio))
        self.labelECL2.setPixmap(QPixmap("data/digit/2_img.png").scaled(50,50, Qt.KeepAspectRatio))
        self.labelECL3.setPixmap(QPixmap("data/digit/3_img.png").scaled(50,50, Qt.KeepAspectRatio))
        self.labelECL4.setPixmap(QPixmap("data/digit/4_img.png").scaled(50,50, Qt.KeepAspectRatio))
        self.labelECL5.setPixmap(QPixmap("data/digit/5_img.png").scaled(50,50, Qt.KeepAspectRatio))
        self.labelECL6.setPixmap(QPixmap("data/digit/6_img.png").scaled(50,50, Qt.KeepAspectRatio))
        self.labelECL7.setPixmap(QPixmap("data/digit/7_img.png").scaled(50,50, Qt.KeepAspectRatio))
        self.labelECL8.setPixmap(QPixmap("data/digit/8_img.png").scaled(50,50, Qt.KeepAspectRatio))
        self.labelECL9.setPixmap(QPixmap("data/digit/9_img.png").scaled(50,50, Qt.KeepAspectRatio))
        self.labelECL0.show()
        self.labelECL1.show()
        self.labelECL2.show()
        self.labelECL3.show()
        self.labelECL4.show()
        self.labelECL5.show()
        self.labelECL6.show()
        self.labelECL7.show()
        self.labelECL8.show()
        self.labelECL9.show()
        self.labelECL0ACC.setText("0%")
        self.labelECL1ACC.setText("0%")
        self.labelECL2ACC.setText("0%")
        self.labelECL3ACC.setText("0%")
        self.labelECL4ACC.setText("0%")
        self.labelECL5ACC.setText("0%")
        self.labelECL6ACC.setText("0%")
        self.labelECL7ACC.setText("0%")
        self.labelECL8ACC.setText("0%")
        self.labelECL9ACC.setText("0%")

        self.pushButtonFL.clicked.connect(self.btnClickFL)
        self.pushButtonECL.clicked.connect(self.btnClickECL)
        self.pushButtonCL.clicked.connect(self.btnClickCL)

        self.graphWidgetFL.setXRange(0,20)
        self.graphWidgetFL.setYRange(0.0,0.02)
        log_handlerFL = QPlainTextEditLoggerFL(self.textEditFL, self.graphWidgetFL,\
                                                 self.labelFL0ACC, self.labelFL1ACC, self.labelFL2ACC,\
                                                 self.labelFL3ACC, self.labelFL4ACC, self.labelFL5ACC,\
                                                 self.labelFL6ACC, self.labelFL7ACC, self.labelFL8ACC,\
                                                 self.labelFL9ACC)
        fl_logger.addHandler(log_handlerFL)

        self.graphWidgetECL.setXRange(0,20)
        self.graphWidgetECL.setYRange(0.0,0.4)
        log_handlerECL = QPlainTextEditLoggerECL(self.textEditECL, self.graphWidgetECL,\
                                                 self.labelECL0ACC, self.labelECL1ACC, self.labelECL2ACC,\
                                                 self.labelECL3ACC, self.labelECL4ACC, self.labelECL5ACC,\
                                                 self.labelECL6ACC, self.labelECL7ACC, self.labelECL8ACC,\
                                                 self.labelECL9ACC)
        ecl_logger.addHandler(log_handlerECL)


        self.graphWidgetCL.setXRange(0,20)
        self.graphWidgetCL.setYRange(0.0,0.025)
        log_handlerCL = QPlainTextEditLoggerCL(self.textEditCL, self.graphWidgetCL,\
                                                 self.labelCL0ACC, self.labelCL1ACC, self.labelCL2ACC,\
                                                 self.labelCL3ACC, self.labelCL4ACC, self.labelCL5ACC,\
                                                 self.labelCL6ACC, self.labelCL7ACC, self.labelCL8ACC,\
                                                 self.labelCL9ACC)
        cl_logger.addHandler(log_handlerCL)



    def initUI(self):
        self.setWindowTitle('PyQt5')
        self.move(300,300)
        self.resize(400,200)
        self.show()

    def btnClickFL(self):
        logging.debug('clicked FL')
        self.runFLTask()

    def btnClickECL(self):
        logging.debug('clicked ECL')
        self.runECLTask()

    def btnClickCL(self):
        logging.debug('clicked CL')
        self.runCLTask()

    def reportProgress(self, n):
        #self.stepLabel.setText(f"Long-Running Step: {n}")
        print('End')

    def runFLTask(self):
        # Step 2: Create a QThread object
        self.threadFL = QThread()
        # Step 3: Create a worker object
        self.workerFL = WorkerFL()
        # Step 4: Move worker to the thread
        self.workerFL.moveToThread(self.threadFL)
        # Step 5: Connect signals and slots
        self.threadFL.started.connect(self.workerFL.run)
        self.workerFL.finished.connect(self.threadFL.quit)
        self.workerFL.finished.connect(self.workerFL.deleteLater)
        self.threadFL.finished.connect(self.threadFL.deleteLater)
        #self.workerECL.progress.connect(self.reportProgress)
        # Step 6: Start the thread
        self.threadFL.start()

        # Final resets
        self.pushButtonFL.setEnabled(False)
        self.threadFL.finished.connect(
            lambda: self.pushButtonFL.setEnabled(True)
            )

    def runECLTask(self):
        # Step 2: Create a QThread object
        self.threadECL = QThread()
        # Step 3: Create a worker object
        self.workerECL = WorkerECL()
        # Step 4: Move worker to the thread
        self.workerECL.moveToThread(self.threadECL)
        # Step 5: Connect signals and slots
        self.threadECL.started.connect(self.workerECL.run)
        self.workerECL.finished.connect(self.threadECL.quit)
        self.workerECL.finished.connect(self.workerECL.deleteLater)
        self.threadECL.finished.connect(self.threadECL.deleteLater)
        #self.workerECL.progress.connect(self.reportProgress)
        # Step 6: Start the thread
        self.threadECL.start()

        # Final resets
        self.pushButtonECL.setEnabled(False)
        self.threadECL.finished.connect(
            lambda: self.pushButtonECL.setEnabled(True)
        )

    def runCLTask(self):
        # Step 2: Create a QThread object
        self.threadCL = QThread()
        # Step 3: Create a worker object
        self.workerCL = WorkerCL()
        # Step 4: Move worker to the thread
        self.workerCL.moveToThread(self.threadCL)
        # Step 5: Connect signals and slots
        self.threadCL.started.connect(self.workerCL.run)
        self.workerCL.finished.connect(self.threadCL.quit)
        self.workerCL.finished.connect(self.workerCL.deleteLater)
        self.threadCL.finished.connect(self.threadCL.deleteLater)
        #self.worker.progress.connect(self.reportProgress)
        # Step 6: Start the thread
        self.threadCL.start()

        # Final resets
        self.pushButtonCL.setEnabled(False)
        self.threadCL.finished.connect(
            lambda: self.pushButtonCL.setEnabled(True)
        )




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    ex.show()
    sys.exit(app.exec_())
