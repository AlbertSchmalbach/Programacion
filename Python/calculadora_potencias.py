def potencia_r(base,exp):
  if exp==0:
    return 1
  if exp==1:
    return base
  else: 
    return base * potencia_r(base,exp-1)