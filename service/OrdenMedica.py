class OrdenMedica():
    """Class representing a Orden Medica"""
    def __init__(self, identifier, status, category):
        self.identifier = identifier
        self.status = status
        self.category = category
        self.order_detail = []

    def add_order_detail(self, order_detail):
        """ Add Order Detail"""
        self.order_detail.append(order_detail)
        return len(self.order_detail) - 1

    def get_order_detail(self, p_index):
        """ Gets Order Detail by Index"""
        if p_index >= len(self.order_detail):
            return 'There is no such Order Detail'
        else:
            return self.order_detail[p_index]

    def get_all_order_detail(self):
        """ Gets all Order Detail"""
        return self.preexistence

    def remove_orderDetail(self, n_order_detail):
        """ Removes Order Detail by Index"""
        self.order_detail.pop(n_order_detail)
        return len(self.order_detail) - 1

    def get_formatted_OrderStatus(self):
        """ Gets Order Status"""
        return self.identifier + ' ' + self.status


if __name__ == '__main__':
    OrdenMedica_instance = OrdenMedica('id1', 'Aprobado', 'Med')
    print('El Estado de la OM es  ', OrdenMedica_instance.get_formatted_OrderStatus())
