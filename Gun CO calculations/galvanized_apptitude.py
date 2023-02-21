#additive with other mods on your weapon and is not applied on following hits and not instant status porocs
bass_damage = 0
unique_procs = 0
bonus_proc_damage =  unique_procs * 0.4
damage_mods = 0

#simple damagae calculation
total_damage =  round(bass_damage * (1 + damage_mods + bonus_proc_damage), 1)
print(total_damage)