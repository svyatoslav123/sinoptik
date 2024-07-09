from PyQt6.QtWidgets import *
import requests
def nuni_window():
     window = QDialog()
     window.resize(300, 200)
     city = QLineEdit("")


     city1 = QLabel("місто:")
     temp_min1 = QLabel("мінімальна температура:")
     temp_max1 = QLabel("максимальна температура:")
     description1 = QLabel("опис:")
     description = QLineEdit("")

     temp_min = QLineEdit("")
     temp_max = QLineEdit("")


     otrym = QPushButton("Отримати прогноз погоди:)")
     main_line = QVBoxLayout()

     h1 = QHBoxLayout()
     h2 = QHBoxLayout()
     h3 = QHBoxLayout()
     h4 = QHBoxLayout()
     h5 = QHBoxLayout()
     h1.addWidget(city1)

     h1.addWidget(city)



     h3.addWidget(temp_min1)
     h3.addWidget(temp_min)
     h4.addWidget(temp_max1)
     h4.addWidget(temp_max)
     h5.addWidget(description1)
     h5.addWidget(description)




     main_line.addLayout(h1)
     main_line.addLayout(h2)
     main_line.addLayout(h3)
     main_line.addLayout(h4)
     main_line.addLayout(h5)
     main_line.addWidget(otrym)



     def dd():
          citye = city.text()
          city.setStyleSheet("""
                     QLineEdit{

                     background-color: #D3E5EA;


                     }

               """)

          url1 = f"https://api.openweathermap.org/data/2.5/weather?q={citye}&appid=bd97a2f8ede4aaad49878a1c3eb7e3c3"
          r = requests.get(url1)
          if r.status_code == 200:
               res = r.json()
               mint = res["main"]["temp_min"]-273.15
               maxt = res["main"]["temp_max"]-273.15
               des = res["weather"][0]["description"]
               temp_min.setText(str(mint))
               temp_max.setText(str(maxt))
               description.setText(str(des))

     otrym.clicked.connect(dd)


     window.setLayout(main_line)
     window.exec()