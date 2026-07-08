pasta=("alfredo","italian",20,"medium")
samosa=("chicken samosa","pakistani",15,"easy")
print("recipe 1:",pasta)
print("name:",pasta[0])
print("cuisine:",pasta[1])
print("difficulty:",pasta[-1])

all_recipes=(pasta,samosa)
print("first recipe name:",all_recipes[0][0])
print("second recipe time:",all_recipes[1][2],"minutes")
print("samosa details sliced:",all_recipes[1:3])

print("pasta recipe details")
for details in pasta:
    print("-",details)

pasta_ingrediants={"olive oil","garlic","pasta","milk","seasoning","tomato paste"}
samosa_ingrediants={"samosa patty","minced chicken","seasoning"}
print("pasta ingrediants:",pasta_ingrediants)
print("samosa ingrediants:",samosa_ingrediants)   
print("total pasta ingrediants:",len(pasta_ingrediants)) 
pasta_ingrediants.add("cheese")
pasta_ingrediants.discard("tomato paste")
print("updated pasta recipe:",pasta_ingrediants)

samosa_ingrediants.add("olive oil")
print("updated samosa ingrediants:",samosa_ingrediants)

all_ingrediants=pasta_ingrediants.union(samosa_ingrediants)
common_ingrediants=pasta_ingrediants.intersection(samosa_ingrediants)
only_pasta=pasta_ingrediants.difference(samosa_ingrediants)
only_samosa=samosa_ingrediants.difference(pasta_ingrediants)
non_common_ingrediants=pasta_ingrediants.symmetric_difference(samosa_ingrediants)
print("all ingrediants:",all_ingrediants)
print("common ingrediants:",common_ingrediants)
print("ingrediants of pasta:",only_pasta)
print("ingediants of samosa:",only_samosa)
print("non common ingrediants:",non_common_ingrediants)