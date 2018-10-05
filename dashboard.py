import tkinter as tk
import tkinter.messagebox as mb
from tkinter import *
import serial, time
import csv
import datetime

now = datetime.datetime.now()
arduino = serial.Serial("COM3", 9600)

#Funciones
# LED
def toggleLed():
    '''
    use
    t_btn.config('text')[-1]
    to get the present state of the toggle button
    '''
    if t_btnLed.config('text')[-1] == 'Encender':
        arduino.write(b'l')
        t_btnLed.config(text='Apagar',image = imgLedOn)
    else:
        arduino.write(b'l')
        t_btnLed.config(text='Encender',image = imgLedOff)
#MOTOR
def toggleMotor():
    '''
    use
    t_btn.config('text')[-1]
    to get the present state of the toggle button
    '''
    if t_btnMotor.config('text')[-1] == 'Encender':
        arduino.write(b'm')
        t_btnMotor.config(text='Apagar',image = imgMotorOn)
    else:
        arduino.write(b'm')
        t_btnMotor.config(text='Encender',image = imgMotorOff)
# TEMPERATURA
def actualizar_temperatura():
    arduino.write(b't')
    date = now.strftime("%Y-%m-%d")
    hour = now.strftime("%H:%M:%S")
    data = float(arduino.readline().decode("utf-8"))
    lblTemp.config(text = data)
    #GUARDAR EN ARCHIVO CSV
    data = [date,hour,data]
    myFile =  open('temperatura.csv','a', encoding='utf8')
    writer = csv.writer(myFile, delimiter=',' , lineterminator='\n')
    writer.writerow(data)
    myFile.close()
# HUMEDAD
def actualizar_humedad():
    arduino.write(b'h')
    date = now.strftime("%Y-%m-%d")
    hour = now.strftime("%H:%M:%S")
    data = float(arduino.readline().decode("utf-8"))
    lblHum.config(text = data)
    #GUARDAR EN ARCHIVO CSV
    data = [date,hour,data]
    myFile =  open('humedad.csv','a', encoding='utf8')
    writer = csv.writer(myFile, delimiter=',' , lineterminator='\n')
    writer.writerow(data)
    myFile.close()
# GAS
def actualizar_gas():
    arduino.write(b'g')
    date = now.strftime("%Y-%m-%d")
    hour = now.strftime("%H:%M:%S")
    data = arduino.readline().decode("utf-8")
    lblGas.config(text = data)
    #GUARDAR EN ARCHIVO CSV
    data = [date,hour,data]
    myFile =  open('gas.csv','a', encoding='utf8')
    writer = csv.writer(myFile, delimiter=',' , lineterminator='\n')
    writer.writerow(data)
    myFile.close()
# LUMIMOSIDAD
def actualizar_luminosidad():
    arduino.write(b'f')
    date = now.strftime("%Y-%m-%d")
    hour = now.strftime("%H:%M:%S")
    data = float(arduino.readline().decode("utf-8"))
    lblLum.config(text = data)
    #GUARDAR EN ARCHIVO CSV
    data = [date,hour,data]
    myFile =  open('luminosidad.csv','a', encoding='utf8')
    writer = csv.writer(myFile, delimiter=',' , lineterminator='\n')
    writer.writerow(data)
    myFile.close()
def actualizar():
    arduino.write(b'd')
    data = arduino.readline().decode("utf-8")
    sep = data.split()
    date = now.strftime("%Y-%m-%d")
    hour = now.strftime("%H:%M:%S")
    dataTem = sep[0]
    dataHum = sep[1]
    dataLum = sep[2]
    data = [date,hour,dataTem,dataHum,dataLum]
    lblTemp.config(text = float(sep[0]))
    lblHum.config(text = float(sep[1]))
    lblLum.config(text = sep[2])
    #GUARDAR EN ARCHIVO CSV
    myFile =  open('registro.csv','a', encoding='utf8')
    writer = csv.writer(myFile, delimiter=',' , lineterminator='\n')
    writer.writerow(data)
    myFile.close()

win = tk.Tk()
win.title("Projecto U1")
win.geometry("400x430")
win.resizable(0,0)

# Path de las imagenes
imgTem = PhotoImage(file="./assets/temperature.png")
imgHum = PhotoImage(file="./assets/humidity.png")
imgLum = PhotoImage(file="./assets/luminosity.png")
imgGas = PhotoImage(file="./assets/gas.png")
imgMotorOn = PhotoImage(file="./assets/motorOn.png")
imgMotorOff = PhotoImage(file="./assets/motorOff.png")
imgLedOn = PhotoImage(file="./assets/ledOn.png")
imgLedOff = PhotoImage(file="./assets/ledOff.png")

# Etiquetas e imagenes
tk.Label(win, text="Temperatura").grid(row=0, column=0)
btnTemp = tk.Button(text="Temperatura",image = imgTem,  command=actualizar_temperatura)
btnTemp.grid(row=1, column=0)
lblTemp = tk.Label(win, text="Actualiza")
lblTemp.grid(row=2, column=0)

tk.Label(win, text="Humedad").grid(row=0, column=1)
#tk.Label(win, text="Humedad",image = imgHum).grid(row=1, column=1)
btnHum = tk.Button(text="Humedad",image = imgHum,  command=actualizar_humedad)
btnHum.grid(row=1, column=1)
lblHum = tk.Label(win, text="Actualiza")
lblHum.grid(row=2, column=1)


tk.Label(win, text="Luminosidad").grid(row=0, column=2)
btnLum = tk.Button(text="Luminosidad",image = imgLum,  command=actualizar_luminosidad)
btnLum.grid(row=1, column=2)
lblLum = tk.Label(win, text="Actualiza")
lblLum.grid(row=2, column=2)

tk.Label(win, text="").grid(row=3, column=0)

tk.Label(win, text="Presencia de gas").grid(row=4, column=0)
tk.Label(win, text="Presencia de gas",image = imgGas).grid(row=5, column=0)
btnGas = tk.Button(text="Presencia de gas",image = imgGas,  command=actualizar_gas)
btnGas.grid(row=5, column=0)
lblGas = tk.Label(win, text="Actualiza")
lblGas.grid(row=6, column=0)

tk.Label(win, text="Led").grid(row=4, column=1)
tk.Label(win, text="Motor").grid(row=4, column=2)

# Toggle buttons
t_btnLed = tk.Button(text="Encender",image=imgLedOff, command=toggleLed)
t_btnLed.grid(row=5, column=1, sticky=tk.W+tk.E)
t_btnMotor = tk.Button(text="Encender",image=imgMotorOff, command=toggleMotor)
t_btnMotor.grid(row=5, column=2, sticky=tk.W+tk.E)
t_btnDatos = tk.Button(text="Actualizar", command=actualizar)
t_btnDatos.grid(row=7, column=0, sticky=tk.W+tk.E)
#tk.Button(win, text='+', command=sumar).grid(row=4, column=0, sticky=tk.W+tk.E)

tk.mainloop()