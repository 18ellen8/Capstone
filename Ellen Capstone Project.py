#Ellen Richards Capstone Project
 
import os 
import tkinter
import tkinter.messagebox
root = tkinter.Tk()
root.title("Tokyo Destination: Subway Guide")

#Functions
def fastest_route():
	pass

def cheapest_route():
	pass

def least_transfers():
	pass

def quit(): 
	pass
# 	global root
# 	root.quit()

#Elements
lbl_title = tkinter.Label(root, text = "The Best Routes to the Most Popular Tokyo Destinations from Tokyo Station!" , bg = "white")
lbl_title.grid(row = 0, column = 1)

lbl_city = tkinter.Label(root, text = "City" , bg = "white")
lbl_city.grid(row = 1, column = 0)

lb_cities = tkinter.Listbox(root)
lb_cities.grid(row = 2, column = 0)

lbl_destinations = tkinter.Label(root, text = "Destinations" , bg = "white")
lbl_destinations.grid(row = 1, column = 1 )

lb_destination_options = tkinter.Listbox(root)
lb_destination_options.grid(row = 2, column = 1)

lbl_options = tkinter.Label(root, text = "Subway Options" , bg = "white")
lbl_options.grid(row = 1, column = 2)

btn_fastest_route = tkinter.Button(root, text = "Fastest Route" , command = fastest_route)
btn_fastest_route.grid(row = 1, column = 2)

btn_cheapest_route = tkinter.Button(root, text = "Cheapest Route" , command = cheapest_route)
btn_cheapest_route.grid(row = 2, column = 2)

btn_least_transfers = tkinter.Button(root, text = "Least Transfers" , command = least_transfers)
btn_least_transfers.grid(row = 3, column = 2)

lbl_route = tkinter.Label(root, text = "Route" , bg = "white")
lbl_route.grid(row = 0, column = 3)

# lbl_display = tkinter.Label(root, text = "" )
# lbl_display.grid(row = 0, column = 0)

btn_quit = tkinter.Button(root, text = "Quit" , command = quit)
btn_quit.grid(row = 4, column = 5)

	
root.mainloop()
root.destroy()
	
	
