Cr = int(input("Enter Crit% : "))
CrR = int(input("Enter Crit_Resistance% : "))
Cd = int(input("Enter Crit_Dmg% : "))
CdR = int(input("Enter Crit_Dmg_Resistance% : "))
Atk = int(input("Enter atk : "))
BA = int(input("Enter Brocken_Armor : "))
DI = int(input("Enter Dmg immune : "))
Armor = int(input("Enter Armor : "))



# P = Broken armor - Enemy_DI, P is capped at 1 and  P = 0 if enemy_DI > broken armor.
# a = the attack power as shown in the stats page of the hero 
# x = crit - enemy crit resistance, it is 0 if crit < CR, x cant be higher than 160%.
# y = crit dmg - enemy crit dmg resistance,  0 if cd < cdr
# T = skill damage multiplier, for example generals main skill level 1 is 260% the damage, 260% being the multiplier.


# Basic attack no crit:
# raw damage = a * (1 + P)

# Basic attack crit: 
# raw damage = a(1 + P)(1 + x + xy)

# Skill attack damage no crit:
# raw damage = a(1 + A)(1 + P)(T + J)

# Skill attack damage when crit:
# raw damage = a(1 + A)(1 + P)(T + J)(1 + x + xy)

P = BA - DI
x = Cr - CrR
y = Cd - CdR

# Crit_Frml = (1+Cr-CrR+(Cr-CrR)+(Cd-CdR))
Crit_Frml = (1+x+(x)+(y))

dmg11 = Atk*(1+P)
dmg12 = dmg11*Crit_Frml
print(dmg11)
print(dmg12)