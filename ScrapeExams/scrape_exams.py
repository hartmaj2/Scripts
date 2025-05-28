# We will scrape the data from SIS and then analyze it.
# The data can be got using inspector and saving the index.php file
# Terminy zkousek -> click on details icon on top left corner of the exam box in the calendar

from bs4 import BeautifulSoup, Tag


html_filepath = "ScrapeExams/index.php"

file = open(html_filepath)

soup = BeautifulSoup("".join(file.readlines()),"html.parser")

def get_relevant_table(soup : BeautifulSoup) -> Tag:
    relevant_table_class = "tab1"
    tables = soup.find_all("table",{"class":relevant_table_class})

    relevant_table_index = 4
    table = tables[relevant_table_index]
    if not isinstance(table,Tag):
        exit()
    return table

def get_relevant_rows(table : Tag) -> list[Tag]:
    raw_rows = table.find_all("tr")[2:]
    rows = []
    for row in raw_rows:
        rows.append(row)
    return rows

def get_spec_from_row(row : Tag) -> str:
    relevant_col_id = 2
    col = row.find_all("td")[relevant_col_id]
    if not isinstance(col,Tag):
        raise ValueError
    a = col.find("a")
    if not isinstance(a,Tag):
        raise ValueError
    return a.text

def strip_spec_code(spec_string : str) -> str:
    index = spec_string.find("(")
    return spec_string[:index]

def get_specs_occurences_dict(soup : BeautifulSoup) -> dict[str,int]:
    table = get_relevant_table(soup)
    rows = get_relevant_rows(table)

    specs_dict = {}
    for row in rows:
        spec = strip_spec_code(get_spec_from_row(row))
        if spec not in specs_dict:
            specs_dict[spec] = 0
        specs_dict[spec] += 1

    return specs_dict

def print_dict(d : dict) -> None:
    for key,value in d.items():
        print(f"{value:02d} {key}")

specs_dict  = get_specs_occurences_dict(soup)
print_dict(specs_dict)