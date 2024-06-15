from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
import requests

from mynyla import mynyla_window
from nuni import nuni_window

app = QApplication([])

window = QWidget()
window.resize(900, 500)

mayb= QPushButton("Отримати прогноз майбутьньоЇ погоди:)")
myn = QPushButton("Отримати прогноз минулоЇ погоди:)")
otrym = QPushButton("Отримати прогноз погоди:)")
nyn = QPushButton("Отримати прогноз погоди на нині:)")

JA = QLabel()
JA_img = QPixmap("tebErmH1.webp")
JA_img = JA_img.scaledToWidth(760)
JA.setPixmap(JA_img)


main_line = QHBoxLayout()

h1 = QVBoxLayout()
h2 = QVBoxLayout()


h1.addWidget(myn)
h1.addWidget(mayb)
h1.addWidget(nyn)

h2.addWidget(JA)


main_line.addLayout(h1)
main_line.addLayout(h2)











nyn.clicked.connect(nuni_window)
myn.clicked.connect(mynyla_window)
window.setLayout(main_line)
window.show()
app.exec()
