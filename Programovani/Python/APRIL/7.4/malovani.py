import tkinter as tk
cv = tk.Canvas()
cv.pack()


# uděla obdelnik
#cv.create_rectangle(50, 50, 100, 100) #x1, y1, x2, y2
#cv.create_rectangle(101, 101, 150, 150) #x1, y1, x2, y2

#cv.create_rectangle(100,50,100+80,50+80) #x1, y1, x2, y2
#cv.create_rectangle(200,50,200+80,50+80) #x1, y1, x2, y2 nebo 100,50,250,200
#cv.create_rectangle(110,60,110+60,120) #x1, y1, x2, y2 nebo 100+25,50+25,250-25,200-25

#cv.create_rectangle(125, 175, 225, 225, fill="red")
#cv.create_rectangle(135, 135, 215, 175, fill="blue")
#cv.create_rectangle(145, 115, 205, 135, fill="green")

#vlajka
#cv.create_rectangle(50, 50, 300, 100, fill="red")
#cv.create_rectangle(50, 100, 300, 150, fill="white")
#cv.create_rectangle(50, 150, 300, 200, fill="blue")

cv.create_rectangle(50, 50, 300, 200, fill="white")
cv.create_rectangle(110, 50, 140, 200, fill="blue")
cv.create_rectangle(50, 150, 300, 110, fill="blue")

tk.mainloop()