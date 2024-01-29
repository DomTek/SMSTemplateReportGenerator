import customtkinter
from tkinter import Tk, IntVar, W, N

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("900x600")

checkbox_var = IntVar()


def on_checkbox_toggle():
    if checkbox_var.get() == 1:
        label_CustomerPO.grid(row=11, column=0, pady=12, padx=10, sticky=W)
        entry_CustomerPO.grid(row=11, column=1, pady=2, padx=5, sticky=W)
    else:
        label_CustomerPO.grid_remove()
        entry_CustomerPO.grid_remove()


def checkbox_callback(*args):
    on_checkbox_toggle()


def report():
    entry_report.delete("1.0", "end")
    # Clear the existing text in the textbox, if you want to replace it
    entry_report.delete("1.0", "end")

    # Insert new text into the textbox for entry_Start
    entry_report.insert("end", "Start Time/Date: " + entry_Start.get() + "\n")

    # Insert new text into the textbox for entry_Finish on the next line
    entry_report.insert("end", "Finish Time/Date: " + entry_Finish.get() + "\n")

    entry_report.insert("end", "Fault Survey: " + entry_FaultSurvey.get() + "\n")

    entry_report.insert("end", "Fault Finding: " + entry_FaultFinding.get("1.0", "end-1c") + "\n")

    entry_report.insert("end", "Fault Test Result: " + entry_FaultTestResult.get() + "\n")

    entry_report.insert("end", "Mitigation: " + entry_Mitigation.get() + "\n")

    entry_report.insert("end", "Follow up required?: " + entry_FollowUp.get() + "\n")

    entry_report.insert("end", "JSEA: " + entry_JSEA.get() + "\n")

    entry_report.insert("end", "Equipment Location: " + entry_EquipmentLocation.get() + "\n")


frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="Report Template Generator")
label.grid(row=0, columnspan=2, pady=12, padx=10)

# Labels
label_Start = customtkinter.CTkLabel(master=frame, text="Start Date & Time:")
label_Finish = customtkinter.CTkLabel(master=frame, text="Finish Date & Time:")
label_FaultSurvey = customtkinter.CTkLabel(master=frame, text="Fault Survey:")
label_FaultFinding = customtkinter.CTkLabel(master=frame, text="Fault Finding:")
label_FaultTestResult = customtkinter.CTkLabel(master=frame, text="Fault Test Result:")
label_report = customtkinter.CTkLabel(master=frame, text="Report")
label_mitigation = customtkinter.CTkLabel(master=frame, text="Mitigation:")
label_FollowUpRequired = customtkinter.CTkLabel(master=frame, text="Follow Up Required: ")
label_JSEA = customtkinter.CTkLabel(master=frame, text="JSEA: ")
label_EquipmentLocation = customtkinter.CTkLabel(master=frame, text="Equipment Location: ")
label_Chargeable = customtkinter.CTkLabel(master=frame, text="Chargeable?")
label_CustomerPO = customtkinter.CTkLabel(master=frame, text="Customer PO# ")

# Label placement
label_Start.grid(row=1, column=0, pady=2, padx=5)
label_Finish.grid(row=2, column=0, pady=2, padx=5)
label_FaultSurvey.grid(row=3, column=0, pady=2, padx=5, sticky=W)
label_FaultFinding.grid(row=4, column=0, pady=2, padx=5, sticky=W+N)
label_FaultTestResult.grid(row=5, column=0, pady=2, padx=5, sticky=W)
label_mitigation.grid(row=6, column=0, pady=2, padx=5, sticky=W)
label_FollowUpRequired.grid(row=7, column=0, pady=2, padx=5, sticky=W)
label_JSEA.grid(row=8, column=0, pady=2, padx=5, sticky=W)
label_EquipmentLocation.grid(row=9, column=0, pady=2, padx=5, sticky=W)
label_report.grid(row=0, column=3, pady=2, padx=5, )
label_Chargeable.grid(row=10, column=0, pady=12, padx=10, sticky=W)
# label_CustomerPO.grid(row=11, column=0, pady=12, padx=10, sticky=W)

# Entry fields
entry_Start = customtkinter.CTkEntry(master=frame, placeholder_text="Start Date & Time")
entry_Finish = customtkinter.CTkEntry(master=frame, placeholder_text="Finish Date & Time")
entry_FaultSurvey = customtkinter.CTkEntry(master=frame, placeholder_text="Fault survey", width=300)
# entry_FaultFinding = customtkinter.CTkEntry(master=frame, placeholder_text="Fault Finding")
entry_FaultFinding = customtkinter.CTkTextbox(master=frame, height=100, width=300)
entry_FaultTestResult = customtkinter.CTkEntry(master=frame, placeholder_text="Fault Result")
entry_Mitigation = customtkinter.CTkEntry(master=frame, placeholder_text="Mitigation")
entry_FollowUp = customtkinter.CTkOptionMenu(master=frame, values=["No", "Yes"])
# entry_FollowUp = customtkinter.CTkEntry(master=frame, placeholder_text="Follow Up")
entry_JSEA = customtkinter.CTkEntry(master=frame, placeholder_text="JSEA")
entry_EquipmentLocation = customtkinter.CTkEntry(master=frame, placeholder_text="Equipment Location")
entry_report = customtkinter.CTkTextbox(master=frame, height=250, width=300)
entry_CustomerPO = customtkinter.CTkEntry(master=frame, placeholder_text="PO")


# Entry Field Placement
entry_Start.grid(row=1, column=1, pady=2, padx=5, sticky=W)
entry_Finish.grid(row=2, column=1, pady=2, padx=5, sticky=W)
entry_FaultSurvey.grid(row=3, column=1, pady=2, padx=5)
entry_FaultFinding.grid(row=4, column=1, pady=2, padx=5)
entry_FaultTestResult.grid(row=5, column=1, pady=2, padx=5, sticky=W)
entry_Mitigation.grid(row=6, column=1, pady=2, padx=5, sticky=W)
entry_FollowUp.grid(row=7, column=1, pady=2, padx=5, sticky=W)
entry_JSEA.grid(row=8, column=1, pady=2, padx=5, sticky=W)
entry_EquipmentLocation.grid(row=9, column=1, pady=2, padx=5, sticky=W)
entry_report.grid(row=1, rowspan=6, column=3, pady=2, padx=5, sticky=N)
# entry_CustomerPO.grid(row=11, column=1, pady=2, padx=5, sticky=W)


# Checkbox setup
checkbox_chargable = customtkinter.CTkCheckBox(master=frame, text="", variable=checkbox_var)
checkbox_chargable.grid(row=10, column=1, pady=12, padx=10, sticky=W)


# Trace changes to the checkbox_var
checkbox_var.trace_add("write", checkbox_callback)

# Create button to create report from template
button = customtkinter.CTkButton(master=frame, text="Create", command=report)
button.grid(row=12, column=1, pady=12, padx=10)



root.mainloop()
