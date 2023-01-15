from tkinter import *
from tkinter import ttk
import customtkinter
import tkintermapview


def find_location():
    location = entry.get()
    map_widget.set_address(location, marker=True)  # сюда передаем переменную location для поиска адреса
    # marker - ставит чек поинт на карте - место обозначения
    hints.append(location)
    hint_widget.configure(values=hints)  # лбнолвляем виджет с нашими вводами


# функция для элемента по нажатию нашего комбобокса
def enter_hint(event):  # когда биндим какое то событие по комбобоксу и получаем событие
    location = hint_widget.get()  # достаем локацию на которую телепортировались
    map_widget.set_address(location, marker=True)  # далее заносим в entry
    entry.delete(0, END)  # вначале чистим его сначала до конца
    entry.insert(0, location)


hints = ['']  # список хранения запросов


def enter_map(combo_server):
    map_enter = combo_server.get()
    map_widget.set_tile_server(server_save[map_enter], max_zoom=22)


# далее подумать как обновить карту
# можно посмотреть на пример
# но там с конструктором
# https://github.com/Mastermehan/TkinterMapView/blob/main/examples/map_with_customtkinter.py

# создал окно ткинтер
window = Tk()
window.geometry(f"{800}x{600}")
window.title("google maps")

server_save = {'OpenStreetMap (default)': "https://a.tile.openstreetmap.org/{z}/{x}/{y}.png",
               'google normal': "https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga",
               'google satellite': "https://mt0.google.com/vt/lyrs=s&hl=en&x={x}&y={y}&z={z}&s=Ga",
               'painting style': "http://c.tile.stamen.com/watercolor/{z}/{x}/{y}.png"}
#
#
# Создали комбобокс для выбора режима карты
server = ['OpenStreetMap (default)', 'google normal', 'google satellite', 'painting style']
combo_server = customtkinter.CTkComboBox(window, values=server)
combo_server.place(x=5, y=60)

# создал виджет карты
map_widget = tkintermapview.TkinterMapView(window, width=640, height=600, corner_radius=0)
map_widget.set_tile_server(server_save['OpenStreetMap (default)'], max_zoom=22)  # google normal
map_widget.place(relx=0.2, rely=0.5, anchor=W)  # сместил относительно лево 0,2 (0 до 1)

# Создаем комбобокс раньше чем поле ввода. В нем сохранять будем наши запросы
hint_widget = ttk.Combobox(window, values=hints, font=('', 15))
hint_widget.place(x=250, y=20, width=418)  # позиция поля в пространстве

# Создаю поле ввода
entry = customtkinter.CTkEntry(window, width=400)  # длина поля
entry.place(x=250, y=20)  # позиция поля в пространстве

# Создаем кнопку поиска
button = customtkinter.CTkButton(window, text='ПОИСК', text_color='white', width=20, corner_radius=10,
                                 command=find_location)
button.place(x=690, y=20)

# Создали лэйбл над комбобокс
lable = customtkinter.CTkLabel(window, text="Режим карты", font=("Arial", 16), text_color='black', corner_radius=5)
lable.place(x=4, y=32)

# биндим далее из def enter_hint(event)
hint_widget.bind('<<ComboboxSelected>>', enter_hint)

window.mainloop()
