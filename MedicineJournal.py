print("MEDICINE JOURNAL")
print("A little pill to help you thrive, Keeping your best health alive.")
print("Options: cold, headache, fever, body pain, cough, sore throat,  stomach ache,  cramps, acidity, vomiting, motion sickness, diarrhoea, allergy, cut, burn")
# Ask the user for input
symptom = input("What's your symptom: ")
# Simple if-else logic to check the answer
if symptom == "cold":
    print("Suggestion: Levocetirizine, Benadryl, Censtin Cold")
    print("Avoid: cold things, sugary foods,excessive caffeine, dairy products")
elif symptom == "headache":
    print("Suggestion: Paracetamol, Ibuprofen, Saridon, Excedrin Rest")
    print("Avoid: Caffeine, stressful situations, cheese, chocolates, loud noises")
elif symptom == "fever":
     print("Suggestion: Paracetamol 500mg, Dolo 650, Calpol, Drink Water/ORSL, apply cloth cloth on head")
     print("Avoid: caffine, cold things, greasy and spicy food, cold baths")
elif symptom == "bodypain":
    print("Suggestion: Combiflam, paracetamol 500mg, Rest well")
    print("Avoid: sugar, fried foods, excessive salt,phusical exhausion")
elif symptom == "cough":
    print("Suggestion: Vicks DayQuil Cough, Benadryl Cough Formula Syrup , Cofsils, Honey & Warm Water")
    print("Avoid: cool things, sugary foods,excessive caffeine, greasy and spicy foods")
elif symptom == "sore throat":
    print("Suggestion: Strepsils, Vicks VapoCOOL,Benadryl Cough Formula Syrup, salt water gargle")
    print("Avoid: crunchy, hard, dry foods, spicy, acidic, oily foods, caffine, extreme hot or cold foods")
elif symptom == "stomach ache":
    print("Suggestion: antacids, Tylenol, Light and easily digestable food")
    print("Avoid: fatty, fried, and spicy foods, dairy products, and highly acidic foods")
elif symptom == "cramps":
    print("Suggestion: Advil, crosin, aleve, hot pack, dark chocolate")
    print("Avoid: processed foods, sugary snacks, high-sodium foods, fatty foods, caffeine, and spicy foods, physical activities")
elif symptom == "acidity":
    print("Suggestion: Pan40, Pantop, ENO, Drink Cold Milk")
    print("Avoid: fatty and fried foods, spicy ingredients, and acidic foods")
elif symptom == "vomiting":
    print("Suggestion: Avomine, domperidone, smell citrus, chew on clove")
    print("Avoid: strong odors, fatty, greasy, spicy, and strongly flavored foods, caffeine, and carbonated drinks")
elif symptom == "motion sickness":
    print("Suggestion: dramamine, cyclizine")
    print("Avoid: heavy, greasy, spicy,strong-smelling foods, reading or looking at screens, strong odors, and sitting in a rear-facing seat")
elif symptom == "diarrhoea,":
    print("Suggestion: loperamide, brakke, derolac, stay hydrated, drink lots of fluids")
    print("Avoid: fatty, fried, and spicy foods, as well as high-fiber, gassy, and dairy products, and caffine")
elif symptom == "allergy":
    print("Suggestion: Cetirizine")
    print("Avoid: dust, foods that might cause allergic rxn")
elif symptom == "cut":
    print("Suggestion: Wash it and put a Band-aid, boroplus, severe bleeding consult doctor, if it is a scratch by a metal get tetanus")
    print("Avoid: avoid using hydrogen peroxide or iodine for cleaning, picking at scabs, exposing the wound to dirt")
elif symptom == "burn":
    print("Suggestion: Put petroleum jelly  or Aloe Vera or Cold Water,cover it with a sterile, non-fluffy bandage, and seek medical attention for serious burns")
    print("Avoid: avoid applying ice, butter, toothpaste, or other greasy substances; do not break blisters; do not remove clothing stuck to the burn; and do not use fluffy cotton bandages")
else:
    print("Sorry, I don't know that one. Please see a doctor.")
# End saying to the user
print("HOPE YOU GET WELL SOON :) !!!")
