  * Rewrite *login_app* to act like an API. Remove templates and
return JSON data in responses to all it's endpoints.
  * Add Order model with user_id and time of order
  * Add OrderLine model with products information (product name, and price)
  * Add additional */orders* endpoint to *login_app/main.py* secured
    by *login_required* decorator. This endpoint should return list of
    orders related to user.
  * Add create-database flask cli
