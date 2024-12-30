# A) Diferencia en portcentaje entre el curso actual y:

    # - el mas rapido de otros cursos
    # - el mas lento de otros cursos
    # - el promedio de los cursos
    
#Promedio de duaracion
otros_cursos_min = 2.5
otros_cursos_max = 7
otros_cursos_promedio = 4
dalto_curso = 1.5

# Duracion de crudos
crudo_promedio = 5
crudo_dalto = 3.5



# Diferencia de duracion
diferencia_con_min = 100 - (dalto_curso / otros_cursos_min * 100);
print(f'El curso de Dalto dura un {diferencia_con_min}% menos que el mas rapido')

# el mas lento
diferencia_con_max = 100 - (dalto_curso  * 1000 // otros_cursos_max / 10);
print(f'El curso de Dalto dura un {diferencia_con_max}% menos que el mas lento')

# el promedio
diferencia_con_promedio = 100 - (dalto_curso / otros_cursos_promedio * 100);
print(f'El curso de Dalto dura un {diferencia_con_promedio}% menos que el promedio')
print('----------')
    
# B) Porcentaje de material inservible que se reduce en:

# - el promedio de los cursos
crudo_promedio_diff = 100 - otros_cursos_promedio / crudo_promedio * 100;

print(f'El crudo promedio es de: {crudo_promedio_diff}%')    
  
    
 # - el curso actual ( este curso) 
crudo_promedio_dalto = 100 - dalto_curso * 1000 // crudo_dalto / 10;
print(f'El crudo promedio de dalto es de: {crudo_promedio_dalto}%')  
print('----------')
 
# C) ver 10 horas de este curso a cuantas horas de otros cursos equivale? y al reves?
print(f'ver 10 horas de este curso equivale a ver {otros_cursos_promedio * 100 // dalto_curso /10} horas de otros')
print(f'ver 10 horas de otros cursos equivale a ver {dalto_curso * 100 // otros_cursos_promedio /10} horas de este curso')

