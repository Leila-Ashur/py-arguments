# def addition(a,b):
#    answer= a+b
#    return answer
      
# def subtract(a,b):
#    answer= a-b
#    return answer
   
   
# def divide(a,b):
#    answer= a*b
#    return answer

# def multiply(a,b):
#    answer= a%b
#    return answer

# def remainder(a,b):
#    answer= a%b
#    return answer

# def sum(* numbers):
#    answer =
#    for number in numbers:
#        answer +=number
#    return answer
# write a functions that attempts
#    answer=1

#   def integers(* numbers):
#     for number in numbers:
#       answer*= number
#       return answer
   
def student_attributes(**kwargs):
   for key, value in kwargs.items():
      print(f"{key} : {value}")

def my_country(country= "Burundi"):
    print(f"Hello from {country}")