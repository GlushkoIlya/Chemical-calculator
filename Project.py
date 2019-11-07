import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QPushButton, QWidget, QLabel, \
    QMainWindow, QCheckBox, \
    QComboBox, QFileDialog, QTextEdit, QTextBrowser
import faulthandler


class Main(QMainWindow):  # Ошибок нет

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
        self.nextWindow.show()


class AtomnayaMassa(QWidget):  # Ошибок вроде нет
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

        if bt == c[0]:
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
        if self.stuff:
            self.nextWindow = AtomnayaMassaAnswer(self.stuff,
                                                  self.label.text())
            self.nextWindow.show()
        # Ошибок вроде нет


class AtomnayaMassaAnswer(QWidget):  # Есть ошибка, а так всё должно работать
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
                tb1.setText(self.tb1.toPlainText() + str(aa[i][1]) + ' * Ar(' + str(aa[i][2]) + ')')
            else:
                self.tb1.setText(
                    self.tb1.toPlainText() + ' + ' + str(aa[i][1]) + ' * Ar(' + str(
                        aa[i][2]) + ')')
        self.tb1.setText(self.tb1.toPlainText() + ' = ')
        for i in range(len(aa)):
            if i == 0:
                self.tb1.setText(
                    self.tb1.toPlainText() + str(aa[i][1]) + ' * ' + str(aa[i][0]))
            else:
                self.tb1.setText(
                    self.tb1.toPlainText() + ' + ' + str(aa[i][1]) + ' * ' + str(
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
        t = self.spinBox.text()
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


class FormulaByRatio3(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('FormulaByRatio3.ui', self)


class FormulaByRatio4(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('FormulaByRatio4.ui', self)


class FormulaByRatio5(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('FormulaByRatio5.ui', self)


class FormulaByPercents(QWidget):  # Ошибок вроде нет
    def __init__(self):
        super().__init__()
        uic.loadUi('FormulaByPercents.ui', self)
        self.pushButton.clicked.connect(self.do_next)

    def do_next(self):
        t = self.spinBox.text()
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
        self.pb1.clicked.connect(self.pbclicked)
        self.pb2.clicked.connect(self.pbclicked)
        self.pb3.clicked.connect(self.pbclicked)
        self.pb4.clicked.connect(self.pbclicked)

    def pbclicked(self):
        self.bt = self.sender()
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

    def do_next(self):
        pass

    def add_element(self):
        bt = self.sender()
        text = bt.text().split()[0]
        self.bt.setText(text)

    def add_number(self):
        bt = self.sender()
        c = [self.zero, self.one, self.two, self.three, self.four, self.five,
             self.six, self.seven, self.eight, self.nine]

        if bt == c[0]:
            self.bt.setText(self.label.text() + "\N{SUBSCRIPT ZERO}")
            x = 0
        elif bt == c[1]:
            self.bt.setText(self.label.text() + "\N{SUBSCRIPT ONE}")
            x = 1
        elif bt == c[2]:
            self.bt.setText(self.label.text() + "\N{SUBSCRIPT TWO}")
            x = 2
        elif bt == c[3]:
            self.bt.setText(self.label.text() + "\N{SUBSCRIPT THREE}")
            x = 3
        elif bt == c[4]:
            self.bt.setText(self.label.text() + "\N{SUBSCRIPT FOUR}")
            x = 4
        elif bt == c[5]:
            self.bt.setText(self.label.text() + "\N{SUBSCRIPT FIVE}")
            x = 5
        elif bt == c[6]:
            self.bt.setText(self.label.text() + "\N{SUBSCRIPT SIX}")
            x = 6
        elif bt == c[7]:
            self.bt.setText(self.label.text() + "\N{SUBSCRIPT SEVEN}")
            x = 7
        elif bt == c[8]:
            self.bt.setText(self.label.text() + "\N{SUBSCRIPT EIGHT}")
            x = 8
        elif bt == c[9]:
            self.bt.setText(self.label.text() + "\N{SUBSCRIPT NINE}")
            x = 9
        self.kol += str(x)


class FormulaByPercents3(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('FormulaByPercents3.ui', self)


class FormulaByPercents4(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('FormulaByPercents4.ui', self)


class FormulaByPercents5(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('FormulaByPercents5.ui', self)


faulthandler.enable()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main()
    ex.show()
    sys.exit(app.exec())
