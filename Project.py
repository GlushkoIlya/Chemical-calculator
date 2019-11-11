import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QPushButton, QWidget, QLabel, \
    QMainWindow, QCheckBox, \
    QComboBox, QFileDialog, QTextEdit, QTextBrowser, QScrollArea, QVBoxLayout
from PyQt5.QtGui import QPixmap
import sqlite3


class Main(QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.setWindowTitle('Химический калькулятор')
        self.cbox.activated[str].connect(self.next)

    def next(self, text):
        if text == "Масса вещества":
            self.nextWindow = AtomnayaMassa()
            self.nextWindow.show()
        elif text == "Вывод формулы вещества по отношению масс элементов" \
                     " в данном веществе":
            self.nextWindow = FormulaByRatio()
        elif text == "Вывод формулы вещества по массовым долям элементов":
            self.nextWindow = FormulaByPercents()
        elif text == "Таблица Менделеева":
            self.nextWindow = Mend()
        elif text == "История":
            self.nextWindow = History()
        self.nextWindow.show()


class History(QWidget):
    def __init__(self):
        super().__init__()
        self.btns = {}
        uic.loadUi('History.ui', self)
        self.base = sqlite3.connect("history.db")
        self.initUI()

    def am(self):
        sa = self.btns[self.sender()][1]
        s = self.btns[self.sender()][2]
        sa = sa[1:]
        sa = sa[:-1]
        sa = sa.split(', ')
        for j in range(len(sa)):
            sa[j] = sa[j].split(':')
            sa[j][0] = sa[j][0][1:]
            sa[j][0] = sa[j][0][:-1]
            sa[j][1] = int(sa[j][1])
        self.nextWindow = AtomnayaMassaAnswer(sa, s)
        self.nextWindow.show()

    def fbr(self):
        sa = self.btns[self.sender()][1]
        sb = self.btns[self.sender()][2]
        sa = sa[1:]
        sa = sa[:-1]
        sb = sb[1:]
        sb = sb[:-1]
        sa = sa.split(', ')
        sb = sb.split(', ')
        for j in range(len(sa)):
            sa[j] = sa[j][1:]
            sa[j] = sa[j][:-1]
            sb[j] = sb[j][1:]
            sb[j] = sb[j][:-1]
        self.nextWindow = FBRAns(sa, sb)
        self.nextWindow.show()

    def fbp(self):
        sa = self.btns[self.sender()][1]
        sb = self.btns[self.sender()][2]
        sa = sa[1:]
        sa = sa[:-1]
        sb = sb[1:]
        sb = sb[:-1]
        sa = sa.split(', ')
        sb = sb.split(', ')
        for j in range(len(sa)):
            sa[j] = sa[j][1:]
            sa[j] = sa[j][:-1]
            sb[j] = sb[j][1:]
            sb[j] = sb[j][:-1]
        self.nextWindow = FBRAns(sa, sb)
        self.nextWindow.show()

    def remove(self):
        cur = self.base.cursor()
        cur.execute("DELETE from History")
        self.base.commit()

    def initUI(self):
        cur = self.base.cursor()
        result = cur.execute("Select * from History").fetchall()
        self.pb.clicked.connect(self.remove)
        self.scrollArea.setWidgetResizable(True)
        for i in range(len(result)):
            btn = QPushButton(str(result[i][0]), self)
            btn.setText(result[i][0])
            self.verticalLayout.addWidget(btn)
            if result[i][0] == 'Масса вещества':
                btn.clicked.connect(self.am)
            elif result[i][
                0] == 'Вывод формулы вещества по отношению масс элементов в ' \
                      'данном веществе':
                btn.clicked.connect(self.fbr)
            elif result[i][
                0] == 'Вывод формулы вещества по массовым долям элементов':
                btn.clicked.connect(self.fbp)
            self.btns[btn] = result[i]
        # keys = list(self.btns.keys())
        # for i in keys:
        #     if self.btns[i][0] == 'Масса вещества':
        #         bbb :QPushButton = i
        #         bbb.clicked.connect(self.am)
        #     elif self.btns[i][
        #         0] == 'Вывод формулы вещества по отношению масс элементов в ' \
        #               'данном веществе':
        #         i.clicked.connect(self.fbr)
        #     elif self.btns[i][
        #         0] == 'Вывод формулы вещества по массовым долям элементов':
        #         i.clicked.connect(self.fbp)


class Mend(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        SCREEN_SIZE = [1200, 800]
        self.setGeometry(1200, 800, *SCREEN_SIZE)
        self.setWindowTitle('Таблица Менделеева')
        self.pixmap = QPixmap('Mend.jpg')
        self.image = QLabel(self)
        self.image.move(0, 0)
        self.image.resize(1200, 800)
        self.image.setPixmap(self.pixmap)


class AtomnayaMassa(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('AM.ui', self)
        self.stuff = []
        self.kol = ''
        self.initUi()

    def initUi(self):
        self._N.clicked.connect(self.add_element)
        self._Ra.clicked.connect(self.add_element)
        self._Rb.clicked.connect(self.add_element)
        self._Rh.clicked.connect(self.add_element)
        self._I.clicked.connect(self.add_element)
        self._Rn.clicked.connect(self.add_element)
        self._Co.clicked.connect(self.add_element)
        self._Po.clicked.connect(self.add_element)
        self._V.clicked.connect(self.add_element)
        self._Tl.clicked.connect(self.add_element)
        self._Hs.clicked.connect(self.add_element)
        self._Ni.clicked.connect(self.add_element)
        self._Br.clicked.connect(self.add_element)
        self._Hf.clicked.connect(self.add_element)
        self._Fe.clicked.connect(self.add_element)
        self._Pt.clicked.connect(self.add_element)
        self._Sc.clicked.connect(self.add_element)
        self._Bh.clicked.connect(self.add_element)
        self._Al.clicked.connect(self.add_element)
        self._In.clicked.connect(self.add_element)
        self._Te.clicked.connect(self.add_element)
        self._F.clicked.connect(self.add_element)
        self._B.clicked.connect(self.add_element)
        self._Ba.clicked.connect(self.add_element)
        self._Sg.clicked.connect(self.add_element)
        self._Cs.clicked.connect(self.add_element)
        self._Os.clicked.connect(self.add_element)
        self._Nb.clicked.connect(self.add_element)
        self._Ge.clicked.connect(self.add_element)
        self._Mg.clicked.connect(self.add_element)
        self._Y.clicked.connect(self.add_element)
        self._Mt.clicked.connect(self.add_element)
        self._Be.clicked.connect(self.add_element)
        self._W.clicked.connect(self.add_element)
        self._Hg.clicked.connect(self.add_element)
        self._Ir.clicked.connect(self.add_element)
        self._Cl.clicked.connect(self.add_element)
        self._Ds.clicked.connect(self.add_element)
        self._As.clicked.connect(self.add_element)
        self._Ac.clicked.connect(self.add_element)
        self._Fr.clicked.connect(self.add_element)
        self._P.clicked.connect(self.add_element)
        self._Db.clicked.connect(self.add_element)
        self._Tc.clicked.connect(self.add_element)
        self._Sn.clicked.connect(self.add_element)
        self._Ne.clicked.connect(self.add_element)
        self._Ti.clicked.connect(self.add_element)
        self._Au.clicked.connect(self.add_element)
        self._Ga.clicked.connect(self.add_element)
        self._Na.clicked.connect(self.add_element)
        self._La.clicked.connect(self.add_element)
        self._O.clicked.connect(self.add_element)
        self._Xe.clicked.connect(self.add_element)
        self._Ar.clicked.connect(self.add_element)
        self._Cd.clicked.connect(self.add_element)
        self._Se.clicked.connect(self.add_element)
        self._Ag.clicked.connect(self.add_element)
        self._Mn.clicked.connect(self.add_element)
        self._Ta.clicked.connect(self.add_element)
        self._At.clicked.connect(self.add_element)
        self._Si.clicked.connect(self.add_element)
        self._Ca.clicked.connect(self.add_element)
        self._Zr.clicked.connect(self.add_element)
        self._Pb.clicked.connect(self.add_element)
        self._Sb.clicked.connect(self.add_element)
        self._Kr.clicked.connect(self.add_element)
        self._Rf.clicked.connect(self.add_element)
        self._Cu.clicked.connect(self.add_element)
        self._H.clicked.connect(self.add_element)
        self._Pd.clicked.connect(self.add_element)
        self._Ru.clicked.connect(self.add_element)
        self._Sr.clicked.connect(self.add_element)
        self._Re.clicked.connect(self.add_element)
        self._Zn.clicked.connect(self.add_element)
        self._Cr.clicked.connect(self.add_element)
        self._Mo.clicked.connect(self.add_element)
        self._Bi.clicked.connect(self.add_element)
        self._C.clicked.connect(self.add_element)
        self._K.clicked.connect(self.add_element)
        self._He.clicked.connect(self.add_element)
        self._Li.clicked.connect(self.add_element)
        self._S.clicked.connect(self.add_element)
        self.one.clicked.connect(self.add_number)
        self.two.clicked.connect(self.add_number)
        self.three.clicked.connect(self.add_number)
        self.four.clicked.connect(self.add_number)
        self.five.clicked.connect(self.add_number)
        self.six.clicked.connect(self.add_number)
        self.seven.clicked.connect(self.add_number)
        self.eight.clicked.connect(self.add_number)
        self.nine.clicked.connect(self.add_number)
        self.zero.clicked.connect(self.add_number)
        self.next.clicked.connect(self.do_next)
        self.remove.clicked.connect(self.Remove)

    def Remove(self):
        if self.kol != '':
            self.stuff[-1].append(int(self.kol))
            self.kol = ''
        if self.stuff:
            del self.stuff[-1][-1]
            if not self.stuff[-1]:
                del self.stuff[-1]
            a = []
            t = ''
            text = self.label.text()

            for i in range(1, len(text) + 1):
                v = True
                tr = text[0 - i]
                if text[-1].isalpha():
                    if text[0 - i].isupper():
                        a.append(i)
                        break
                    else:
                        a.append(i)
                else:
                    if text[0 - i].isalpha():
                        break
                    else:
                        a.append(i)
            for i in range(1, len(text) + 1):
                if i not in a:
                    t += text[0 - i]
            k = ''
            for i in range(1, len(t) + 1):
                k += t[0 - i]
            self.label.setText(k)

    def add_element(self):
        if self.label.text() == 'Начните вводить формулу вещества':
            self.label.setText('')
        if self.kol != '':
            self.stuff[-1].append(int(self.kol))
            self.kol = ''
        bt = self.sender()
        t = bt.text().split()[0]
        self.label.setText(self.label.text() + '' + t)
        self.stuff.append([t])

    def add_number(self):
        bt = self.sender()
        c = [self.zero, self.one, self.two, self.three, self.four, self.five,
             self.six, self.seven, self.eight, self.nine]
        x = ''

        if bt == c[0] and self.kol != '':
            self.label.setText(self.label.text() + "\N{SUBSCRIPT ZERO}")
            x = 0
        elif bt == c[1]:
            self.label.setText(self.label.text() + "\N{SUBSCRIPT ONE}")
            x = 1
        elif bt == c[2]:
            self.label.setText(self.label.text() + "\N{SUBSCRIPT TWO}")
            x = 2
        elif bt == c[3]:
            self.label.setText(self.label.text() + "\N{SUBSCRIPT THREE}")
            x = 3
        elif bt == c[4]:
            self.label.setText(self.label.text() + "\N{SUBSCRIPT FOUR}")
            x = 4
        elif bt == c[5]:
            self.label.setText(self.label.text() + "\N{SUBSCRIPT FIVE}")
            x = 5
        elif bt == c[6]:
            self.label.setText(self.label.text() + "\N{SUBSCRIPT SIX}")
            x = 6
        elif bt == c[7]:
            self.label.setText(self.label.text() + "\N{SUBSCRIPT SEVEN}")
            x = 7
        elif bt == c[8]:
            self.label.setText(self.label.text() + "\N{SUBSCRIPT EIGHT}")
            x = 8
        elif bt == c[9]:
            self.label.setText(self.label.text() + "\N{SUBSCRIPT NINE}")
            x = 9
        self.kol += str(x)

    def do_next(self):
        if self.kol != '':
            self.stuff[-1].append(int(self.kol))
            self.kol = ''
        v = True
        for i in self.stuff:
            if i[-1] == 0:
                v = False
        if v:
            if self.stuff:
                self.nextWindow = AtomnayaMassaAnswer(self.stuff,
                                                      self.label.text())
                self.nextWindow.show()
        # Ошибок вроде нет


class AtomnayaMassaAnswer(QWidget):
    def __init__(self, arg, s):
        self.mend = {'N': [14], 'Ra': [226], 'Rb': [85], 'Rh': [103],
                     'I': [127], 'Rn': [222], 'Co': [59], 'Po': [209],
                     'V': [51], 'Tl': [204],
                     'Hs': [265], 'Ni': [59], 'Br': [80], 'Hf': [178],
                     'Fe': [56], 'Pt': [195], 'Sc': [45], 'Bh': [262],
                     'Al': [27], 'In': [115],
                     'Te': [128], 'F': [19], 'B': [11], 'Ba': [137],
                     'Sg': [263], 'Cs': [133], 'Os': [190], 'Nb': [93],
                     'Ge': [73], 'Mg': [24],
                     'Y': [89], 'Mt': [266], 'Be': [9], 'W': [184],
                     'Hg': [201], 'Ir': [192], 'Cl': [35], 'Ds': [265],
                     'As': [75], 'Ac': [227],
                     'Fr': [223], 'P': [31], 'Db': [262], 'Tc': [99],
                     'Sn': [119], 'Ne': [20], 'Ti': [48], 'Au': [197],
                     'Ga': [70], 'Na': [23],
                     'La': [139], 'O': [16], 'Xe': [131], 'Ar': [40],
                     'Cd': [112], 'Se': [79], 'Ag': [108], 'Mn': [55],
                     'Ta': [181], 'At': [210],
                     'Si': [28], 'Ca': [40], 'Zr': [91], 'Pb': [207],
                     'Sb': [122], 'Kr': [84], 'Rf': [261], 'Cu': [64],
                     'H': [1], 'Pd': [106],
                     'Ru': [101], 'Sr': [88], 'Re': [186], 'Zn': [65],
                     'Cr': [52], 'Mo': [96], 'Bi': [209], 'C': [12],
                     'K': [39], 'He': [4],
                     'Li': [7], 'S': [32]}
        super().__init__()
        uic.loadUi('AMAns.ui', self)
        a = {}
        for i in range(len(arg)):
            if arg[i][0] not in a.keys():
                if len(arg[i]) == 1:
                    a[arg[i][0]] = 1
                else:
                    a[arg[i][0]] = arg[i][1]
            else:
                if len(arg[i]) == 1:
                    a[arg[i][0]] += 1
                else:
                    a[arg[i][0]] += arg[i][1]
        self.arg = a
        self.base = sqlite3.connect("history.db")
        cur = self.base.cursor()
        cur.execute(
            "INSERT INTO History(operation, input1, input2) VALUES('Масса вещества', ?, ?)",
            (str(self.arg), s,))
        self.base.commit()
        self.s = s
        self.initUI()

    def initUI(self):
        self.name.setText(self.s)
        aa = []
        a = []
        k = list(self.arg.keys())
        k0 = k[0]
        m0 = self.mend[k0]
        arg0 = self.arg[k0]
        v = []
        for i in k:
            v = [self.mend[i][0], self.arg[i], i]
            aa.append(v)
            a.append(v[0] * v[1])
        d = a.copy()
        d.sort()
        M = 0
        for i in a:
            M += i
        k = d[0]
        tb1: QTextBrowser = self.tb1
        self.tb2.setText('')
        self.tb3.setText('')
        tb1.setText('M(' + self.s + ') = ')
        for i in range(len(aa)):
            if i == 0:
                tb1.setText(
                    self.tb1.toPlainText() + str(aa[i][1]) + ' * Ar(' + str(
                        aa[i][2]) + ')')
            else:
                self.tb1.setText(
                    self.tb1.toPlainText() + ' + ' + str(
                        aa[i][1]) + ' * Ar(' + str(
                        aa[i][2]) + ')')
        self.tb1.setText(self.tb1.toPlainText() + ' = ')
        for i in range(len(aa)):
            if i == 0:
                self.tb1.setText(
                    self.tb1.toPlainText() + str(aa[i][1]) + ' * ' + str(
                        aa[i][0]))
            else:
                self.tb1.setText(
                    self.tb1.toPlainText() + ' + ' + str(
                        aa[i][1]) + ' * ' + str(
                        aa[i][0]))
        self.tb1.setText(self.tb1.toPlainText() + ' = ')
        for i in range(len(aa)):
            if i == 0:
                self.tb1.setText(
                    self.tb1.toPlainText() + str(aa[i][1] * aa[i][0]))
            else:
                self.tb1.setText(
                    self.tb1.toPlainText() + ' + ' + str(aa[i][1] * aa[i][0]))
        self.tb1.setText(self.tb1.toPlainText() + ' = ' + str(M))
        h = ''
        g = ''
        q = ''
        for i in aa:
            if i != aa[0]:
                q += ': '
                g += ': '
                h += ': '
            h += (str(i[0] * i[1] / k) + ' ')
            g += (str(i[0] * i[1]) + ' ')
            q += ('m(' + str(i[2]) + ') ')
        self.tb2.setText(q + '= ' + g + '= ' + h)
        for i in range(len(aa)):
            self.tb3.setText(
                self.tb3.toPlainText() + '\nw(' + str(aa[i][2]) + ') = ' + str(
                    aa[i][0] * aa[i][1]) + ' / ' + str(M) + ' * 100% = ' +
                str(aa[i][0] * aa[i][1] / M * 100 + 0.005)[:5] + '%')


class FormulaByRatio(QWidget):  # Ошибок вроде нет
    def __init__(self):
        super().__init__()
        uic.loadUi('FormulaByRatio.ui', self)
        self.pushButton.clicked.connect(self.do_next)

    def do_next(self):
        t = int(self.spinBox.text())
        if t == 2:
            self.nextWindow = FormulaByRatio2()
        elif t == 3:
            self.nextWindow = FormulaByRatio3()
        elif t == 4:
            self.nextWindow = FormulaByRatio4()
        elif t == 5:
            self.nextWindow = FormulaByRatio5()
        self.nextWindow.show()


class FormulaByRatio2(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('FormulaByRatio2.ui', self)
        self.setWindowTitle('Ввод')
        self.pb1.clicked.connect(self.pb1clicked)
        self.pb2.clicked.connect(self.pb2clicked)
        self.pb3.clicked.connect(self.pb1clicked)
        self.pb4.clicked.connect(self.pb2clicked)
        self.next.clicked.connect(self.do_next)
        self.bt1 = ' '
        self.bt2 = ' '
        self.stuff = ['', '']
        self.one.clicked.connect(self.add_number)
        self.two.clicked.connect(self.add_number)
        self.three.clicked.connect(self.add_number)
        self.four.clicked.connect(self.add_number)
        self.five.clicked.connect(self.add_number)
        self.six.clicked.connect(self.add_number)
        self.seven.clicked.connect(self.add_number)
        self.eight.clicked.connect(self.add_number)
        self.nine.clicked.connect(self.add_number)
        self.zero.clicked.connect(self.add_number)
        self.point.clicked.connect(self.add_number)
        self.remove.clicked.connect(self.Remove)
        self._N.clicked.connect(self.add_element)
        self._Ra.clicked.connect(self.add_element)
        self._Rb.clicked.connect(self.add_element)
        self._Rh.clicked.connect(self.add_element)
        self._I.clicked.connect(self.add_element)
        self._Rn.clicked.connect(self.add_element)
        self._Co.clicked.connect(self.add_element)
        self._Po.clicked.connect(self.add_element)
        self._V.clicked.connect(self.add_element)
        self._Tl.clicked.connect(self.add_element)
        self._Hs.clicked.connect(self.add_element)
        self._Ni.clicked.connect(self.add_element)
        self._Br.clicked.connect(self.add_element)
        self._Hf.clicked.connect(self.add_element)
        self._Fe.clicked.connect(self.add_element)
        self._Pt.clicked.connect(self.add_element)
        self._Sc.clicked.connect(self.add_element)
        self._Bh.clicked.connect(self.add_element)
        self._Al.clicked.connect(self.add_element)
        self._In.clicked.connect(self.add_element)
        self._Te.clicked.connect(self.add_element)
        self._F.clicked.connect(self.add_element)
        self._B.clicked.connect(self.add_element)
        self._Ba.clicked.connect(self.add_element)
        self._Sg.clicked.connect(self.add_element)
        self._Cs.clicked.connect(self.add_element)
        self._Os.clicked.connect(self.add_element)
        self._Nb.clicked.connect(self.add_element)
        self._Ge.clicked.connect(self.add_element)
        self._Mg.clicked.connect(self.add_element)
        self._Y.clicked.connect(self.add_element)
        self._Mt.clicked.connect(self.add_element)
        self._Be.clicked.connect(self.add_element)
        self._W.clicked.connect(self.add_element)
        self._Hg.clicked.connect(self.add_element)
        self._Ir.clicked.connect(self.add_element)
        self._Cl.clicked.connect(self.add_element)
        self._Ds.clicked.connect(self.add_element)
        self._As.clicked.connect(self.add_element)
        self._Ac.clicked.connect(self.add_element)
        self._Fr.clicked.connect(self.add_element)
        self._P.clicked.connect(self.add_element)
        self._Db.clicked.connect(self.add_element)
        self._Tc.clicked.connect(self.add_element)
        self._Sn.clicked.connect(self.add_element)
        self._Ne.clicked.connect(self.add_element)
        self._Ti.clicked.connect(self.add_element)
        self._Au.clicked.connect(self.add_element)
        self._Ga.clicked.connect(self.add_element)
        self._Na.clicked.connect(self.add_element)
        self._La.clicked.connect(self.add_element)
        self._O.clicked.connect(self.add_element)
        self._Xe.clicked.connect(self.add_element)
        self._Ar.clicked.connect(self.add_element)
        self._Cd.clicked.connect(self.add_element)
        self._Se.clicked.connect(self.add_element)
        self._Ag.clicked.connect(self.add_element)
        self._Mn.clicked.connect(self.add_element)
        self._Ta.clicked.connect(self.add_element)
        self._At.clicked.connect(self.add_element)
        self._Si.clicked.connect(self.add_element)
        self._Ca.clicked.connect(self.add_element)
        self._Zr.clicked.connect(self.add_element)
        self._Pb.clicked.connect(self.add_element)
        self._Sb.clicked.connect(self.add_element)
        self._Kr.clicked.connect(self.add_element)
        self._Rf.clicked.connect(self.add_element)
        self._Cu.clicked.connect(self.add_element)
        self._H.clicked.connect(self.add_element)
        self._Pd.clicked.connect(self.add_element)
        self._Ru.clicked.connect(self.add_element)
        self._Sr.clicked.connect(self.add_element)
        self._Re.clicked.connect(self.add_element)
        self._Zn.clicked.connect(self.add_element)
        self._Cr.clicked.connect(self.add_element)
        self._Mo.clicked.connect(self.add_element)
        self._Bi.clicked.connect(self.add_element)
        self._C.clicked.connect(self.add_element)
        self._K.clicked.connect(self.add_element)
        self._He.clicked.connect(self.add_element)
        self._Li.clicked.connect(self.add_element)
        self._S.clicked.connect(self.add_element)

    def pb1clicked(self):
        self.bt1 = self.sender()
        self.bt2 = ' '

    def pb2clicked(self):
        self.bt2 = self.sender()
        self.bt1 = ' '

    def Remove(self):
        if self.bt2 != ' ':
            self.bt2.setText(self.bt2.text()[:-1])

    def add_number(self):
        if self.bt2 != ' ' and len(self.bt2.text()) < 5:
            bt = self.sender()
            text = str(bt.text())
            if (
                    self.bt2.text() == '' or '.' in self.bt2.text()) and text == '.':
                pass
            elif text == '.':
                self.bt2.setText(self.bt2.text() + text)
            else:
                if float(self.bt2.text() + text) == float(
                        self.bt2.text() + text) * 10 // 10:
                    self.bt2.setText(str(int(self.bt2.text() + text)))
                else:
                    self.bt2.setText(str(float(self.bt2.text() + text)))

    def do_next(self):
        self.cifr = [str(self.pb2.text()), str(self.pb4.text())]
        if '' not in self.cifr:
            cifr = list(map(lambda x: float(x), self.cifr))
            if '' not in self.stuff and 0 not in cifr:
                self.nextWindow = FBRAns(self.stuff, self.cifr)
                self.nextWindow.show()

    def add_element(self):
        if self.bt1 != ' ':
            bt = self.sender()
            t = bt.text().split()[0]
            self.bt1.setText(t)
            stuff = t
            if self.bt1 == self.pb1:
                self.stuff[0] = stuff
            elif self.bt1 == self.pb3:
                self.stuff[1] = stuff


class FormulaByRatio3(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('FormulaByRatio3.ui', self)
        self.setWindowTitle('Ввод')
        self.pb1.clicked.connect(self.pb1clicked)
        self.pb2.clicked.connect(self.pb2clicked)
        self.pb3.clicked.connect(self.pb1clicked)
        self.pb4.clicked.connect(self.pb2clicked)
        self.pb5.clicked.connect(self.pb1clicked)
        self.pb6.clicked.connect(self.pb2clicked)
        self.next.clicked.connect(self.do_next)
        self.bt1 = ' '
        self.bt2 = ' '
        self.stuff = ['', '', '']
        self.one.clicked.connect(self.add_number)
        self.two.clicked.connect(self.add_number)
        self.three.clicked.connect(self.add_number)
        self.four.clicked.connect(self.add_number)
        self.five.clicked.connect(self.add_number)
        self.six.clicked.connect(self.add_number)
        self.seven.clicked.connect(self.add_number)
        self.eight.clicked.connect(self.add_number)
        self.nine.clicked.connect(self.add_number)
        self.zero.clicked.connect(self.add_number)
        self.point.clicked.connect(self.add_number)
        self.remove.clicked.connect(self.Remove)
        self._N.clicked.connect(self.add_element)
        self._Ra.clicked.connect(self.add_element)
        self._Rb.clicked.connect(self.add_element)
        self._Rh.clicked.connect(self.add_element)
        self._I.clicked.connect(self.add_element)
        self._Rn.clicked.connect(self.add_element)
        self._Co.clicked.connect(self.add_element)
        self._Po.clicked.connect(self.add_element)
        self._V.clicked.connect(self.add_element)
        self._Tl.clicked.connect(self.add_element)
        self._Hs.clicked.connect(self.add_element)
        self._Ni.clicked.connect(self.add_element)
        self._Br.clicked.connect(self.add_element)
        self._Hf.clicked.connect(self.add_element)
        self._Fe.clicked.connect(self.add_element)
        self._Pt.clicked.connect(self.add_element)
        self._Sc.clicked.connect(self.add_element)
        self._Bh.clicked.connect(self.add_element)
        self._Al.clicked.connect(self.add_element)
        self._In.clicked.connect(self.add_element)
        self._Te.clicked.connect(self.add_element)
        self._F.clicked.connect(self.add_element)
        self._B.clicked.connect(self.add_element)
        self._Ba.clicked.connect(self.add_element)
        self._Sg.clicked.connect(self.add_element)
        self._Cs.clicked.connect(self.add_element)
        self._Os.clicked.connect(self.add_element)
        self._Nb.clicked.connect(self.add_element)
        self._Ge.clicked.connect(self.add_element)
        self._Mg.clicked.connect(self.add_element)
        self._Y.clicked.connect(self.add_element)
        self._Mt.clicked.connect(self.add_element)
        self._Be.clicked.connect(self.add_element)
        self._W.clicked.connect(self.add_element)
        self._Hg.clicked.connect(self.add_element)
        self._Ir.clicked.connect(self.add_element)
        self._Cl.clicked.connect(self.add_element)
        self._Ds.clicked.connect(self.add_element)
        self._As.clicked.connect(self.add_element)
        self._Ac.clicked.connect(self.add_element)
        self._Fr.clicked.connect(self.add_element)
        self._P.clicked.connect(self.add_element)
        self._Db.clicked.connect(self.add_element)
        self._Tc.clicked.connect(self.add_element)
        self._Sn.clicked.connect(self.add_element)
        self._Ne.clicked.connect(self.add_element)
        self._Ti.clicked.connect(self.add_element)
        self._Au.clicked.connect(self.add_element)
        self._Ga.clicked.connect(self.add_element)
        self._Na.clicked.connect(self.add_element)
        self._La.clicked.connect(self.add_element)
        self._O.clicked.connect(self.add_element)
        self._Xe.clicked.connect(self.add_element)
        self._Ar.clicked.connect(self.add_element)
        self._Cd.clicked.connect(self.add_element)
        self._Se.clicked.connect(self.add_element)
        self._Ag.clicked.connect(self.add_element)
        self._Mn.clicked.connect(self.add_element)
        self._Ta.clicked.connect(self.add_element)
        self._At.clicked.connect(self.add_element)
        self._Si.clicked.connect(self.add_element)
        self._Ca.clicked.connect(self.add_element)
        self._Zr.clicked.connect(self.add_element)
        self._Pb.clicked.connect(self.add_element)
        self._Sb.clicked.connect(self.add_element)
        self._Kr.clicked.connect(self.add_element)
        self._Rf.clicked.connect(self.add_element)
        self._Cu.clicked.connect(self.add_element)
        self._H.clicked.connect(self.add_element)
        self._Pd.clicked.connect(self.add_element)
        self._Ru.clicked.connect(self.add_element)
        self._Sr.clicked.connect(self.add_element)
        self._Re.clicked.connect(self.add_element)
        self._Zn.clicked.connect(self.add_element)
        self._Cr.clicked.connect(self.add_element)
        self._Mo.clicked.connect(self.add_element)
        self._Bi.clicked.connect(self.add_element)
        self._C.clicked.connect(self.add_element)
        self._K.clicked.connect(self.add_element)
        self._He.clicked.connect(self.add_element)
        self._Li.clicked.connect(self.add_element)
        self._S.clicked.connect(self.add_element)

    def pb1clicked(self):
        self.bt1 = self.sender()
        self.bt2 = ' '

    def pb2clicked(self):
        self.bt2 = self.sender()
        self.bt1 = ' '

    def Remove(self):
        if self.bt2 != ' ':
            self.bt2.setText(self.bt2.text()[:-1])

    def add_number(self):
        if self.bt2 != ' ' and len(self.bt2.text()) < 5:
            bt = self.sender()
            text = str(bt.text())
            if (
                    self.bt2.text() == '' or '.' in self.bt2.text()) and text == '.':
                pass
            elif text == '.':
                self.bt2.setText(self.bt2.text() + text)
            else:
                if '.' in self.bt2.text():
                    self.bt2.setText(self.bt2.text() + text)
                elif float(self.bt2.text() + text) == float(
                        self.bt2.text() + text) * 10 // 10:
                    self.bt2.setText(str(int(self.bt2.text() + text)))
                else:
                    self.bt2.setText(str(float(self.bt2.text() + text)))

    def do_next(self):
        self.cifr = [str(self.pb2.text()), str(self.pb4.text()),
                     str(self.pb6.text())]
        if '' not in self.cifr:
            cifr = list(map(lambda x: float(x), self.cifr))
            if '' not in self.stuff and 0 not in cifr:
                self.nextWindow = FBRAns(self.stuff, self.cifr)
                self.nextWindow.show()

    def add_element(self):
        if self.bt1 != ' ':
            bt = self.sender()
            t = bt.text().split()[0]
            self.bt1.setText(t)
            stuff = t
            if self.bt1 == self.pb1:
                self.stuff[0] = stuff
            elif self.bt1 == self.pb3:
                self.stuff[1] = stuff
            elif self.bt1 == self.pb5:
                self.stuff[2] = stuff


class FormulaByRatio4(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('FormulaByRatio4.ui', self)
        self.setWindowTitle('Ввод')
        self.pb1.clicked.connect(self.pb1clicked)
        self.pb2.clicked.connect(self.pb2clicked)
        self.pb3.clicked.connect(self.pb1clicked)
        self.pb4.clicked.connect(self.pb2clicked)
        self.pb5.clicked.connect(self.pb1clicked)
        self.pb6.clicked.connect(self.pb2clicked)
        self.pb7.clicked.connect(self.pb1clicked)
        self.pb8.clicked.connect(self.pb2clicked)
        self.next.clicked.connect(self.do_next)
        self.bt1 = ' '
        self.bt2 = ' '
        self.stuff = ['', '', '', '']
        self.one.clicked.connect(self.add_number)
        self.two.clicked.connect(self.add_number)
        self.three.clicked.connect(self.add_number)
        self.four.clicked.connect(self.add_number)
        self.five.clicked.connect(self.add_number)
        self.six.clicked.connect(self.add_number)
        self.seven.clicked.connect(self.add_number)
        self.eight.clicked.connect(self.add_number)
        self.nine.clicked.connect(self.add_number)
        self.zero.clicked.connect(self.add_number)
        self.point.clicked.connect(self.add_number)
        self.remove.clicked.connect(self.Remove)
        self._N.clicked.connect(self.add_element)
        self._Ra.clicked.connect(self.add_element)
        self._Rb.clicked.connect(self.add_element)
        self._Rh.clicked.connect(self.add_element)
        self._I.clicked.connect(self.add_element)
        self._Rn.clicked.connect(self.add_element)
        self._Co.clicked.connect(self.add_element)
        self._Po.clicked.connect(self.add_element)
        self._V.clicked.connect(self.add_element)
        self._Tl.clicked.connect(self.add_element)
        self._Hs.clicked.connect(self.add_element)
        self._Ni.clicked.connect(self.add_element)
        self._Br.clicked.connect(self.add_element)
        self._Hf.clicked.connect(self.add_element)
        self._Fe.clicked.connect(self.add_element)
        self._Pt.clicked.connect(self.add_element)
        self._Sc.clicked.connect(self.add_element)
        self._Bh.clicked.connect(self.add_element)
        self._Al.clicked.connect(self.add_element)
        self._In.clicked.connect(self.add_element)
        self._Te.clicked.connect(self.add_element)
        self._F.clicked.connect(self.add_element)
        self._B.clicked.connect(self.add_element)
        self._Ba.clicked.connect(self.add_element)
        self._Sg.clicked.connect(self.add_element)
        self._Cs.clicked.connect(self.add_element)
        self._Os.clicked.connect(self.add_element)
        self._Nb.clicked.connect(self.add_element)
        self._Ge.clicked.connect(self.add_element)
        self._Mg.clicked.connect(self.add_element)
        self._Y.clicked.connect(self.add_element)
        self._Mt.clicked.connect(self.add_element)
        self._Be.clicked.connect(self.add_element)
        self._W.clicked.connect(self.add_element)
        self._Hg.clicked.connect(self.add_element)
        self._Ir.clicked.connect(self.add_element)
        self._Cl.clicked.connect(self.add_element)
        self._Ds.clicked.connect(self.add_element)
        self._As.clicked.connect(self.add_element)
        self._Ac.clicked.connect(self.add_element)
        self._Fr.clicked.connect(self.add_element)
        self._P.clicked.connect(self.add_element)
        self._Db.clicked.connect(self.add_element)
        self._Tc.clicked.connect(self.add_element)
        self._Sn.clicked.connect(self.add_element)
        self._Ne.clicked.connect(self.add_element)
        self._Ti.clicked.connect(self.add_element)
        self._Au.clicked.connect(self.add_element)
        self._Ga.clicked.connect(self.add_element)
        self._Na.clicked.connect(self.add_element)
        self._La.clicked.connect(self.add_element)
        self._O.clicked.connect(self.add_element)
        self._Xe.clicked.connect(self.add_element)
        self._Ar.clicked.connect(self.add_element)
        self._Cd.clicked.connect(self.add_element)
        self._Se.clicked.connect(self.add_element)
        self._Ag.clicked.connect(self.add_element)
        self._Mn.clicked.connect(self.add_element)
        self._Ta.clicked.connect(self.add_element)
        self._At.clicked.connect(self.add_element)
        self._Si.clicked.connect(self.add_element)
        self._Ca.clicked.connect(self.add_element)
        self._Zr.clicked.connect(self.add_element)
        self._Pb.clicked.connect(self.add_element)
        self._Sb.clicked.connect(self.add_element)
        self._Kr.clicked.connect(self.add_element)
        self._Rf.clicked.connect(self.add_element)
        self._Cu.clicked.connect(self.add_element)
        self._H.clicked.connect(self.add_element)
        self._Pd.clicked.connect(self.add_element)
        self._Ru.clicked.connect(self.add_element)
        self._Sr.clicked.connect(self.add_element)
        self._Re.clicked.connect(self.add_element)
        self._Zn.clicked.connect(self.add_element)
        self._Cr.clicked.connect(self.add_element)
        self._Mo.clicked.connect(self.add_element)
        self._Bi.clicked.connect(self.add_element)
        self._C.clicked.connect(self.add_element)
        self._K.clicked.connect(self.add_element)
        self._He.clicked.connect(self.add_element)
        self._Li.clicked.connect(self.add_element)
        self._S.clicked.connect(self.add_element)

    def pb1clicked(self):
        self.bt1 = self.sender()
        self.bt2 = ' '

    def pb2clicked(self):
        self.bt2 = self.sender()
        self.bt1 = ' '

    def Remove(self):
        if self.bt2 != ' ':
            self.bt2.setText(self.bt2.text()[:-1])

    def add_number(self):
        if self.bt2 != ' ' and len(self.bt2.text()) < 5:
            bt = self.sender()
            text = str(bt.text())
            if (
                    self.bt2.text() == '' or '.' in self.bt2.text()) and text == '.':
                pass
            elif text == '.':
                self.bt2.setText(self.bt2.text() + text)
            else:
                if float(self.bt2.text() + text) == int(
                        self.bt2.text() + text):
                    self.bt2.setText(str(int(self.bt2.text() + text)))
                else:
                    self.bt2.setText(str(float(self.bt2.text() + text)))

    def do_next(self):
        self.cifr = [str(self.pb2.text()), str(self.pb4.text()),
                     str(self.pb6.text()), str(self.pb8.text())]
        if '' not in self.cifr:
            cifr = list(map(lambda x: float(x), self.cifr))
            if '' not in self.stuff and 0 not in cifr:
                self.nextWindow = FBRAns(self.stuff, self.cifr)
                self.nextWindow.show()

    def add_element(self):
        if self.bt1 != ' ':
            bt = self.sender()
            t = bt.text().split()[0]
            self.bt1.setText(t)
            stuff = t
            if self.bt1 == self.pb1:
                self.stuff[0] = stuff
            elif self.bt1 == self.pb3:
                self.stuff[1] = stuff
            elif self.bt1 == self.pb5:
                self.stuff[2] = stuff
            elif self.bt1 == self.pb7:
                self.stuff[3] = stuff


class FormulaByRatio5(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('FormulaByRatio5.ui', self)
        self.setWindowTitle('Ввод')
        self.pb1.clicked.connect(self.pb1clicked)
        self.pb2.clicked.connect(self.pb2clicked)
        self.pb3.clicked.connect(self.pb1clicked)
        self.pb4.clicked.connect(self.pb2clicked)
        self.pb5.clicked.connect(self.pb1clicked)
        self.pb6.clicked.connect(self.pb2clicked)
        self.pb7.clicked.connect(self.pb1clicked)
        self.pb8.clicked.connect(self.pb2clicked)
        self.pb9.clicked.connect(self.pb1clicked)
        self.pb10.clicked.connect(self.pb2clicked)
        self.next.clicked.connect(self.do_next)
        self.bt1 = ' '
        self.bt2 = ' '
        self.stuff = ['', '', '', '', '']
        self.one.clicked.connect(self.add_number)
        self.two.clicked.connect(self.add_number)
        self.three.clicked.connect(self.add_number)
        self.four.clicked.connect(self.add_number)
        self.five.clicked.connect(self.add_number)
        self.six.clicked.connect(self.add_number)
        self.seven.clicked.connect(self.add_number)
        self.eight.clicked.connect(self.add_number)
        self.nine.clicked.connect(self.add_number)
        self.zero.clicked.connect(self.add_number)
        self.point.clicked.connect(self.add_number)
        self.remove.clicked.connect(self.Remove)
        self._N.clicked.connect(self.add_element)
        self._Ra.clicked.connect(self.add_element)
        self._Rb.clicked.connect(self.add_element)
        self._Rh.clicked.connect(self.add_element)
        self._I.clicked.connect(self.add_element)
        self._Rn.clicked.connect(self.add_element)
        self._Co.clicked.connect(self.add_element)
        self._Po.clicked.connect(self.add_element)
        self._V.clicked.connect(self.add_element)
        self._Tl.clicked.connect(self.add_element)
        self._Hs.clicked.connect(self.add_element)
        self._Ni.clicked.connect(self.add_element)
        self._Br.clicked.connect(self.add_element)
        self._Hf.clicked.connect(self.add_element)
        self._Fe.clicked.connect(self.add_element)
        self._Pt.clicked.connect(self.add_element)
        self._Sc.clicked.connect(self.add_element)
        self._Bh.clicked.connect(self.add_element)
        self._Al.clicked.connect(self.add_element)
        self._In.clicked.connect(self.add_element)
        self._Te.clicked.connect(self.add_element)
        self._F.clicked.connect(self.add_element)
        self._B.clicked.connect(self.add_element)
        self._Ba.clicked.connect(self.add_element)
        self._Sg.clicked.connect(self.add_element)
        self._Cs.clicked.connect(self.add_element)
        self._Os.clicked.connect(self.add_element)
        self._Nb.clicked.connect(self.add_element)
        self._Ge.clicked.connect(self.add_element)
        self._Mg.clicked.connect(self.add_element)
        self._Y.clicked.connect(self.add_element)
        self._Mt.clicked.connect(self.add_element)
        self._Be.clicked.connect(self.add_element)
        self._W.clicked.connect(self.add_element)
        self._Hg.clicked.connect(self.add_element)
        self._Ir.clicked.connect(self.add_element)
        self._Cl.clicked.connect(self.add_element)
        self._Ds.clicked.connect(self.add_element)
        self._As.clicked.connect(self.add_element)
        self._Ac.clicked.connect(self.add_element)
        self._Fr.clicked.connect(self.add_element)
        self._P.clicked.connect(self.add_element)
        self._Db.clicked.connect(self.add_element)
        self._Tc.clicked.connect(self.add_element)
        self._Sn.clicked.connect(self.add_element)
        self._Ne.clicked.connect(self.add_element)
        self._Ti.clicked.connect(self.add_element)
        self._Au.clicked.connect(self.add_element)
        self._Ga.clicked.connect(self.add_element)
        self._Na.clicked.connect(self.add_element)
        self._La.clicked.connect(self.add_element)
        self._O.clicked.connect(self.add_element)
        self._Xe.clicked.connect(self.add_element)
        self._Ar.clicked.connect(self.add_element)
        self._Cd.clicked.connect(self.add_element)
        self._Se.clicked.connect(self.add_element)
        self._Ag.clicked.connect(self.add_element)
        self._Mn.clicked.connect(self.add_element)
        self._Ta.clicked.connect(self.add_element)
        self._At.clicked.connect(self.add_element)
        self._Si.clicked.connect(self.add_element)
        self._Ca.clicked.connect(self.add_element)
        self._Zr.clicked.connect(self.add_element)
        self._Pb.clicked.connect(self.add_element)
        self._Sb.clicked.connect(self.add_element)
        self._Kr.clicked.connect(self.add_element)
        self._Rf.clicked.connect(self.add_element)
        self._Cu.clicked.connect(self.add_element)
        self._H.clicked.connect(self.add_element)
        self._Pd.clicked.connect(self.add_element)
        self._Ru.clicked.connect(self.add_element)
        self._Sr.clicked.connect(self.add_element)
        self._Re.clicked.connect(self.add_element)
        self._Zn.clicked.connect(self.add_element)
        self._Cr.clicked.connect(self.add_element)
        self._Mo.clicked.connect(self.add_element)
        self._Bi.clicked.connect(self.add_element)
        self._C.clicked.connect(self.add_element)
        self._K.clicked.connect(self.add_element)
        self._He.clicked.connect(self.add_element)
        self._Li.clicked.connect(self.add_element)
        self._S.clicked.connect(self.add_element)

    def pb1clicked(self):
        self.bt1 = self.sender()
        self.bt2 = ' '

    def pb2clicked(self):
        self.bt2 = self.sender()
        self.bt1 = ' '

    def Remove(self):
        if self.bt2 != ' ':
            self.bt2.setText(self.bt2.text()[:-1])

    def add_number(self):
        if self.bt2 != ' ' and len(self.bt2.text()) < 5:
            bt = self.sender()
            text = str(bt.text())
            if (
                    self.bt2.text() == '' or '.' in self.bt2.text()) and text == '.':
                pass
            elif text == '.':
                self.bt2.setText(self.bt2.text() + text)
            else:
                if float(self.bt2.text() + text) == float(
                        self.bt2.text() + text) * 10 // 10:
                    self.bt2.setText(str(int(self.bt2.text() + text)))
                else:
                    self.bt2.setText(str(float(self.bt2.text() + text)))

    def do_next(self):
        self.cifr = [str(self.pb2.text()), str(self.pb4.text()),
                     str(self.pb6.text()), str(self.pb8.text()),
                     str(self.pb10.text())]
        if '' not in self.cifr:
            cifr = list(map(lambda x: float(x), self.cifr))
            if '' not in self.stuff and 0 not in cifr:
                self.nextWindow = FBRAns(self.stuff, self.cifr)
                self.nextWindow.show()

    def add_element(self):
        if self.bt1 != ' ':
            bt = self.sender()
            t = bt.text().split()[0]
            self.bt1.setText(t)
            stuff = t
            if self.bt1 == self.pb1:
                self.stuff[0] = stuff
            elif self.bt1 == self.pb3:
                self.stuff[1] = stuff
            elif self.bt1 == self.pb5:
                self.stuff[2] = stuff
            elif self.bt1 == self.pb7:
                self.stuff[3] = stuff
            elif self.bt1 == self.pb9:
                self.stuff[4] = stuff


class FBRAns(QWidget):
    def __init__(self, arg1, arg2):
        self.base = sqlite3.connect("history.db")
        cur = self.base.cursor()
        cur.execute(
            "INSERT INTO History(operation, input1, input2) VALUES('Вывод формулы вещества по отношению масс элементов в данном веществе', ?, ?)",
            (str(arg1), str(arg2),))
        self.base.commit()
        super().__init__()
        uic.loadUi('FBRAns.ui', self)
        self.mend = {'N': [14], 'Ra': [226], 'Rb': [85], 'Rh': [103],
                     'I': [127], 'Rn': [222], 'Co': [59], 'Po': [209],
                     'V': [51], 'Tl': [204],
                     'Hs': [265], 'Ni': [59], 'Br': [80], 'Hf': [178],
                     'Fe': [56], 'Pt': [195], 'Sc': [45], 'Bh': [262],
                     'Al': [27], 'In': [115],
                     'Te': [128], 'F': [19], 'B': [11], 'Ba': [137],
                     'Sg': [263], 'Cs': [133], 'Os': [190], 'Nb': [93],
                     'Ge': [73], 'Mg': [24],
                     'Y': [89], 'Mt': [266], 'Be': [9], 'W': [184],
                     'Hg': [201], 'Ir': [192], 'Cl': [35], 'Ds': [265],
                     'As': [75], 'Ac': [227],
                     'Fr': [223], 'P': [31], 'Db': [262], 'Tc': [99],
                     'Sn': [119], 'Ne': [20], 'Ti': [48], 'Au': [197],
                     'Ga': [70], 'Na': [23],
                     'La': [139], 'O': [16], 'Xe': [131], 'Ar': [40],
                     'Cd': [112], 'Se': [79], 'Ag': [108], 'Mn': [55],
                     'Ta': [181], 'At': [210],
                     'Si': [28], 'Ca': [40], 'Zr': [91], 'Pb': [207],
                     'Sb': [122], 'Kr': [84], 'Rf': [261], 'Cu': [64],
                     'H': [1], 'Pd': [106],
                     'Ru': [101], 'Sr': [88], 'Re': [186], 'Zn': [65],
                     'Cr': [52], 'Mo': [96], 'Bi': [209], 'C': [12],
                     'K': [39], 'He': [4],
                     'Li': [7], 'S': [32]}
        self.base = sqlite3.connect("history.db")
        self.ln = len(arg1)
        self.stuff = arg1
        self.cifr0 = arg2
        self.cifr = []
        m = 0
        for i in range(self.ln):
            t = self.cifr0[i].split('.')
            if len(t) > 1:
                t1 = len(t[1])
                if t1 > m:
                    m = t1
        m = int('1' + '0' * m)
        for i in range(self.ln):
            self.cifr.append(str(float(self.cifr0[i]) * m))
        self.initUI()

    def initUI(self):
        per = ['a', 'b', 'c', 'd', 'e']
        res = []
        lt = []
        dano1 = ''
        dano2 = ''
        dano3 = ''
        s0 = ''
        s1 = ''
        s2 = ''
        s3 = ''
        s4 = ''
        for i in range(self.ln):
            if i != 0:
                dano1 += ' : '
                dano2 += ' : '
                dano3 += ' : '
            dano1 += 'm( ' + self.stuff[i] + ' )'
            dano2 += self.cifr0[i]
            dano3 += self.cifr[i]
        self.dano.setText(dano1 + ' = ' + dano2 + ' = ' + dano3)

        for i in range(self.ln):
            lt.append(float(str(
                float(self.cifr[i]) / self.mend[self.stuff[i]][0] + 0.0005)[
                            :5]))
        ltcopy = lt.copy()
        ltcopy.sort()
        for i in range(self.ln):
            s0 += (self.stuff[i] + ' - ' + per[i] + ';   ')
            res.append(float(str(lt[i] / ltcopy[0] + 0.005)[:4]))
            if i != 0:
                s2 += '  :  '
                s3 += '  :  '
                s4 += '  :  '
                s1 += '  :  '
            s1 += per[i]
            s2 += (str(self.cifr[i]) + '/' + str(
                self.mend[self.stuff[i]][0]))
            s3 += str(lt[i]) + '/' + str(ltcopy[0])
            s4 += str(res[-1])
        self.tb1.setText(s0)
        self.tb2.setText(s1 + ' = ' + s2 + ' = ' + s3 + ' = ' + s4)
        ans = ''
        v = True
        for i in range(self.ln):
            if float(res[i] * 10 // 10) != res[i]:
                for j in range(1, 100):
                    if float(res[i] * j * 10 // 10) != res[i] * j:
                        pass
                    else:
                        for k in range(len(res)):
                            res[k] *= j
                        break
        for i in range(self.ln):
            if float(res[i] * 10 // 10) != res[i]:
                v = False
        if not v:
            self.ans.setText('Калькулятор не может это посчитать')
        else:
            for i in range(self.ln):
                ans += self.stuff[i]
                for k in range(len(str(res[i]))):
                    if str(res[i])[k] == '1' and len(str(res[i])) - k > 1 and \
                            str(res[i])[k + 1] == '.':
                        pass
                    elif str(res[i])[k] == '.':
                        break
                    elif str(res[i])[k] == '1':
                        ans += '\N{SUBSCRIPT ONE}'
                    elif str(res[i])[k] == '2':
                        ans += '\N{SUBSCRIPT TWO}'
                    elif str(res[i])[k] == '3':
                        ans += '\N{SUBSCRIPT THREE}'
                    elif str(res[i])[k] == '4':
                        ans += '\N{SUBSCRIPT FOUR}'
                    elif str(res[i])[k] == '5':
                        ans += '\N{SUBSCRIPT FIVE}'
                    elif str(res[i])[k] == '6':
                        ans += '\N{SUBSCRIPT SIX}'
                    elif str(res[i])[k] == '7':
                        ans += '\N{SUBSCRIPT SEVEN}'
                    elif str(res[i])[k] == '8':
                        ans += '\N{SUBSCRIPT EIGHT}'
                    elif str(res[i])[k] == '9':
                        ans += '\N{SUBSCRIPT NINE}'
                    elif str(res[i])[k] == '0':
                        ans += '\N{SUBSCRIPT ZERO}'
            self.ans.setText(ans)


class FormulaByPercents(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('FormulaByPercents.ui', self)
        self.pushButton.clicked.connect(self.do_next)

    def do_next(self):
        t = int(self.spinBox.text())
        if t == 2:
            self.nextWindow = FormulaByPercents2()
        elif t == 3:
            self.nextWindow = FormulaByPercents3()
        elif t == 4:
            self.nextWindow = FormulaByPercents4()
        elif t == 5:
            self.nextWindow = FormulaByPercents5()
        self.nextWindow.show()


class FormulaByPercents2(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('FormulaByPercents2.ui', self)
        self.setWindowTitle('Ввод')

        self.pb1.clicked.connect(self.pb1clicked)
        self.pb2.clicked.connect(self.pb2clicked)
        self.pb3.clicked.connect(self.pb1clicked)
        self.pb4.clicked.connect(self.pb2clicked)
        self.next.clicked.connect(self.do_next)
        self.bt1 = ' '
        self.bt2 = ' '
        self.stuff = ['', '']
        self.one.clicked.connect(self.add_number)
        self.two.clicked.connect(self.add_number)
        self.three.clicked.connect(self.add_number)
        self.four.clicked.connect(self.add_number)
        self.five.clicked.connect(self.add_number)
        self.six.clicked.connect(self.add_number)
        self.seven.clicked.connect(self.add_number)
        self.eight.clicked.connect(self.add_number)
        self.nine.clicked.connect(self.add_number)
        self.zero.clicked.connect(self.add_number)
        self.point.clicked.connect(self.add_number)
        self.remove.clicked.connect(self.Remove)
        self._N.clicked.connect(self.add_element)
        self._Ra.clicked.connect(self.add_element)
        self._Rb.clicked.connect(self.add_element)
        self._Rh.clicked.connect(self.add_element)
        self._I.clicked.connect(self.add_element)
        self._Rn.clicked.connect(self.add_element)
        self._Co.clicked.connect(self.add_element)
        self._Po.clicked.connect(self.add_element)
        self._V.clicked.connect(self.add_element)
        self._Tl.clicked.connect(self.add_element)
        self._Hs.clicked.connect(self.add_element)
        self._Ni.clicked.connect(self.add_element)
        self._Br.clicked.connect(self.add_element)
        self._Hf.clicked.connect(self.add_element)
        self._Fe.clicked.connect(self.add_element)
        self._Pt.clicked.connect(self.add_element)
        self._Sc.clicked.connect(self.add_element)
        self._Bh.clicked.connect(self.add_element)
        self._Al.clicked.connect(self.add_element)
        self._In.clicked.connect(self.add_element)
        self._Te.clicked.connect(self.add_element)
        self._F.clicked.connect(self.add_element)
        self._B.clicked.connect(self.add_element)
        self._Ba.clicked.connect(self.add_element)
        self._Sg.clicked.connect(self.add_element)
        self._Cs.clicked.connect(self.add_element)
        self._Os.clicked.connect(self.add_element)
        self._Nb.clicked.connect(self.add_element)
        self._Ge.clicked.connect(self.add_element)
        self._Mg.clicked.connect(self.add_element)
        self._Y.clicked.connect(self.add_element)
        self._Mt.clicked.connect(self.add_element)
        self._Be.clicked.connect(self.add_element)
        self._W.clicked.connect(self.add_element)
        self._Hg.clicked.connect(self.add_element)
        self._Ir.clicked.connect(self.add_element)
        self._Cl.clicked.connect(self.add_element)
        self._Ds.clicked.connect(self.add_element)
        self._As.clicked.connect(self.add_element)
        self._Ac.clicked.connect(self.add_element)
        self._Fr.clicked.connect(self.add_element)
        self._P.clicked.connect(self.add_element)
        self._Db.clicked.connect(self.add_element)
        self._Tc.clicked.connect(self.add_element)
        self._Sn.clicked.connect(self.add_element)
        self._Ne.clicked.connect(self.add_element)
        self._Ti.clicked.connect(self.add_element)
        self._Au.clicked.connect(self.add_element)
        self._Ga.clicked.connect(self.add_element)
        self._Na.clicked.connect(self.add_element)
        self._La.clicked.connect(self.add_element)
        self._O.clicked.connect(self.add_element)
        self._Xe.clicked.connect(self.add_element)
        self._Ar.clicked.connect(self.add_element)
        self._Cd.clicked.connect(self.add_element)
        self._Se.clicked.connect(self.add_element)
        self._Ag.clicked.connect(self.add_element)
        self._Mn.clicked.connect(self.add_element)
        self._Ta.clicked.connect(self.add_element)
        self._At.clicked.connect(self.add_element)
        self._Si.clicked.connect(self.add_element)
        self._Ca.clicked.connect(self.add_element)
        self._Zr.clicked.connect(self.add_element)
        self._Pb.clicked.connect(self.add_element)
        self._Sb.clicked.connect(self.add_element)
        self._Kr.clicked.connect(self.add_element)
        self._Rf.clicked.connect(self.add_element)
        self._Cu.clicked.connect(self.add_element)
        self._H.clicked.connect(self.add_element)
        self._Pd.clicked.connect(self.add_element)
        self._Ru.clicked.connect(self.add_element)
        self._Sr.clicked.connect(self.add_element)
        self._Re.clicked.connect(self.add_element)
        self._Zn.clicked.connect(self.add_element)
        self._Cr.clicked.connect(self.add_element)
        self._Mo.clicked.connect(self.add_element)
        self._Bi.clicked.connect(self.add_element)
        self._C.clicked.connect(self.add_element)
        self._K.clicked.connect(self.add_element)
        self._He.clicked.connect(self.add_element)
        self._Li.clicked.connect(self.add_element)
        self._S.clicked.connect(self.add_element)

    def pb1clicked(self):
        self.bt1 = self.sender()
        self.bt2 = ' '

    def pb2clicked(self):
        self.bt2 = self.sender()
        self.bt1 = ' '

    def Remove(self):
        if self.bt2 != ' ':
            self.bt2.setText(self.bt2.text()[:-1])

    def add_number(self):
        if self.bt2 != ' ' and len(self.bt2.text()) < 5:
            bt = self.sender()
            text = str(bt.text())
            if (
                    self.bt2.text() == '' or '.' in self.bt2.text()) and text == '.':
                pass
            elif text == '.':
                self.bt2.setText(self.bt2.text() + text)
            else:
                if float(self.bt2.text() + text) == float(
                        self.bt2.text() + text) * 10 // 10:
                    self.bt2.setText(str(int(self.bt2.text() + text)))
                else:
                    self.bt2.setText(str(float(self.bt2.text() + text)))

    def do_next(self):
        self.cifr = [str(self.pb2.text()), str(self.pb4.text())]
        if '' not in self.cifr:
            cifr = list(map(lambda x: float(x), self.cifr))
            if '' not in self.stuff and sum(
                    cifr) == 100 and 0 not in cifr:
                self.nextWindow = FBPAns(self.stuff, self.cifr)
                self.nextWindow.show()

    def add_element(self):
        if self.bt1 != ' ':
            bt = self.sender()
            t = bt.text().split()[0]
            self.bt1.setText(t)
            stuff = t
            if self.bt1 == self.pb1:
                self.stuff[0] = stuff
            elif self.bt1 == self.pb3:
                self.stuff[1] = stuff


class FormulaByPercents3(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('FormulaByPercents3.ui', self)
        self.setWindowTitle('Ввод')
        self.pb1.clicked.connect(self.pb1clicked)
        self.pb2.clicked.connect(self.pb2clicked)
        self.pb3.clicked.connect(self.pb1clicked)
        self.pb4.clicked.connect(self.pb2clicked)
        self.pb5.clicked.connect(self.pb1clicked)
        self.pb6.clicked.connect(self.pb2clicked)
        self.next.clicked.connect(self.do_next)
        self.bt1 = ' '
        self.bt2 = ' '
        self.stuff = ['', '', '']
        self.one.clicked.connect(self.add_number)
        self.two.clicked.connect(self.add_number)
        self.three.clicked.connect(self.add_number)
        self.four.clicked.connect(self.add_number)
        self.five.clicked.connect(self.add_number)
        self.six.clicked.connect(self.add_number)
        self.seven.clicked.connect(self.add_number)
        self.eight.clicked.connect(self.add_number)
        self.nine.clicked.connect(self.add_number)
        self.zero.clicked.connect(self.add_number)
        self.point.clicked.connect(self.add_number)
        self.remove.clicked.connect(self.Remove)
        self._N.clicked.connect(self.add_element)
        self._Ra.clicked.connect(self.add_element)
        self._Rb.clicked.connect(self.add_element)
        self._Rh.clicked.connect(self.add_element)
        self._I.clicked.connect(self.add_element)
        self._Rn.clicked.connect(self.add_element)
        self._Co.clicked.connect(self.add_element)
        self._Po.clicked.connect(self.add_element)
        self._V.clicked.connect(self.add_element)
        self._Tl.clicked.connect(self.add_element)
        self._Hs.clicked.connect(self.add_element)
        self._Ni.clicked.connect(self.add_element)
        self._Br.clicked.connect(self.add_element)
        self._Hf.clicked.connect(self.add_element)
        self._Fe.clicked.connect(self.add_element)
        self._Pt.clicked.connect(self.add_element)
        self._Sc.clicked.connect(self.add_element)
        self._Bh.clicked.connect(self.add_element)
        self._Al.clicked.connect(self.add_element)
        self._In.clicked.connect(self.add_element)
        self._Te.clicked.connect(self.add_element)
        self._F.clicked.connect(self.add_element)
        self._B.clicked.connect(self.add_element)
        self._Ba.clicked.connect(self.add_element)
        self._Sg.clicked.connect(self.add_element)
        self._Cs.clicked.connect(self.add_element)
        self._Os.clicked.connect(self.add_element)
        self._Nb.clicked.connect(self.add_element)
        self._Ge.clicked.connect(self.add_element)
        self._Mg.clicked.connect(self.add_element)
        self._Y.clicked.connect(self.add_element)
        self._Mt.clicked.connect(self.add_element)
        self._Be.clicked.connect(self.add_element)
        self._W.clicked.connect(self.add_element)
        self._Hg.clicked.connect(self.add_element)
        self._Ir.clicked.connect(self.add_element)
        self._Cl.clicked.connect(self.add_element)
        self._Ds.clicked.connect(self.add_element)
        self._As.clicked.connect(self.add_element)
        self._Ac.clicked.connect(self.add_element)
        self._Fr.clicked.connect(self.add_element)
        self._P.clicked.connect(self.add_element)
        self._Db.clicked.connect(self.add_element)
        self._Tc.clicked.connect(self.add_element)
        self._Sn.clicked.connect(self.add_element)
        self._Ne.clicked.connect(self.add_element)
        self._Ti.clicked.connect(self.add_element)
        self._Au.clicked.connect(self.add_element)
        self._Ga.clicked.connect(self.add_element)
        self._Na.clicked.connect(self.add_element)
        self._La.clicked.connect(self.add_element)
        self._O.clicked.connect(self.add_element)
        self._Xe.clicked.connect(self.add_element)
        self._Ar.clicked.connect(self.add_element)
        self._Cd.clicked.connect(self.add_element)
        self._Se.clicked.connect(self.add_element)
        self._Ag.clicked.connect(self.add_element)
        self._Mn.clicked.connect(self.add_element)
        self._Ta.clicked.connect(self.add_element)
        self._At.clicked.connect(self.add_element)
        self._Si.clicked.connect(self.add_element)
        self._Ca.clicked.connect(self.add_element)
        self._Zr.clicked.connect(self.add_element)
        self._Pb.clicked.connect(self.add_element)
        self._Sb.clicked.connect(self.add_element)
        self._Kr.clicked.connect(self.add_element)
        self._Rf.clicked.connect(self.add_element)
        self._Cu.clicked.connect(self.add_element)
        self._H.clicked.connect(self.add_element)
        self._Pd.clicked.connect(self.add_element)
        self._Ru.clicked.connect(self.add_element)
        self._Sr.clicked.connect(self.add_element)
        self._Re.clicked.connect(self.add_element)
        self._Zn.clicked.connect(self.add_element)
        self._Cr.clicked.connect(self.add_element)
        self._Mo.clicked.connect(self.add_element)
        self._Bi.clicked.connect(self.add_element)
        self._C.clicked.connect(self.add_element)
        self._K.clicked.connect(self.add_element)
        self._He.clicked.connect(self.add_element)
        self._Li.clicked.connect(self.add_element)
        self._S.clicked.connect(self.add_element)

    def pb1clicked(self):
        self.bt1 = self.sender()
        self.bt2 = ' '

    def pb2clicked(self):
        self.bt2 = self.sender()
        self.bt1 = ' '

    def Remove(self):
        if self.bt2 != ' ':
            self.bt2.setText(self.bt2.text()[:-1])

    def add_number(self):
        if self.bt2 != ' ' and len(self.bt2.text()) < 5:
            bt = self.sender()
            text = str(bt.text())
            if (
                    self.bt2.text() == '' or '.' in self.bt2.text()) and text == '.':
                pass
            elif text == '.':
                self.bt2.setText(self.bt2.text() + text)
            else:
                if float(self.bt2.text() + text) == float(
                        self.bt2.text() + text) * 10 // 10:
                    self.bt2.setText(str(int(self.bt2.text() + text)))
                else:
                    self.bt2.setText(str(float(self.bt2.text() + text)))

    def do_next(self):
        self.cifr = [str(self.pb2.text()), str(self.pb4.text()),
                     str(self.pb6.text())]
        if '' not in self.cifr:
            cifr = list(map(lambda x: float(x), self.cifr))
            if '' not in self.stuff and sum(
                    cifr) == 100 and 0 not in cifr:
                self.nextWindow = FBPAns(self.stuff, self.cifr)
                self.nextWindow.show()

    def add_element(self):
        if self.bt1 != ' ':
            bt = self.sender()
            t = bt.text().split()[0]
            self.bt1.setText(t)
            stuff = t
            if self.bt1 == self.pb1:
                self.stuff[0] = stuff
            elif self.bt1 == self.pb3:
                self.stuff[1] = stuff
            elif self.bt1 == self.pb5:
                self.stuff[2] = stuff


class FormulaByPercents4(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('FormulaByPercents4.ui', self)
        self.setWindowTitle('Ввод')
        self.pb1.clicked.connect(self.pb1clicked)
        self.pb2.clicked.connect(self.pb2clicked)
        self.pb3.clicked.connect(self.pb1clicked)
        self.pb4.clicked.connect(self.pb2clicked)
        self.pb5.clicked.connect(self.pb1clicked)
        self.pb6.clicked.connect(self.pb2clicked)
        self.pb7.clicked.connect(self.pb1clicked)
        self.pb8.clicked.connect(self.pb2clicked)
        self.next.clicked.connect(self.do_next)
        self.bt1 = ' '
        self.bt2 = ' '
        self.stuff = ['', '', '', '']
        self.one.clicked.connect(self.add_number)
        self.two.clicked.connect(self.add_number)
        self.three.clicked.connect(self.add_number)
        self.four.clicked.connect(self.add_number)
        self.five.clicked.connect(self.add_number)
        self.six.clicked.connect(self.add_number)
        self.seven.clicked.connect(self.add_number)
        self.eight.clicked.connect(self.add_number)
        self.nine.clicked.connect(self.add_number)
        self.zero.clicked.connect(self.add_number)
        self.point.clicked.connect(self.add_number)
        self.remove.clicked.connect(self.Remove)
        self._N.clicked.connect(self.add_element)
        self._Ra.clicked.connect(self.add_element)
        self._Rb.clicked.connect(self.add_element)
        self._Rh.clicked.connect(self.add_element)
        self._I.clicked.connect(self.add_element)
        self._Rn.clicked.connect(self.add_element)
        self._Co.clicked.connect(self.add_element)
        self._Po.clicked.connect(self.add_element)
        self._V.clicked.connect(self.add_element)
        self._Tl.clicked.connect(self.add_element)
        self._Hs.clicked.connect(self.add_element)
        self._Ni.clicked.connect(self.add_element)
        self._Br.clicked.connect(self.add_element)
        self._Hf.clicked.connect(self.add_element)
        self._Fe.clicked.connect(self.add_element)
        self._Pt.clicked.connect(self.add_element)
        self._Sc.clicked.connect(self.add_element)
        self._Bh.clicked.connect(self.add_element)
        self._Al.clicked.connect(self.add_element)
        self._In.clicked.connect(self.add_element)
        self._Te.clicked.connect(self.add_element)
        self._F.clicked.connect(self.add_element)
        self._B.clicked.connect(self.add_element)
        self._Ba.clicked.connect(self.add_element)
        self._Sg.clicked.connect(self.add_element)
        self._Cs.clicked.connect(self.add_element)
        self._Os.clicked.connect(self.add_element)
        self._Nb.clicked.connect(self.add_element)
        self._Ge.clicked.connect(self.add_element)
        self._Mg.clicked.connect(self.add_element)
        self._Y.clicked.connect(self.add_element)
        self._Mt.clicked.connect(self.add_element)
        self._Be.clicked.connect(self.add_element)
        self._W.clicked.connect(self.add_element)
        self._Hg.clicked.connect(self.add_element)
        self._Ir.clicked.connect(self.add_element)
        self._Cl.clicked.connect(self.add_element)
        self._Ds.clicked.connect(self.add_element)
        self._As.clicked.connect(self.add_element)
        self._Ac.clicked.connect(self.add_element)
        self._Fr.clicked.connect(self.add_element)
        self._P.clicked.connect(self.add_element)
        self._Db.clicked.connect(self.add_element)
        self._Tc.clicked.connect(self.add_element)
        self._Sn.clicked.connect(self.add_element)
        self._Ne.clicked.connect(self.add_element)
        self._Ti.clicked.connect(self.add_element)
        self._Au.clicked.connect(self.add_element)
        self._Ga.clicked.connect(self.add_element)
        self._Na.clicked.connect(self.add_element)
        self._La.clicked.connect(self.add_element)
        self._O.clicked.connect(self.add_element)
        self._Xe.clicked.connect(self.add_element)
        self._Ar.clicked.connect(self.add_element)
        self._Cd.clicked.connect(self.add_element)
        self._Se.clicked.connect(self.add_element)
        self._Ag.clicked.connect(self.add_element)
        self._Mn.clicked.connect(self.add_element)
        self._Ta.clicked.connect(self.add_element)
        self._At.clicked.connect(self.add_element)
        self._Si.clicked.connect(self.add_element)
        self._Ca.clicked.connect(self.add_element)
        self._Zr.clicked.connect(self.add_element)
        self._Pb.clicked.connect(self.add_element)
        self._Sb.clicked.connect(self.add_element)
        self._Kr.clicked.connect(self.add_element)
        self._Rf.clicked.connect(self.add_element)
        self._Cu.clicked.connect(self.add_element)
        self._H.clicked.connect(self.add_element)
        self._Pd.clicked.connect(self.add_element)
        self._Ru.clicked.connect(self.add_element)
        self._Sr.clicked.connect(self.add_element)
        self._Re.clicked.connect(self.add_element)
        self._Zn.clicked.connect(self.add_element)
        self._Cr.clicked.connect(self.add_element)
        self._Mo.clicked.connect(self.add_element)
        self._Bi.clicked.connect(self.add_element)
        self._C.clicked.connect(self.add_element)
        self._K.clicked.connect(self.add_element)
        self._He.clicked.connect(self.add_element)
        self._Li.clicked.connect(self.add_element)
        self._S.clicked.connect(self.add_element)

    def pb1clicked(self):
        self.bt1 = self.sender()
        self.bt2 = ' '

    def pb2clicked(self):
        self.bt2 = self.sender()
        self.bt1 = ' '

    def Remove(self):
        if self.bt2 != ' ':
            self.bt2.setText(self.bt2.text()[:-1])

    def add_number(self):
        if self.bt2 != ' ' and len(self.bt2.text()) < 5:
            bt = self.sender()
            text = str(bt.text())
            if (
                    self.bt2.text() == '' or '.' in self.bt2.text()) and text == '.':
                pass
            elif text == '.':
                self.bt2.setText(self.bt2.text() + text)
            else:
                if float(self.bt2.text() + text) == float(
                        self.bt2.text() + text) * 10 // 10:
                    self.bt2.setText(str(int(self.bt2.text() + text)))
                else:
                    self.bt2.setText(str(float(self.bt2.text() + text)))

    def do_next(self):
        self.cifr = [str(self.pb2.text()), str(self.pb4.text()),
                     str(self.pb6.text()), str(self.pb8.text())]
        if '' not in self.cifr:
            cifr = list(map(lambda x: float(x), self.cifr))
            if '' not in self.stuff and sum(
                    cifr) == 100 and 0 not in cifr:
                self.nextWindow = FBPAns(self.stuff, self.cifr)
                self.nextWindow.show()

    def add_element(self):
        if self.bt1 != ' ':
            bt = self.sender()
            t = bt.text().split()[0]
            self.bt1.setText(t)
            stuff = t
            if self.bt1 == self.pb1:
                self.stuff[0] = stuff
            elif self.bt1 == self.pb3:
                self.stuff[1] = stuff
            elif self.bt1 == self.pb5:
                self.stuff[2] = stuff
            elif self.bt1 == self.pb7:
                self.stuff[3] = stuff


class FormulaByPercents5(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('FormulaByPercents5.ui', self)
        self.setWindowTitle('Ввод')
        self.pb1.clicked.connect(self.pb1clicked)
        self.pb2.clicked.connect(self.pb2clicked)
        self.pb3.clicked.connect(self.pb1clicked)
        self.pb4.clicked.connect(self.pb2clicked)
        self.pb5.clicked.connect(self.pb1clicked)
        self.pb6.clicked.connect(self.pb2clicked)
        self.pb7.clicked.connect(self.pb1clicked)
        self.pb8.clicked.connect(self.pb2clicked)
        self.pb9.clicked.connect(self.pb1clicked)
        self.pb10.clicked.connect(self.pb2clicked)
        self.next.clicked.connect(self.do_next)
        self.bt1 = ' '
        self.bt2 = ' '
        self.stuff = ['', '', '', '', '']
        self.one.clicked.connect(self.add_number)
        self.two.clicked.connect(self.add_number)
        self.three.clicked.connect(self.add_number)
        self.four.clicked.connect(self.add_number)
        self.five.clicked.connect(self.add_number)
        self.six.clicked.connect(self.add_number)
        self.seven.clicked.connect(self.add_number)
        self.eight.clicked.connect(self.add_number)
        self.nine.clicked.connect(self.add_number)
        self.zero.clicked.connect(self.add_number)
        self.point.clicked.connect(self.add_number)
        self.remove.clicked.connect(self.Remove)
        self._N.clicked.connect(self.add_element)
        self._Ra.clicked.connect(self.add_element)
        self._Rb.clicked.connect(self.add_element)
        self._Rh.clicked.connect(self.add_element)
        self._I.clicked.connect(self.add_element)
        self._Rn.clicked.connect(self.add_element)
        self._Co.clicked.connect(self.add_element)
        self._Po.clicked.connect(self.add_element)
        self._V.clicked.connect(self.add_element)
        self._Tl.clicked.connect(self.add_element)
        self._Hs.clicked.connect(self.add_element)
        self._Ni.clicked.connect(self.add_element)
        self._Br.clicked.connect(self.add_element)
        self._Hf.clicked.connect(self.add_element)
        self._Fe.clicked.connect(self.add_element)
        self._Pt.clicked.connect(self.add_element)
        self._Sc.clicked.connect(self.add_element)
        self._Bh.clicked.connect(self.add_element)
        self._Al.clicked.connect(self.add_element)
        self._In.clicked.connect(self.add_element)
        self._Te.clicked.connect(self.add_element)
        self._F.clicked.connect(self.add_element)
        self._B.clicked.connect(self.add_element)
        self._Ba.clicked.connect(self.add_element)
        self._Sg.clicked.connect(self.add_element)
        self._Cs.clicked.connect(self.add_element)
        self._Os.clicked.connect(self.add_element)
        self._Nb.clicked.connect(self.add_element)
        self._Ge.clicked.connect(self.add_element)
        self._Mg.clicked.connect(self.add_element)
        self._Y.clicked.connect(self.add_element)
        self._Mt.clicked.connect(self.add_element)
        self._Be.clicked.connect(self.add_element)
        self._W.clicked.connect(self.add_element)
        self._Hg.clicked.connect(self.add_element)
        self._Ir.clicked.connect(self.add_element)
        self._Cl.clicked.connect(self.add_element)
        self._Ds.clicked.connect(self.add_element)
        self._As.clicked.connect(self.add_element)
        self._Ac.clicked.connect(self.add_element)
        self._Fr.clicked.connect(self.add_element)
        self._P.clicked.connect(self.add_element)
        self._Db.clicked.connect(self.add_element)
        self._Tc.clicked.connect(self.add_element)
        self._Sn.clicked.connect(self.add_element)
        self._Ne.clicked.connect(self.add_element)
        self._Ti.clicked.connect(self.add_element)
        self._Au.clicked.connect(self.add_element)
        self._Ga.clicked.connect(self.add_element)
        self._Na.clicked.connect(self.add_element)
        self._La.clicked.connect(self.add_element)
        self._O.clicked.connect(self.add_element)
        self._Xe.clicked.connect(self.add_element)
        self._Ar.clicked.connect(self.add_element)
        self._Cd.clicked.connect(self.add_element)
        self._Se.clicked.connect(self.add_element)
        self._Ag.clicked.connect(self.add_element)
        self._Mn.clicked.connect(self.add_element)
        self._Ta.clicked.connect(self.add_element)
        self._At.clicked.connect(self.add_element)
        self._Si.clicked.connect(self.add_element)
        self._Ca.clicked.connect(self.add_element)
        self._Zr.clicked.connect(self.add_element)
        self._Pb.clicked.connect(self.add_element)
        self._Sb.clicked.connect(self.add_element)
        self._Kr.clicked.connect(self.add_element)
        self._Rf.clicked.connect(self.add_element)
        self._Cu.clicked.connect(self.add_element)
        self._H.clicked.connect(self.add_element)
        self._Pd.clicked.connect(self.add_element)
        self._Ru.clicked.connect(self.add_element)
        self._Sr.clicked.connect(self.add_element)
        self._Re.clicked.connect(self.add_element)
        self._Zn.clicked.connect(self.add_element)
        self._Cr.clicked.connect(self.add_element)
        self._Mo.clicked.connect(self.add_element)
        self._Bi.clicked.connect(self.add_element)
        self._C.clicked.connect(self.add_element)
        self._K.clicked.connect(self.add_element)
        self._He.clicked.connect(self.add_element)
        self._Li.clicked.connect(self.add_element)
        self._S.clicked.connect(self.add_element)

    def pb1clicked(self):
        self.bt1 = self.sender()
        self.bt2 = ' '

    def pb2clicked(self):
        self.bt2 = self.sender()
        self.bt1 = ' '

    def Remove(self):
        if self.bt2 != ' ':
            self.bt2.setText(self.bt2.text()[:-1])

    def add_number(self):
        if self.bt2 != ' ' and len(self.bt2.text()) < 5:
            bt = self.sender()
            text = str(bt.text())
            if (
                    self.bt2.text() == '' or '.' in self.bt2.text()) and text == '.':
                pass
            elif text == '.':
                self.bt2.setText(self.bt2.text() + text)
            else:
                if float(self.bt2.text() + text) == float(
                        self.bt2.text() + text) * 10 // 10:
                    self.bt2.setText(str(int(self.bt2.text() + text)))
                else:
                    self.bt2.setText(str(float(self.bt2.text() + text)))

    def do_next(self):
        self.cifr = [str(self.pb2.text()), str(self.pb4.text()),
                     str(self.pb6.text()), str(self.pb8.text()),
                     str(self.pb10.text())]
        if '' not in self.cifr:
            cifr = list(map(lambda x: float(x), self.cifr))
            if '' not in self.stuff and sum(
                    cifr) == 100 and 0 not in cifr:
                self.nextWindow = FBPAns(self.stuff, self.cifr)
                self.nextWindow.show()

    def add_element(self):
        if self.bt1 != ' ':
            bt = self.sender()
            t = bt.text().split()[0]
            self.bt1.setText(t)
            stuff = t
            if self.bt1 == self.pb1:
                self.stuff[0] = stuff
            elif self.bt1 == self.pb3:
                self.stuff[1] = stuff
            elif self.bt1 == self.pb5:
                self.stuff[2] = stuff
            elif self.bt1 == self.pb7:
                self.stuff[3] = stuff
            elif self.bt1 == self.pb9:
                self.stuff[4] = stuff


class FBPAns(QWidget):
    def __init__(self, arg1, arg2):
        self.base = sqlite3.connect("history.db")
        cur = self.base.cursor()
        cur.execute(
            "INSERT INTO History(operation, input1, input2) VALUES('Вывод формулы вещества по массовым долям элементов', ?, ?)",
            (str(arg1), str(arg2),))
        self.base.commit()
        super().__init__()
        uic.loadUi('FBPAns.ui', self)
        self.mend = {'N': [14], 'Ra': [226], 'Rb': [85], 'Rh': [103],
                     'I': [127], 'Rn': [222], 'Co': [59], 'Po': [209],
                     'V': [51], 'Tl': [204],
                     'Hs': [265], 'Ni': [59], 'Br': [80], 'Hf': [178],
                     'Fe': [56], 'Pt': [195], 'Sc': [45], 'Bh': [262],
                     'Al': [27], 'In': [115],
                     'Te': [128], 'F': [19], 'B': [11], 'Ba': [137],
                     'Sg': [263], 'Cs': [133], 'Os': [190], 'Nb': [93],
                     'Ge': [73], 'Mg': [24],
                     'Y': [89], 'Mt': [266], 'Be': [9], 'W': [184],
                     'Hg': [201], 'Ir': [192], 'Cl': [35], 'Ds': [265],
                     'As': [75], 'Ac': [227],
                     'Fr': [223], 'P': [31], 'Db': [262], 'Tc': [99],
                     'Sn': [119], 'Ne': [20], 'Ti': [48], 'Au': [197],
                     'Ga': [70], 'Na': [23],
                     'La': [139], 'O': [16], 'Xe': [131], 'Ar': [40],
                     'Cd': [112], 'Se': [79], 'Ag': [108], 'Mn': [55],
                     'Ta': [181], 'At': [210],
                     'Si': [28], 'Ca': [40], 'Zr': [91], 'Pb': [207],
                     'Sb': [122], 'Kr': [84], 'Rf': [261], 'Cu': [64],
                     'H': [1], 'Pd': [106],
                     'Ru': [101], 'Sr': [88], 'Re': [186], 'Zn': [65],
                     'Cr': [52], 'Mo': [96], 'Bi': [209], 'C': [12],
                     'K': [39], 'He': [4],
                     'Li': [7], 'S': [32]}
        self.base = sqlite3.connect("history.db")
        self.ln = len(arg1)
        self.stuff = arg1
        self.cifr = arg2
        self.initUI()

    def initUI(self):
        per = ['a', 'b', 'c', 'd', 'e']
        res = []
        lt = []
        s0 = ''
        s1 = ''
        s2 = ''
        s3 = ''
        s4 = ''
        self.dano.setText(
            'w( ' + self.stuff[0] + ' ) = ' + self.cifr[0] + ' %')
        for i in range(1, self.ln):
            self.dano.setText(
                self.dano.toPlainText() + '\nw( ' + self.stuff[i] + ' ) = ' +
                self.cifr[i] + ' %')
        for i in range(self.ln):
            lt.append(float(str(
                float(self.cifr[i]) / self.mend[self.stuff[i]][0] + 0.0005)[
                            :5]))
        ltcopy = lt.copy()
        ltcopy.sort()
        for i in range(self.ln):
            s0 += (self.stuff[i] + ' - ' + per[i] + ';   ')
            res.append(float(str(lt[i] / ltcopy[0] + 0.005)[:4]))
            if i != 0:
                s2 += '  :  '
                s3 += '  :  '
                s4 += '  :  '
                s1 += '  :  '
            s1 += per[i]
            s2 += (str(self.cifr[i]) + '/' + str(
                self.mend[self.stuff[i]][0]))
            s3 += str(lt[i]) + '/' + str(ltcopy[0])
            s4 += str(res[-1])
        self.tb1.setText(s0)
        self.tb2.setText(s1 + ' = ' + s2 + ' = ' + s3 + ' = ' + s4)
        ans = ''
        v = True
        r = 0
        for i in range(self.ln):
            if float(res[i] * 10 // 10) != res[i]:
                r += 1
                for j in range(1, 100):
                    if float(res[i] * j * 10 // 10) != res[i] * j:
                        pass
                    else:
                        for k in range(len(res)):
                            res[k] *= j
                        break
        for i in range(self.ln):
            if float(res[i] * 10 // 10) != res[i]:
                v = False
        if not v:
            self.ans.setText('Калькулятор не может это посчитать')
        else:
            for i in range(self.ln):
                ans += self.stuff[i]
                for k in range(len(str(res[i]))):
                    if str(res[i])[k] == '1' and len(str(res[i])) - k > 1 and \
                            str(res[i])[k + 1] == '.':
                        pass
                    elif str(res[i])[k] == '.':
                        break
                    elif str(res[i])[k] == '1':
                        ans += '\N{SUBSCRIPT ONE}'
                    elif str(res[i])[k] == '2':
                        ans += '\N{SUBSCRIPT TWO}'
                    elif str(res[i])[k] == '3':
                        ans += '\N{SUBSCRIPT THREE}'
                    elif str(res[i])[k] == '4':
                        ans += '\N{SUBSCRIPT FOUR}'
                    elif str(res[i])[k] == '5':
                        ans += '\N{SUBSCRIPT FIVE}'
                    elif str(res[i])[k] == '6':
                        ans += '\N{SUBSCRIPT SIX}'
                    elif str(res[i])[k] == '7':
                        ans += '\N{SUBSCRIPT SEVEN}'
                    elif str(res[i])[k] == '8':
                        ans += '\N{SUBSCRIPT EIGHT}'
                    elif str(res[i])[k] == '9':
                        ans += '\N{SUBSCRIPT NINE}'
                    elif str(res[i])[k] == '0':
                        ans += '\N{SUBSCRIPT ZERO}'
            self.ans.setText(ans)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main()
    ex.show()
    sys.exit(app.exec())
