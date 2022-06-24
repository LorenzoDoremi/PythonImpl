from numpy import power

# algoritmo per trovare il numero di reti e sottoreti di un IPV4 data una MASK CIDR
def subnetCalc(a,b,c,d,mask):

    bits = 32
    if a <=126:
      bits = 8
    if a >= 128 and a <= 191:
      bits = 16
    if a >= 192 and a <= 223:
      bits = 24

    subnets = power(2, mask-bits)
    hosts_per_subnet = power(2, 32 - mask) - 2;
    
    print(subnets)
    print(hosts_per_subnet)
    print(hosts_per_subnet * subnets)
    
    


subnetCalc(192,168,2,0, 26)




      