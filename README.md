here are the urls and their functions
type/          you can add and list pizza type using this url
size/          you can add and list pizza size using this url
toppings/      you can add and list pizza toppings using this url
createsquare/  you create square pizza using this endpoint  you should post in request body with parameters pizza_type,pizza_size,pizza_toppings 
               pizza toppings must be entered with comma seperator (',') ex: "tomato,onion"
createregular/ you create square pizza using this endpoint  you should post in request body with parameters pizza_type,pizza_size,pizza_toppings 
               pizza toppings must be entered with comma seperator (',') ex: "tomato,onion"  
               
getall/        you can list all the created pizza's using this endpoint 
               you can filter by using type and size  ex getall/?type=regular, getall/?size=medium
               you can filter by using both type and size  ex getall/?type=regular&size=medium
            
delete/id/     you can delete any created pizza by passing id to this endpoint ex:delete/3/
               this deletes pizza with id 3
