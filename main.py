

from importQuery import ExecuteSQL



arr_bd = [
    "siprem_prueba_almacen"
    # "siprem_vatia_formacion",	
    # "siprem_vatia_ae",	
    # "siprem_vatia_tsi",	
    # "siprem_vatia_ele",	
    # "siprem_vatia_sie",	
    # "siprem_vatia_selco",	
    # "siprem_vatia_sepc",	
    # "siprem_vatia_green",	
    # "siprem_vatia_ab",	
    # "siprem_vatia_dz",	
    # "siprem_vatia_dtsj",	
    # "siprem_vatia_ness",	
    # "siprem_vatia_aci",	
    # "siprem_vatia_tev",	
    # "siprem_vatia_c2i",	
    # "siprem_vatia_cgms",	
    # "siprem_vatia_c3i",	
    # "siprem_vatia_drt",	
    # "siprem_vatia_tvcgm",	
    # "siprem_vatia_semsi",	
    # "siprem_vatia_soling",	
    # "siprem_vatia_hitta",	
    # "siprem_vatia_mont",	
    # "siprem_vatia_trabel"
]



if __name__ == "__main__":

    sql = ExecuteSQL()

    sql.execute_query_file(arr_bd)



