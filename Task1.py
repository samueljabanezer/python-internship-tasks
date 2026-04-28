import os
 
try:
    # Step 1: Create file and write student names
    with open("students.txt", "w") as file:
        names = ["John", "Alice", "Bob", "Eve", "Charlie"]
        for name in names:
            file.write(name + "\n")
    print("[OK] students.txt created successfully.")
 
    # Step 2: Read data back from file
    with open("students.txt", "r") as file:
        data = file.readlines()
    print("Original Data:", [n.strip() for n in data])
 
    # Step 3: Process - convert to uppercase and save
    with open("updated_students.txt", "w") as file:
        for name in data:
            file.write(name.strip().upper() + "\n")
    print("[OK] Processed and saved to updated_students.txt")
 
    # Step 4: Rename file to final name
    os.rename("updated_students.txt", "final_students.txt")
    print("[OK] File renamed to final_students.txt")
 
    # Step 5: Verify the file exists
    if os.path.exists("final_students.txt"):
        print("[OK] Verified: final_students.txt exists.")
 
except FileNotFoundError as e:
    print("File not found:", e)
except PermissionError as e:
    print("Permission denied:", e)
except Exception as e:
    print("Unexpected error:", e)
