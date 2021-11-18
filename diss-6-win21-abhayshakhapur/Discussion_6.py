# Discuission 6 Debugger

# This function returns the largest number
def top_list(num_list):
    print("top_list")
    sortA = sorted(num_list)
    top = sortA
    return top[0]

# This function returns the key-value pair of most populated city
def top_dict(city_dict):
    print("top_dict")
    sortB = sorted(city_dict, key=city_dict.get)
    top = sortB[0]
    return top



# Print the city and population for the top 3 cities (sorting dictionary by value)
def top_three(city_dict):
    print("top_three")
    sortC = sorted(city_dict, key=lambda x: x[1], reverse=True)
    the_three = sortC
    return the_three

# Remove cities that start with 'L'
def remove_cities(city_dict, starts_with):
    print("remove_cities")
    new_list = {}
    for i in city_dict:
        if city_dict[i] != starts_with:
            new_list = city_dict[i]
    return new_list



# Task 1: Print the largest number in the list
num_list = [3,5,22,110,238,12,183,62,682,0,532,991,3,1023,1983,1829,11,193,121,1538,10099,1223,432,5552,1083,1023,1983,1829,11,193,121,1538,10099,1223,432,5552,1083,1023,1983,1829,11,193,121,1538,10099,1223,432,5552,108243,1023,1983,1829,11,193,121,15338,10099,1223,432,5552,1083]
print(top_list(num_list))

# Task 2: Print the most populated city
city_list = {'Lima':8481415,'Bangkok':8249117,'Cairo':10230350,'Tehran':846782,'Moscow':11541000,'New Delhi':16787949, 'Lagos':14368000, 'Jakarta':10187595,'Kinshasa':10125000,'Seoul':9989795,'Mexico City':8985339,'Manila':12877253,'Dhaka':8906000,'London':8630100,'Hanoi':7587800,'Hong Kong':7482500,'Tokyo':13742906, 'Lansing': 117159}
print(top_dict(city_list))

# Task 3: Print the city and population for the top 3 cities.
print(top_three(city_list))

# Task 4: Remove cities that start with 'L'
print(remove_cities(city_list, 'L'))


