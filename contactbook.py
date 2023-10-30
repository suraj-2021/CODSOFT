import tkinter as tk
from tkinter import messagebox
from tkinterthemes import ThemedStyle

# Initialize the main application window
app = tk.Tk()
app.title("Contact Manager")

# Create a list to store contacts
contacts = []

# Function to add a new contact
def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()
    
    if name and phone:
        contacts.append({"Name": name, "Phone": phone, "Email": email, "Address": address})
        clear_fields()
        messagebox.showinfo("Success", "Contact added successfully.")
    else:
        messagebox.showerror("Error", "Name and Phone are required fields.")

# Function to view all contacts
def view_contacts():
    contacts_list.delete(0, tk.END)
    for contact in contacts:
        name = contact["Name"]
        phone = contact["Phone"]
        contacts_list.insert(tk.END, f"{name}: {phone}")

# Function to search for a contact
def search_contact():
    query = search_entry.get().lower()
    contacts_list.delete(0, tk.END)
    for contact in contacts:
        name = contact["Name"].lower()
        phone = contact["Phone"]
        if query in name or query in phone:
            contacts_list.insert(tk.END, f"{contact['Name']}: {contact['Phone']}")

# Function to update a contact
def update_contact():
    selected_index = contacts_list.curselection()
    if selected_index:
        index = selected_index[0]
        name = name_entry.get()
        phone = phone_entry.get()
        email = email_entry.get()
        address = address_entry.get()
        if name and phone:
            contact = contacts[index]
            contact["Name"] = name
            contact["Phone"] = phone
            contact["Email"] = email
            contact["Address"] = address
            clear_fields()
            messagebox.showinfo("Success", "Contact updated successfully.")
        else:
            messagebox.showerror("Error", "Name and Phone are required fields.")
    else:
        messagebox.showerror("Error", "Select a contact to update.")

# Function to delete a contact
def delete_contact():
    selected_index = contacts_list.curselection()
    if selected_index:
        index = selected_index[0]
        contacts.pop(index)
        clear_fields()
        messagebox.showinfo("Success", "Contact deleted successfully.")
    else:
        messagebox.showerror("Error", "Select a contact to delete.")

# Function to clear input fields
def clear_fields():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)

# Create and configure GUI components
name_label = tk.Label(app, text="Name:")
name_label.grid(row=0, column=0)
name_entry = tk.Entry(app)
name_entry.grid(row=0, column=1)

phone_label = tk.Label(app, text="Phone:")
phone_label.grid(row=1, column=0)
phone_entry = tk.Entry(app)
phone_entry.grid(row=1, column=1)

email_label = tk.Label(app, text="Email:")
email_label.grid(row=2, column=0)
email_entry = tk.Entry(app)
email_entry.grid(row=2, column=1)

address_label = tk.Label(app, text="Address:")
address_label.grid(row=3, column=0)
address_entry = tk.Entry(app)
address_entry.grid(row=3, column=1)

add_button = tk.Button(app, text="Add Contact", command=add_contact)
add_button.grid(row=4, column=0, columnspan=2)

contacts_list = tk.Listbox(app, selectmode=tk.SINGLE)
contacts_list.grid(row=0, column=2, rowspan=6)

view_button = tk.Button(app, text="View Contacts", command=view_contacts)
view_button.grid(row=6, column=0, columnspan=2)

search_label = tk.Label(app, text="Search:")
search_label.grid(row=7, column=0)
search_entry = tk.Entry(app)
search_entry.grid(row=7, column=1)
search_button = tk.Button(app, text="Search", command=search_contact)
search_button.grid(row=7, column=2)

update_button = tk.Button(app, text="Update Contact", command=update_contact)
update_button.grid(row=8, column=0, columnspan=2)

delete_button = tk.Button(app, text="Delete Contact", command=delete_contact)
delete_button.grid(row=9, column=0, columnspan=2)

# Increase the window size
app.geometry("800x400")

# Apply Windows 11 style theme
style = ThemedStyle(app)
style.set_theme("breeze")

# Start the GUI main loop
app.mainloop()
