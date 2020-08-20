# session5-anilbhatt1

# Arguments & Parameters; Positional and Keyword Arguments

* **Positional arguments** are arguments that can be called by their position in the function definition.

* **Keyword arguments** are arguments that can be called by their name.

* **Required arguments** are arguments that must be passed to the function.

* **Optional arguments** are argument that can be not passed to function. In python, optional arguments are arguments that have a default value.

# Unpacking

* **Packed Value**  Values are bundled together in some way. Any iterable can be considered as packed value
     * List
     * Tuple
     * String
     * Dictionaries
* **Unpacking** is act of splitting into individual variables contained in List or Tuple
* The Unpacking into individual variables is based on positions of each element
* Dictionaries and sets can be iterated, but there is no guarantee in the order of result match with iterable.


# Extended Unpacking
* We achieve Extended Unpacking using * and ** operator
* `*` Unpacking Operator
   * `*` operator used will unpacks whatever values comes after this operator to a variable
   * `*` Operator must be used only **`ONCE`** in the LHS unpacking assignment. It can be used to RHS only when concatenating two lists
   * `*` Operator can be used with set and dictionaries but the order has no guarantee and dictionaries will iterate with keys but not with values.

* `**` Unpacking Operator
   * `**` Operator can helps us to unpack key: value pair of dictionaries.
   * `**` Operator cannot be used on LHS of an assignment.
   * `**` whenever we try to concatenate two dictionaries, duplicates will be removed and there is no guarantee of order
  
* Python supports Nested Unpacking

# *args
* Exhaust optional arguments
* We cannot add more arguments after the *args

# Keyword Arguments
* Python allows functions to be called using keyword arguments. When we call functions in this way, the order (position) of the arguments can be changed.

# License
[MIT](https://choosealicense.com/licenses/mit/)


# Funcitons Used
 time_it
 squared_power_list
 polygon_area
 temp_converter
 speed_converter
