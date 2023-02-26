# multipliers from mods and status ticks
bane_of_grineer= 0.3
primed_bane_of_grineer = 0.55
serration = 1.65
slash_tick = 0.35
heat_tick = 0.5
electric_tick = 0.5
toxin_tick = 0.5
gas_tick = 0.5

# faction = (1 + 0.55)**2
# print(faction)

#damage totals
base_damage = 0
damage_mods = 0
elemental_damage_mods = 0
strength_mods = 0
status_tick = 0
double_dip = 0

#damage calculations
damage_total = round( base_damage * (1 + damage_mods) * (1 + primed_bane_of_grineer))

status_tick = slash_tick * (1 + damage_total) * (1 + primed_bane_of_grineer)

double_dip_multipler= (1 + primed_bane_of_grineer)**2

print(damage_total)
print(status_tick)
print(double_dip)


'''
    Modded Damage = 100 × (1 + 1.65) × (1 + 0.3) = 344.5
    Tick damage = 0.35 × 344.5 × (1 + 0.3) = 156.7475

As can be seen in the above calculations for tick damage, Faction Damage is applied twice, making their effective bonus = (1+Faction Bonus)^2. Which is +69% for the 30% Faction Damage mods and +140.25% for the 55% Primed Faction Damage mods. 
'''


