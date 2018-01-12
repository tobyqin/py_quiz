class switch:
    def __init__(self, case_path):
        self.switch_to = case_path
        self._invoke = False

    def case(self, key, method):
        if self.switch_to == key and not self._invoke:
            self._invoke = True
            method()

        return self

    def default(self, method):
        if not self._invoke:
            self._invoke = True
            method()


# example
def cn(): pass


def us(): pass


def default(): pass


switch("cn").case("cn", cn).case("us", us).default(default)
# if language = "cn", only method <cn> will be invoked.
# if language = "us", only method <us> will be invoked.
# if language = "jp", only method <default> will be invoked.

def cn(): pass
def us1(): pass
def us2(): pass

switch("us").case("us", us1).case("cn", cn).case("us", us2)
# if language = "us", only method <us1> will be invoked.