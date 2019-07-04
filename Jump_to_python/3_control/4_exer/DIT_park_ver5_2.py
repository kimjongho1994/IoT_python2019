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

info_dictionary = {"����":0,"���":2000,"û�ҳ�":3000,"����":5000,"����":0}
coupons = {"���� Ƽ��":5, "���� Ƽ��":3}
customer_counter = 0
is_perchased = False

while True:
    print(infomation)
    customer_age = int(input("���̸� �Է��ϼ���.")) 
    if customer_age in range(0, 4):
        customer_level = '����'
    elif customer_age in range(4, 14):
        customer_level = '���'
    elif customer_age in range(14, 19):
        customer_level = 'û�ҳ�'
    elif customer_age in range(19, 66):
        customer_level = '����'
    elif customer_age >=66:
        customer_level = '����'
    else:
        print("�ٽ� �Է��ϼ���\n")
        continue
    print("\n���ϴ� {0}����̸� ����� {1}�� �Դϴ�.".format(customer_level, info_dictionary[customer_level]))
    cashOrCredit = int(input("\n��� ������ �����ϼ���. (1: ����, 2: ���� ���� �ſ�ī��)"))
    if cashOrCredit == 1:
        checkIn = int(input("\n����� �Է��ϼ���."))
        if checkIn < info_dictionary[customer_level]:
            print("\n%d���� ���ڶ��ϴ�. �Է��Ͻ� %d���� �ݳ��մϴ�." % (((info_dictionary[customer_level]) - checkIn), checkIn))
        else:
            is_perchased = True
            if checkIn == info_dictionary[customer_level]:
                print("\n�����մϴ�. Ƽ���� �����մϴ�.")
            else:
                print("\n�����մϴ�. Ƽ���� �����ϰ� �Ž����� %d���� ��ȯ�մϴ�." % (checkIn - (info_dictionary[customer_level])))
    elif cashOrCredit == 2:
        is_perchased = True
        credit_pay = info_dictionary[customer_level] * 0.9
        if customer_age in range(60, 66):
            credit_pay *= 0.95
        print("\n%.0f�� ���� �Ǿ����ϴ�. Ƽ���� �����մϴ�." % (credit_pay))

    if is_perchased and customer_level not in ['����', '����']:
        customer_counter += 1
        print("\n%d��° ��" % customer_counter)
        if customer_counter % 7 == 0 and coupons["���� Ƽ��"] != 0:
            coupons["���� Ƽ��"] = coupons["���� Ƽ��"] - 1
            print("\n�����մϴ�. 1�ֳ� �̺�Ʈ�� ��÷�Ǿ����ϴ�. ���� ���� Ƽ���� �����մϴ�. �ܿ� ����Ƽ�� %d��" % coupons["���� Ƽ��"])
        elif customer_counter % 4 == 0 and coupons["���� Ƽ��"] != 0:
            coupons["���� Ƽ��"] = coupons["���� Ƽ��"] - 1
            print("\n�����մϴ�. ����ȸ���� ���� �̺�Ʈ�� ��÷�Ǽ̽��ϴ�. ���� ȸ�� ���� Ƽ���� �����մϴ�. �ܿ� ����Ƽ�� %d��" % coupons["���� Ƽ��"])
        is_perchased = False
