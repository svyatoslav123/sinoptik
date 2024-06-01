from PyQt6.QtWidgets import *
import requests
def mynyla_window():
     window = QDialog()
     window.resize(400, 300)
     city = QLineEdit("")
     data = QLineEdit("")
     time = QLineEdit("")
     rezyltat = QLineEdit("")
     city1 = QLabel("місто:")
     data1 = QLabel("дата:")
     time1 = QLabel("година:")
     rezyltat1 = QLabel("результат:")
     otrym = QPushButton("Отримати прогноз погоди:)")
     main_line = QHBoxLayout()

     h1 = QVBoxLayout()
     h2 = QVBoxLayout()
     h1.addWidget(city1)

     h2.addWidget(city)
     h1.addWidget(data1)
     h2.addWidget(data)
     h1.addWidget(time1)
     h2.addWidget(time)
     h1.addWidget(rezyltat1)
     h2.addWidget(rezyltat)
     h1.addWidget(otrym)

     main_line.addLayout(h1)
     main_line.addLayout(h2)

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
     window.exec()