from PyQt6.QtWidgets import *
import requests
def mynyla_window():
     window = QDialog()
     window.resize(400, 300)
     city = QLineEdit("")
     data = QLineEdit("")
     time = QLineEdit("")
     rezyltat = QLineEdit("")
     rezyltat4= QLineEdit("")
     city1 = QLabel("місто:")
     data1 = QLabel("мінімальна температура:")
     time1 = QLabel("максимальна температура:")
     rezyltat1 = QLabel("опис:")
     rezyltat2 = QLabel("точна дата:")
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
     h1.addWidget(rezyltat2)
     h2.addWidget(rezyltat4)
     h1.addWidget(otrym)

     main_line.addLayout(h1)
     main_line.addLayout(h2)

     def dd():
          citye = city.text()

          url1 = f"https://api.openweathermap.org/data/2.5/forecast?q={citye}&appid=bd97a2f8ede4aaad49878a1c3eb7e3c3"
          r = requests.get(url1)
          if r.status_code == 200:
               res = r.json()
               mint = res["list"][0]["main"]["temp_min"]-273.15
               maxt = res["list"][0]["main"]["temp"]-273.15
               des = res["list"][1]["weather"][0]["description"]
               dt = res["list"][6]["dt_txt"]
               rezyltat.setText(str(des))
               rezyltat4.setText(str(dt))


               data.setText(str(mint))
               time.setText(str(maxt))


     otrym.clicked.connect(dd)


     window.setLayout(main_line)
     window.exec()