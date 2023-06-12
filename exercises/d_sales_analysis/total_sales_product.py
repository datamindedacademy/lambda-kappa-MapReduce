def sales_analysis(sales_file):
    with open(sales_file, 'r') as file:
        header = file.readline()  # We want to skip the header, so we do nothing with it, just read it
        sales_records = file.readlines()  # Store the following lines

    # TODO: Map phase

    # TODO: Reduce phase

    return None


if __name__ == '__main__':
    sales_file = "../resources/sales.csv"
    result = sales_analysis(sales_file)
    print(result)
