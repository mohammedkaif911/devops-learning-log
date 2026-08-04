
student_scores = {
    "Kaif": 95, "Sam": 38, "Alex": 75, "Guest": 42,
    "John": 15, "Sarah": 88, "Mike": 55, "Emily": 92,
    "David": 30, "Jessica": 64, "Chris": 41, "Amanda": 71,
    "James": 22, "Ashley": 83, "Robert": 12, "Megan": 79,
    "William": 90, "Taylor": 48, "Joseph": 35, "Emma": 67
}

audit_results = {name: "pass" if score >= 40 else "fail" for name, score in student_scores.items()}

print("=========================================")
print("★ SRE STUDENT ACADEMIC AUDIT BOARD ★")
print("=========================================\n")

for name, status in audit_results.items():
    icon = "✓ PASS" if status == "pass" else "✗ FAIL"
    print(f"  Student: {name:<10} | Status: {icon}")

print("\n=========================================")