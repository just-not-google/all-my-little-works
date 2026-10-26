p_coffee_drinker = 0.65
p_cancer = 0.005
p_coffee_drinker_given_cancer = 0.85
p_cancer_given_coffee_drinker = p_coffee_drinker_given_cancer * p_cancer / p_coffee_drinker
print(p_cancer_given_coffee_drinker)