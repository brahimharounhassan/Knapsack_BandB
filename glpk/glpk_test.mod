set OBJETS;

param poids{OBJETS};
param valeur{OBJETS};
param masse_sac;

var x{OBJETS}, binary;

maximize grande_valeur_possible:
    sum{i in OBJETS} valeur[i] * x[i];

subject to masse_total_sac:
    sum{i in OBJETS} poids[i] * x[i] <= masse_sac;

data;

end;

