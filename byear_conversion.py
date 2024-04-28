import csv
    
# Specify input and output file paths
tsv_file = 'education_incoming.tsv'
csv_file = 'educaton_incoming_with_year.csv'

# Open TSV file for reading and CSV file for writing
with open(tsv_file, 'r', newline='', encoding='utf-8') as tsvfile, \
     open(csv_file, 'w', newline='', encoding='utf-8') as csvfile:

    # Create TSV reader and CSV writer objects
    tsv_reader = csv.reader(tsvfile, delimiter='\t')
    csv_writer = csv.writer(csvfile, delimiter=',')

    # Read each row from TSV and write to CSV
    indx = 0
    new_rows = []
    for row in tsv_reader:
        if indx == 0:
           years=row[1:22]
           modified_row = row[0].replace('\\TIME_PERIOD', ',Year,Income')
           modified_row = modified_row.replace('geo','Country').split(',')
           title_row = [x.title() for x in modified_row]
           csv_writer.writerow(title_row)
        if indx > 1:
            for index in range(1,22):
                splitted_row = row[0].split(',')
                new_rows.append([splitted_row[0], splitted_row[1],splitted_row[2], splitted_row[3], splitted_row[4], splitted_row[5], splitted_row[6], years[index-1].strip(),row[index].strip()])
            csv_writer.writerows(new_rows) 
            new_rows = []           
        indx = indx + 1
        #csv_writer.writerow(row)

print("Conversion completed successfully!")