while True:
    try:
        x = float(input("กว้าง"))
        y = float(input("ยาว"))
        break
    except ValueError:
        print("Please try again.")

area = x * y
perimeter = (2*x) + (2*y)

if x == y:
    print(f"  {y}")
    print("*" * 5)
    print(f"*   *{x}")
    print("*" * 5)
    z = "สี่เหลี่ยมจัตุรัส"
elif y < x or x < y:
    print(f"  {y}")
    print("*" * 7)
    print(f"*     *{x}")
    print("*" * 7)
    z = "สี่เหลี่ยมผืนผ้า"

print(f"พื้นที่ : {area} ความยาวรอบรูป : {perimeter} และเป็นรูป{z}")