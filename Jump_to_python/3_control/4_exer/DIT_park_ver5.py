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
#info_dictionary = {"����":0,"���":2000,"û�ҳ�":3000,"����":5000,"����":0}
coupons = {0:[5, "���� Ƽ��"], 1:[3, "���� Ƽ��"]}
customer_counter = 0
is_perchased = False

while True:
    print(infomation)
    customer_age = int(input("���̸� �Է��ϼ���.")) 
    if customer_age in range(0, 4):
        customer_level = 0
#        customer_level = '����'
    elif customer_age in range(4, 14):
        customer_level = 1
    elif customer_age in range(14, 19):
        customer_level = 2
    elif customer_age in range(19, 66):
        customer_level = 3
    elif customer_age >=66:
        customer_level = 4
    else:
        print("�ٽ� �Է��ϼ���\n")
        continue
    print("\n���ϴ� {0}����̸� ����� {1}�� �Դϴ�.".format(info_dictionary[customer_level][1], info_dictionary[customer_level][0]))
    cashOrCredit = int(input("\n��� ������ �����ϼ���. (1: ����, 2: ���� ���� �ſ�ī��)"))
    if cashOrCredit == 1:
        checkIn = int(input("\n����� �Է��ϼ���."))
        if checkIn < info_dictionary[customer_level][0]:
            print("\n%d���� ���ڶ��ϴ�. �Է��Ͻ� %d���� �ݳ��մϴ�." % (((info_dictionary[customer_level][0]) - checkIn), checkIn))
        else:
            is_perchased = True
            if checkIn == info_dictionary[customer_level][0]:
                print("\n�����մϴ�. Ƽ���� �����մϴ�.")
            else:
                print("\n�����մϴ�. Ƽ���� �����ϰ� �Ž����� %d���� ��ȯ�մϴ�." % (checkIn - (info_dictionary[customer_level][0])))
    elif cashOrCredit == 2:
        is_perchased = True
        credit_pay = info_dictionary[customer_level][0] * 0.9
        if customer_age in range(60, 66):
            credit_pay *= 0.95
        print("\n%.0f�� ���� �Ǿ����ϴ�. Ƽ���� �����մϴ�." % (credit_pay))

    if is_perchased and customer_level != 0 and customer_level != 4:
        customer_counter += 1
        if customer_counter % 7 == 0 and coupons[0][0] != 0:
            coupons[0][0] = coupons[0][0] - 1
            print("\n�����մϴ�. 1�ֳ� �̺�Ʈ�� ��÷�Ǿ����ϴ�. ���� ���� Ƽ���� �����մϴ�. �ܿ� ����Ƽ�� %d��" % coupons[0][0])
        elif customer_counter % 4 == 0 and coupons[1][0] != 0:
            coupons[1][0] = coupons[1][0] - 1
            print("\n�����մϴ�. ����ȸ���� ���� �̺�Ʈ�� ��÷�Ǽ̽��ϴ�. ���� ȸ�� ���� Ƽ���� �����մϴ�. �ܿ� ����Ƽ�� %d��" % coupons[1][0])
        is_perchased = False
