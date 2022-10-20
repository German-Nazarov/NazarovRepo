import numpy as np
import matplotlib.pyplot as plt

#1. Чтение данных из data и settings
with open("settings.txt", "r") as settings:
    tmp = [float(i) for i in settings.read().split("\n")]
    #print(tmp)

data_array = np.loadtxt("data.txt", dtype = int)
#print(data_array)

#2. Перевод показаний АЦП в вольты, номеров отсчётов в секунды
volts = data_array * float(tmp[1])
times = np.linspace(0, len(data_array)*tmp[0], len(data_array))

print(volts)
print(times)


#4. Настройка цвета и формы линии, размера и цвета маркеров, частоты отображений маркеров и легенды
fig, ax = plt.subplots()
ax.plot(times, volts, linewidth=2.0, color = "blue")
ax.scatter(times[::50], volts[::50], linewidth=2.7, color = "blue")
ax.set_title("Процесс заряда и разряда конденсатора в RC-цепочке")
ax.legend(['Основной график', 'Маркеры'])

#5. Задание максимальных и минимальных значений для шкалы
ax.set_xlim([0, 12])
ax.set_ylim([0, 3])

#6. Подписи осей
ax.set_xlabel("Время, с")
ax.set_ylabel("Напряжение, В")

#7. Название графика, с настройками его месторасположения и переносом текста...
ax.set_title("Процесс заряда и разряда конденсатора в RC-цепочке")

#8. Наличие сетки (главной и дополнительной), настройка её цвета и стиля
ax.minorticks_on()
ax.grid(which='major', color='k', linestyle='-', linewidth=0.5)
ax.grid(which='minor', color='k', linestyle=':')

#9. Текст с временем зарядки и разрядки
ax.text(0.32, 0.55, 'Хороший график', horizontalalignment='center', verticalalignment='center', transform=ax.transAxes)

#3. Построение + сохранение графика в файл в формате .svg
fig.savefig("Graph.svg")
plt.show()