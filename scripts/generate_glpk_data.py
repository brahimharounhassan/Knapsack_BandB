import os

ROOT_DIR = os.path.abspath(os.curdir)

TEST_DATA = os.path.join(ROOT_DIR.split("scripts")[0],"data/")
GLPK_DATA = os.path.join(ROOT_DIR.split("scripts")[0],"glpk/data/")

def create_glpk_data(filename: str):
    fname = "sac"+filename.split(f"sac")[-1].replace("txt","dat")
    total_weight = None
    weights, values, objects = [], [], []
    with open(filename, 'r') as f:
        data  = f.readlines()
        total_weight = int(data[0])
        for i, val in enumerate(data[1:]):
            if len(val) > 1:    
                weight = int(val[:-1].strip().split(" ")[0])
                weights.append(weight)
                value = int(val[:-1].strip().split(" ")[1])
                values.append(value)
                objects.append(f"obj_{i+1}")
                
    with open(os.path.join(GLPK_DATA,fname), 'w') as f:
        f.write("data;\n\n")
        f.write("set OBJETS := ")
        for i in objects:
            f.write(i+" ")
        f.write(';\n\n')
        f.write("param poids :=\n")
        
        for i, j in zip(objects, weights):
            f.write('\t' + i + '\t' + str(j) + '\n')
        f.write(';\n\nparam valeur :=\n')
        for i, j in zip(objects, values):
            f.write('\t' + i + '\t' + str(j) + '\n')
        f.write(f';\n\nparam masse_sac := {total_weight};\n\nend;')  
        
        
for i in range(5):
    create_glpk_data(os.path.join(TEST_DATA,f"sac{i}.txt"))