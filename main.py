# Import ทั้ง 10 โมดูล
import module1
import module2
import module3
import module4
import module5
import module6
import module7
import module8
import module9
import module10

def main():
    print("=== เริ่มต้นรันโปรแกรมจาก main.py ===\n")

    # เรียกใช้ Module 1
    print(f"Module 1 (บวกเลข): 15 + 5 = {module1.add(15, 5)}")

    # เรียกใช้ Module 2
    print(f"Module 2 (ทักทาย): {module2.greet('สมชาย')}")

    # เรียกใช้ Module 3
    print(f"Module 3 (สุ่มเลข 1-100): {module3.get_random_number()}")

    # เรียกใช้ Module 4
    print(f"Module 4 (แปลง 30°C เป็น °F): {module4.celsius_to_fahrenheit(30)}°F")

    # เรียกใช้ Module 5
    print(f"Module 5 (เช็ก 8 เป็นเลขคู่ไหม): {module5.is_even(8)}")

    # เรียกใช้ Module 6
    print(f"Module 6 (พื้นที่วงกลมรัศมี 7): {module6.circle_area(7):.2f}")

    # เรียกใช้ Module 7
    print(f"Module 7 (จัดฟอร์แมตเงิน): {module7.format_currency(1250000)}")

    # เรียกใช้ Module 8
    print(f"Module 8 (วันที่ปัจจุบัน): {module8.get_current_date()}")

    # เรียกใช้ Module 9
    print(f"Module 9 (หาค่ามากสุดใน [3, 9, 2, 15, 4]): {module9.find_max([3, 9, 2, 15, 4])}")

    # เรียกใช้ Module 10
    print(f"Module 10 (กลับข้อความ 'Python'): {module10.reverse_string('Python')}")

if __name__ == "__main__":
    main()