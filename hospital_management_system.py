from tkinter import *
from tkinter import ttk
import random
import time
import datetime
from tkinter import messagebox
import cx_Oracle


class Hospital:
    def __init__(self,root):
        self.root = root
        self.root.title("Hospital Management System")
        self.root.geometry("1540x800+0+0")

        self.NameOfTablets = StringVar()
        self.ref = StringVar()
        self.Dose = StringVar()
        self.NumberOfTablets = StringVar()
        self.Lot = StringVar()
        self.IssuedDate = StringVar()
        self.expiryDate = StringVar()
        self.DailyDose = StringVar()
        self.sideEffect = StringVar()
        self.FurtherInformation = StringVar()
        self.StorageAdvice = StringVar()
        self.DrivingUsingMachine = StringVar()
        self.howToUseMedication = StringVar()
        self.patientId = StringVar()
        self.nhsNumber = StringVar()
        self.patientName = StringVar()
        self.DateOfBirth = StringVar()
        self.PatientAddress = StringVar()

        lbltitle = Label(self.root, bd=20, relief=RIDGE, text='HOSPITAL MANAGEMENT SYSTEM', fg="red", bg="white",
                         font=("times new roman", 50, "bold"))
        lbltitle.pack(side=TOP, fill=X)

        # DATA FRAME

        DataFrame = Frame(self.root, bd=20, relief=RIDGE)
        DataFrame.place(x=0, y=130, width=1530, height=400)

        dataframeLeft = LabelFrame(DataFrame, bd=10, relief=RIDGE, padx=10, font=("times new roman", 12, "bold"),
                                   text="Patient Information")
        dataframeLeft.place(x=0, y=5, width=980, height=350)

        dataframeRight = LabelFrame(DataFrame, bd=10, relief=RIDGE, padx=10, font=("times new roman", 12, "bold"),
                                    text="Prescription")
        dataframeRight.place(x=990, y=5, width=460, height=350)

        # button frame

        ButtonFrame = Frame(self.root, bd=20, relief=RIDGE)
        ButtonFrame.place(x=0, y=530, width=1530, height=70)

        # DETAILS FRAME
        detailsFrame = Frame(self.root, bd=20, relief=RIDGE)
        detailsFrame.place(x=0, y=600, width=1530, height=190)

        # data frame left

        lblNameTablet = Label(dataframeLeft, text="Names of Tablet", font=("arial", 12, "bold"), padx=2, pady=6)
        lblNameTablet.grid(row=0, column=0)

        comNameTablet = ttk.Combobox(dataframeLeft, textvariable=self.NameOfTablets, state="readonly",
                                     font=("arial", 12, "bold"),
                                     width=33)
        comNameTablet["value"] = ("Nice", "Corona vaccine", "Acetaminophen", "Adderall", "Amlodipine", "Ativan")
        comNameTablet.current(0)
        comNameTablet.grid(row=0, column=1)

        lblref = Label(dataframeLeft, font=("arial", 12, "bold"), text="Reference no:", padx=2, pady=6)
        lblref.grid(row=1, column=0, sticky=W)
        txtref = Entry(dataframeLeft, textvariable=self.ref, font=("arial", 13, "bold"), width=35)
        txtref.grid(row=1, column=1)

        lblDose = Label(dataframeLeft, font=("arial", 12, "bold"), text="Dose:", padx=2, pady=6)
        lblDose.grid(row=2, column=0, sticky=W)
        txtDose = Entry(dataframeLeft, textvariable=self.Dose, font=("arial", 13, "bold"), width=35)
        txtDose.grid(row=2, column=1)

        lblNoOfTablets = Label(dataframeLeft, font=("arial", 12, "bold"), text="No of Tablets:", padx=2, pady=6)
        lblNoOfTablets.grid(row=3, column=0, sticky=W)
        txtNoOfTablets = Entry(dataframeLeft, textvariable=self.NumberOfTablets, font=("arial", 13, "bold"), width=35)
        txtNoOfTablets.grid(row=3, column=1)

        lblLot = Label(dataframeLeft, font=("arial", 12, "bold"), text="Lot:", padx=2, pady=6)
        lblLot.grid(row=4, column=0, sticky=W)
        txtLot = Entry(dataframeLeft, textvariable=self.Lot, font=("arial", 13, "bold"), width=35)
        txtLot.grid(row=4, column=1)

        lblissueDate = Label(dataframeLeft, font=("arial", 12, "bold"), text="Issue Date:", padx=2, pady=6)
        lblissueDate.grid(row=5, column=0, sticky=W)
        txtissueDate = Entry(dataframeLeft, textvariable=self.IssuedDate, font=("arial", 13, "bold"), width=35)
        txtissueDate.grid(row=5, column=1)

        lblexpDate = Label(dataframeLeft, font=("arial", 12, "bold"), text="Expiry Date:", padx=2, pady=6)
        lblexpDate.grid(row=6, column=0, sticky=W)
        txtexpDate = Entry(dataframeLeft, textvariable=self.expiryDate, font=("arial", 13, "bold"), width=35)
        txtexpDate.grid(row=6, column=1)

        lblDailyDose = Label(dataframeLeft, font=("arial", 12, "bold"), text="Daily Dose:", padx=2, pady=6)
        lblDailyDose.grid(row=7, column=0, sticky=W)
        txtDailyDose = Entry(dataframeLeft, textvariable=self.DailyDose, font=("arial", 13, "bold"), width=35)
        txtDailyDose.grid(row=7, column=1)

        lblSideEffect = Label(dataframeLeft, font=("arial", 12, "bold"), text="side Effect:", padx=2, pady=6)
        lblSideEffect.grid(row=8, column=0, sticky=W)
        txtSideEffect = Entry(dataframeLeft, textvariable=self.sideEffect, font=("arial", 13, "bold"), width=35)
        txtSideEffect.grid(row=8, column=1)

        lblFurtherInfo = Label(dataframeLeft, font=("arial", 12, "bold"), text="Further Information:", padx=2, pady=6)
        lblFurtherInfo.grid(row=0, column=2, sticky=W)
        txtFurtherInfo = Entry(dataframeLeft, textvariable=self.FurtherInformation, font=("arial", 13, "bold"), width=35)
        txtFurtherInfo.grid(row=0, column=3)

        lblBP = Label(dataframeLeft, font=("arial", 12, "bold"), text="Blood Pressure:", padx=2, pady=6)
        lblBP.grid(row=1, column=2, sticky=W)
        txtBP = Entry(dataframeLeft, textvariable=self.DrivingUsingMachine, font=("arial", 13, "bold"), width=35)
        txtBP.grid(row=1, column=3)

        lblStorage = Label(dataframeLeft, font=("arial", 12, "bold"), text="storage Advice:", padx=2, pady=6)
        lblStorage.grid(row=2, column=2, sticky=W)
        txtStorage = Entry(dataframeLeft, textvariable = self.StorageAdvice ,font=("arial", 13, "bold"), width=35)
        txtStorage.grid(row=2, column=3)

        lblMedicine = Label(dataframeLeft, font=("arial", 12, "bold"), text="Medication:", padx=2, pady=6)
        lblMedicine.grid(row=3, column=2, sticky=W)
        txtMedicine = Entry(dataframeLeft, textvariable=self.howToUseMedication, font=("arial", 13, "bold"), width=35)
        txtMedicine.grid(row=3, column=3)

        lblId = Label(dataframeLeft, font=("arial", 12, "bold"), text="Patient Id:", padx=2, pady=6)
        lblId.grid(row=4, column=2, sticky=W)
        txtId = Entry(dataframeLeft, textvariable=self.patientId, font=("arial", 13, "bold"), width=35)
        txtId.grid(row=4, column=3)

        lblNhsNo = Label(dataframeLeft, font=("arial", 12, "bold"), text="NHS Number:", padx=2, pady=6)
        lblNhsNo.grid(row=5, column=2, sticky=W)
        txtNhsNo = Entry(dataframeLeft, textvariable=self.nhsNumber, font=("arial", 13, "bold"), width=35)
        txtNhsNo.grid(row=5, column=3)

        lblname = Label(dataframeLeft, font=("arial", 12, "bold"), text="Patient Name:", padx=2, pady=6)
        lblname.grid(row=6, column=2, sticky=W)
        txtname = Entry(dataframeLeft, textvariable=self.patientName, font=("arial", 13, "bold"), width=35)
        txtname.grid(row=6, column=3)

        lbldob = Label(dataframeLeft, font=("arial", 12, "bold"), text="Date Of Birth:", padx=2, pady=6)
        lbldob.grid(row=7, column=2, sticky=W)
        txtdob = Entry(dataframeLeft, textvariable=self.DateOfBirth, font=("arial", 13, "bold"), width=35)
        txtdob.grid(row=7, column=3)

        lblAdd = Label(dataframeLeft, font=("arial", 12, "bold"), text="Patient Address:", padx=2, pady=6)
        lblAdd.grid(row=8, column=2, sticky=W)
        txtAdd = Entry(dataframeLeft, textvariable=self.PatientAddress, font=("arial", 13, "bold"), width=35)
        txtAdd.grid(row=8, column=3)

        # data frame right

        self.txtPrescription = Text(dataframeRight, font=("arial", 12, "bold"), width=47, height=16, padx=2, pady=6)
        self.txtPrescription.grid(row=0, column=0),

        # buttons
        btnPrescription = Button(ButtonFrame, text="Prescription", bg="green", fg="white", font=("arial", 12, "bold"),
                                 width=23, padx=2, pady=6)
        btnPrescription.grid(row=0, column=0)

        btnPrescriptionData = Button(ButtonFrame,command = self.iPrescriptionData, text="Prescription Data", bg="green", fg="white",
                                     font=("arial", 12, "bold"),
                                     width=23, padx=2, pady=6)
        btnPrescriptionData.grid(row=0, column=1)

        btnUpdate = Button(ButtonFrame, text="Update", bg="green", fg="white", font=("arial", 12, "bold"),
                           width=23, padx=2, pady=6)
        btnUpdate.grid(row=0, column=2)

        btnDelete = Button(ButtonFrame, text="Delete", bg="green", fg="white", font=("arial", 12, "bold"),
                           width=23, padx=2, pady=6)
        btnDelete.grid(row=0, column=3)

        btnClear = Button(ButtonFrame, text="Clear", bg="green", fg="white", font=("arial", 12, "bold"),
                          width=23, padx=2, pady=6)
        btnClear.grid(row=0, column=4)

        btnExit = Button(ButtonFrame, text="Exit", bg="green", fg="white", font=("arial", 12, "bold"),
                         width=23, padx=2, pady=6)
        btnExit.grid(row=0, column=5)

        # table

        # scrollbar

        scroll_x = Scrollbar(detailsFrame, orient=HORIZONTAL)
        scroll_y = Scrollbar(detailsFrame, orient=VERTICAL)
        self.hospital_table = ttk.Treeview(detailsFrame,
                                           column=("nameOfTablet", "ref", "dose", "noOfTablets", "lot", "issueDate",
                                                   "expDate", "dailyDose", "storage", "nhsNumber", "pname", "dob",
                                                   "address"),
                                           xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x = ttk.Scrollbar(command=self.hospital_table.xview)
        scroll_y = ttk.Scrollbar(command=self.hospital_table.yview)

        self.hospital_table.heading("nameOfTablet", text="Name Of Tablet")
        self.hospital_table.heading("ref", text="Reference No")
        self.hospital_table.heading("dose", text="Dose")
        self.hospital_table.heading("noOfTablets", text="No Of Tablets")
        self.hospital_table.heading("lot", text="Lot")
        self.hospital_table.heading("issueDate", text="Issue Date")
        self.hospital_table.heading("expDate", text="Expiry Date")
        self.hospital_table.heading("dailyDose", text="Daily Dose")
        self.hospital_table.heading("storage", text="Storage")
        self.hospital_table.heading("nhsNumber", text="NHS Number")
        self.hospital_table.heading("pname", text="Patient Name")
        self.hospital_table.heading("dob", text="DOB")
        self.hospital_table.heading("address", text="Address")

        self.hospital_table["show"] = "headings"

        self.hospital_table.column("nameOfTablet", width=100)
        self.hospital_table.column("ref", width=100)
        self.hospital_table.column("dose", width=100)
        self.hospital_table.column("noOfTablets", width=100)
        self.hospital_table.column("lot", width=100)
        self.hospital_table.column("issueDate", width=100)
        self.hospital_table.column("expDate", width=100)
        self.hospital_table.column("dailyDose", width=100)
        self.hospital_table.column("storage", width=100)
        self.hospital_table.column("nhsNumber", width=100)
        self.hospital_table.column("pname", width=100)
        self.hospital_table.column("dob", width=100)
        self.hospital_table.column("address", width=100)

        self.hospital_table.pack(fill=BOTH, expand=1)



        #functionality declarations

    








root = Tk()
ob = Hospital(root)
root.mainloop()