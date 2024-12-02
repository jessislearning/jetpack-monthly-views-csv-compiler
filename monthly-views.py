import pandas as pd
import glob

# Please insert the correct folder path for your files
folder_path = '/localdirectory/folder/'  
file_pattern = folder_path + '*.csv'

# list to store dataframes
dataframes = []

# Debug: Check if files are being detected
files = glob.glob(file_pattern)
if not files:
    print("No CSV files found in the specified folder. Please check the folder path and file extensions.")
else:
    print(f"Found {len(files)} CSV file(s): {files}")

# Taking data from each csv file to compile in 'dataframes'
for file in files:
    try:
        # Extract the month from the filename
        month = file.split('/')[-1].split('.')[0]
        
        # Load the CSV file into a DataFrame
        df = pd.read_csv(file, header=None, names=['Post Title', 'Views', 'URL'])
        
        # Add a column for the month
        df['Month'] = month
        
        # Only keep the relevant columns
        df = df[['Post Title', 'Views', 'Month']]
        
        # Append the dataframe to the list
        dataframes.append(df)
    except Exception as e:
        print(f"Error processing file {file}: {e}")

# Check if any dataframes were created
if not dataframes:
    print("No dataframes were created. Please check the CSV file contents and structure.")
else:
    # Combine all dataframes into one
    combined_df = pd.concat(dataframes, ignore_index=True)

    # Pivot the table to show post titles and views for each month
    result_table = combined_df.pivot_table(
        index='Post Title',
        columns='Month',
        values='Views',
        aggfunc='sum',
        fill_value=0
    )

    # Reset the index for better readability
    result_table.reset_index(inplace=True)

    # Sum views over all included months
    result_table['Total Views'] = result_table.iloc[:, 1:].sum(axis=1)

    # Save the resulting table to a CSV file
    output_file = 'results/monthly_views_summary.csv'
    result_table.to_csv(output_file, index=False)

    print(f"Table saved to {output_file}")

    # This part of the code creates a 'tidy table' which rearranges the original table to a long format for easier plotting
    tidy_table = pd.melt(
    result_table,
    id_vars=['Post Title'],  # Columns to keep as identifiers
    var_name='Month',        # Name of the new column for months
    value_name='Views'       # Name of the new column for views
    )

    # Remove the "Total Views" rows (optional if plotting only monthly data)
    tidy_table = tidy_table[tidy_table['Month'] != 'Total Views']

    # Save the tidy table to a CSV file
    output_tidy_file = 'results/monthly_views_tidy.csv'
    tidy_table.to_csv(output_tidy_file, index=False)

    print(f"Tidy table saved to {output_tidy_file}")

