input_csv_file = "Articles.csv"
output_txt_file = "Output_Date.txt"
# Initialize a list to store the extracted articles
extracted_articles = []
with open(input_csv_file, "r") as csv_file:
    lines = csv_file.readlines()

for line_number, line in enumerate(lines, start=1):
    if 7 <= line_number <= 9:
        # Assuming the CSV uses a comma as the delimiter
        columns = line.split(',')
        if len(columns) >= 2:
            # Assuming the "Date" column is at index 1
            article = columns[1].strip()
            extracted_articles.append(article)
if extracted_articles:
    # Write the extracted articles to the output text file
    with open(output_txt_file, "w") as txt_file:
        for article in extracted_articles:
            txt_file.write(article + "\n")
