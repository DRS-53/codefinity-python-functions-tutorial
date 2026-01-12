def merge_shopping_lists(*shopping_lists):
    merged_list = ""  # Step 1    
 
    for shopping_list in shopping_lists: 
        merged_list += ", ".join(shopping_list) + ", "
 
    merged_list = merged_list.strip(", ")  # Step 4
    return merged_list 


# Example usage
alice_list = ['Bread', 'Milk', 'Eggs']
bob_list = ['Meat', 'Potatoes']
charlie_list = ['Fruits', 'Juice']

# Testing the result
final_shopping_list = merge_shopping_lists(alice_list, bob_list, charlie_list)
print(final_shopping_list)