# coding: cp949
infomation = """
====I N F O M A T I O N====
  0 ~ 3��(��  ��): ����
 4 ~ 13��(���): 2000��
14 ~ 18��(û�ҳ�): 3000��
19 ~ 65��(��  ��): 5000��
66�� �̻�(��  ��): ����
===========================
"""

info_dictionary = {0:[0, "����"],1:[2000, "���"],2:[3000, "û�ҳ�"],3:[5000, "����"],4:[0, "����"]}

customer_age = -1

while True:
    print(infomation)
    customer_age = int(input("���̸� �Է��ϼ���.")) 
    if customer_age >=0 and customer_age <= 3:
        customer_level = 0
    elif customer_age >=4 and customer_age <= 13:
        customer_level = 1
    elif customer_age >=14 and customer_age <= 18:
        customer_level = 2
    elif customer_age >=19 and customer_age <= 65:
        customer_level = 3
    elif customer_age >=66:
        customer_level = 4
    else:
        print("�ٽ� �Է��ϼ���\n")
        continue
    print("���ϴ� {0}����̸� ����� {1}�� �Դϴ�.\n".format(info_dictionary[customer_level][1], info_dictionary[customer_level][0]))

    checkIn = int(input("����� �Է��ϼ���."))
    if checkIn < info_dictionary[customer_level][0]:
        print("%d���� ���ڶ��ϴ�. �Է��Ͻ� %d���� �ݳ��մϴ�." % ((((info_dictionary[customer_level][0]) - checkIn), checkIn)))
    else:
        if checkIn == info_dictionary[customer_level][0]:
            print("�����մϴ�. Ƽ���� �����մϴ�.")
        else:
            print("�����մϴ�. Ƽ���� �����ϰ� �Ž����� %d���� ��ȯ�մϴ�." % ((checkIn - (info_dictionary[customer_level][0]))))

