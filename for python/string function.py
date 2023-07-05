Some_countries_name= "Pakistan,USA,Canada,  Australia"
print(Some_countries_name)
print(len(Some_countries_name))
print(Some_countries_name.endswith("Australia"))
print(Some_countries_name.count("Pakistan"))
print(Some_countries_name.capitalize())#it makes first letter capital
print(Some_countries_name.find("Cary"))
print(Some_countries_name.replace("USA","Turkey"))
double_spaces= Some_countries_name.find("  ")
print(double_spaces)
Some_countries_name=Some_countries_name.replace("  "," ")
print(Some_countries_name)