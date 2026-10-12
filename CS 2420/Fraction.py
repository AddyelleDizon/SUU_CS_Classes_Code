def gcd(m, n):
    while m % n != 0:
        m, n = n, m % n
    return n

class Fraction:
    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom

        if not isinstance(top, int) or not isinstance(bottom, int):
            raise TypeError("Numerator and denominator must be integers")
        if bottom == 0:
            raise ValueError("Denominator cannot be zero")
        
        commonden = gcd(top, bottom)
        self.num = top // commonden
        self.den = bottom // commonden

    def __str__(self):
        return "{:d}/{:d}".format(self.num, self.den)

    def __eq__(self, other_fraction):
        first_num = self.num * other_fraction.den
        second_num = other_fraction.num * self.den
        return first_num == second_num
  
    def __add__(self, other_fraction):
        # adding fractions, (a/b)+(c/d)=(ad-bc)/bd
        new_num = self.num * other_fraction.den + self.den * other_fraction.num
        new_den = self.den * other_fraction.den
        cmmn = gcd(new_num, new_den)
        return Fraction(new_num // cmmn, new_den // cmmn)

    def show(self):
        print("{:d}/{:d}".format(self.num, self.den))
#Homework    
    def get_num(self):
        return self.num

    def get_den(self):
        return self.den

    def __sub__(self, other_fraction):
        # for subtracting fractions, (a/b)-(c/d)=(ad-bc)/bd
        new_num = self.num * other_fraction.den - self.den * other_fraction.num 
        new_den = self.den * other_fraction.den
        cmmn = gcd(new_num, new_den)
        return Fraction(new_num//cmmn, new_den//cmmn)

    def __mul__(self, other_fraction):
        # for multiplying fractions, (a/b)*(c/d)=(ac)/(bd)
        new_num = self.num * other_fraction.num
        new_den = self.den * other_fraction.den
        cmmn = gcd(new_num, new_den)
        return Fraction(new_num//cmmn, new_den//cmmn)

    def __truediv__(self, other_fraction):
        # for dividing fractions, (a/b)/(c/d)=(a/b)*(d/c)
        new_num = self.num * other_fraction.den
        new_den = self.den * other_fraction.num
        cmmn = gcd(new_num, new_den)
        return Fraction(new_num//cmmn, new_den//cmmn)

    def __gt__(self, other_fraction):
        # for finding greater than (>), the first fraction must be greater than the second
        # (a/b) > (c/d); since fractions can be turned into decimals, if left_dec > right_dec, return true
        left_num = self.num / self.den
        right_num = other_fraction.num / other_fraction.den
        if left_num > right_num:
            return True
        else:
            return False

    def __ge__(self, other_fraction):
        # for finding greater than or equal to(>=), the first fraction must be greater than (or equal to) the second
        # (a/b) >= (c/d); since fractions can be turned into decimals, if left_dec > right_dec, and/or left_dec == right_dec return true
        left_num = self.num / self.den
        right_num = other_fraction.num / other_fraction.den
        if left_num >= right_num:
            return True
        else:
            return False
        
    def __lt__(self, other_fraction):
        # for finding less than (>), the first fraction must be lesser than the second
        # (a/b) < (c/d); since fractions can be turned into decimals, if left_dec < right_dec
        left_num = self.num / self.den
        right_num = other_fraction.num / other_fraction.den
        if left_num < right_num:
            return True
        else:
            return False

    def __le__(self, other_fraction):
        # for finding lesser than (<=), the first fraction must be lesser than the second
        # (a/b) <= (c/d); since fractions can be turned into decimals, if left_dec < right_dec, and/or left_dec == right_dec return true
        left_num = self.num / self.den
        right_num = other_fraction.num / other_fraction.den
        if left_num <= right_num:
            return True
        else:
            return False

    def __ne__(self, other_fraction):
        # not equal to, neither fractions must be the same
        # (a/b) != (c/d); therefore, return true
        left_num = self.num / self.den
        right_num = other_fraction.num / other_fraction.den
        if left_num != right_num:
            return True
        else:
            return False
