# coding: cp949

service = """
   \\
  ( \\   ( (
  )  \\  ) )
==============
 \          /==
  \ coffee /   |
   \  ��  / ===
  ==========
"""

coffee = 10
money = 0
coffee_price = 300

while True:
    
    money = int(input("���� �־� �ּ���: "))
    if money >= coffee_price:
        if money > coffee_price:
            print("�Ž����� %d�� �帮��, " % (money - coffee_price), end = "")
        print("Ŀ�Ǹ� �帳�ϴ�.")
        print(service)
        coffee = coffee - 1
    else:
        print("���� �ٽ� �����ְ� Ŀ�Ǹ� ���� �ʽ��ϴ�.")
    
    print("���� Ŀ���� ���� %d�� �Դϴ�." % coffee)

    if coffee == 0:
        print("Ŀ�ǰ� �� ���������ϴ�. �ǸŸ� �����մϴ�.")
        break
