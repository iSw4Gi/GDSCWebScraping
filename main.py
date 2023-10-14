# Author : @iSw4Gi 
# GDSC Web Scraping 
# Analysis & Web Grapping 



# Importing Libraries
import pandas as pd 
import random


df = pd.read_excel('data.xlsx' , header=0)
# Specify the column label you want to print
desired_column = 'Unnamed: 6'

df = df.dropna(subset=[desired_column])


# Print all rows in the 'Unnamed: 4' column
print(df[desired_column])


# Initialize the HTML content
html_content = ''

# HTML template for each row
row_template = """
<div class="box">
    <span class="tag" id="{tag_id}">{day}</span>
    <p>{tag}</p>
    <div class="box-footer">
        <div class="date">
            <li><i class="fa-solid fa-calendar-days"></i>
            <span>{date}</span>
        </div>
    </div>
</div>
"""
# List of possible 'tag_id' values
possible_tag_ids = ["green", "red", "yellow"]

# Iterate over the DataFrame rows and fill in the HTML template
for index, row in df.iterrows():
    tag_id = random.choice(possible_tag_ids)
    row_data = {
        'tag_id': tag_id,
        'day':row['Unnamed: 2'],
        'tag': row[desired_column],
        'date': row['Unnamed: 3'],    # Replace 'Date_Column' with the actual column name for the date
    }
    html_content += row_template.format(**row_data)
# The final HTML content with all rows
final_html = f"""
<div class="box-column">
    <div class="box-header">
        <h5><span class="num">{df.shape[0]}</span></h5>
        <li><i class="fa-solid fa-plus"></i>
    </div>
    {html_content}
</div>
"""

# Read the template HTML file
with open('template.html', 'r', encoding='utf-8') as template_file:
    template_content = template_file.read()

# Combine the template with the generated content
final_html = template_content.replace("<!-- INSERT_CONTENT_HERE -->", final_html)

# Save the combined HTML content to a new file
with open('index.html', 'w', encoding='utf-8') as output_file:
    output_file.write(final_html)

print("Generated HTML has been merged with the template and saved as 'index.html'.")
