class Employee:
    def __init__(self, ids, name_sname, base, st, status):
        self.ids = ids
        self.name = name_sname
        self.base = float(base)
        self.st = int(st)
        self.status = status

    def calculateSalary(self):
        return self.base


class Ingener_Programist(Employee):
    def __init__(self, ids, name_sname, base, st, status, G, Y):
        self.Y = int(Y)-int(st)
        self.G = int(G)
        Employee.__init__(self, ids, name_sname, base, st, status)

    def calculateSalary(self):
        return float(self.G*self.base*((self.Y/10)+1))

    def employees_ids(self):
        return str(self.ids)


class Others(Employee):
    def __init__(self, ids, name_sname, base, st, status, Y):
        self.Y = int(Y)-int(st)
        Employee.__init__(self, ids, name_sname, base, st, status)

    def calculateSalary(self):
        return float((self.base*(10+(self.Y//3)))/10)



class Testers(Employee):
    def __init__(self, ids, name_sname, base, st, status, Y):
        self.Y = int(Y)-int(st)
        Employee.__init__(self, ids, name_sname, base, st, status)

    def calculateSalary(self):
        return float(self.base*(1+(self.Y/5)))



class HRD(Employee):
    def __init__(self, ids, name_sname, base, st, status, Y):
        self.Y = int(Y)-int(st)
        Employee.__init__(self, ids, name_sname, base, st, status)

    def calculateSalary(self):
        return float(self.base*(1+(self.Y/6)))



def alls(emp, tY):
    temp1=0
    temp2=0
    temp02=0
    temp3=0
    temp01=0
    for k in range(int(input('Кількість працівників типу {}: '.format(emp.__name__)))):
        temp4=input("{}-й працівник. Введіть наступні параметри - ІПН, ім'я, базову ставку, рік у якому почав роботу, статус{}: ".format(k+1, ', рівень' if emp.__name__ == 'Ingener_Programist' else ''))
        temp5=temp4
        temp4=temp4.split()
        temp4.append(tY)
        f=open('emp.txt', 'a', encoding='UTF-8')
        f.write(temp5+'\n')
        f.close()
        f=open('empbill.txt', 'a', encoding='UTF-8')
        temp0=emp(*temp4[:3], *temp4[3:])
        sal=temp0.calculateSalary()
        temp1+=float(sal)
        temp2+=float(sal)*0.18
        if temp0.status == 'звичайний':
            temp02+=int(sal)*0.22
            h=float(sal)*0.22
        elif temp02.status == 'інвалід':
            temp02+=int(sal)*0.0841
            h=float(sal)*0.0841
        temp3+=float(sal)*0.015
        temp01+=float(sal)-h-float(sal)*0.015-float(sal)*0.18
        f.write(str(k+1)+'. '+str(temp4[0])+' '+str(temp4[1])+' '+str(float(sal)*0.18)+' '+str(float(sal)*0.015)+' '+str(float(sal)-h-float(sal)*0.015-float(sal)*0.18)+' '+str(h)+'\n')
        f.close()
    return temp1, temp2, temp02, temp3, temp01


if __name__ == '__main__':
    f=open('emp.txt', 'w', encoding='UTF-8')
    f.write('Список працівників компанії:\n')
    f.close()
    f=open('empbill.txt', 'w', encoding='UTF-8')
    f.write('Розрахункова відомість про працівників:\n==============================================================\n'+"ІПН   Ім'я   ПДФО   В.збір   до виплати   нарах. ЄСВ\n==============================================================\n")
    f.close()
    suma, nal, sumaall=0, 0, 0
    emp=[Ingener_Programist, Testers, HRD, Others]
    tY=int(input("Який зараз рік? - "))
    for k in emp:
        temp=alls(k, tY)
        suma+=temp[0]
        nal+=temp[1]+temp[2]+temp[3]
        sumaall+=temp[4]
    print('Видатки по ЗП = '+str(round(suma, 2)))
    print('Податки з ЗП працівників і нарахувань підприємства = '+str(round(nal, 2)))
    print('Виплати працівникам "на руки" компанії = '+str(round(sumaall, 2)))
    f=open('empbill.txt', 'a', encoding='UTF-8')
    f.write('==============================================================\n                        Разом:  '+str(temp[1])+' '+str(temp[3])+' '+str(temp[4])+' '+str(temp[2]))
    f.close()