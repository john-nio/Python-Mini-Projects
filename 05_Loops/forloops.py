file_list = ["report.csv", "data.xlsx", "summary.docx", "report.csv", "data.csv"]

for i in file_list:
    if file_list.count(i) > 1:
        print("Duplicate Found")
    break
else:
    print("All files are unique")
