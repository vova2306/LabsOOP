class IndexValueError(KeyError):
    def __init__(self, ern, mes):
        super().__init__()
        self.ern = ern
        self.mes = mes

    def __str__(self):
        return str(self.mes)

class DictIntFloat:
    def __init__(self, mn=None):
        if isinstance(mn, dict):
            for key, value in mn.items():
                if not isinstance(key, int) and not isinstance(value, (int, float)):
                    raise IndexValueError("IndexValueError:", "Ключ не є цілочисельним і значення не є ціло- чи дробовочисельним!")
                if not isinstance(key, int):
                    raise IndexValueError("IndexValueError:", "Ключ не є цілочисельним!")
                if not isinstance(value, (int, float)):
                    raise IndexValueError("IndexValueError:", "Значення не є ціло- чи дробовочисельним!")
            self.mn = mn
        elif mn is None:
            self.mn = {}
        else:
            raise TypeError

    def __setitem__(self, key, value):
        if not isinstance(key, int) and not isinstance(value, (int, float)):
            raise IndexValueError("IndexValueError:", "Ключ не є цілочисельним і значення не є ціло- чи дробовочисельним!")
        if not isinstance(key, int):
            raise IndexValueError("IndexValueError:", "Ключ не є цілочисельним!")
        if not isinstance(value, (int, float)):
            raise IndexValueError("IndexValueError:", "Значення не є ціло- чи дробовочисельним!")
        self.mn[key] = value

    def __str__(self):
        return str(self.mn)

class Polynom(DictIntFloat):
    def __init__(self, mn=None):
        if isinstance(mn, Polynom):
            self.mn = mn.mn
        else:
            DictIntFloat.__init__(self, mn)
        self.mn = self.delzeros()

    def fileinputpolynom(self, fi):
        f=open(fi)
        for l in f:
            i,j=map(float, l.split())
            self.mn[i]=j
        f.close()
        self.mn=self.delzeros()

    def delzeros(self, mn=None):
        if mn is None:
            mn=self.mn
        u={i:mn[i] for i in mn if mn[i]!=0}
        if len(u)==0:
            u[0]=0
        return u

    def __add__(self, a):
        u=copy.deepcopy(self.mn)
        if isinstance(a, (float, int)):
            if 0 in u:
                u[0]+=a
                return Polynom(self.delzeros(u))
            else:
                u[0]=a
                return Polynom(self.delzeros(u))
        elif isinstance(a, Polynom):
            u.update(a.mn)
            new_mn={i:self.mn.get(i, 0)+a.mn.get(i, 0) for i in u}
            return Polynom(self.delzeros(new_mn))
        else:
            raise TypeError('Операція не має сенсу.')

    def __sub__(self, a):
        u=copy.deepcopy(self.mn)
        if isinstance(a, (float, int)):
            if 0 in u:
                u[0]-=a
                return Polynom(self.delzeros(u))
            else:
                u[0]=-a
                return Polynom(self.delzeros(u))
        elif isinstance(a, Polynom):
            u.update(a.mn)
            new_mn={i:self.mn.get(i, 0)-a.mn.get(i, 0) for i in u}
            return Polynom(self.delzeros(new_mn))
        else:
            raise TypeError('Операція не має сенсу.')

    def __mul__(self, a):
        u={}
        if isinstance(a, (float, int)):
            for i in self.mn:
                u[i]=self.mn[i] *a
            return Polynom(self.delzeros(u))
        elif isinstance(a, Polynom):
            for k in self.mn:
                for l in a.mn:
                    u[k+l]=u.get(k+l, 0)+self.mn[k]*a.mn[l]
            return Polynom(self.delzeros(u))
        else:
            raise TypeError('Операція не має сенсу.')

    def __call__(self, x):
        return sum([self.mn[i]*x**i for i in self.mn])

    def __getitem__(self, l):
        try:
            return self.mn[l]
        except KeyError:
            return None

    def derivpolynom(self, n=1):
        u=copy.deepcopy(self.mn)
        for i in range(n):
            u={i-1:u[i]*i for i in u if i!=0}
        return self.delzeros()


    def set(self, i, j):
        self.mn[i]=j
        self.mn=self.delzeros()

    def __str__(self):
        ls=[str(self.mn[i])+'*x**'+str(i) for i in sorted(self.mn, reverse=True) if self.mn[i]!=0]
        s=' + '.join(ls)
        return s

import copy
if __name__=='__main__':
    try:
        mn1 = Polynom({'a': 4, 9: 4, 3: 5, 4: 3.5, 5: 2, 7: 1, 11: 0, 0: 2})
        mn2 = Polynom({12: 9, 11: 'a', 4: 3, 6.5: 2, 2: 1, 13: 0})
        out=mn1+mn2*mn1*mn2-mn1
        print('Многочлени:')
        print('P1 =', mn1)
        print('P2 =', mn2)
        print('\nРезультат виразу p1+p2*p1*p2-p1:\nP = '+str(out)+'\n')
    except IndexValueError as exc:
        print(exc.ern, exc.mes, '\n')
    try:
        mn1 = Polynom({10: 4, 9: 4, 3: 5, 4: 0, 5: 2, 7: 1, 11: 0, 0: 2})
        mn2 = Polynom({12: 9, 11: 4, 4: 3, 8: 2, 2: 1, 13: 0})
        out=mn1+mn2*mn1*mn2-mn1
        print('Многочлени:')
        print('P1 =', mn1)
        print('P2 =', mn2)
        print('\nРезультат виразу p1+p2*p1*p2-p1:\nP = '+str(out)+'\n')
    except IndexValueError as exc:
        print(exc.ern, exc.mes, '\n')
