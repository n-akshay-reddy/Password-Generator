from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for char in range(randint(2, 4))]

    password_list = password_numbers + password_symbols + password_letters
    shuffle(password_list)

    #password = ""
    #for char in password_list:
    #  password += char
    # the above can be written as
    password = "".join(password_list)
    password_entry.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():



    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    new_data = {
        website:{
            "email":email,
            "password":password
        }
    }

    if len(website)==0 or len(password)==0:
        messagebox.showinfo(title="Ooops", message="plese make sure that you haven't left any of the fields empty.")

    else:
        try:
            with open("data.jason", "r") as data_file:
                #reading old data
                data = json.load(data_file)
        except:
            with open("data.json", "w") as data_file:
                #Saving update data
                json.dump(new_data, data_file, indent=4)
        else:
            #updating old data with new data
            data.update(new_data)
            with open("data.json", "w") as data_file:
                #Saving update data
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = website_entry.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No Data Found for the {website} exists.")
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Generator")
window.config(pady=20,padx=20)

canvas = Canvas(height=200, width=200)
logo_imp = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_imp)
canvas.grid(row=0, column=1)

#Labels

website_label = Label(text="website:")
website_label.grid(row=1, column=0)

email_label = Label(text="Email/username:")
email_label.grid(row=2, column=0)

password_label = Label(text="password:")
password_label.grid(row=3, column=0)

#Entries
website_entry = Entry(width=25)
website_entry.grid(row=1, column=1)
website_entry.focus()

email_entry = Entry(width=45)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "nakshayreddy369@gmail.com")

password_entry = Entry(width=25)
password_entry.grid(row=3, column=1)

#Buttons
search_button = Button(text="Search", width=13, command=find_password)
search_button.grid(row=1, column=2)
generate_password = Button(text="Generate Password", command=generate_password)
generate_password.grid(row=3, column=2)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)





window.mainloop()