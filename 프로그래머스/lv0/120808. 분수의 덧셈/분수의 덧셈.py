from fractions import Fraction

def solution(numer1, denom1, numer2, denom2):
    answer = []

    sumValue = Fraction(numer1,denom1) + Fraction(numer2, denom2)
    answer.append(sumValue.numerator)
    answer.append(sumValue.denominator)
    
    
    return answer