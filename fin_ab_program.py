from finite_abelian_groups import primefac, power_count, prime_pows, decompose_ahead, produce_factors
import os 
def all_factorizations(theint):
    return produce_factors(decompose_ahead(prime_pows(primefac(theint))))
    
print("Finite abelian group of order: ")
ord = input()
try:
   val = int(ord)
except ValueError:
   print("That's not an integer!")
if val < 2:
    print("Pick something bigger.")
else:
   the_factors = all_factorizations(val)
   print(the_factors)

def group_fac_for_latex(list_facts):
   latex_code = ""
   for fact in list_facts:
      for i in range(len(fact)):
        num = fact[i]
        if i == 0:    
            latex_code += "$\\mathbb{Z}_" + "{" + str(num) + "}" + "\\times "
        elif i == len(fact) - 1:
            latex_code += "\\mathbb{Z}_" + "{" + str(num) + "}$" + " \\newline"   
        else: 
            latex_code += "\\mathbb{Z}_" + "{" + str(num) + "}" + "\\times "
      latex_code += "\n"
   return latex_code
file = open('finite_abelian_factorization.tex', 'w')
file.write("\\documentclass[12pt,letterpaper,boxed]{maths_v5}\n" 
+ "\\usepackage[margin=1in]{geometry}\n" 
+ "\\usepackage{lmodern}\n" 
+ "\\usepackage{amsmath}\n"
+ "\\begin{document}\n"
+ "\\begin{center}\n"
+ "Finite Abelian Groups of Order :" + str(ord) + "\\newline \n"
+ group_fac_for_latex(the_factors)
+ "\\end{center}\n"
+ "\\end{document}\n")
file.close()

os.system("latex finite_abelian_factorization.tex")
os.system("pdflatex finite_abelian_factorization.tex")
os.system("open finite_abelian_factorization.pdf")
