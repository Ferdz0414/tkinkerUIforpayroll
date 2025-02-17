import tkinter as tk
import payrolls
from tkinter import messagebox

sss = 1000
pagibig = 100
philhealth = 210
tax = 1500
minimum = 645
allowance = 1500

login_window = tk.Tk()
login_window.title("Payroll System")
login_window.geometry("1000x500")
login_window.configure(bg="#333333")

#Log in Page

frame = tk.Frame(login_window, bg="#333333")
frame.pack(pady=20)

label = tk.Label(frame, text="Login", bg="#333333", font=("Arial", 30))
userid_label = tk.Label(frame, text="User ID", bg="#333333", font=("Arial", 15))
userid_entry = tk.Entry(frame, font=("Arial", 15))
password_label = tk.Label(frame, text="Password", bg="#333333", font=("Arial", 15))
password_entry = tk.Entry(frame, show="*", font=("Arial", 15))

#Input Userid and Password
label.grid(row=0, column=0, columnspan=2, pady=40, padx=100)
userid_label.grid(row=1, column=0, pady=10, padx=20)
userid_entry.grid(row=1, column=1, pady=5, padx=20)
password_label.grid(row=2, column=0, pady=5, padx=20)
password_entry.grid(row=2, column=1, pady=5, padx=20)


def login():
    userid = "Admin"
    password = "Admin1234"

    #Validation of Log in
    if userid_entry.get() == userid and password_entry.get() == password:
        messagebox.showinfo(title="Login Success", message="Log in Successfully.")
        login_window.destroy()
        payroll_process()
    else:
        messagebox.showinfo(title="Invalid Login", message="Your Password or User ID does not match.")

btn = tk.Button(frame, text="Log In", font=("Arial", 15), command=login)
btn.grid(row=3, column=0, columnspan=2, pady=10, padx=20)

#Process of payroll

def payroll_process():
    global payprocess_window, name_entry, work_entry, days_entry

    payprocess_window = tk.Tk()
    payprocess_window.title("Payroll Process System")
    payprocess_window.geometry("1000x500")
    payprocess_window.configure(bg="#333333")

    
    #Input of Payroll
    tk.Label(payprocess_window, text="Employee Name", bg="#333333", fg="white", font=("Arial", 15) ,padx=100).pack(pady=5)
    name_entry = tk.Entry(payprocess_window, font=("Arial", 15))
    name_entry.pack(pady=5)

    tk.Label(payprocess_window, text="Position", bg="#333333", fg="white", font=("Arial", 15), padx=100).pack(pady=5)
    work_entry = tk.Entry(payprocess_window, font=("Arial", 15))
    work_entry.pack(pady=5)
    
    tk.Label(payprocess_window, text="Days Worked", bg="#333333", fg="white", font=("Arial", 15), padx=100).pack(pady=5)
    days_entry = tk.Entry(payprocess_window, font=("Arial", 15))
    days_entry.pack(pady=5)
    
    bnt = tk.Button(payprocess_window, text="Process of Payroll", font=("Arial", 15), command=payrollprocess)
    bnt.pack(pady=10)

def payrollprocess():
    empname = name_entry.get()
    work = work_entry.get()
    employee_days = days_entry.get()

    #Payroll Process Validation

    if not empname or not work or not employee_days.isdigit():
        messagebox.showinfo(title="Error", message="Fill out all fields Correctly")
        return
    else:
        messagebox.showinfo(title="Successfully Process", message="Successfully Payroll Computation")
        
        

    employee_days = int(employee_days)

    basicsalary = payrolls.minimum(employee_days, minimum)
    gross = payrolls.allowance(basicsalary, allowance)
    deduction = payrolls.deduction(sss, pagibig, philhealth, tax)
    netamount = payrolls.gross(gross, deduction)

    displaysalary(empname, work, employee_days, gross, deduction, netamount)

    #Display of Payroll

def displaysalary(empname, work, employee_days, gross, deduction, netamount):
    paydisplay_window = tk.Toplevel()
    paydisplay_window.title("Payroll Display System")
    paydisplay_window.geometry("1000x500")
    paydisplay_window.configure(bg="#333333")

    payroll_summary = (
        f"===============================\n"
        f"Employee Information\n"
        f"Employee Name: {empname}\n"
        f"Position: {work}\n"
        f"===============================\n"
        f"Daily Wage\n"
        f"Days Worked: {employee_days}\n"
        f"Total Gross Pay: {gross}\n"
        f"===============================\n"
        f"Government Benefits\n"
        f"SSS : {sss}\n"
        f"Pagibig : {pagibig}\n"
        f"Philhealth : {philhealth}\n"
        f"Tax : {tax}\n"
        f"Total Deduction: {deduction}\n"
        f"===============================\n"
        f"Total Net Salary\n"
        f"Net Salary: {netamount}\n"
        f"==============================="
    )

    #Output of Payroll
    tk.Label(paydisplay_window, text="Salary Computation", font=("Arial", 30), bg="#333333", fg="white", pady=10, padx=100).pack(pady=10)
    tk.Label(paydisplay_window, text=payroll_summary, bg="#333333", fg="white",font=("Arial", 13), justify="left").pack(pady=10)

login_window.mainloop()
