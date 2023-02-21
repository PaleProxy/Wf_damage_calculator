# Stats from mods in percentages
base_damage = 0
damage_mods = 0
elemental_damage_mods = 0
strength_mods = 0

#optional damage increase not sure if multiplicative or additive
combo_multiplier = 0.25

damage_total = round(base_damage * (1 + damage_mods) * (1 + elemental_damage_mods) * (1 + strength_mods), 1)
print(damage_total)

#mass vitrify stack amount
mass_vitrify_amount = 0.5 * damage_total
print(round(mass_vitrify_amount, 1))