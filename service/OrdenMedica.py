
Skip to content
Pull requests
Issues
Marketplace
Explore
@carlosariasmaury
Learn Git and GitHub without any code!

Using the Hello World guide, you’ll start a branch, write comments, and open a pull request.
carlosariasmaury /
pythonApiV4

1
0

    0

Code
Issues
Pull requests
Actions
Projects
Wiki
Security
Insights

    Settings

pythonApiV4/service/client.py /
alejandro triana Initial commit
Latest commit 0299c23 3 days ago
History
0 contributors
34 lines (26 sloc) 1021 Bytes
""" Class representing a client
    """
class Client():

    def __init__(self, name, last_name, doc_id):
        self.name = name
        self.last_name = last_name
        self.doc_id = doc_id
        self.preexistence = []

    def add_preexistence(self, nPreexistence):
        self.preexistence.append(nPreexistence)
        return len(self.preexistence) - 1

    def get_preexistence(self, pIndex):
        if pIndex >= len(self.preexistence):
            return 'There is no such preexistence'
        else:
            return self.preexistence[pIndex]

    def get_all_preexistence(self):
        return self.preexistence

    def remove_preexistence(self, n_preexistence):
        self.preexistence.pop(n_preexistence)
        return len(self.preexistence) - 1

    def get_formatted_name(self):
        return self.name + ' ' + self.last_name


if __name__ == '__main__':
    client_instance = Client('uno', 'dos', '113565')
    print('User Abbas has been added with id ', client_instance.get_formatted_name())

    © 2020 GitHub, Inc.
    Terms
    Privacy
    Security
    Status
    Help
    Contact GitHub
    Pricing
    API
    Training
    Blog
    About

