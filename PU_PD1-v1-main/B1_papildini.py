# ----------------------------------------------------------------------
# B1. Python — rindu skaits pa līmeņiem
# ----------------------------------------------------------------------

# Saskaiti, cik žurnālā ir rindu katram līmenim, un izvadi tos no biežākā uz retāko. Aizpildi abas vietas, kur stāv TODO.
#
# Aizpildi vietu, kur stāv TODO. Tad palaid.
# ----------------------------------------------------------------------                                                                                                Pirms saraksta izvadi tekstu "Limenu kopsavilkums".

skaits = {}

with open("sistema.log", encoding="utf-8") as f:
    for rinda in f:
        limenis = rinda.split()[2]

        if limenis in skaits:
            skaits[limenis] += 1
        else:
            skaits[limenis] = 1

print("Limenu kopsavilkums")

for limenis in skaits:
    print(limenis, skaits[limenis])
