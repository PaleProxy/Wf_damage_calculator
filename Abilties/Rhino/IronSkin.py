modified_health = 0
base_health = 1200
base_armor = 653
armor_multiplier = 8.1
armor_mods = 1.375
ability_strength =3.2
absorbed_damage = 0

#parastitc?
parasitic_multiplier = 3.2
shields = 1100
parasitic_armor = parasitic_multiplier * shields

modified_health = (base_health + (armor_multiplier * base_armor * (1 + armor_mods) + parasitic_armor)) * (1 + ability_strength) + absorbed_damage
print(modified_health)