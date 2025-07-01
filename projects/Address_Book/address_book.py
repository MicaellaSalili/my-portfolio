import tkinter as tk
from tkinter import messagebox, simpledialog
from tkinter import *
from tkinter.filedialog import askopenfilename

number = 1
file_opened = ''
fileIsOpen = False
class AddressBook:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Address Book")
        self.root.geometry("550x450")
        menu1 = tk.Menu(self.root)
        self.root.config(menu=menu1)

        bg_color = "#F0F0F0"
        label_font = ("Arial", 12)
        entry_font = ("Arial", 12)
        button_font = ("Arial", 12, "bold")

        self.root.configure(bg=bg_color)

        self.Fname_label = tk.Label(self.root, text="First Name:", font=label_font, bg=bg_color)
        self.Fname_entry = tk.Entry(self.root, font=entry_font)
        self.Lname_label = tk.Label(self.root, text="Last Name:", font=label_font, bg=bg_color)
        self.Lname_entry = tk.Entry(self.root, font=entry_font)
        self.email_label = tk.Label(self.root, text="Email:", font=label_font, bg=bg_color)
        self.email_entry = tk.Entry(self.root, font=entry_font)
        self.phone_label = tk.Label(self.root, text="Phone:", font=label_font, bg=bg_color)
        self.phone_entry = tk.Entry(self.root, font=entry_font)

        button_width = 15
        button_padx = 10
        button_pady = 5

        self.add_button = tk.Button(self.root, text="Add Contact", font=button_font, width=button_width, bg="#4CAF50", fg="white", command=self.add_contact)
        self.edit_button = tk.Button(self.root, text="Edit Contact", font=button_font, width=button_width, bg="#FF9800",fg="white", command=self.edit_contact)
        self.view_button = tk.Button(self.root, text="View Contacts", font=button_font, width=button_width, bg="#2196F3",fg="white", command=self.view_contacts)
        self.delete_button = tk.Button(self.root, text="Delete Contact", font=button_font, width=button_width, bg="#F44336",fg="white", command=self.delete_contact)
        self.search_label = tk.Label(self.root, text="Search Contact:", font=label_font, bg=bg_color)
        self.search_entry = tk.Entry(self.root, font=entry_font)
        self.search_button = tk.Button(self.root, text="Search", font=button_font, width=button_width, bg="#9C27B0",fg="white", command=self.search_contact)
        self.file_button = tk.Button(self.root, text="File Open", font=button_font, width=button_width, bg="#676a5f",fg="white", command=self.openfile)
        self.exit_button = tk.Button(self.root, text="Exit", font=button_font, width=button_width, bg="#607D8B", fg="white", command=self.exit_program)

        self.Fname_label.grid(row=0, column=0, padx=10, pady=10)
        self.Fname_entry.grid(row=0, column=1, padx=10, pady=10)
        self.Lname_label.grid(row=1, column=0, padx=10, pady=10)
        self.Lname_entry.grid(row=1, column=1, padx=10, pady=10)
        self.email_label.grid(row=2, column=0, padx=10, pady=10)
        self.email_entry.grid(row=2, column=1, padx=10, pady=10)
        self.phone_label.grid(row=3, column=0, padx=10, pady=10)
        self.phone_entry.grid(row=3, column=1, padx=10, pady=10)

        self.add_button.grid(row=4, column=1, padx=10, pady=10)
        self.edit_button.grid(row=2, column=2, padx=10, pady=10)
        self.view_button.grid(row=1, column=2, padx=10, pady=10)
        self.delete_button.grid(row=3, column=2, padx=10, pady=10)
        self.search_label.grid(row=5, column=0, padx=10, pady=10)
        self.search_entry.grid(row=5, column=1, padx=10, pady=10)
        self.search_button.grid(row=5, column=2, padx=10, pady=10)
        self.file_button.grid(row=0, column=2)
        self.exit_button.grid(row=6, column=1, padx=10, pady=10)

        self.root.mainloop()

    def openfile(self):
        global file_opened, fileIsOpen
        file_path = askopenfilename(title="Open File", filetypes=[("Text Files", ".txt"), ("All Files", ".*")])
        print("Selected file:", file_path)

        file_opened = file_path
        fileIsOpen = True


    def add_contact(self):
        if fileIsOpen is True:
            global number
            with open(file_opened, "r") as file:
                ent_number = file.readlines()

            lent_number = len(ent_number)
            number = int(lent_number) + 1

            if number > 100:
                messagebox.showerror("Error", "Contact list is full. Delete a contact to add another.")

                self.Fname_entry.delete(0, "end")
                self.Lname_entry.delete(0, "end")
                self.email_entry.delete(0, "end")
                self.phone_entry.delete(0, "end")
                return
            try:
                entry = []
                Fname = self.Fname_entry.get()
                Lname = self.Lname_entry.get()
                email = self.email_entry.get()
                phone = self.phone_entry.get()

                if not Fname or not Lname or not email or not phone:
                    messagebox.showerror("Error", "Please enter the details correctly.")
                    return

                for name in [Fname, Lname]:
                    if not name.replace(' ', '').isalpha():
                        messagebox.showerror("Error", "Please enter a valid name.")
                        return

                if "@" not in email or "." not in email:
                    messagebox.showerror("Error", "Please enter a valid email address.")
                    return

                if not phone.isdigit() or len(phone) != 11:
                    messagebox.showerror("Error", "Please enter a valid 11-digit phone number.")
                    return

                with open(file_opened, "r") as file:
                    contacts = file.readlines()
                    for contact in contacts:
                        if email in contact:
                            messagebox.showerror("Error", "Email address already exists.")
                            return
                        if phone in contact:
                            messagebox.showerror("Error", "Phone number already exists.")
                            return

                entry.append(f" Name: {Fname} {Lname}, Address: {email}, Contact No.: {phone}\n")
                if True:
                    with open(file_opened, "a") as file:
                        file.write(str(number))
                        file.write(''.join(entry))

                self.Fname_entry.delete(0, "end")
                self.Lname_entry.delete(0, "end")
                self.email_entry.delete(0, "end")
                self.phone_entry.delete(0, "end")

                messagebox.showinfo("Add Contact", "Contact added successfully.")
            except Exception as e:
                messagebox.showerror("Error", str(e))
        else:
            messagebox.showerror("Error", "No file is currently opened")


    def view_contacts(self):
        if fileIsOpen is True:
            top = Toplevel(self.root)
            top.geometry("800x500")
            top.title("View Contacts")

            scrollbar = Scrollbar(top)
            scrollbar.pack(side=RIGHT, fill=Y)

            text = Text(top, yscrollcommand=scrollbar.set)
            text.pack(fill=BOTH, expand=True)

            scrollbar.config(command=text.yview)

            with open(file_opened, "r") as file:
                content = file.read()
                text.insert(END, content)
        else:
            messagebox.showerror("Error", "No file is currently opened")


    def edit_contact(self):
        if fileIsOpen is True:
            entry_number = self.get_number()

            if not entry_number:
                return

            with open(file_opened, "r") as file:
                lines = file.readlines()

            found_index = None
            for index, line in enumerate(lines):
                if line.startswith(str(entry_number)):
                    found_index = index
                    break

            if found_index is None:
                messagebox.showerror("Error", "Contact not found.")
                return

            found_contact = lines[found_index]
            contact_parts = found_contact.strip().split(", ")
            contact_number = str(found_index + 1)  # Extract the contact number
            fname = contact_parts[0].split(":")[1].strip().split()[0]
            lname = contact_parts[0].split(":")[1].strip().split()[1]
            email = contact_parts[1].split(":")[1].strip()
            phone = contact_parts[2].split(":")[1].strip()

            self.Fname_entry.delete(0, "end")
            self.Fname_entry.insert("end", fname)
            self.Lname_entry.delete(0, "end")
            self.Lname_entry.insert("end", lname)
            self.email_entry.delete(0, "end")
            self.email_entry.insert("end", email)
            self.phone_entry.delete(0, "end")
            self.phone_entry.insert("end", phone)

            self.edit_button.config(state="disabled")
            self.add_button.config(state="disabled")

            def save_edit():
                updated_fname = self.Fname_entry.get()
                updated_lname = self.Lname_entry.get()
                updated_email = self.email_entry.get()
                updated_phone = self.phone_entry.get()

                if not updated_fname or not updated_lname or not updated_email or not updated_phone:
                    messagebox.showerror("Error", "Please enter the details correctly.")
                    return

                for name in [updated_fname, updated_lname]:
                    if not name.replace(' ', '').isalpha():
                        messagebox.showerror("Error", "Please enter a valid name.")
                        return

                if "@" not in updated_email or "." not in updated_email:
                    messagebox.showerror("Error", "Please enter a valid email address.")
                    return

                if not updated_phone.isdigit() or len(updated_phone) != 11:
                    messagebox.showerror("Error", "Please enter a valid 11-digit phone number.")
                    return

                updated_contact = f"{contact_number} Name: {updated_fname} {updated_lname}, Address: {updated_email}, Contact No.: {updated_phone}\n"
                lines[found_index] = updated_contact

                with open(file_opened, "w") as file:
                    file.writelines(lines)

                self.Fname_entry.delete(0, "end")
                self.Lname_entry.delete(0, "end")
                self.email_entry.delete(0, "end")
                self.phone_entry.delete(0, "end")

                self.edit_button.config(state="normal")
                self.add_button.config(state="normal")

                messagebox.showinfo("Edit Contact", "Contact updated successfully.")

                save_button.grid_remove()
                cancel_button.grid_remove()

            save_button = tk.Button(self.root, text="Save", command=save_edit)
            save_button.grid(row=7, column=0)

            def cancel_edit():
                self.Fname_entry.delete(0, "end")
                self.Lname_entry.delete(0, "end")
                self.email_entry.delete(0, "end")
                self.phone_entry.delete(0, "end")

                self.edit_button.config(state="normal")
                self.add_button.config(state="normal")

                save_button.grid_remove()
                cancel_button.grid_remove()

            cancel_button = tk.Button(self.root, text="Cancel", command=cancel_edit)
            cancel_button.grid(row=7, column=2)
        else:
            messagebox.showerror("Error", "No file is currently opened")

    def get_number(self):
        number = simpledialog.askinteger("Edit Contact", "Enter the number of contact you want to edit:")
        return number

    def delete_contact(self):
        if fileIsOpen is True:
            global number
            entry_number = self.get_number()

            if not entry_number:
                return

            with open(file_opened, "r") as file:
                lines = file.readlines()

            found_index = None
            for index, line in enumerate(lines):
                if line.startswith(str(entry_number)):
                    found_index = index
                    break

            if found_index is None:
                messagebox.showerror("Error", "Contact not found.")
                return

            del lines[found_index]

            with open(file_opened, "w") as file:
                file.writelines(lines)

            for index, line in enumerate(lines):
                if line.strip():
                    contact_number = line.split()[0]
                    new_number = index + 1
                    updated_line = line.replace(contact_number, str(new_number), 1)
                    lines[index] = updated_line

            with open(file_opened, "w") as file:
                file.writelines(lines)

            messagebox.showinfo("Delete Contact", "Contact deleted successfully.")

            self.Fname_entry.delete(0, "end")
            self.Lname_entry.delete(0, "end")
            self.email_entry.delete(0, "end")
            self.phone_entry.delete(0, "end")
        else:
            messagebox.showerror("Error", "No file is currently opened")

    def search_contact(self):
        if fileIsOpen is True:
            keyword = self.search_entry.get()

            if not keyword:
                messagebox.showerror("Error", "Type any of this: Firstname, Lastname, Address, or Contact No.")
                return

            with open(file_opened, "r") as file:
                contacts = file.readlines()

            found_contacts = []
            for contact in contacts:
                if keyword.lower() in contact.lower():
                    found_contacts.append(contact.strip())

            if found_contacts:
                messagebox.showinfo("Search Results", "\n".join(found_contacts))
            else:
                messagebox.showinfo("Search Results", f"No contacts found for '{keyword}'.")

            self.search_entry.delete(0, "end")
        else:
            messagebox.showerror("Error", "No file is currently opened")


    def exit_program(self):
        if self.Fname_entry.get() or self.Lname_entry.get() or self.email_entry.get() or self.phone_entry.get():
            result = messagebox.askyesno("Exit Program", "Are you sure you want to exit without saving?")
            if not result:
                return

        self.root.quit()

AddressBook()
