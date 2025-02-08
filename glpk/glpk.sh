#!/bin/bash

if [[ -z "$1" ]]; then
  echo "Erreur : Veuillez fournir le nom du fichier 'sacx' en tant que paramètre."
  exit 1
fi

SAC_FILE="$1"  
MODEL_FILE="glpk_test.mod"
DATA_FILE="data/${SAC_FILE}.dat" 
OUTPUT_FILE="output/${SAC_FILE}.txt"  

if [[ ! -f $MODEL_FILE ]]; then
  echo "Erreur : Le fichier modèle '$MODEL_FILE' est introuvable."
  exit 1
fi

if [[ ! -f $DATA_FILE ]]; then
  echo "Erreur : Le fichier de données  '$DATA_FILE'  est introuvable."
  exit 1
fi

OUTPUT_DIR=$(dirname "$OUTPUT_FILE")
if [[ ! -d $OUTPUT_DIR ]]; then
  mkdir -p $OUTPUT_DIR
fi

echo "Exécution de GLPK avec le modèle  $MODEL_FILE, les données: $DATA_FILE, sortie: $OUTPUT_FILE"
glpsol --model $MODEL_FILE --data $DATA_FILE --output $OUTPUT_FILE


if [[ $? -eq 0 ]]; then
  echo "Exécution terminée avec succès. Consultez la solution dans '$OUTPUT_FILE'."
else
  echo "Erreur : L'exécution de GLPK a échoué."
  exit 2
fi

