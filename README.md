# babsonscraper


**TODO:**
- [ ] we could run scheduling, so that you cannot call getPeriod("breakfast") past breakfast, since that raises an error. Instead, add 1 to the date so that it returns the breakfast menu for tomorrow. Or we could return an error like "Cant look at breakfast menu past breakfast". OR we can default to the same period of the following date, if that meal period has already passed. 
- lunch < 2
- breakfast < 11
- dinner < 8
- [ ] add ```self.portion``` into ```Food``` class and assign it in ```getFoodItems```
- [ ] get rid of asterisk in elements in ```self.filters```
- [ ] add option to specify date, perhaps by passing date as a parameter in `getPeriod(period, date=date.today())` with default value set to `date.today()`. see TODO #1, default will be next day if period has passed.
- [ ] implement flask backend and a db (mysql?) that stores menu items throughout day and purges at night to save memory?


**All attributes of a Food object are strings except nutrients and filters, which are lists of strings:** <br>
Example nutrients: <br>
```['Calories:360(kcal)', 'Protein (g):18(g)', 'Total Carbohydrates (g):25(g)', 'Sugar (g):16(g)', 'Total Fat (g):20(g)', 'Saturated Fat (g):3(g)', 'Cholesterol (mg):90(mg)', 'Dietary Fiber (g):2(g)', 'Sodium (mg):1070(mg)', 'Potassium (mg):510(mg)', 'Calcium (mg):30(mg)', 'Iron (mg):1.9(mg)', 'Trans Fat (g):-(g)', 'Vitamin D (IU):5+(IU)', 'Vitamin C (mg):33+(mg)', 'Calories From Fat:180(kcal)', 'Vitamin A (RE):50+(RE)', 'Saturated Fat + Trans Fat (g):5+(g)']``` 
<br><br> Example filters: <br>
```['allergen:Onion', 'allergen:Gluten', 'allergen:Milk', 'allergen:Wheat', 'allergen:Alcohol', 'allergen:Garlic', 'allergen:Mustard*', 'allergen:Soy', 'allergen:Orange', 'allergen:Poultry', 'allergen:Mushroom', 'allergen:Celery*', 'allergen:Sesame Seeds']``` 
</p>

