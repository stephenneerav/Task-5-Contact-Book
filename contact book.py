import tkinter as tk
from tkinter import messagebox, simpledialog

class Contact:
    def __init__(self, store_name, phone, email, address):
        self.store_name = store_name
        self.phone = phone
        self.email = email
        self.address = address

class ContactManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Manager")
        
        self.contacts = []
        
        self.setup_ui()

    def setup_ui(self):
        
        self.add_frame = tk.Frame(self.root)
        self.add_frame.pack(pady=10)
        
        tk.Label(self.add_frame, text="Store Name:").grid(row=0, column=0)
        self.store_name_entry = tk.Entry(self.add_frame)
        self.store_name_entry.grid(row=0, column=1)

        tk.Label(self.add_frame, text="Phone Number:").grid(row=1, column=0)
        self.phone_entry = tk.Entry(self.add_frame)
        self.phone_entry.grid(row=1, column=1)

        tk.Label(self.add_frame, text="Email:").grid(row=2, column=0)
        self.email_entry = tk.Entry(self.add_frame)
        self.email_entry.grid(row=2, column=1)

        tk.Label(self.add_frame, text="Address:").grid(row=3, column=0)
        self.address_entry = tk.Entry(self.add_frame)
        self.address_entry.grid(row=3, column=1)
        
        self.add_button = tk.Button(self.add_frame, text="Add Contact", command=self.add_contact)
        self.add_button.grid(row=4, columnspan=2, pady=5)

        
        self.list_frame = tk.Frame(self.root)
        self.list_frame.pack(pady=10)
        
        self.contact_listbox = tk.Listbox(self.list_frame, width=50)
        self.contact_listbox.pack()
        
        
        self.search_frame = tk.Frame(self.root)
        self.search_frame.pack(pady=10)
        
        tk.Label(self.search_frame, text="Search:").grid(row=0, column=0)
        self.search_entry = tk.Entry(self.search_frame)
        self.search_entry.grid(row=0, column=1)
        
        self.search_button = tk.Button(self.search_frame, text="Search", command=self.search_contact)
        self.search_button.grid(row=0, column=2)

        
        self.update_delete_frame = tk.Frame(self.root)
        self.update_delete_frame.pack(pady=10)
        
        self.update_button = tk.Button(self.update_delete_frame, text="Update Contact", command=self.update_contact)
        self.update_button.grid(row=0, column=0, padx=5)
        
        self.delete_button = tk.Button(self.update_delete_frame, text="Delete Contact", command=self.delete_contact)
        self.delete_button.grid(row=0, column=1, padx=5)

    def add_contact(self):
        store_name = self.store_name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()

        if not (store_name and phone and email and address):
            messagebox.showwarning("Input Error", "All fields are required")
            return

        contact = Contact(store_name, phone, email, address)
        self.contacts.append(contact)
        self.update_contact_listbox()
        self.clear_entries()

    def update_contact_listbox(self):
        self.contact_listbox.delete(0, tk.END)
        for contact in self.contacts:
            self.contact_listbox.insert(tk.END, f"{contact.store_name} - {contact.phone}")

    def clear_entries(self):
        self.store_name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)

    def search_contact(self):
        search_term = self.search_entry.get().lower()
        results = [c for c in self.contacts if search_term in c.store_name.lower() or search_term in c.phone]
        
        self.contact_listbox.delete(0, tk.END)
        for contact in results:
            self.contact_listbox.insert(tk.END, f"{contact.store_name} - {contact.phone}")

    def update_contact(self):
        selected_index = self.contact_listbox.curselection()
        if not selected_index:
            messagebox.showwarning("Selection Error", "No contact selected")
            return

        selected_index = selected_index[0]
        contact = self.contacts[selected_index]

        updated_store_name = simpledialog.askstring("Input", "Store Name:", initialvalue=contact.store_name)
        updated_phone = simpledialog.askstring("Input", "Phone Number:", initialvalue=contact.phone)
        updated_email = simpledialog.askstring("Input", "Email:", initialvalue=contact.email)
        updated_address = simpledialog.askstring("Input", "Address:", initialvalue=contact.address)

        if not (updated_store_name and updated_phone and updated_email and updated_address):
            messagebox.showwarning("Input Error", "All fields are required")
            return

        contact.store_name = updated_store_name
        contact.phone = updated_phone
        contact.email = updated_email
        contact.address = updated_address

        self.update_contact_listbox()

    def delete_contact(self):
        selected_index = self.contact_listbox.curselection()
        if not selected_index:
            messagebox.showwarning("Selection Error", "No contact selected")
            return

        selected_index = selected_index[0]
        del self.contacts[selected_index]
        self.update_contact_listbox()

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactManagerApp(root)
    root.mainloop()
