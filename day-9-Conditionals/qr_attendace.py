import cv2
from pyzbar.pyzbar import decode
from datetime import date
import pickle

# Load employee list from pickle (simulate persistent storage)
try:
    with open("employee_data.pkl", "rb") as f:
        employee_list = pickle.load(f)
except FileNotFoundError:
    employee_list = []

def save_data():
    with open("employee_data.pkl", "wb") as f:
        pickle.dump(employee_list, f)

def mark_attendance(emp_id):
    today = str(date.today())
    for employee in employee_list:
        if employee['Emp_id'] == emp_id:
            if not employee['attendance'] or today not in employee['attendance'][-1]:
                employee['attendance'].append({today: 'p'})
                print(f"Marked Present for {employee['name']} on {today}")
                save_data()
                return
            else:
                print(f"Attendance already marked for {employee['name']} today.")
                return
    print("Employee ID not found!")

cap = cv2.VideoCapture(0)

print("Scanning QR... Press 'q' to quit.")
while True:
    success, frame = cap.read()
    for barcode in decode(frame):
        emp_id = int(barcode.data.decode('utf-8'))
        mark_attendance(emp_id)

    cv2.imshow('QR Scanner', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
