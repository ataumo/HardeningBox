from FileFunctions import *
from UpdateMainCsv import *

tool = input("""
#################################################################################################################### _ 0 X #
#                                                                                                                          #
#   /$$   /$$                           /$$                     /$$                     /$$$$$$$                           #
#  | $$  | $$                          | $$                    |__/                    | $$__  $$                          #
#  | $$  | $$  /$$$$$$   /$$$$$$   /$$$$$$$  /$$$$$$  /$$$$$$$  /$$ /$$$$$$$   /$$$$$$ | $$  \ $$  /$$$$$$  /$$   /$$      #
#  | $$$$$$$$ |____  $$ /$$__  $$ /$$__  $$ /$$__  $$| $$__  $$| $$| $$__  $$ /$$__  $$| $$$$$$$  /$$__  $$|  $$ /$$/      #
#  | $$__  $$  /$$$$$$$| $$  \__/| $$  | $$| $$$$$$$$| $$  \ $$| $$| $$  \ $$| $$  \ $$| $$__  $$| $$  \ $$ \  $$$$/       #
#  | $$  | $$ /$$__  $$| $$      | $$  | $$| $$_____/| $$  | $$| $$| $$  | $$| $$  | $$| $$  \ $$| $$  | $$  >$$  $$       #
#  | $$  | $$|  $$$$$$$| $$      |  $$$$$$$|  $$$$$$$| $$  | $$| $$| $$  | $$|  $$$$$$$| $$$$$$$/|  $$$$$$/ /$$/\  $$      #
#  |__/  |__/ \_______/|__/       \_______/ \_______/|__/  |__/|__/|__/  |__/ \____  $$|_______/  \______/ |__/  \__/      #
#                                                                             /$$  \ $$                                    #
#                                                                            |  $$$$$$/                                    #
#                                                                             \______/                                     #
#                                                                                                                          #
################################################## By Guillaume de Rybel ###################################################              

Welcome to the Hardening Box !

This tool box allows you to use and transform Hardening Data. You will be able to transform CSV extract into PowerPoint slides or Excel tables in easy ways !

This is based on CIS policies, so it might differ with other organizations.

    1. Add audit result to a CSV file
    2. Add policies Microsoft Links to CSV
    3. Scrap policies from CIS pdf file (https://downloads.cisecurity.org/#/)
    4. Add scrapped data to CSV file
    5. Excel <-> CSV convertion
    6. Transform CSV into PowerPoint slides

Choose your tool (1->6): """)

if tool == '1':
    # Add audit result to a CSV file
    original_filepath = input('Which base hardening file should I look for (e.g. : filename.csv) : ')
    original_file = FileFunctions(original_filepath)
    original_file.checkIfFileExistsAndReadable()
    original_dataframe = original_file.readCsvFile()

    adding_filepath = input('Which audit result file should I look for (e.g. : filename.csv) : ')
    adding_file = FileFunctions(adding_filepath)
    adding_file.checkIfFileExistsAndReadable()
    adding_dataframe = adding_file.readCsvFile()

    output_column_name = input('What will be the name of the output column (e.g. : context1) : ')
    output_column_index = input('What will be the index of the output column (e.g. : 15) : ')

    csv = UpdateMainCsv(original_dataframe, original_filepath, adding_dataframe, adding_filepath)
    csv.AddAuditResult()

    print('\nAudit column added successfully.')

elif tool == '2':
    # Add policies Microsoft Links to CSV
    pass

elif tool == '3':
    # Scrap policies from CIS pdf file (https://downloads.cisecurity.org/#/)
    pass

elif tool == '4':
    # Add scrapped data to CSV file
    pass

elif tool == '5':
    # Excel <-> CV convertion
    pass

elif tool == '6':
    # Transform CSV into PowerPoint slides
    pass

else:
    print('\nTool selected not in list.')


print("""
Thanks for using HardeningBox, see you later !

##############################################################################################################################
""")