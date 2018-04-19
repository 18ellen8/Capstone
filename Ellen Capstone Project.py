#Ellen Richards Capstone Project
 
import os 
import tkinter
import tkinter.messagebox

root = tkinter.Tk()
root.title("Tokyo Destination: Subway Guide")

cities = ["Tokyo"]
options = ["Tokyo Tower", "Shibuya Crossing", "Asakusa", "Tokyo Skytree", "Harajuku"]
def update_listbox():
	for city in cities:
		lb_cities.insert("end" , city)
	#for option in options:
		#lb_options.insert("end" , option)

def select_city(xy):
	if lb_cities.get("active") == "Tokyo":
		lb_options.insert("end", "Tokyo Tower")
		lb_options.insert("end", "Shibuya Crossing")	
		lb_options.insert("end", "Asakusa")			
		lb_options.insert("end", "Tokyo Skytree")

def select_destination(xy):
	if lb_options.get("active") == "Shibuya Crossing":
		lbl_fastest_route["text"] = "Fastest Route: 21 minutes\n\n1. Take the Marunochi line to Akasaka-Mitsuke\n\n2. Take the Ginza Line to Shibuya\n\n3. Follow signs for the Hachiko exit"
		lbl_cheapest_route["text"] = "Cheapest Route: 200 yen\n\n1. Take the Marunochi line to Otemachi Stsation\n\n2. Take the Hanzomon Line to Shibuya station\n\n3. Follow signs for the Hachiko exit"
		lbl_least_transfers["text"] = "Fewest Transfers: 0 transfers\n\n1. Take the JR Yamanote line to Shibuya station\n\n2. Follow signs for exit the Hachiko exit\n\n"
	
	elif lb_options.get("active") == "Tokyo Tower":
		lbl_fastest_route["text"] = "Fastest Route: 17 minutes\n\n1. Take the Marunochi line to Kasumigaseki\n\n2. Take Hibiya Line to Kamiyacho\n\n3. Follow signs for exit 2"
		lbl_cheapest_route["text"] = "Cheapest Route: 160 yen\n\n1. Take the JR Yamanote line to Hamamatsucho station\n\n2. Follow signs for exit North station\n\n3. Walk 15 minutes"
		lbl_least_transfers["text"] = "Fewest Transfers: 0 transfers\n\n1. Take the JR Yamanote line to Hamamatsucho station\n\n2. Follow signs for exit North station\n\n3. Walk 15 minutes"
	
	elif lb_options.get("active") == "Asakusa":
		lbl_fastest_route["text"] = "Fastest Route: 13 minutes\n\n1. Take the Keihintohuku Line to Ueno station\n\n2. Take the Ginza line to Asakusa station\n\n3. Follow signs for your desired exit"
		lbl_cheapest_route["text"] = "Cheapest Route: 170 yen\n\n1. Walk from Tokyo Station to Nihonbashi station\n\n2. Take the Ginza line to Asakusa station\n\n3. Follow signs for your desired exit"
		lbl_least_transfers["text"] = "Fewest Transfers: 0 transfers\n\n1. Walk from Tokyo Station to Nihonbashi station\n\n2. Take the Ginza line to Asakusa station\n\n3. Follow signs for your desired exit"

	elif lb_options.get("active") == "Tokyo Skytree":
		lbl_fastest_route["text"] = "Fastest Route: 18 minutes\n\n1. Take the Yamanote Line to Akihabara station\n\n2. Take the Chuo-Sobu Line to Asakusabashi station\n\n3. Take the Asakusa Line to Honjo-Azumbashi staion\n\n4. Follow signs for Tokyo Skytree"
		lbl_cheapest_route["text"] = "Cheapest Route: 200 yen\n\n1. Take the Marunochi Line to Otemachi\n\n2. Take the Hanzomon Line to Oshiage Station\n\n3. Walk 5 minutes."
		lbl_least_transfers["text"] = "Fewest Transfers: 1 transfer\n\n1. Take the Marunochi Line to Otemachi\n\n2. Take the Hanzomon Line to Oshiage Station\n\n3. Walk 5 minutes."

	
# elif lb_destinations.get("active") == "Shibuya Crossing":
# 	elif lb_destinations.get("active") == "Asakusa":
# 	else:
	#elif lb_destinations.get("active") == "Tokyo Skytree"
# lbl_fastest_route["text"] = "Hibiya Line"
# lbl_cheapest_route["text"] = "Oedo Line"
# lbl_least_transfers["text"] = "Ginza Line"
#Functions
#def fastest_route():
	#pass
#def cheapest_route():
	#pass
#def least_transfers():
	#pass
def quit(): 
	confirm = tkinter.messagebox.askyesno("Confirm", "Data will not be saved. Are you sure you want to quit?")
	if confirm: 
		global root
		root.quit()
#Elements
lbl_title = tkinter.Label(root, text = "The Best Routes to the Most Popular Tokyo Destinations from Tokyo Station!" , bg = "white")
lbl_title.grid(row = 0, column = 1)

lbl_city = tkinter.Label(root, text = "City" , bg = "white")
lbl_city.grid(row = 1, column = 0)

lb_cities = tkinter.Listbox(root)
lb_cities.grid(row = 2, column = 0, rowspan=3)

lbl_destinations = tkinter.Label(root, text = "Destinations" , bg = "white")
lbl_destinations.grid(row = 1, column = 1 )

lb_options = tkinter.Listbox(root)
lb_options.grid(row = 2, column = 1, rowspan=3)

lbl_options = tkinter.Label(root, text = "Subway Options" , bg = "white")
lbl_options.grid(row = 1, column = 2)

#btn_fastest_route = tkinter.Button(root, text = "Fastest Route" , command = fastest_route)
#btn_fastest_route.grid(row = 1, column = 2)
#btn_cheapest_route = tkinter.Button(root, text = "Cheapest Route" , command = cheapest_route)
#btn_cheapest_route.grid(row = 2, column = 2)
#btn_least_transfers = tkinter.Button(root, text = "Least Transfers" , command = least_transfers)
#btn_least_transfers.grid(row = 3, column = 2)

lbl_fastest_route = tkinter.Label(root, text = "Fastest Route:")
lbl_fastest_route.grid(row = 2, column = 2)

lbl_cheapest_route = tkinter.Label(root, text = "Cheapest Route:")
lbl_cheapest_route.grid(row = 3, column = 2)

lbl_least_transfers = tkinter.Label(root, text = "Least Transfers:")
lbl_least_transfers.grid(row = 4, column = 2)

# lbl_route = tkinter.Label(root, text = "Routes" , bg = "white")
# lbl_route.grid(row = 0, column = 3)
# lbl_display = tkinter.Label(root, text = "" )
# lbl_display.grid(row = 0, column = 0)

btn_quit = tkinter.Button(root, text = "Quit" , command = quit)
btn_quit.grid(row = 9, column = 3)

lb_cities.bind("<<ListboxSelect>>", select_city)	
lb_options.bind("<<ListboxSelect>>", select_destination)	



	
update_listbox()	
root.mainloop()
root.destroy()
	
	
