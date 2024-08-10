# the general way to return a value from a list or dict is either indexing or spcifiying rhe key in case of dict but in py we have an unpacking operator that is * which will unpack the values and return it in the same order let see 
def vault(gold,silver,bronze):
    return (gold * 17 + silver) * 29 + bronze

# values = [12,40,65]

# print(f"{vault(*values)} bronze") # *values is unpacking operator which will unpack the values and return them in the same order as they were given in the function call

# lets say we have a dictionary like
values = {"gold":12, "silver":40, "bronze":65}
print(f"{vault(**values)} bronze")
