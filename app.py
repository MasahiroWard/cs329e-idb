from flask import Flask # Import Flask package
from flask import render_template # Import render_template function
app = Flask(__name__) # Construct Flask object named 'app'

'''
@app.route() defines the URLs that route to the index() function.
The URLs will be appended to the end of the base URL.
Links within HTML files should use the defined routes (for example '/index') as
the values for href attributes.

URLs that will call the index() function if running app.py on localhost:
	http://localhost:5000/
	http://localhost:5000/index
'''
@app.route('/') # URL for function (default for home page)
@app.route('/index') # Secondary URL for function
def index():
	return render_template('index.html') # located in templates/
	
@app.route('/cuisine')
def cuisine():
	return render_template('Cuisine.html')
	
@app.route('/recipe')
def recipe():
	return render_template('Recipe.html')
	
@app.route('/ingredients')
def ingredients():
	return render_template('Ingredients.html')
	
@app.route('/about')
def about():
	return render_template('About.html')

@app.route('/cuisine_jap')
def cuisine_jap():
	return render_template('Cuisine_Japanese.html')

@app.route('/cuisine_ind')
def cuisine_ind():
	return render_template('Cuisine_Indian.html')

@app.route('/cuisine_french')
def cuisine_french():
	return render_template('Cuisine_French.html')		

@app.route('/cuisine_chi')
def cuisine_chi():
	return render_template('Cuisine_Chinese.html')		

@app.route('/cuisine_filipino')
def cuisine_filipino():
	return render_template('Cuisine_Filipino.html')		

@app.route('/cuisine_greek')
def cuisine_greek():
	return render_template('Cuisine_Greek.html')		

@app.route('/recipe_cps')
def recipe_cps():
	return render_template('Recipe_chinesepeppersteak.html')

@app.route('/recipe_ic')
def recipe_ic():
	return render_template('Recipe_indiancurry.html')
	
@app.route('/recipe_gca')
def recipe_gca():
	return render_template('Recipe_grilledchickenadobo.html')
	
@app.route('/recipe_lbs')
def recipe_lbs():
	return render_template('Recipe_lemonbutterscallops.html')
	
@app.route('/recipe_m')
def recipe_m():
	return render_template('Recipe_moussaka.html')
	
@app.route('/recipe_s')
def recipe_s():
	return render_template('Recipe_sushi.html')
	
@app.route('/ingredients_ss')
def ingredients_ss():
	return render_template('Ingredient_SoySauce.html')
	
@app.route('/ingredients_bl')
def ingredients_bl():
	return render_template('Ingredient_BayLeaves.html')	
	
@app.route('/ingredients_m')
def ingredients_m():
	return render_template('Ingredient_Milk.html')	
	
@app.route('/ingredients_t')
def ingredients_t():
	return render_template('Ingredient_Turmeric.html')	
	
@app.route('/ingredients_wr')
def ingredients_wr():
	return render_template('Ingredient_Whiterice.html')	
	
@app.route('/ingredients_w')
def ingredients_w():
	return render_template('Ingredient_Wine.html')	

	
if __name__ == '__main__':
	app.run('107.170.30.222','80') # Run application