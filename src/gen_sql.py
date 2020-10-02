import json                    
import os         
import sys
        
datafiles = sys.argv[1]

tables = [                 
     {"filename": "DEATH_CAUSE",
      "columns":[
           {"name": "PATID",      "levels": [ {"name": "GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG", "type": "id", "count": -1 } ] },
           ]     
      },                                                                                                                   
     # The DX column on the MED_ADMIN table  takes several hours on 93k patients                              
     {"filename": "MED_ADMIN",
          "columns":[
           {"name": "MEDADMINID",        "levels": [ {"name": "XXXXXXXXXX-XXX-A000000", "type":"id", "count": -1 } ] },
           {"name": "PATID",        "levels": [ {"name": "GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG", "type":"id", "count": -1 } ] },
           {"name": "ENCOUNTERID",  "levels": [ {"name": "GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG", "type":"id", "count": -1 } ] },
           {"name": "PRESCRIBINGID",      "levels": [ {"name": "000000000000", "type":"id", "count": -1 } ] },
           {"name": "MEDADMIN_PROVIDERID",      "levels": [ {"name": "00000000", "type":"id", "count": -1 } ] },
           {"name": "MEDADMIN_START_DATE", "levels": [ {"name": "YYYY-MM-DD 00:00:00", "type": "YMD", "count": -1 } ] },
           {"name": "MEDADMIN_STOP_DATE", "levels": [ {"name": "YYYY-MM-DD 00:00:00", "type": "YMD", "count": -1 } ] },
           {"name": "MEDADMIN_STOP_TIME", "levels": [ {"name": "00:00", "count": -1, "type": "HH:MM" } ] },
           {"name": "MEDADMIN_DOSE_ADMIN", "levels": [ {"name": "x.x", "count": -1, "type":"real" } ] },                        
           ]                                                                                                              
      },                                                                                                                        
     {"filename": "LAB_RESULT_CM",                                                                              
      "columns":[                                                                                              
           {"name": "LAB_RESULT_CM_ID",        "levels": [ {"name": "XXXXXXXXXX_XXXXXXXXXX_X", "type":"id", "count": -1 } ] },
           {"name": "PATID",        "levels": [ {"name": "GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG", "type":"id", "count": -1 } ] },
           {"name": "ENCOUNTERID",  "levels": [ {"name": "GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG", "type":"id", "count": -1 } ] },
           {"name": "LAB_ORDER_DATE", "levels": [ {"name": "YYYY-MM-DD 00:00:00", "type": "YMD", "count": -1 } ] },
           {"name": "SPECIMEN_DATE", "levels": [ {"name": "YYYY-MM-DD 00:00:00", "type": "YMD", "count": -1 } ] },
           {"name": "SPECIMEN_TIME", "levels": [ {"name": "00:00", "count": -1, "type": "HH:MM" } ] },               
           {"name": "RESULT_DATE", "levels": [ {"name": "YYYY-MM-DD 00:00:00", "type": "YMD", "count": -1 } ] },            
           {"name": "RESULT_TIME", "levels": [ {"name": "00:00", "count": -1, "type": "HH:MM" } ] },                        
           {"name": "RESULT_NUM", "levels": [ {"name": "x.x", "count": -1, "type":"real" } ] },                
           {"name": "NORM_RANGE_LOW", "levels": [ {"name": "x.x", "count": -1, "type":"real" } ] }, # xxx has empty strings
           {"name": "NORM_RANGE_HIGH", "levels": [ {"name": "x.x", "count": -1, "type":"real" } ] }, 
           {"name": "RAW_RESULT", "levels": [ {"name": "POSITIVE", "count": -1, "type":"text" } ] }, # this is a value but could be a string ('POSITIVE') so don't categorize it
           ]
      },
     {"filename": "DIAGNOSIS",
      "columns":[
           {"name": "DIAGNOSISID",      "levels": [ {"name": "GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG", "type":"id", "count": -1 } ] },
           {"name": "PATID",      "levels": [ {"name": "GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG", "type":"id", "count": -1 } ] },
           {"name": "ENCOUNTERID",      "levels": [ {"name": "GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG", "type":"id", "count": -1 } ] },
           {"name": "ADMIT_DATE", "levels": [ {"name": "YYYY-MM-DD 00:00:00", "type":"YMD", "count": -1 } ] },
           {"name": "PROVIDERID",      "levels": [ {"name": "00000000", "type":"id", "count": -1 } ] },                                    
           {"name": "DX_DATE", "levels": [ {"name": "YYYY-MM-DD 00:00:00", "type":"YMD", "count": -1 } ] }
           ]                                                                                           
      },    
     {"filename": "DISPENSING",
      "columns":[]          
      },           
     {"filename": "EXTRACT_VALIDATION",                                                                                            
      "columns":[]                                                                                                            
      },                                                                                                                      
     {"filename": "IMMUNIZATION",                                                                                  
      "columns":[]                                                                                    
      },                                                                                 
     {"filename": "PRO_CM",                                                              
      "columns":[]                                                                              
      },                                                                                       
     {"filename": "DEATH",                                                                         
      "columns":[
           {"name": "PATID",      "levels": [ {"name": "GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG", "type": "id", "count": -1 } ] },
           {"name": "DEATH_DATE", "levels": [ {"name": "YYYY-MM-DD 00:00:00", "type": "YMD", "count": -1 } ] }
           ]     
      },                                                                                                                       
     {"filename": "DEMOGRAPHIC",                                                                                            
      "columns":[                                                                                                        
           {"name": "PATID",      "levels": [ {"name": "GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG", "type":"id", "count": -1 } ] },
           {"name": "BIRTH_DATE", "levels": [ {"name": "YYYY-MM", "type":"YM", "count": -1 } ] }
           ]
      },                     
     {"filename": "CONDITION",
      "columns":[                                                                                      
           {"name": "CONDITIONID",      "levels": [ {"name": "GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG", "type":"id", "count": -1 } ] },
           {"name": "PATID",      "levels": [ {"name": "GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG", "type":"id", "count": -1 } ] },
           {"name": "ENCOUNTERID",      "levels": [ {"name": "GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG", "type":"id", "count": -1 } ] },
           {"name": "REPORT_DATE", "levels": [ {"name": "YYYY-MM-DD 00:00:00", "type": "YMD", "count": -1 } ] },
           {"name": "ONSET_DATE", "levels": [ {"name": "YYYY-MM-DD 00:00:00", "type": "YMD", "count": -1 } ] },                    
           {"name": "RESOLVE_DATE", "levels": [ {"name": "YYYY-MM-DD 00:00:00", "type": "YMD", "count": -1 } ] }            
           ]                                                                                                                
      },                                                                                                       
     {"filename": "OBS_CLIN",                                                                          
      "columns":[                                                                                           
           {"name": "OBSCLINID",        "levels": [ {"name": "XXXXXXXXXX_XXXXX-X_XX", "type":"id", "count": -1 } ] },
           {"name": "PATID",        "levels": [ {"name": "GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG", "type":"id", "count": -1 } ] },
           {"name": "ENCOUNTERID",  "levels": [ {"name": "GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG", "type":"id", "count": -1 } ] },
           {"name": "OBSCLIN_PROVIDERID",      "levels": [ {"name": "00000000", "type":"id", "count": -1 } ] },
           {"name": "OBSCLIN_DATE", "levels": [ {"name": "YYYY-MM-DD 00:00:00", "type": "YMD", "count": -1 } ] },                 
           {"name": "OBSCLIN_TIME", "levels": [ {"name": "00:00", "count": -1, "type": "HH:MM" } ] },                       
           {"name": "OBSCLIN_RESULT_NUM", "levels": [ {"name": "x.x", "count": -1, "type":"real" } ] },                     
           ]                                                                                                  
      },                                                                                                        
     {"filename": "ENCOUNTER",                                                                      
      "columns":[                                                                                                                        
           {"name": "ENCOUNTERID",      "levels": [ {"name": "GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG", "type":"id", "count": -1 } ] },
           {"name": "PATID",      "levels": [ {"name": "GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG", "type":"id", "count": -1 } ] },
           {"name": "ADMIT_DATE", "levels": [ {"name": "YYYY-MM-DD 00:00:00", "count": -1, "type":"YMD" } ] },
           {"name": "ADMIT_TIME", "levels": [ {"name": "00:00", "count": -1, "type": "HH:MM" } ] },
                                             {"name": "DISCHARGE_DATE", "levels": [ {"name": "YYYY-MM-DD", "count": -1, "type":"YMD" } ] },
           {"name": "DISCHARGE_TIME", "levels": [ {"name": "00:00", "count": -1, "type":"HH:MM" } ] },                      
           {"name": "PROVIDERID",      "levels": [ {"name": "00000000", "type":"id", "count": -1 } ] },                     
           ]                                                                                              
      },                                                                                                          
       {"filename": "VITAL",                                                                          
        "columns":[                                                                                               
             {"name": "VITALID",      "levels": [ {"name": "GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG_SM_1", "type":"id", "count": -1 } ] },
             {"name": "PATID",        "levels": [ {"name": "GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG", "type":"id", "count": -1 } ] },
             {"name": "ENCOUNTERID",  "levels": [ {"name": "GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG", "type":"id", "count": -1 } ] },
             {"name": "MEASURE_DATE", "levels": [ {"name": "YYYY-MM-DD 00:00:00", "type": "YMD", "count": -1 } ] },
             {"name": "MEASURE_TIME", "levels": [ {"name": "00:00", "count": -1, "type":"HH:MM" } ] },
             {"name": "HT", "levels": [ {"name": "x.x", "count": -1, "type":"real" } ] },                   
             {"name": "WT", "levels": [ {"name": "x.x", "count": -1, "type":"real" } ] },
             {"name": "DIASTOLIC", "levels": [ {"name": "x.x", "count": -1, "type":"real" } ] },
             {"name": "SYSTOLIC", "levels": [ {"name": "x.x", "count": -1, "type":"real" } ] },
             {"name": "ORIGINAL_BMI", "levels": [ {"name": "x.x", "count": -1, "type":"real" } ] },
             ]              
        },                           
     {"filename": "LDS_ADDRESS_HISTORY",
      "columns":[                 
           {"name": "ADDRESSID",    "levels": [ {"name": "GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG-A1", "type":"id", "count": -1 } ] },
           {"name": "PATID",        "levels": [ {"name": "GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG", "type":"id", "count": -1 } ] },
           {"name": "ADDRESS_PERIOD_START", "levels": [ {"name": "YYYY-MM-DD 00:00:00", "type": "YMD", "count": -1 } ] },
           {"name": "ADDRESS_PERIOD_END", "levels": [ {"name": "YYYY-MM-DD 00:00:00", "type": "YMD", "count": -1 } ] },
           ]          
      },                        
     {"filename": "PROVIDER",
      "columns":[                           
           {"name": "PROVIDERID",      "levels": [ {"name": "00000000", "type":"id", "count": -1 } ] },
           ]                  
      },  
     {"filename": "PROCEDURES",                                  
      "columns":[
           {"name": "PROCEDURESID",        "levels": [ {"name": "GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG", "type":"id", "count": -1 } ] },
           {"name": "PATID",        "levels": [ {"name": "GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG", "type":"id", "count": -1 } ] },
           {"name": "ENCOUNTERID",  "levels": [ {"name": "GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG", "type":"id", "count": -1 } ] },
           {"name": "ADMIT_DATE", "levels": [ {"name": "YYYY-MM-DD 00:00:00", "type": "YMD", "count": -1 } ] },
           {"name": "PROVIDERID",      "levels": [ {"name": "00000000", "type":"id", "count": -1 } ] },
           {"name": "PX_DATE", "levels": [ {"name": "YYYY-MM-DD 00:00:00", "type": "YMD", "count": -1 } ] },
           ]                         
      },                            
     {"filename": "OBS_GEN",                       
      "columns":[                                
           {"name": "OBSGENID",        "levels": [ {"name": "ADTXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX", "type":"id", "count": -1 } ] },
           {"name": "PATID",        "levels": [ {"name": "GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG", "type":"id", "count": -1 } ] },
           {"name": "ENCOUNTERID",  "levels": [ {"name": "GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG", "type":"id", "count": -1 } ] },
           {"name": "OBSGEN_PROVIDERID",      "levels": [ {"name": "00000000", "type":"id", "count": -1 } ] },
           {"name": "OBSGEN_DATE", "levels": [ {"name": "YYYY-MM-DD 00:00:00", "type": "YMD", "count": -1 } ] },
           {"name": "OBSGEN_TIME", "levels": [ {"name": "00:00", "count": -1, "type": "HH:MM" } ] },                
           {"name": "OBSGEN_ID_MODIFIED",        "levels": [ {"name": "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX", "type":"id", "count": -1 } ] },
           ]                    
      },
     {"filename": "PRESCRIBING",                  
      "columns":[                                       
           {"name": "PRESCRIBINGID",        "levels": [ {"name": "XXXXXXXXXX-XXX", "type":"id", "count": -1 } ] },
           {"name": "PATID",        "levels": [ {"name": "GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG", "type":"id", "count": -1 } ] },
           {"name": "ENCOUNTERID",  "levels": [ {"name": "GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG", "type":"id", "count": -1 } ] },
           {"name": "RX_PROVIDERID",      "levels": [ {"name": "00000000", "type":"id", "count": -1 } ] },
           {"name": "RX_ORDER_DATE", "levels": [ {"name": "YYYY-MM-DD 00:00:00", "type": "YMD", "count": -1 } ] },
           {"name": "RX_ORDER_TIME", "levels": [ {"name": "00:00", "count": -1, "type": "HH:MM" } ] },
           {"name": "RX_START_DATE", "levels": [ {"name": "YYYY-MM-DD 00:00:00", "type": "YMD", "count": -1 } ] },
           {"name": "RX_END_DATE", "levels": [ {"name": "YYYY-MM-DD 00:00:00", "type": "YMD", "count": -1 } ] },
           {"name": "RX_QUANTITY", "levels": [ {"name": "x.x", "count": -1, "type":"real" } ] },
           {"name": "RX_REFILLS", "levels": [ {"name": "x", "count": -1, "type":"int" } ] },                                                  
           {"name": "RX_DAYS_SUPPLY", "levels": [ {"name": "x", "count": -1, "type":"int" } ] },
           # maybe comment  this out later to add all the medication descriptions?
           {"name": "RAW_RX_MED_NAME", "levels": [ {"name": "description", "count": -1, "type":"text" } ] },
           ]                               
      },                                                      
     ]                                                           
                                     
