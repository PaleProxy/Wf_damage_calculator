#Whipclaw base stats
whipclaw_crit_chance = 0.25
whipclaw_crit_multiplier = 2
whipclaw_status_chance = 0.2

#base damage distribution is distributed evenly 
slash_damage = 0.3
impact_damage = 0.3
puncture_damage = 0.3

# Base stats from mods in percentage
base_damage = 0
damage_mods = 0
elemental_mods = 0
strength_mods = 0

# status tick rate
status_tick_rate = 0.5 * (base_damage * (1 + damage_mods))

#combo maths
whipclaw_combo_multiplier = 0.25

#Ensnare multiplier
ensnare_multiplier = 2

#strangle dome distribution
strangle_dome_spread = 0.5

#final base damage calculation
damage_total = round(base_damage * (1 + damage_mods) * (1+ elemental_mods) * (1 +strength_mods), 1)
print(damage_total)
