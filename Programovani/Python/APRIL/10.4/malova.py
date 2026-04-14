import tkinter as tk
cv = tk.Canvas()
cv.pack()

#cv.create_rectangle(50, 50, 100, 100, fill="green")
#cv.create_rectangle(50+25, 50, 100+25, 100, fill="white")
#cv.create_rectangle(50+50, 50, 100+25, 100, fill="orange")


#cv.create_rectangle(20, 50, 30, 150, fill="blue")
#cv.create_rectangle(20, 50, 190, 60, fill="red")
#cv.create_rectangle(180, 50, 190, 150, fill="blue")
#cv.create_rectangle(30, 150, 190, 140, fill="red")

#pres_sebe.py

#cv.create_rectangle(50, 50, 150, 150, fill="white")
#cv.create_rectangle(70, 70, 150+20, 150+20, fill="blue")
#cv.create_rectangle(70+20, 70+20, 150+40, 150+40, fill="red")
#cv.create_rectangle(70+40, 70+40, 150+60, 150+60, fill="pink")

x = 100
y = 100
posuv = 20
#cv.create_rectangle(x, y, x + (posuv * 5), y + (posuv * 5), fill="red")
#cv.create_rectangle(x + 20, y + 20, x + (posuv * 4), y + (posuv * 4), fill="blue")
#cv.create_rectangle(x + 40, y + 40, x + (posuv * 3), y + (posuv * 3), fill="white")

rect = cv.create_rectangle(10, 10, 200, 100, fill="red")
rect = cv.create_rectangle(10, 40, 200, 70, fill="white")
rect = cv.create_rectangle(40, 10, 70, 100, fill="white")
rect = cv.create_rectangle(10, 50, 200, 60, fill="blue")
rect = cv.create_rectangle(50, 10, 60, 100, fill="blue")

tk.mainloop()