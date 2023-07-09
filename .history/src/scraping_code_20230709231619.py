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

def extract_decision_listing_data(response):
    # Initialize an empty list to store decision data
    decision_data_list = []

    # Extract the lines containing decisions
    lines = response.xpath('//div[@class="birkarar col-sm-12"]')
    for i, line in enumerate(lines):
        # Initialize an empty dictionary for each decision
        decision_data = {}

        title = line.xpath('//titles/text()')[i].get().strip()

        decision_data['title'] = title.strip() if title else ""

        # Extract the application topic
        topic = line.xpath('.//div[@class="basvurukonualani"]/text()').get()
        decision_data['topic'] = topic.strip() if topic else ""

        # Extract the decision information
        info = line.xpath('.//div[@class="kararbilgileri"]/text()').get()
        decision_data['detailed_info'] = info.strip() if info else ""

        # Extract the href
        href = line.xpath('.//a[@class="waves-effect "]/@href').get()
        decision_data['link'] = href if href else ""

        # Add the decision data to the list
        decision_data_list.append(decision_data)

    return decision_data_list
