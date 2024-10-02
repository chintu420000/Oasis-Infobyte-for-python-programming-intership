import tkinter as tk
import csv
import os
import matplotlib.pyplot as plt
class BMICalculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Simple BMI Calculator")
        tk.Label(self, text="Weight (kg):").grid(row=0, column=0, padx=10, pady=10)
        self.weight_var = tk.DoubleVar()
        tk.Entry(self, textvariable=self.weight_var).grid(row=0, column=1, padx=10, pady=10)
        tk.Label(self, text="Height (m):").grid(row=1, column=0, padx=10, pady=10)
        self.height_var = tk.DoubleVar()
        tk.Entry(self, textvariable=self.height_var).grid(row=1, column=1, padx=10, pady=10)
        tk.Button(self, text="Calculate BMI", command=self.calculate_bmi).grid(row=2, column=0, columnspan=2, pady=10)
        self.result_var = tk.StringVar()
        tk.Label(self, text="BMI:").grid(row=3, column=0, padx=10, pady=10)
        tk.Entry(self, textvariable=self.result_var, state='readonly').grid(row=3, column=1, padx=10, pady=10)
        tk.Button(self, text="View Trends", command=self.view_trends).grid(row=4, column=0, columnspan=2, pady=10)
    def calculate_bmi(self):
        weight = self.weight_var.get()
        height = self.height_var.get()
        if weight > 0 and height > 0:
            bmi = weight / (height ** 2)
            self.result_var.set(f"{bmi:.2f}")
            self.save_data(weight, height, bmi)
            self.categorize_bmi(bmi)
    def categorize_bmi(self, bmi):
        if bmi < 18.5:
            category = "Underweight"
        elif 18.5 <= bmi < 24.9:
            category = "Normal weight"
        elif 25 <= bmi < 29.9:
            category = "Overweight"
        else:
            category = "Obesity"
        tk.messagebox.showinfo("BMI Category", f"You are classified as: {category}")
    def save_data(self, weight, height, bmi):
        file_exists = os.path.isfile('bmi_data.csv')
        with open('bmi_data.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            if not file_exists:
                writer.writerow(['Weight', 'Height', 'BMI'])
            writer.writerow([weight, height, bmi])
    def view_trends(self):
        if not os.path.isfile('bmi_data.csv'):
            tk.messagebox.showwarning("No Data", "No historical data available.")
            return
        weights, heights, bmis = [], [], []
        with open('bmi_data.csv', mode='r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header
            for row in reader:
                weights.append(float(row[0]))
                heights.append(float(row[1]))
                bmis.append(float(row[2]))
        plt.plot(bmis, marker='o')
        plt.title("BMI Trend")
        plt.xlabel("Entries")
        plt.ylabel("BMI")
        plt.axhline(y=24.9, color='r', linestyle='--', label='Normal Upper Limit')
        plt.axhline(y=18.5, color='g', linestyle='--', label='Normal Lower Limit')
        plt.legend()
        plt.show()
app = BMICalculator()
app.mainloop()
