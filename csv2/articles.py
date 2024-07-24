input_csv_file = "Articles.csv"
output_txt_file = "Output.csv"
cape_town_rows = []
filtered_rows = []
with open("Articles.csv", "r") as csv_file:
   lines = csv_file.readlines()
   print(lines)
   cape_town_rows.append(lines[0])
for line in lines[1:]:
   parts = line.strip().split(',')
   article = parts[0]
   date = parts[1]
   day, month, year = date.split('-')
   day = int(day)
   month = int(month)
   year = int(year)
   print(day, month, year)       
   if "CAPE TOWN" in article.upper():
      cape_town_rows.append(line)
   elif day > 2 and month > 1 and year > 2015:
      filtered_rows.append(line)
with open(output_txt_file, "w") as txt_file:
   txt_file.writelines(cape_town_rows)
with open(output_txt_file, "a") as txt_file:
   txt_file.writelines(filtered_rows)
