def extract_table_data(xpath_object, columns = 2 ):
    if columns != 2:
        raise ValueError('Only 2 columns are supported')
    data = {}

    # Extract table rows
    rows = xpath_object.xpath('.//tr')

    # Iterate over each row
    for row in rows:
        # Extract key-value pairs from each row
        key = row.xpath('.//td[1]/text()').get().strip()
        value = row.xpath('.//td[2]/text()').get().strip()

        # Store the data in the dictionary
        data[key] = value

    return data
