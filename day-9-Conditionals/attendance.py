#  1. Employee Attendance Tracker

from datetime import date, timedelta

class Employee:
    """Manages employee records and attendance"""

    employee_list = []
    count = 1000  # Employee ID starts from 1001

    def create_employee(self, name, age):
        Employee.count += 1
        employee = {
            'Emp_id': Employee.count,
            'name': name,
            'age': age,
            'attendance': []  # Initialize empty attendance list
        }
        self.employee_list.append(employee)
        print(f"Employee created successfully! Employee ID: {employee['Emp_id']}")

    def display_employee_all(self):
        if not self.employee_list:
            print("No employees found.")
            return
        for employee in self.employee_list:
            print(f"Emp ID: {employee['Emp_id']}, Name: {employee['name']}, Age: {employee['age']}")

    def mark_attendance(self, emp_id):
        for employee in self.employee_list:
            if employee['Emp_id'] == emp_id:
                last_seven_days = [date.today() - timedelta(days=i) for i in range(6, -1, -1)]
                attendance_data = {}

                for day in last_seven_days:
                    while True:
                        attendance = input(f"Enter attendance for {day} ('p' for present, 'a' for absent): ").strip().lower()
                        if attendance in ['p', 'a']:
                            attendance_data[str(day)] = attendance
                            break
                        print("Invalid input! Please enter 'p' or 'a'.")

                employee['attendance'].append(attendance_data)
                print("Attendance marked successfully!")
                return
        print("Employee ID not found!")

    def view_attendance(self, emp_id):
        for employee in self.employee_list:
            if employee['Emp_id'] == emp_id:
                if not employee['attendance']:
                    print("No attendance records found for this employee.")
                    return
                print(f"Attendance for {employee['name']}:")
                for record in employee['attendance']:
                    for date, status in record.items():
                        print(f"{date}: {'Present' if status == 'p' else 'Absent'}")
                return
        print("Employee ID not found!")

    def get_employee_id(self, name):
        for employee in self.employee_list:
            if employee['name'].lower() == name.lower():
                return employee['Emp_id']
        print("Employee not found!")
        return None

    def delete_employee(self, emp_id):
        for employee in self.employee_list:
            if employee['Emp_id'] == emp_id:
                self.employee_list.remove(employee)
                print("Employee deleted successfully!")
                return
        print("Employee ID not found!")


employee_manager = Employee()

while True:
        print("\nSelect an operation:")
        print("1. Create Employee")
        print("2. View All Employees")
        print("3. Mark Attendance")
        print("4. View Attendance")
        print("5. Delete Employee")
        print("6. Exit")

        try:
            user_choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 6.")
            continue

        if user_choice == 1:
            name = input("Enter employee name: ").strip()
            try:
                age = int(input("Enter employee age: "))
                employee_manager.create_employee(name, age)
            except ValueError:
                print("Invalid age! Please enter a valid number.")

        elif user_choice == 2:
            employee_manager.display_employee_all()

        elif user_choice == 3:
            try:
                emp_id = int(input("Enter Employee ID to mark attendance: "))
                employee_manager.mark_attendance(emp_id)
            except ValueError:
                print("Invalid ID! Please enter a valid number.")

        elif user_choice == 4:
            try:
                emp_id = int(input("Enter Employee ID to view attendance: "))
                employee_manager.view_attendance(emp_id)
            except ValueError:
                print("Invalid ID! Please enter a valid number.")

        elif user_choice == 5:
            try:
                emp_id = int(input("Enter Employee ID to delete: "))
                employee_manager.delete_employee(emp_id)
            except ValueError:
                print("Invalid ID! Please enter a valid number.")

        elif user_choice == 6:
            print("Exiting the program...")
            break

        else:
            print("Invalid choice! Please enter a number between 1 and 6.")




 #2. Password Strength Checker

def check_password_strength(password):
    """Evaluates the strength of a given password without using regex."""

    # Initialize criteria flags
    has_upper = has_lower = has_digit = has_special = False
    special_chars = "!@#$%^&*(),.?\":{}|<>"

    # Check each character in the password
    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif char in special_chars:
            has_special = True

    # Length check
    length_criteria = len(password) >= 8

    # Calculate strength score
    strength_score = sum([length_criteria, has_upper, has_lower, has_digit, has_special])

    # Determine password strength
    if strength_score == 5:
        return "Strong Password "
    elif strength_score >= 3:
        return "Medium Password "
    else:
        return "Weak Password "



password = input("Enter a password to check its strength: ").strip()
result = check_password_strength(password)
print(f"Password Strength: {result}")

#Problem 6: Bank Loan Eligibility System
#Create a program to check if a user is eligible for a bank loan based on salary, age, and credit score using nested conditionals.
    

def check_loan_eligibility():
    
    salary = float(input("Enter your monthly salary: "))
    age = int(input("Enter your age: "))
    credit_score = int(input("Enter your credit score (300 to 850): "))

    
    min_salary = 30000     # Minimum monthly salary
    min_age = 21           # Minimum age
    max_age = 60           # Maximum age
    min_credit_score = 650 # Minimum credit score

    
    if age >= min_age and age <= max_age:
        if salary >= min_salary:
            if credit_score >= min_credit_score:
                print("You are eligible for the loan.")
            else:
                print(" Not eligible: Your credit score is too low.")
        else:
            print(" Not eligible: Your salary is too low.")
    else:
        print(" Not eligible: Your age is not within the eligible range.")


