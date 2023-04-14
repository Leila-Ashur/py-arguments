#  def hello(names):
#  for name in names:
#      print(f"hello{name}")
    
    #  A function named concatenate_args that takes any number of string arguments in
# positional arguments format andconcatenates them into a single string

def  concatenate_args(*args):
    concatenate_str= ''
    for arg in args:
        concatenate_str +=arg
    return concatenate_str
    
    # A function named concatenate_kwargs that takes any number of string arguments in keyword arguments  format and
    # concatenates them into a single string
    def concatenate_kwargs(**kwargs):
        result=" ,"
        for flask in kwargs.values():
            result +=flask
    return result
    
    
    
  

   