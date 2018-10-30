class Sales(object):
    def __init__(self, data):
        self.__sales_data = data

    def get_average(self):
        return sum(self.__sales_data) / len(self.__sales_data)

    def add_sale(self, sale):
        try:
            sale_float = float(sale)
        except ValueError:
            sale_float = 0
        self.__sales_data.append(sale_float)


def read_data_from_file(filename):
    data = list()
    with open(filename) as file_pointer:
        for line in file_pointer:
            try:
                data.append(float(line))
            except ValueError:
                pass
    return data


def main():
    data = read_data_from_file("sales.txt")
    sales = Sales(data)
    average_sales = sales.get_average()
    print("Average sales: {:.2f}".format(average_sales))
    sales.add_sale(78.5)
    average_sales = sales.get_average()
    print("Average sales: {:.2f}".format(average_sales))

main()
