""" Class representing a Orden Medica
    """
class OrdenMedica():

    def __init__(self, identifier, status, category):
        self.identifier = identifier
        self.status = status
        self.category = category
        self.orderDetail = []

    def add_orderDetail(self, orderDetail):
        self.orderDetail.append(orderDetail)
        return len(self.orderDetail) - 1

    def get_orderDetail(self, pIndex):
        if pIndex >= len(self.orderDetail):
            return 'There is no such orderDetail'
        else:
            return self.orderDetail[pIndex]

    def get_all_orderDetail(self):
        return self.preexistence

    def remove_orderDetail(self, n_orderDetail):
        self.orderDetail.pop(n_orderDetail)
        return len(self.orderDetail) - 1

    def get_formatted_OrderStatus(self):
        return self.identifier + ' ' + self.status


if __name__ == '__main__':
    client_instance = Client('id1', 'Aprobado', 'Med')
    print('El Estado de la OM es  ', client_instance.get_formatted_OrderStatus())
