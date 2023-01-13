def getMinSetPrice(setPriceArr):
    return min(setPriceArr)

def getMinSinglePrice(singlePriceArr):
    return min(singlePriceArr)

def getSingleAndSetPrice(count, singlePrice, setPrice):
    price = 0
    while(count >= 6):
        price += setPrice
        count -= 6
    price += singlePrice*count
        
    return price

def getSinglePrice(count, singlePrice):
    return count * singlePrice

def getSetPrice(count, setPrice):
    price = 0
    while(count > 0):
        price += setPrice
        count -= 6
    return price



n,m = map(int,input().split())
setPriceArr = list()
singlePriceArr = list()
for _ in range(m):
    setPrice, singlePrice = map(int,input().split())
    setPriceArr.append(setPrice)
    singlePriceArr.append(singlePrice)

minSetPrice = getMinSetPrice(setPriceArr)
minSinglePrice = getMinSinglePrice(singlePriceArr)

singleAndSetPrice = getSingleAndSetPrice(n,minSinglePrice,minSetPrice)
singlePrice = getSinglePrice(n, minSinglePrice)
setPrice = getSetPrice(n, minSetPrice)

print(min({singleAndSetPrice,singlePrice,setPrice}))