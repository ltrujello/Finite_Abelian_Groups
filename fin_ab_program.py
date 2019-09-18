from finite_abelian_groups import primefac, power_count, prime_pows, decompose_ahead, produce_factors
import os 
def all_factorizations(theint):
    return produce_factors(decompose_ahead(prime_pows(primefac(theint))))
    
print("Finite abelian group of order: ")
ord = input()
try:
   val = int(eval(ord))
except ValueError:
   print("That's not an integer!")
if val < 2:
    print("Pick something bigger.")
else:
   the_factors = all_factorizations(val)

def group_fac_for_latex(list_facts):
    latex_code = ""
    for fact in list_facts:
        #latex_code += "$"
        for i in range(len(fact)):
            num = fact[i]
            if i == 0:    
                latex_code += "\\mathbb{Z}_" + "{" + str(num) + "}"
            elif i == len(fact) - 1:
                latex_code += "\\times \\mathbb{Z}_" + "{" + str(num) + "}"   
            else: 
                latex_code += "\\times \\mathbb{Z}_" + "{" + str(num) + "}" + "\\times "
        if fact != list_facts[-1]:
            latex_code += "\\\\"
    return latex_code
file = open('finite_abelian_factorization.tex', 'w')
file.write("\\documentclass[12pt,letterpaper,boxed]{maths_v5}\n" 
+ "\\usepackage[margin=0.3in]{geometry}\n" 
+ "\\usepackage{lmodern}\n" 
+ "\\usepackage{amsmath}\n"
+ "\\allowdisplaybreaks\n"
+ "\\begin{document}\n"
+ "\\begin{center}\n"
+ "Finite Abelian Groups of Order: " + str(val) + "\\newline \n"
+ "\\end{center}\n"
+ "\\begin{align}"
+ group_fac_for_latex(the_factors)
+ "\\end{align}"
+ "\\end{document}\n")
file.close()

print("All unique factorizations of " + str(val) + " are ", the_factors)
os.system("latex finite_abelian_factorization.tex")
os.system("pdflatex finite_abelian_factorization.tex")
os.system("open finite_abelian_factorization.pdf")
