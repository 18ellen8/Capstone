#Ellen Richards Capstone Project
 
import os 
import tkinter
import tkinter.messagebox
import time

#rush hour warning message box for 8-9am and also 5pm#
root = tkinter.Tk()
root.title("Tokyo Subway Guide")
root.geometry("900x600")

cities = ["Tokyo"]
options = ["Tokyo Tower", "Shibuya Crossing", "Asakusa", "Tokyo Skytree", "Harajuku", "Omotesando", "Imperial Palace"]
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
		print("Shibuya Crossing")		
		lbl_fastest_route["text"] = "Fastest Route: 21 minutes\n\n1. Take the Marunochi line to Akasaka-Mitsuke\n\n2. Take the Ginza Line to Shibuya\n\n3. Follow signs for the Hachiko exit"
		lbl_cheapest_route["text"] = "Cheapest Route: 200 yen\n\n1. Take the Marunochi line to Otemachi Stsation\n\n2. Take the Hanzomon Line to Shibuya station\n\n3. Follow signs for the Hachiko exit"
		lbl_least_transfers["text"] = "Fewest Transfers: 0 transfers\n\n1. Take the JR Yamanote line to Shibuya station\n\n2. Follow signs for exit the Hachiko exit\n\n"
		img_destination = tkinter.PhotoImage(file="Shibuya.gif")
		lbl_image.configure(image=img_destination)
		lbl_image.image = img_destination
	

	elif lb_options.get("active") == "Tokyo Tower":
		print("Tokyo Tower")	
		lbl_fastest_route["text"] = "Fastest Route: 17 minutes\n\n1. Take the Marunochi line to Kasumigaseki\n\n2. Take Hibiya Line to Kamiyacho\n\n3. Follow signs for exit 2"
		lbl_cheapest_route["text"] = "Cheapest Route: 160 yen\n\n1. Take the JR Yamanote line to Hamamatsucho station\n\n2. Follow signs for exit North station\n\n3. Walk 15 minutes"
		lbl_least_transfers["text"] = "Fewest Transfers: 0 transfers\n\n1. Take the JR Yamanote line to Hamamatsucho station\n\n2. Follow signs for exit North station\n\n3. Walk 15 minutes"
		img_destination = tkinter.PhotoImage(file="tokyo_tower.gif")
		lbl_image.configure(image=img_destination)
		lbl_image.image = img_destination
	
	
	elif lb_options.get("active") == "Asakusa":
		print("Asakusa")	
		lbl_fastest_route["text"] = "Fastest Route: 13 minutes\n\n1. Take the Keihintohuku Line to Ueno station\n\n2. Take the Ginza line to Asakusa station\n\n3. Follow signs for your desired exit"
		lbl_cheapest_route["text"] = "Cheapest Route: 170 yen\n\n1. Walk from Tokyo Station to Nihonbashi station\n\n2. Take the Ginza line to Asakusa station\n\n3. Follow signs for your desired exit"
		lbl_least_transfers["text"] = "Fewest Transfers: 0 transfers\n\n1. Walk from Tokyo Station to Nihonbashi station\n\n2. Take the Ginza line to Asakusa station\n\n3. Follow signs for your desired exit"
		img_destination = tkinter.PhotoImage(file="Asakusa.gif")
		lbl_image.configure(image=img_destination)
		lbl_image.image = img_destination
	
	
	elif lb_options.get("active") == "Tokyo Skytree":
		print("Tokyo Skytree")	
		lbl_fastest_route["text"] = "Fastest Route: 18 minutes\n\n1. Take the Yamanote Line to Akihabara station\n\n2. Take the Chuo-Sobu Line to Asakusabashi station\n\n3. Take the Asakusa Line to Honjo-Azumbashi staion\n\n4. Follow signs for Tokyo Skytree."
		lbl_cheapest_route["text"] = "Cheapest Route: 200 yen\n\n1. Take the Marunochi Line to Otemachi\n\n2. Take the Hanzomon Line to Oshiage Station\n\n3. Walk 5 minutes."
		lbl_least_transfers["text"] = "Fewest Transfers: 1 transfer\n\n1. Take the Marunochi Line to Otemachi\n\n2. Take the Hanzomon Line to Oshiage Station\n\n3. Walk 5 minutes."
		img_destination = tkinter.PhotoImage(file="1-5.gif")
		lbl_image.configure(image=img_destination)
		lbl_image.image = img_destination
		
				
	# elif lb_options.get("active") == "Omotesando":
