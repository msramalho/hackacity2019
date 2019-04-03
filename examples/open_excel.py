from ipdb import set_trace          # easy debug
from pprint import pprint as pp     # pretty print things

import xlrd


# Excel file - example with Portugal's population density by administrative zone...
population_density_excel = xlrd.open_workbook('examples\\_example_pop_density.xlsx')
# first sheet from Excel file
population_density_sheet = population_density_excel.sheet_by_index(0)


def read_data_into_array(worksheet):
    """ Helper function to read worksheet into dictionary of values, but could be changed to list """
    # get header names from worksheet
    headers = [worksheet.cell_value(0, col) for col in range(worksheet.ncols)]
    # transform the workbook to a list of dictionary
    data = [{headers[col]: worksheet.cell_value(row, col)
             for col in range(worksheet.ncols)
             } for row in range(1, worksheet.nrows)]
    return data


# dictionary of all values
density_dictionary = read_data_into_array(population_density_sheet)

set_trace()

