#1. Employee Attendance Tracker

#Implement a system that tracks employee attendance.
#Use loops to process multiple employees and conditionals to check attendance.
#Mark employees as "Needs Attention" if absent for more than 3 consecutive days.

def track_attendance():
    attendance = {}
    
    #taking input 
    no_of_employees = int(input("Enter the number of employees: "))
    
    
    for _ in range(no_of_employees):
        employee_name = input("Enter the name of employee: ")
        attendance[employee_name] = []  
        
        for day in range(1, 8):
            st = input(f"Enter attendance for {employee_name} on day {day} (P for Present, A for Absent): ").strip().upper()
            while st not in ['P', 'A']:
                print("Invalid input. Please enter only in capitals as 'P' for Present or 'A' for Absent.")
                st = input(f"Enter attendance for {employee_name} on day {day} (P for Present, A for Absent): ").strip().upper()
            attendance[employee_name].append(st)

    
    needs_attention = {}

    # Check attendance for each employee
    for employee, days in attendance.items():
        consecutive_absences = 0
        
        for st in days:
            if st == 'A':
                consecutive_absences += 1
                if consecutive_absences > 3:
                    needs_attention[employee] = "Needs Attention"
                    break  
            else:
                consecutive_absences = 0  

    
    print("\nSummary of attendance")
    for employee, days in attendance.items():
        print(f"{employee}: {days}")
    
    print("\nEmployees that need attention:")
    if needs_attention:
        for employee in needs_attention:
            print(f"{employee}: {needs_attention[employee]}")
    else:
        print("No employees need attention.")

# Run the attendance tracker
track_attendance()

 

#name age input 
#empoyee id should be given by system  give one example 1000 and then +1 everytime an employee is added 
#print every detail of employee as a dictionary
#dont take day - take dates of 7 days 
#mark attendance 
#modify attendance
#delete empoylee
#print summary - highlight the students who needs attention 
#implement switch case in such questions


#make dictionary of dictionary like employee id  should be key and name and age should be its value in a separate dictionary , there should be a nested dictionary
# like {"101" :  {name :" ___" ,
                  age:" __" } 
      }