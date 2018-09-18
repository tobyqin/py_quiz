class switch(object):
    def __init__(self, case_path):
        self.switch_to = case_path
        self._invoked = False

    def case(self, key, method):
        if self.switch_to == key and not self._invoked:
            self._invoked = True
            method()

        return self

    def default(self, method):
        if not self._invoked:
            self._invoked = True
            method()


# example
def cn(): print('cn')


def us(): print('us')


def fail(): print('default')


switch("cn").case("cn", cn).case("us", us).default(fail)
# if language = "cn", only method <cn> will be invoked.
# if language = "us", only method <us> will be invoked.
# if language = "jp", only method <default> will be invoked.

switch("jp").case("cn", cn).case("us", us)


def us1(): print('us1')


def us2(): print('us2')


switch("us").case("us", us1).case("cn", cn).case("us", us2)
# if language = "us", only method <us1> will be invoked.

