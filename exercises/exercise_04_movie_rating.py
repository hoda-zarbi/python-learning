"""
Exercise 04

Topic:
- Variables
- Data Types
- Input
- Output
- Conditional Statement

Project:
movie rating

Objective:
Practice using variables, data types, user input,
conditional statements, and output by creating
a simple movie rating program.
"""
print()
# Get movie information from the user
movie_title = input("Enter Movie Title: ")
imdb_rating = float(input("Enter IMDB: "))
number_of_votes = int(input("Enter Number of Votes: "))

if imdb_rating >= 7.5 and number_of_votes >= 50:
    recommendation = "Highly Recommended!" 
    
elif imdb_rating >= 5.5 and number_of_votes >= 50:
    recommendation = "Worth Watching:)"
    
else:
    recommendation = "Not Recommended"
# Display the movie rating report
print("========================")       
print("====== Movie Rating ======")
print("Movie Title: ", movie_title)
print("IMDB Rating: ", imdb_rating)
print("Number of Votes: ", number_of_votes)
print("Recommendation: ", recommendation)
print("========================")
