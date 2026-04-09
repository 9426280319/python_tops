def validate_date(date_str):
    """Validates date format YYYY-MM-DD"""
    parts = date_str.split('-')
    if len(parts) != 3 or len(parts[0]) != 4 or len(parts[1]) != 2 or len(parts[2]) != 2:
        return False
    try:
        year, month, day = map(int, parts)
        if 1 <= month <= 12 and 1 <= day <= 31:
            return True
    except:
        pass
    return False

def validate_roll(roll):
    """Checks if roll number already exists"""
    return roll not in students

# Global data storage
students = {}  # {roll: {'name': str, 'course': str, 'attendance': {date: 'P/A'}}}

def mark_attendance():
    """Mark daily attendance for a student"""
    print("\n--- Attendance Marking ---")
    roll = input("Enter Roll Number: ").strip()
    
    if roll in students:
        print(f"Student already exists: {students[roll]['name']}")
    else:
        name = input("Enter Student Name: ").strip()
        course = input("Enter Course: ").strip()
        students[roll] = {'name': name, 'course': course, 'attendance': {}}
        print(f"New student {name} added!")
    
    date = input("Enter Date (YYYY-MM-DD): ").strip()
    if not validate_date(date):
        print("Invalid date format! Use YYYY-MM-DD")
        return
    
    status = input("Present(P) or Absent(A)? ").strip().upper()
    if status not in ['P', 'A']:
        print("Invalid status! Use P or A")
        return
    
    if date in students[roll]['attendance']:
        print("Attendance already marked for this date!")
        return
    
    students[roll]['attendance'][date] = status
    print("Attendance marked successfully!")

def generate_report():
    """Generate attendance report"""
    print("\n--- Attendance Report ---")
    print("1. Single Student  2. Full Class")
    choice = input("Choose: ").strip()
    
    if choice == '1':
        roll = input("Enter Roll Number: ").strip()
        if roll not in students:
            print("Student not found!")
            return
        student = students[roll]
        show_student_report(student, roll)
    else:
        print_full_class_report()

def show_student_report(student, roll):
    """Display single student report"""
    attendance = student['attendance']
    total_days = len(attendance)
    if total_days == 0:
        print("No attendance records!")
        return
    
    present_days = sum(1 for status in attendance.values() if status == 'P')
    percentage = (present_days / total_days) * 100
    
    print(f"\nStudent: {student['name']} (Roll: {roll}, Course: {student['course']})")
    print(f"Total Days: {total_days}, Present: {present_days}, Absent: {total_days-present_days}")
    print(f"Attendance %: {percentage:.1f}%")
    
    if percentage < 75:
        print("DEFAULTER - Attendance < 75%")
    else:
        print("Good Attendance")

def print_full_class_report():
    """Display class summary"""
    if not students:
        print("No students registered!")
        return
    
    print("\n{'Roll':20} {'Name':20} {'Course':15} {'Total':6} {'Present':6} {'%':5}")
    print("-" * 70)
    
    defaulters = []
    for roll, student in students.items():
        attendance = student['attendance']
        total = len(attendance)
        if total > 0:
            present = sum(1 for s in attendance.values() if s == 'P')
            pct = (present/total)*100
            status = "DEFAULTER" if pct < 75 else "OK"
            if status == "DEFAULTER":
                defaulters.append((student['name'], pct))
            
            print(f"{roll:20} {student['name'][:19]:20} {student['course'][:14]:15} "
                  f"{total:6} {present:6} {pct:5.1f}%")
    
    if defaulters:
        print("\nDEFAULTERS:")
        for name, pct in defaulters:
            print(f"  {name}: {pct:.1f}%")

def main_menu():
    """Main program loop"""
    while True:
        print("\nEduTrack - Attendance Management")
        print("1. Mark Attendance")
        print("2. Generate Report") 
        print("3. Exit")
        choice = input("Choose option: ").strip()
        
        if choice == '1':
            mark_attendance()
        elif choice == '2':
            generate_report()
        elif choice == '3':
            print("Thank you for using EduTrack!")
            break
        else:
            print("Invalid option!")

# Run the program
if __name__ == "__main__":
    main_menu()
