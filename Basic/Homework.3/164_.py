import math

n = int(input("n = ")) # tiv, vori qarakusin eranish tiv e

if n > 10 and n < 32:
    """[n > 10] <=> n tivy mec e amenapoqr eranish tvi qarakusi armatic"""
    """[n < 32] <=> n tivy poqr e amenamec eranish tvi qarakusi armatic"""
    print(int(math.pow(n + 1, 2)))
else:
    print("nermucel [11; 31] mijakayqin patkanox 'n' tiv")