# Important: as of November 28th this project needs to be ran locally as Heroku which was the hosting it, has closed its free tier services.


# hiddenInMyKitchenRecipes

APP available at: https://github.com/sylleryum/hiddenInMyKitchenRecipes<br>
Rest API for this APP available here: https://github.com/sylleryum/hiddenInMyKitchenRecipesFrontend

Find recipes based on ingredients used or ingredients that you have <br>
(This repo is for the Backend Rest API only, Angular frontend is available at https://github.com/sylleryum/hiddenInMyKitchenRecipesFrontend)

## POST Endpoints

### Endpoints/auth/users: create new user
* body: 
{
"username": "chooseUser",
"password": "choosePWD"
}


### Endpoints/auth/token/login: login with username/password to receive token
* body: 
{
"username": "chooseUser",
"password": "choosePWD"
}
* on success: auth_token received

## GET Endpoints
**All get requests need to include header with key = Authorization, value = Token YOUR AUTH_TOKEN RECEIVED FROM /auth/token/login**

* /ingredients: provides a list of all ingredients available

* /search?ingredients={ingredientsCommaSeparated}: searchs recipes based on ingredients, comma separated

* /recipe/{recipeID}: returns the recipe from ID provided (ID is received on search)