def get_column_type(column):        
     ty = column["levels"][0]["type"]              
     if ty == "YMD":                             
          return "timestamp", True                                                                                                
     elif ty == "YM":                                                                                                       
          return 'text', False                                                                                              
     elif ty == "HH:MM":                                                                                      
          return "time", True                                                                                   
     elif ty == "int":                                                                                              
          return "integer", True                                                                                                         
     elif ty == "real":         
          return "text", True # "real", True
     elif ty == "id" or ty == "text":             
          return "text", False                          
     else:                                                                                                        
          raise RuntimeError(f"unsupported column type {column}")                                                           
                                                                                                                            
with open("create.sql", "w") as outf:                                                                     
    with open("ingest.sql", "w") as ingestf:                                                                      
        with open("delete.sql", "w") as deletef:                                                      
            with open("drop.sql", "w") as dropf:                                                                  
                for table in tables:                                                                            
                    table_name = table["filename"]                                              
                    column_types = {}                                                                                                         
                    force_nulls = []                                                            
                    for column in table["columns"]:                               
                        col_name = column["name"]                                                           
                        ty, force_null = get_column_type(column)
                        column_types[col_name] = ty           
                        if force_null:                           
                            force_nulls.append(col_name)
                    tablefi = f"{datafiles}/{table_name}.csv"
                    if os.path.isfile(tablefi):
                        with open(tablefi) as f:
                            colnames_full = map(lambda x: x.replace('"', "").replace("\n", ""), f.readline().split("|"))
                    
                        columns = []  
                     
                        for col_name in colnames_full:
                            if col_name not in column_types:
                                print(f"not specified {col_name}")
                                col_type = "text"
                            else:   
                                col_type = column_types[col_name]
                                            
                            columns.append(f'{col_name} {col_type}')
                              
                        outf.write(f'create table {table_name} ({",".join(columns)});\n')
                        psql_cmd = f"\\copy {table_name} FROM '{datafiles}/{table_name}.csv' WITH CSV HEADER DELIMITER '|' NULL ''"
                        if len(force_nulls) != 0:
                            psql_cmd += ' FORCE NULL '+",".join(force_nulls)
                        psql_cmd += ';\n'           
                        ingestf.write(psql_cmd)     
                        dropf.write(f'drop table {table_name};\n')
                        deletef.write(f'delete from {table_name};\n')
