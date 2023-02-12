#Creating the items and prices 
medicines = {
    "Paracetamol": 10.50,
    "Loratadine": 11.80,
    "Ibuprofen": 7.25,
    "Cetirizine": 9.50,
    "Pseudoephedrine": 16.50,
    "Dextromethorphan": 8.50,
    "Phenylephrine": 12.99,
    "Fexofenadine": 12.25,
    "Metformin": 10.00,
    "Amoxicillin": 8.00,
    "Ciprofloxacin": 15.50,
    "Azithromycin": 14.50,
    "Clindamycin": 13.50,
    "Amlodipine": 9.75,
    "Lisinopril": 10.75,
    "Ventolin": 11.20,
    "Fluticasone": 16.25,
    "Budesonide": 14.99,
    "Prednisone": 12.75,
    "Prednisolone": 12.50
}

#Taking input from the user 
medicine_input = input("Enter the medicine name: ")

#Checking if the medicine is present in the list
if medicine_input in medicines:
    print(f"The cost of {medicine_input} is ${medicines[medicine_input]}")
else:
    print("Sorry, the medicine is not available in the store.")
