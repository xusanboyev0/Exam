# import json
# import csv
# import pyxlsx
# from django.apps import apps
#
#
#
#
# with open('products.json', 'w') as json_file:
#     json.dump(products, json_file)
#
# with open('categories.csv', 'w', newline='') as csv_file:
#     csv_writer = csv.DictWriter(csv_file, fieldnames=categories[0].keys())
#     csv_writer.writeheader()
#     csv_writer.writerows(categories)
#
# wb = pyxlsx.Workbook()
# ws = wb.active
# ws.append(list(regions[0].keys()))
# for region in regions:
#     ws.append(list(region.values()))
# wb.save('regions.xlsx')
#
# with open('districts.json', 'w') as json_file:
#     json.dump(districts, json_file)