check_loan_eligibility()

#Problem 7: AI Chatbot with Conditional Responses
#Design a simple chatbot that responds differently based on user input (e.g., greetings, questions, or farewell messages).

def ai_chatbot():
    print(" Hello! I'm ChatPy, your friendly AI bot. Type something to begin (type 'exit' to quit).")
    
    while True:
        user_input = input("You: ").lower().strip()

        if user_input in ['hi', 'hello', 'hey']:
            print("ChatPy: Hello there! 👋 How can I assist you today?")
        
        elif '?' in user_input:
            print("ChatPy: That's an interesting question. Let me think... ")
        
        elif user_input in ['bye', 'goodbye', 'see you', 'exit']:
            print("ChatPy: Goodbye! 👋 Have a great day!")
            break
        
        elif 'how are you' in user_input:
            print("ChatPy: I'm just code, but I'm functioning perfectly! 😄 How about you?")
        
        else:
            print("ChatPy: Hmm... I’m still learning. Can you try asking differently? 🤖")


ai_chatbot()

#Problem 8: Traffic Light Simulation
#Simulate a traffic light system using conditionals and loops

import time

def traffic_light_simulation():
    print("🚦 Starting traffic light simulation. Press Ctrl+C to stop.\n")
    
    while True:
        
        print("🔴 RED light - STOP")
        time.sleep(3)  
        
        
        print("🟢 GREEN light - GO")
        time.sleep(3)  
        
        
        print("🟡 YELLOW light - SLOW DOWN")
        time.sleep(2) 
        
        print("-" * 30)  


try:
    traffic_light_simulation()
except KeyboardInterrupt:
    print("\n Traffic light simulation stopped.")

#Banking System with ATM Functionality
#Simulate an ATM system for checking balance, withdrawal, and deposit.

def atm():
    balance = 1000  # Initial balance
    while True:
        print("\n==== Welcome to Python ATM ====")
        print("1. Check Balance")
        print("2. Withdraw")
        print("3. Deposit")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            print(f"Your current balance is: ₹{balance}")

        elif choice == '2':
            try:
                amount = float(input("Enter amount to withdraw: ₹"))
                if amount <= 0:
                    print("Invalid amount. Must be greater than zero.")
                elif amount > balance:
                    print("Insufficient balance!")
                else:
                    balance -= amount
                    print(f"Withdrawal successful. New balance: ₹{balance}")
            except ValueError:
                print("Please enter a valid number.")

        elif choice == '3':
            try:
                amount = float(input("Enter amount to deposit: ₹"))
                if amount <= 0:
                    print("Invalid amount. Must be greater than zero.")
                else:
                    balance += amount
                    print(f"Deposit successful. New balance: ₹{balance}")
            except ValueError:
                print("Please enter a valid number.")

        elif choice == '4':
            print("Thank you for using the Python ATM. Goodbye!")
            break

        else:
            print("Invalid choice. Please select a valid option.")

# Run the ATM system
atm()


#Problem 10: Stock Market Trend Analysis
#Write a program to analyze stock prices and predict buy/sell signals based on historical trends using conditionals.

def analyze_stock_trends(prices):
    if len(prices) < 3:
        print("Need at least 3 days of stock prices to analyze trends.")
        return

    print("Analyzing stock price trends...")

    for i in range(2, len(prices)):
        day1 = prices[i - 2]
        day2 = prices[i - 1]
        day3 = prices[i]

        print(f"\nDays {i-1}, {i}, {i+1} prices: {day1}, {day2}, {day3}")

        if day1 < day2 < day3:
            print("Signal: 📈 SELL (Uptrend detected)")
        elif day1 > day2 > day3:
            print("Signal: 📉 BUY (Downtrend detected)")
        else:
            print("Signal: ➡️ HOLD (No clear trend)")

# Example stock prices for a week
historical_prices = [100, 105, 110, 108, 107, 109, 111, 108]

# Run the trend analysis
analyze_stock_trends(historical_prices)


#Problem 9: Smart Home Automation
#Implement a conditional-based smart home system where temperature, humidity, and motion sensors determine actions (e.g., turning lights and fans on/off).

def smart_home_system(temperature, humidity, motion_detected):
    print(f"\nSensor Readings:")
    print(f"Temperature: {temperature}°C")
    print(f"Humidity: {humidity}%")
    print(f"Motion Detected: {'Yes' if motion_detected else 'No'}")

    # Fan control
    if temperature > 30 or humidity > 70:
        print("Action: 🔄 Fan is ON (High temp or humidity)")
    else:
        print("Action: 📴 Fan is OFF")

    # Light control
    if motion_detected:
        print("Action: 💡 Lights are ON (Motion detected)")
    else:
        print("Action: 💡 Lights are OFF (No motion)")

# Example test cases
smart_home_system(32, 60, True)
smart_home_system(25, 75, False)
smart_home_system(22, 55, False)


