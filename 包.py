
# import package1.my_module1
# import package1.my_module2

# package1.my_module1.info_1()
# package1.my_module2.info_2()


# from package1 import my_module1
# from package1 import my_module2

# my_module1.info_1()
# my_module2.info_2()

from package1.my_module1 import *
from package1.my_module2 import *

info_1()
info_2()