# # # //debugging in python :
# # # bug is called errors
# # # debugging is finding and fixing is errors 
# # # types of errors:
# # # syntax errors: missing of colon and missing of indentation 
# # # runtime errors: division by zero
# # # logical errors: missing of logics
# # # de bugging techniques:
# # # 1.print()
# # # 2.try-except
# # # 3.using pdb
# # pdb is a python  debugger
# # purpose:
# #     1)pause the execution code
# #     2)inspect the variables value
# #     3)to run the code
# pdb commands:
#     1)n-->to execute the ouyput ina next line
#     2)p variable --> to get the the value of a variable
#     3)i-->list nearby code
#     4)c-->continue the execution of code
#     5)s-->
import pdb
def add(a,b):
    pdb.set_trace()#set the breakpoint
    return a+b
