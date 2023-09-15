import pandas as pd

# Changes the initial data into a dataframe
def text_to_df():
    colors = ['🟡', '🟢', '🔵', '🟣']
    dataset = {}

    file = open("data.txt",  encoding="utf8")
    for line in file:
        if line[0] not in colors:
            continue

        string = line[2:].split(":")
        title = string[0].lower()
        words = string[1].strip().lower().replace(" ", "")
        words = words.split(",")
        data = {title: words}
        dataset.update(data)

    
    file.close()

    df = pd.DataFrame.from_dict(dataset).T
    df = df.reset_index()

    # Rename columns
    df.columns = ['titles', 'word1', 'word2', 'word3', 'word4']
    print(df)
    return df
    

