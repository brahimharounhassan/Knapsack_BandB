
import os, sys
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

ROOT_DIR = os.path.abspath(os.curdir)
TEST_DATA = os.path.join(ROOT_DIR.split("scripts")[0],"data/")

class Object:
    """
    Cette classe répresente un objet avec avec son poids, sa valeur et sa density

    weight (float): Le poids de l'objet
    value (float): La valeur de l'objet.
    density (float): La densité dde l'objet
    
    """
    def __init__(self, name, weight, value, density):
        self.name = name
        self.weight = weight
        self.value = value
        self.density = density 

def fractional_solution(rest_capacity, objects):
    """
    Cette fonction permet de calculer le borne supérieur.

    rest_capacity: La capacité restante du sac.
    objects: La ilste des objets non encore explorer.

    """
    total_value = 0

    for object in objects:
        if rest_capacity >= object.weight:
            rest_capacity -= object.weight
            total_value += object.value
        else:
            total_value += object.density * rest_capacity
            break

    return total_value

def bandb(capacity, objects):
    """
    Cette fonction consiste à trouver la meilleur combinaison des objets respectant les contraintes en utilisant 
    l'algo du Branch-and-Bound.

    capacity: La capacité max du sac à ne pas exceder.
    objects: La liste des tous les objets.
    """

    best_value = 0
    best_solution = []

    tree = []
    tree.append((0, 0, capacity, [])) 

    while tree:
        deep, current_value, rest_capacity, selected_objects = tree.pop()

        if deep >= len(objects):
            if current_value > best_value:
                best_value = current_value
                best_solution = selected_objects
            continue

        current_object = objects[deep]

        if current_object.weight <= rest_capacity:
            tree.append((
                deep + 1,
                current_value + current_object.value,
                rest_capacity - current_object.weight,
                selected_objects + [current_object.name]
            ))

        # ub = v + (W-w)*(v_i+1/w_i+1)
        upper_bound = current_value + fractional_solution(rest_capacity, objects[deep+1:])

        if upper_bound > best_value:
            tree.append((deep + 1, current_value, rest_capacity, selected_objects))

    return best_value, best_solution


def get_data(filename):
    """
    Cette fonction permet de lire les données fournies (sac0, sac1, ....) et les triées par densité decroissante.

    filename: Le chemin du fichier.
    """
    objects = []
    total_weight = None
    with open(filename, 'r') as f:
        data = f.readlines()
        total_weight = int(data[0].strip())
        for idx, val in enumerate(data[1:]):
            if len(val) > 1:
                weight = int(val[:-1].strip().split(" ")[0])
                value = int(val[:-1].strip().split(" ")[1])
                density = value / weight
                name = 'obj_' + str(idx)
                objects.append(Object(name, weight, value, density))
    objects.sort(key=lambda x : x.density, reverse=True)
    return total_weight, objects


if __name__ == "__main__":
    if "sac" in sys.argv[-1]:
        fname = sys.argv[-1]+".txt"
    else:
        fname = "sac0.txt"  
    
    filename = os.path.join(TEST_DATA,fname)
    capacity, objects = get_data(filename)

    best_value, best_combination = bandb(capacity, objects)
    best_combination = [obj for obj in objects if obj.name in best_combination]
    best_combination.sort(key=lambda x: int(x.name.strip().split('_')[-1]))
    max_capacity = 0
    
    print()
    logger.info("Objets sélectionnés :")
    for obj in best_combination:
        logger.info(f"{obj.name} - poids: {obj.weight}g ; valeur: {obj.value}")
        max_capacity += obj.weight
    logger.info(f"Capacité du sac : {capacity} / Capacité de la selection: {max_capacity}")
    logger.info(f"Valeur maximale obtenue : {best_value}")
    print()
    