# 		lbl_fastest_route["text"] = "Fastest Route: 15 minutes\n\n1. Take the Marunochi Line to Akasaka-mitsuke station\n\n2. Take the Ginza Line to Omotesando station\n\n3." 
# 		lbl_cheapest_route["text"] = "Cheapest Route:  yen\n\n1. 
# 		lbl_least_transfers["text"] = "Fewest Transfers:  transfer\n\n1. 
# 		img_destination = tkinter.PhotoImage(file=".gif")
# 		lbl_image = tkinter.Label(image=img_destination)
# 		lbl_image.image = img_destination
# 		lbl_image.grid(row=5, column = 4)
		
	elif lb_options.get("active") == "Imperial Palace":
		lbl_fastest_route["text"] = "Fastest Route: 18 minutes\n\n1. Take the Marunochi Line to Otemachi station\n\n2. Use exit C31a and walk for 5 minutes"
		lbl_cheapest_route["text"] = "Cheapest Route: 170 yen\n\n1. Walk from Tokyo station towards Otemachi station\n\n2.Take the Tozai Line to Takebashi station\n\n3. Use exit 1a and walk for 5 minutes"		
		lbl_least_transfers["text"] = "Fewest Transfers: 0 transfer\n\n1. Take the Marunochi Line to Otemachi station\n\n2. Use exit C31a and walk for 5 minutes"
		img_destination = tkinter.PhotoImage(file="Palace.gif")
		lbl_image.configure(image=img_destination)
		lbl_image.image = img_destination
		

		
	if time.strftime("%I") == "08" or time.strftime("%I") == "09":
		tkinter.messagebox.showwarning("Warning", "It is morning rush hour. The trains will be very crowded at this time")
	elif time.strftime("%H") == "17" or time.strftime("%H") == "18":
		tkinter.messagebox.showwarning("Warning", "It is evening rush house. The trains will be very crowded at this time")
	elif time.strftime("%A") == "Saturday" or time.strftime("%A") == "Sunday":
		tkinter.messagebox.showwarning("Warning", "It is a weekend, this destination will be very crowded all day")
	elif time.strftime("%d") in ["1","2","3","4","5"] and time.strftime("%B") == "May":
		tkinter.messagebox.showwarning("Warning", "It is a Holiday, expect transportation and this destination to be busy.")
	elif time.strftime("%d") in ["28", "29", "30"] and time.strftime("%B") == "April":
		tkinter.messagebox.showwarning("Warning", "It is a Holiday, expect transportation and this destination to be busy.")

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
lbl_destinations.grid(row = 5, column = 0)

lb_options = tkinter.Listbox(root)
lb_options.grid(row = 6, column = 0, rowspan=3)

lbl_options = tkinter.Label(root, text = "Subway Options" , bg = "white")
lbl_options.grid(row = 2, column = 1)

#btn_fastest_route = tkinter.Button(root, text = "Fastest Route" , command = fastest_route)
#btn_fastest_route.grid(row = 1, column = 2)
#btn_cheapest_route = tkinter.Button(root, text = "Cheapest Route" , command = cheapest_route)
#btn_cheapest_route.grid(row = 2, column = 2)
#btn_least_transfers = tkinter.Button(root, text = "Least Transfers" , command = least_transfers)
#btn_least_transfers.grid(row = 3, column = 2)

lbl_fastest_route = tkinter.Label(root, text = "Fastest Route:")
lbl_fastest_route.grid(row = 3, column = 1)

lbl_cheapest_route = tkinter.Label(root, text = "Cheapest Route:")
lbl_cheapest_route.grid(row = 4, column = 1)

lbl_least_transfers = tkinter.Label(root, text = "Least Transfers:")
lbl_least_transfers.grid(row = 5, column = 1)

# lbl_route = tkinter.Label(root, text = "Routes" , bg = "white")
# lbl_route.grid(row = 0, column = 3)
# lbl_display = tkinter.Label(root, text = "" )
# lbl_display.grid(row = 0, column = 0)

btn_quit = tkinter.Button(root, text = "Quit" , command = quit)
btn_quit.grid(row = 9, column = 3)

lb_cities.bind("<<ListboxSelect>>", select_city)	
lb_options.bind("<<ListboxSelect>>", select_destination)

img_destination = tkinter.PhotoImage(file="Shibuya.gif")
lbl_image = tkinter.Label(image=img_destination)
lbl_image.image = img_destination
lbl_image.grid(row=1, column = 4, rowspan = 5)	
	
update_listbox()	
root.mainloop()
root.destroy()