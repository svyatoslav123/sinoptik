from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
import requests
app = QApplication([])

window = QWidget()
window.resize(200, 100)

otrym = QPushButton("Отримати прогноз погоди:)")
city = QLineEdit("")
data = QLineEdit("")
time = QLineEdit("")
rezyltat = QLineEdit("")

main_line = QVBoxLayout()

h1 = QHBoxLayout()
h2 = QHBoxLayout()
h3 = QHBoxLayout()
h4 = QHBoxLayout()
h5 = QHBoxLayout()


h1.addWidget(city)
h2.addWidget(data)
h3.addWidget(time)
h4.addWidget(otrym)
h5.addWidget(rezyltat)

main_line.addLayout(h1)
main_line.addLayout(h2)
main_line.addLayout(h3)
main_line.addLayout(h4)
main_line.addLayout(h5)

def dd():
    citye = city.text()
    date = data.text()
    url1 = f"https://api.openweathermap.org/data/2.5/weather?q={citye}&appid=bd97a2f8ede4aaad49878a1c3eb7e3c3"
    r = requests.get(url1)
    if r.status_code == 200:
        res = r.json()
        rezyltat.setText(str(res))








otrym.clicked.connect(dd)
window.setLayout(main_line)
window.show()
app.exec()
