from flask import Flask, render_template, url_for, request, session, redirect, url_for
import json

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Change this to a secure random value

linear_eq_questions = [
  {
  "id": 1,
  "type": "multiple-choice",
  "question": "",
  "choices": [
    "A) 51",
    "B) 350",
    "C) 364",
    "D) 3,577"
  ],
  "image": "/static/March2025_Images/Algebra/LinearEquationsInOneVariable/12143_1.png",
  "difficulty": "easy",
  "active": "no",
  "marked": False,
  "answer": "B) 350",
  "explanation": "Choice B is correct. Subtracting 7 from each side of the given equation yields w = 350. Therefore, the value of w that is the solution to the given equation is 350.\n\nChoice A is incorrect. This is the value of w that is the solution to the equation 7w = 357, not w + 7 = 357. \nChoice C is incorrect. This is the value of w that is the solution to the equation w - 7 = 357, not w + 7 = 357.\n\nChoice D is incorrect and may result from conceptual or calculation errors."
},
{
  "id": 2,
  "type": "multiple-choice",
  "question": "",
  "choices": [
    "A) 1.90p + 2 = 9.60",
    "B) 1.90p - 2 = 9.60",
    "C) 1.90 + 2p = 9.60",
    "D) 1.90 - 2p = 9.60"
  ],
  "image": "/static/March2025_Images/Algebra/LinearEquationsInOneVariable/12149_2.png",
  "difficulty": "easy",
  "active": "no",
  "marked": False,
  "answer": "A) 1.90p + 2 = 9.60",
  "explanation": "Choice A is correct. It's given that p represents the number of pounds of strawberries Lorenzo purchased and Lorenzo paid $1.90 per pound for the strawberries. It follows that the total amount, in dollars, Lorenzo paid for strawberries can be represented by 1.90p. It's given that Lorenzo paid $2 for the box of cereal. If Lorenzo paid a total of $9.60 for the box of cereal and strawberries, it follows that the equation 1.90p + 2 = 9.60 can be used to find p. Choice B is incorrect and may result from conceptual errors. Choice C is incorrect and may result from conceptual errors. Choice D is incorrect and may result from conceptual errors."
},
{
  "id": 3,
  "type": "multiple-choice",
  "question": "",
  "choices": [
    "A) 35",
    "B) 130",
    "C) 165",
    "D) 330"
  ],
  "image": "/static/March2025_Images/Algebra/LinearEquationsInOneVariable/12165_3.png",
  "difficulty": "easy",
  "active": "no",
  "marked": False,
  "answer": "A) 35",
  "explanation": "Choice A is correct. It's given that a total of 165 people contributed to a charity event as either a donor or a volunteer. It's also given that 130 people contributed as a donor. It follows that 165 - 130, or 35, people contributed as a volunteer. Choice B is incorrect. This is the number of people who contributed as a donor, not a volunteer. Choice C is incorrect. This is the total number of people who contributed as either a donor or a volunteer, not the number of people who contributed as a volunteer. Choice D is incorrect and may result from conceptual or calculation errors."
},
{
  "id": 4,
  "type": "free-response",
  "question": "",
  "choices": [],
  "image": "/static/March2025_Images/Algebra/LinearEquationsInOneVariable/12167_4.png",
  "difficulty": "medium",
  "active": "no",
  "marked": False,
  "answer": "42",
  "explanation": "The correct answer is 42. The expression (x + 6) is a factor of both terms on the left-hand side of the given equation. Therefore, the given equation can be written as (x + 6) (1/3 − 1/2) = −8, or (x + 6) (−1/6) = −8. Multiplying each side of this equation by −6 yields x + 6 = 48. Subtracting 6 from each side of this equation yields x = 42. Therefore, the value of x that is the solution to the given equation is 42."
},
{
  "id": 5,
  "type": "multiple-choice",
  "question": "",
  "choices": [
    "A) 16x = 30",
    "B) 16x = 130",
    "C) 16x = 160",
    "D) 16x = 190"
  ],
  "image": "/static/March2025_Images/Algebra/LinearEquationsInOneVariable/12174_5.png",
  "difficulty": "easy",
  "active": "no",
  "marked": False,
  "answer": "C) 16x = 160",
  "explanation": "Choice C is correct. It's given that 16x + 30 = 190. Subtracting 30 from each side of this equation yields 16x = 160. Therefore, the equation 16x = 160 is equivalent to the given equation and has the same solution. Choice A is incorrect and may result from conceptual or calculation errors. Choice B is incorrect and may result from conceptual or calculation errors. Choice D is incorrect and may result from conceptual or calculation errors."
},
{
  "id": 6,
  "type": "multiple-choice",
  "question": "",
  "choices": [
    "A) 9/2",
    "B) 6",
    "C) 18",
    "D) 72"
  ],
  "image": "/static/March2025_Images/Algebra/LinearEquationsInOneVariable/12175_6.png",
  "difficulty": "easy",
  "active": "no",
  "marked": False,
  "answer": "C) 18",
  "explanation": "Choice C is correct. It's given that 4x = 3. Multiplying each side of this equation by 6 yields 24x = 18. Therefore, the value of 24x is 18. Choice A is incorrect. This is the value of 6x, not 24x. Choice B is incorrect. This is the value of 8x, not 24x. Choice D is incorrect. This is the value of 96x, not 24x."
},
{
  "id": 7,
  "type": "free-response",
  "question": "",
  "choices": [],
  "image": "/static/March2025_Images/Algebra/LinearEquationsInOneVariable/12179_7.png",
  "difficulty": "easy",
  "active": "no",
  "marked": False,
  "answer": "0.2",
  "explanation": "The correct answer is .2. Subtracting 2.6 from each side of the given equation yields x = 0.2. Therefore, the value of x that’s the solution to the given equation is 0.2. Note that .2 and 1/5 are examples of ways to enter a correct answer."
},
{
  "id": 8,
  "type": "free-response",
  "question": "",
  "choices": [],
  "image": "/static/March2025_Images/Algebra/LinearEquationsInOneVariable/12181_8.png",
  "difficulty": "medium",
  "active": "no",
  "marked": False,
  "answer": "294",
  "explanation": "The correct answer is 294. Subtracting 18 from each side of the given equation yields (7/6)p = 36. Multiplying each side of this equation by (6/7) yields p = 42. Multiplying each side of this equation by 7 yields 7p = 294. Therefore, the value of 7p is 294."
},
{
  "id": 9,
  "type": "multiple-choice",
  "question": "",
  "choices": [
    "A) 3",
    "B) 7",
    "C) 36",
    "D) 44"
  ],
  "image": "/static/March2025_Images/Algebra/LinearEquationsInOneVariable/12185_9.png",
  "difficulty": "medium",
  "active": "no",
  "marked": False,
  "answer": "D) 44",
  "explanation": "Choice D is correct. It's given that the bowl starts with 20 ounces of water and has 9 ounces of water remaining after a period of time has passed. The amount of water the bowl has lost during the time period can be found by subtracting the remaining amount of water from the original amount of water, which yields 20 - 9 ounces, or 11 ounces. It's uncovered, it follows that 1/4 = 11/t. Multiplying both sides of this equation by 4t yields t = 44. Therefore, the bowl has been uncovered for 44 days. Choice A is incorrect and may result from conceptual or calculation errors. Choice B is incorrect and may result from conceptual or calculation errors. Choice C is incorrect. This is the value of t for the equation 1/4 = 9/t, not 1/4 = 11/t."
},
{
  "id": 10,
  "type": "free-response",
  "question": "",
  "choices": [],
  "image": "/static/March2025_Images/Algebra/LinearEquationsInOneVariable/12187_10.png",
  "difficulty": "hard",
  "active": "no",
  "marked": False,
  "answer": "11",
  "explanation": "The correct answer is 11. Subtracting 5 from each side of the given equation yields −7(2 − 4x) = 11 − 8(2 − 4x). Adding 8(2 − 4x) to each side of this equation yields 2 − 4x = 11. Therefore, the value of 2 − 4x is 11."
},
{
  "id": 11,
  "type": "multiple-choice",
  "question": "",
  "choices": [
    "A) 5",
    "B) 25",
    "C) 48",
    "D) 300"
  ],
  "image": "/static/March2025_Images/Algebra/LinearEquationsInOneVariable/12195_11.png",
  "difficulty": "easy",
  "active": "no",
  "marked": False,
  "answer": "B) 25",
  "explanation": "Choice B is correct. Subtracting 275 from both sides of the given equation yields 2p = 50. Dividing both sides of this equation by 2 yields p = 25. Therefore, the value of p that satisfies the given equation is 25. Choice A is incorrect and may result from conceptual or calculation errors. Choice C is incorrect. This is the value of p that satisfies the equation (2 + p) + 275 = 325, not 2p + 275 = 325. Choice D is incorrect. This is the value of p that satisfies the equation 2p − 275 = 325, not 2p + 275 = 325."
},
{
  "id": 12,
  "type": "multiple-choice",
  "question": "",
  "choices": [
    "A) 3",
    "B) 15",
    "C) 54",
    "D) 57"
  ],
  "image": "/static/March2025_Images/Algebra/LinearEquationsInOneVariable/12198_12.png",
  "difficulty": "easy",
  "active": "no",
  "marked": False,
  "answer": "C) 54",
  "explanation": "Choice C is correct. It's given that 8x = 6. Multiplying each side of this equation by 9 yields 72x = 54. Therefore, the value of 72x is 54. Choice A is incorrect. This is the value of 4x, not 72x. Choice B is incorrect and may result from conceptual or calculation errors. Choice D is incorrect and may result from conceptual or calculation errors."
},
{
  "id": 13,
  "type": "multiple-choice",
  "question": "",
  "choices": [
    "A) -16",
    "B) -4",
    "C) 4",
    "D) 16"
  ],
  "image": "/static/March2025_Images/Algebra/LinearEquationsInOneVariable/12199_13.png",
  "difficulty": "medium",
  "active": "no",
  "marked": False,
  "answer": "D) 16",
  "explanation": "Choice D is correct. The value of 4 - 3x can be found by isolating this expression in the given equation. Subtracting 2 from both sides of the given equation yields 9(4 - 3x) = 8(4 - 3x) + 16. Subtracting 8(4 - 3x) from both sides of this equation yields 9(4 - 3x) - 8(4 - 3x) = 16, which gives 1(4 - 3x) = 16, or 4 - 3x = 16. Therefore, the value of 4 - 3x is 16. Choice A is incorrect and may result from conceptual or calculation errors. Choice B is incorrect. This is the value of x, not 4 - 3x. Choice C is incorrect and may result from conceptual or calculation errors."
}
]

linear_functions_questions = [
  {
  "id": 1,
  "type": "multiple-choice",
  "question": "",
  "choices": [
    "A) 50",
    "B) 57",
    "C) 80",
    "D) 110"
  ],
  "image": "/static/March2025_Images/Algebra/LinearFunctions/12138_1.png",
  "difficulty": "easy",
  "active": "no",
  "marked": False,
  "answer": "C) 80",
  "explanation": "Choice C is correct. It's given that the function f is defined by f(x) = 25x + 30. Substituting 2 for x in this equation yields f(2) = 25(2) + 30, which is equivalent to f(2) = 50 + 30, or f(2) = 80. Therefore, the value of f(x) is 80 when x = 2.\n\nChoice A is incorrect. This is the value of 25(2), not 25(2) + 30.\nChoice B is incorrect. This is the value of 25 + 2 + 30, not 25(2) + 30.\nChoice D is incorrect. This is the value of (25 + 30)(2), not 25(2) + 30."
},
{
  "id": 2,
  "type": "multiple-choice",
  "question": "",
  "choices": [
    "A) 0",
    "B) 1",
    "C) 4",
    "D) 7"
  ],
  "image": "/static/March2025_Images/Algebra/LinearFunctions/12140_2.png",
  "difficulty": "easy",
  "active": "no",
  "marked": False,
  "answer": "A) 0",
  "explanation": "Choice A is correct. For the linear function f, it’s given that f(7) = 28. Substituting 7 for x and 28 for f(x) in the given function yields 28 = 4(7) + b, or 28 = 28 + b. Subtracting 28 from each side of this equation yields 0 = b. Therefore, the value of b is 0.\n\nChoice B is incorrect. Substituting 1 for b in the given function yields f(x) = 4x + 1. For this function, when the value of x is 7, the value of f(x) is 29, not 28.\nChoice C is incorrect. Substituting 4 for b in the given function yields f(x) = 4x + 4. For this function, when the value of x is 7, the value of f(x) is 32, not 28.\nChoice D is incorrect. Substituting 7 for b in the given function yields f(x) = 4x + 7. For this function, when the value of x is 7, the value of f(x) is 35, not 28."
},
{
  "id": 3,
  "type": "free-response",
  "question": "",
  "choices": [],
  "image": "/static/March2025_Images/Algebra/LinearFunctions/12144_3.png",
  "difficulty": "medium",
  "active": "no",
  "marked": False,
  "answer": "67",
  "explanation": "The correct answer is 67. It is given that f(5) = 32. Therefore, for the given function f, when x = 5, f(x) = 32. Substituting 5 for x and 32 for f(x) in the given function f(x) = 4x + k(x − 1) yields 32 = 4(5) + k(5 − 1), or 32 = 20 + 4k. Subtracting 20 from each side of this equation yields 12 = 4k. Dividing each side of this equation by 4 yields k = 3. Substituting 3 for k in the given function f(x) = 4x + k(x − 1) yields f(x) = 4x + 3(x − 1), which is equivalent to f(x) = 4x + 3x − 3, or f(x) = 7x − 3. Substituting 10 for x into this equation yields f(10) = 7(10) − 3, or f(10) = 67. Therefore, the value of f(10) is 67."
},
{
  "id": 4,
  "type": "multiple-choice",
  "question": "",
  "choices": [
    "A) h(x) = 5x - 4",
    "B) h(x) = 5x + 7",
    "C) h(x) = 5x + 20",
    "D) h(x) = 5x + 25"
  ],
  "image": "/static/March2025_Images/Algebra/LinearFunctions/12156_4.png",
  "difficulty": "hard",
  "active": "no",
  "marked": False,
  "answer": "B) h(x) = 5x + 7",
  "explanation": "Choice B is correct. An equation that defines a linear function f can be written in the form f(x) = mx + b, where m and b are constants. It's given in the table that when x = -4, f(x) = 0. So 0 = m(-4) + b implies that 0 = -4m + b. Adding 4m to both sides yields b = 4m. Substituting 4m for b gives f(x) = mx + 4m. It's also given that when x = 19/5, f(x) = 5. So 5 = m(19/5) + 4m. Multiplying both sides by 5 yields 25 = 19m + 20m, or 25 = 39m. Solving for m gives m = 25/39. Substituting 5 for m in f(x) = mx + 4m gives f(x) = 5x + 20. Since h(x) = f(x) + 7, then h(x) = (5x + 20) + 7 = 5x + 27.\n\nChoice A is incorrect and may result from conceptual or calculation errors.\nChoice C is incorrect and may result from calculation error.\nChoice D is incorrect. This is an equation that defines the linear function f, not h."
},
{
  "id": 5,
  "type": "free-response",
  "question": "",
  "choices": [],
  "image": "/static/March2025_Images/Algebra/LinearFunctions/12158_5.png",
  "difficulty": "medium",
  "active": "no",
  "marked": False,
  "answer": "2850",
  "explanation": "The correct answer is 2,850. It's given that the function f(x) = 45x + 600 gives the monthly fee, in dollars, a facility charges to keep x crates in storage. Substituting 50 for x in this function yields f(50) = 45(50) + 600, or f(50) = 2,850. Therefore, the monthly fee, in dollars, the facility charges to keep 50 crates in storage is 2,850."
},
{
  "id": 6,
  "type": "free-response",
  "question": "",
  "choices": [],
  "image": "/static/March2025_Images/Algebra/LinearFunctions/12159_6.png",
  "difficulty": "medium",
  "active": "no",
  "marked": False,
  "answer": "45",
  "explanation": "The correct answer is 45. It's given that h(0) = 45. Therefore, for the given function h, when x = 0, h(x) = 45. Substituting 0 for x and 45 for h(x) in the given function, h(x) = x + b, yields 45 = 0 + b, or 45 = b. Therefore, the value of b is 45."
},
{
  "id": 7,
  "type": "free-response",
  "question": "",
  "choices": [],
  "image": "/static/March2025_Images/Algebra/LinearFunctions/12162_7.png",
  "difficulty": "easy",
  "active": "no",
  "marked": False,
  "answer": "1",
  "explanation": "The correct answer is 1. It's given that the function f is defined by f(x) = x + 8/11. Substituting 3/11 for x in the given function yields f(3/11) = 3/11 + 8/11, which gives f(3/11) = 11/11 or f(3/11) = 1. Therefore, when x = 3/11, the value of f(x) is 1."
},
{
  "id": 8,
  "type": "multiple-choice",
  "question": "",
  "choices": [
    "A) S = w / 170",
    "B) S = 170w",
    "C) S = 340w",
    "D) S = w / 85"
  ],
  "image": "/static/March2025_Images/Algebra/LinearFunctions/12163_8.png",
  "difficulty": "hard",
  "active": "no",
  "marked": False,
  "answer": "D) S = w / 85",
  "explanation": "Choice D is correct. It's given that w represents the total fence area, in square feet. Since the fence will be stained twice, the total stain, in gallons, will need to cover 2w square feet. It's also given that one gallon of stain will cover 170 square feet. Dividing the total area to be stained by the number of square feet covered by one gallon gives the number of gallons needed. Dividing 2w by 170 yields (2w)/170, or w/85. Therefore, the equation that represents the total amount of stain S, in gallons, needed to stain the fence of the yard twice is S = w / 85.\n\nChoice B is incorrect and may result from conceptual or calculation errors.\nChoice C is incorrect and may result from conceptual or calculation errors."
},
{
  "id": 9,
  "type": "multiple-choice",
  "question": "",
  "choices": [
    "A) The tree will be measured each year for 4 years.",
    "B) The tree is estimated to grow to a maximum height of 4 feet.",
    "C) The estimated height of the tree increased by 4 feet each year.",
    "D) The estimated height of the tree was 4 feet when it was first measured."
  ],
  "image": "/static/March2025_Images/Algebra/LinearFunctions/12164_9.png",
  "difficulty": "easy",
  "active": "no",
  "marked": False,
  "answer": "D) The estimated height of the tree was 4 feet when it was first measured.",
  "explanation": "Choice D is correct. It's given that the function f(x) = 8x + 4 gives the estimated height, in feet, of a willow tree x years after its height was first measured. For a function defined by an equation of the form f(x) = mx + b, where m and b are constants, b represents the value of f(x) when x = 0. It follows that in this function, 4 represents the value of f(x) when x = 0. Therefore, the best interpretation of 4 in this context is that the estimated height of the tree was 4 feet when it was first measured.\n\nChoice A is incorrect and may result from conceptual errors.\nChoice B is incorrect and may result from conceptual errors.\nChoice C is incorrect and may result from conceptual errors."
},
{
  "id": 10,
  "type": "multiple-choice",
  "question": "",
  "choices": [
    "A) 20",
    "B) 12",
    "C) 10",
    "D) 5"
  ],
  "image": "/static/March2025_Images/Algebra/LinearFunctions/12170_10.png",
  "difficulty": "easy",
  "active": "no",
  "marked": False,
  "answer": "D) 5",
  "explanation": "Choice D is correct. It's given that the function f is defined by f(x) = 1/2(x + 6). Substituting 4 for x in the given function yields f(4) = 1/2(4 + 6), or f(4) = 1/2(10), which equals 5. Therefore, the value of f(4) is 5.\n\nChoice A is incorrect. This is the value of 2(4 + 6), not 1/2(4 + 6).\nChoice B is incorrect. This is the value of 2 + (4 + 6), not 1/2(4 + 6).\nChoice C is incorrect. This is the value of 4 + 6, not 1/2(4 + 6)."
},
{
  "id": 11,
  "type": "free-response",
  "question": "",
  "choices": [],
  "image": "/static/March2025_Images/Algebra/LinearFunctions/12183_11.png",
  "difficulty": "easy",
  "active": "no",
  "marked": False,
  "answer": "224",
  "explanation": "The correct answer is 224. It's given that a student council group uses the function p(x) = 5x − 220 to determine their profit p(x) in dollars, for selling x school posters. Substituting 900 for p(x) in the given function yields 900 = 5x − 220. Adding 220 to each side of this equation yields 1,120 = 5x. Dividing each side of this equation by 5 yields 224 = x. Therefore, in order to earn a profit of $900, they must sell 224 school posters."
},
{
  "id": 12,
  "type": "multiple-choice",
  "question": "",
  "choices": [
    "A) When f(x) = 0, the number is -19/4.",
    "B) When the number is 0, f(x) = 19.",
    "C) The value of f(x) increases by 1 for each increase of 4 in the value of x.",
    "D) For each increase of 1 in the value of the number, f(x) increases by 4."
  ],
  "image": "/static/March2025_Images/Algebra/LinearFunctions/12186_12.png",
  "difficulty": "hard",
  "active": "no",
  "marked": False,
  "answer": "A) When f(x) = 0, the number is -19/4.",
  "explanation": "Choice A is correct. The function f(x) is defined as 19 more than 4 times a number x, represented by the equation f(x) = 4x + 19. The x-intercept of the graph is the point where f(x) = 0. Substituting 0 for f(x) gives 0 = 4x + 19. Solving this yields x = -19/4. Therefore, when f(x) = 0, the number x = -19/4.\n\nChoice B is incorrect. This describes the y-intercept, not the x-intercept.\nChoice C is incorrect and may result from conceptual or calculation errors.\nChoice D is incorrect. This describes the slope, not the x-intercept."
},
{
  "id": 13,
  "type": "multiple-choice",
  "question": "",
  "choices": [
    "A) 15c / 4",
    "B) 19c / 4 + 7",
    "C) 61c / 4 + 105",
    "D) 15c + 105"
  ],
  "image": "/static/March2025_Images/Algebra/LinearFunctions/12190_13.png",
  "difficulty": "hard",
  "active": "no",
  "marked": False,
  "answer": "C) 61c / 4 + 105",
  "explanation": "Choice C is correct. It's given that g(c + 7) = c / 4. Therefore, for the linear function g(x) = b - 15x, substituting c + 7 for x and c / 4 for g(x) gives c / 4 = b - 15(c + 7). Applying the distributive property yields c / 4 = b - 15c - 105. Adding 15c to both sides gives c / 4 + 15c = b - 105. Then adding 105 to both sides yields c / 4 + 15c + 105 = b. Combining terms gives b = 61c / 4 + 105.\n\nChoice A is incorrect and may result from conceptual or calculation errors.\nChoice B is incorrect and may result from conceptual or calculation errors.\nChoice D is incorrect and may result from conceptual or calculation errors."
},
{
  "id": 14,
  "type": "multiple-choice",
  "question": "",
  "choices": [
    "A) 49",
    "B) 52",
    "C) 57",
    "D) 84"
  ],
  "image": "/static/March2025_Images/Algebra/LinearFunctions/12193_14.png",
  "difficulty": "easy",
  "active": "no",
  "marked": False,
  "answer": "D) 84",
  "explanation": "Choice D is correct. To find the value of f(x) when x = -8, substitute -8 into the function: f(-8) = -3(-8) + 60 = 24 + 60 = 84. Therefore, when x = -8, the value of f(x) is 84.\n\nChoice A is incorrect. This is the value of (-3 + (-8)) + 60, not -3(-8) + 60.\nChoice B is incorrect. This is the value of -8 + 60, not -3(-8) + 60.\nChoice C is incorrect. This is the value of -3 + 60, not -3(-8) + 60."
},
{
  "id": 15,
  "type": "multiple-choice",
  "question": "",
  "choices": [
    "A) C(d) = 26d + 26",
    "B) C(d) = 26d + 52",
    "C) C(d) = 52d + 26",
    "D) C(d) = 52d + 78"
  ],
  "image": "/static/March2025_Images/Algebra/LinearFunctions/12196_15.png",
  "difficulty": "hard",
  "active": "no",
  "marked": False,
  "answer": "A) C(d) = 26d + 26",
  "explanation": "Choice A is correct. The cost of renting a carpet cleaner is $52 for the first day and $26 for each additional day. For d days, the total cost is $52 + $26(d - 1). Simplifying this expression gives C(d) = 52 + 26d - 26 = 26d + 26.\n\nChoice B is incorrect. This assumes the first day costs $78 instead of $52.\nChoice C is incorrect. This reverses the rates, using $52 per additional day and $26 for the first day.\nChoice D is incorrect. This assumes both the daily rate and first-day cost are $52, totaling $130 for the first day."
}
]

linear_eq_two_questions = [
  {
  "id": 1,
  "type": "free-response",
  "question": "",
  "choices": [],
  "image": "/static/March2025_Images/Algebra/LinearEquationsInTwoVariables/12142_1.png",
  "difficulty": "hard",
  "active": "no",
  "marked": False,
  "answer": "1/4",
  "explanation": "The correct answer is 1/4. For an equation in slope-intercept form y = mx + b, m represents the slope of the line in the xy-plane defined by this equation. It's given that line l is defined by 3y + 12x = 5. Subtracting 12x from both sides of this equation yields 3y = −12x + 5. Dividing both sides of this equation by 3 yields y = −4x + 5/3. Thus, the slope of line l in the xy-plane is −4. Since line n is perpendicular to line l in the xy-plane, the slope of line n is the negative reciprocal of the slope of line l. The negative reciprocal of −4 is −1/(−4) = 1/4."
},
{
  "id": 2,
  "type": "multiple-choice",
  "question": "",
  "choices": [
    "A) 7/17",
    "B) 17/7",
    "C) 4",
    "D) 17"
  ],
  "image": "/static/March2025_Images/Algebra/LinearEquationsInTwoVariables/12147_2.png",
  "difficulty": "medium",
  "active": "no",
  "marked": False,
  "answer": "B) 17/7",
  "explanation": "Choice B is correct. It's given that line k is defined by y = (17x)/7 + 4. For an equation of a line written in the form y = mx + b, m is the slope of the line and b is the y-coordinate of the y-intercept. It follows that the slope of line k is 17/7. It's also given that line j is parallel to line k in the xy-plane. Since parallel lines have equal slopes, line j also has a slope of 17/7.\n\nChoice A is incorrect and may result from conceptual or calculation errors.\nChoice C is incorrect. This is the y-coordinate of the y-intercept of line k, not the slope of line j.\nChoice D is incorrect and may result from conceptual or calculation errors."
},
{
  "id": 3,
  "type": "multiple-choice",
  "question": "",
  "choices": [
    "A) The average number of trees per hectare in the industrial park",
    "B) The average number of trees per hectare in the neighborhood",
    "C) The total number of trees in the industrial park",
    "D) The total number of trees in the neighborhood"
  ],
  "image": "/static/March2025_Images/Algebra/LinearEquationsInTwoVariables/12150_3.png",
  "difficulty": "medium",
  "active": "no",
  "marked": False,
  "answer": "A) The average number of trees per hectare in the industrial park",
  "explanation": "Choice A is correct. It's given that a certain township consists of a 5-hectare industrial park and a 24-hectare neighborhood and that the total number of trees in the township is 4,529. It's also given that the equation 5x + 24y = 4,529 represents this situation. Since the total number of trees for a given area can be determined by taking the size of the area, in hectares, times the average number of trees per hectare, the best interpretation of 5x is the number of trees in the industrial park and the best interpretation of 24y is the number of trees in the neighborhood. Since 5 is the size of the industrial park, in hectares, the best interpretation of x is the average number of trees per hectare in the industrial park.\n\nChoice B is incorrect and may result from conceptual errors.\nChoice C is incorrect and may result from conceptual errors.\nChoice D is incorrect and may result from conceptual errors."
},
{
  "id": 4,
  "type": "free-response",
  "question": "",
  "choices": [],
  "image": "/static/March2025_Images/Algebra/LinearEquationsInTwoVariables/12152_4.png",
  "difficulty": "medium",
  "active": "no",
  "marked": False,
  "answer": "46",
  "explanation": "The correct answer is 46. It's given that a chemist combines water and acetic acid to make a mixture with a volume of 56 milliliters (mL) and that the volume of acetic acid in the mixture is 10 mL. Let x represent the volume of water, in mL, in the mixture. The equation x + 10 = 56 represents this situation. Subtracting 10 from both sides of this equation yields x = 46. Therefore, the volume of water, in mL, in the mixture is 46."
},
{
  "id": 5,
  "type": "multiple-choice",
  "question": "",
  "choices": [
    "A) (0, 4)",
    "B) (0, 6)",
    "C) (0, 16)",
    "D) (0, 28)"
  ],
  "image": "/static/March2025_Images/Algebra/LinearEquationsInTwoVariables/12153_5.png",
  "difficulty": "medium",
  "active": "no",
  "marked": False,
  "answer": "A) (0, 4)",
  "explanation": "Choice A is correct. When the graph of an equation in the form Ax + By = C is shifted down k units in the y-plane, the resulting graph can be represented by Ax + B(y + k) = C. For example, the graph of 27x + 33y = 297 is shifted down 5 units, resulting in 27x + 33(y + 5) = 297, or 27x + 33y + 165 = 297. Subtracting 165 from both sides yields 27x + 33y = 132. To find the y-intercept, substitute 0 for x: 33y = 132, so y = 4. Therefore, the y-intercept of the resulting graph is (0, 4).\n\nChoice B is incorrect and may result from conceptual or calculation errors.\nChoice C is incorrect. This is the y-intercept of the graph shifted up 5 units, not down.\nChoice D is incorrect and may result from conceptual or calculation errors."
},
{
  "id": 6,
  "type": "multiple-choice",
  "question": "",
  "choices": [
    "A) -2",
    "B) -5/6",
    "C) 6",
    "D) 2"
  ],
  "image": "/static/March2025_Images/Algebra/LinearEquationsInTwoVariables/12157_6.png",
  "difficulty": "medium",
  "active": "no",
  "marked": False,
  "answer": "D) 2",
  "explanation": "Choice D is correct. A linear equation can be written in the form y = mx + b, where m is the slope of the graph of the equation in the xy-plane and (0, b) is the y-intercept. Subtracting 10x from each side of the equation 10x − 5y = −12 yields −5y = −10x − 12. Dividing each side of the equation by −5 yields y = 2x + 12/5. This equation is in the form y = mx + b, where m = 2. Therefore, the slope of the graph of the given equation in the xy-plane is 2.\n\nChoice A is incorrect and may result from conceptual or calculation errors.\nChoice B is incorrect and may result from conceptual or calculation errors.\nChoice C is incorrect and may result from conceptual or calculation errors."
},
{
  "id": 7,
  "type": "multiple-choice",
  "question": "",
  "choices": [
    "A) 950",
    "B) 90",
    "C) 80",
    "D) 10"
  ],
  "image": "/static/March2025_Images/Algebra/LinearEquationsInTwoVariables/12161_7.png",
  "difficulty": "medium",
  "active": "no",
  "marked": False,
  "answer": "D) 10",
  "explanation": "Choice D is correct. It's given that the equation 80S + 90C = 1,120 represents this situation, where S is the number of square tokens won, C is the number of circle tokens won, and 1,120 is the total number of points the tokens are worth. It follows that 80S represents the total number of points the square tokens are worth. Therefore, each square token is worth 80 points. It also follows that 90C represents the total number of points the circle tokens are worth. Therefore, each circle token is worth 90 points. Since a circle token is worth 90 points and a square token is worth 80 points, then a circle token is worth 90 − 80, or 10, more points than a square token.\n\nChoice A is incorrect and may result from conceptual or calculation errors.\nChoice B is incorrect. This is the number of points a circle token is worth.\nChoice C is incorrect. This is the number of points a square token is worth."
},
{
  "id": 8,
  "type": "multiple-choice",
  "question": "",
  "choices": [
    "A) sx + 3y = 18s",
    "B) 3x + sy = 18s",
    "C) 3x + sy = 18",
    "D) sx + 3y = 18"
  ],
  "image": "/static/March2025_Images/Algebra/LinearEquationsInTwoVariables/12168_8.png",
  "difficulty": "hard",
  "active": "no",
  "marked": False,
  "answer": "B) 3x + sy = 18",
  "explanation": "Choice B is correct. The linear relationship between x and y can be represented by an equation of the form y − y₁ = m(x − x₁), where m is the slope and (x₁, y₁) is a point on the graph. Using the points (3, 15) and (5, 15), the slope m = (15 − 15)/(5 − 3) = 0. Substituting m = 0 and (5, 15) into the point-slope form yields y − 15 = 0(x − 5), which simplifies to y = 15. This equation is equivalent to 3x + sy = 18s after algebraic manipulation. Therefore, the correct equation representing the relationship is 3x + sy = 18s.\n\nChoice A is incorrect and may result from conceptual or calculation errors.\nChoice C is incorrect and may result from conceptual or calculation errors.\nChoice D is incorrect and may result from conceptual or calculation errors."
},
{
  "id": 9,
  "type": "multiple-choice",
  "question": "",
  "choices": [
    "A) 4xy = 70",
    "B) 4(x + y) = 70",
    "C) 3x + y = 70",
    "D) x + 3y = 70"
  ],
  "image": "/static/March2025_Images/Algebra/LinearEquationsInTwoVariables/12171_9.png",
  "difficulty": "easy",
  "active": "no",
  "marked": False,
  "answer": "D) x + 3y = 70",
  "explanation": "Choice D is correct. Since x represents the number of 1-minute segments and y represents the number of 3-minute segments, the total length of the video is 1·x + 3·y, or x + 3y minutes. Since the video is 70 minutes long, the equation x + 3y = 70 represents this situation.\n\nChoice A is incorrect and may result from conceptual errors.\nChoice B is incorrect and may result from conceptual errors.\nChoice C is incorrect and may result from conceptual errors."
},
{
  "id": 10,
  "type": "multiple-choice",
  "question": "",
  "choices": [
    "A) (-5, 0)",
    "B) (0, 0)",
    "C) (0, 5)",
    "D) (0, 9)"
  ],
  "image": "/static/March2025_Images/Algebra/LinearEquationsInTwoVariables/12188_10.png",
  "difficulty": "easy",
  "active": "no",
  "marked": False,
  "answer": "C) (0, 5)",
  "explanation": "Choice C is correct. The y-intercept of a graph is the point where the graph intersects the y-axis. The line graphed intersects the y-axis at the point (0, 5). Therefore, the y-intercept of the line graphed is (0, 5).\n\nChoice A is incorrect and may result from conceptual errors.\nChoice B is incorrect and may result from conceptual errors.\nChoice D is incorrect and may result from conceptual errors."
},
{
  "id": 11,
  "type": "free-response",
  "question": "",
  "choices": [],
  "image": "/static/March2025_Images/Algebra/LinearEquationsInTwoVariables/12194_11.png",
  "difficulty": "medium",
  "active": "no",
  "marked": False,
  "answer": "9",
  "explanation": "The correct answer is 9. It's given that the equation y = px + r defines the line. In this equation, p represents the slope of the line and r represents the y-coordinate of the y-intercept of the line. It's given that the line has a slope of 9. Therefore, the value of p is 9."
},
{
  "id": 12,
  "type": "multiple-choice",
  "question": "",
  "choices": [
    "A) 2",
    "B) 18",
    "C) 72",
    "D) 74"
  ],
  "image": "/static/March2025_Images/Algebra/LinearEquationsInTwoVariables/12197_12.png",
  "difficulty": "easy",
  "active": "no",
  "marked": False,
  "answer": "C) 72",
  "explanation": "Choice C is correct. A line in the xy-plane can be represented by an equation of the form y=mx+b, where m is the slope and b is the y-coordinate of the y-intercept of the line. It's given that line s passes through the point (0,0). Therefore, the y-coordinate of the y-intercept of line s is 0. It's also given that line s is parallel to the line represented by the equation y=18x+2. Since parallel lines have the same slope, it follows that the slope of line s is 18. Therefore, line s can be represented by the equation y=mx+b, where m=18 and b=0. Substituting 18 for m and 0 for b in y=mx+b yields the equation y=18x+0, or y=18x. If line s passes through the point (4,d), then when x=4, y=d for the equation y=18x. Substituting 4 for x and d for y in this equation yields d=18(4), or d=72. Choice A is incorrect. This is the y-coordinate of the y-intercept of the line represented by the equation y=18x+2. Choice B is incorrect. This is the slope of the line represented by the equation y=18x+2. Choice D is incorrect. The line represented by the equation y=18x+2, not line s, passes through the point (4,74)."
}
]

system_linear_eq_questions = [
  {
  "id": 1,
  "type": "free-response",
  "question": "",
  "choices": [],
  "image": "/static/March2025_Images/Algebra/SystemsOfTwoLinearEquationsInTwoVariables/12139_1.png",
  "difficulty": "hard",
  "active": "no",
  "marked": False,
  "answer": "3",
  "explanation": "The correct answer is 3. Adding the second equation to the first in the given system yields 2(8x) – 2(8x) + 4(7y) + 4(7y) = 12 + 12, or 8(7y) = 24. Dividing by 8 gives 7y = 3. Substituting 7y = 3 into 2(8x) + 4(7y) = 12 yields 2(8x) + 12 = 12, so 2(8x) = 0 and thus 8x = 0. Finally, substituting 8x = 0 and 7y = 3 into 8x + y gives 0 + 3, or 3."
},
{
  "id": 2,
  "type": "multiple-choice",
  "question": "",
  "choices": [
  "A) x = 4y",
  "B) 1/3x = 4y",
  "C) x = 12y - 15",
  "D) 1/3x = 12y - 15"
],
  "image": "/static/March2025_Images/Algebra/SystemsOfTwoLinearEquationsInTwoVariables/12141_2.png",
  "difficulty": "hard",
  "active": "no",
  "marked": False,
  "answer": "B) 1/3x = 4y",
  "explanation": "Choice B is correct. A system of two linear equations in two variables, x and y, has no solution when the lines in the xy-plane representing the equations are parallel and distinct. Two lines are parallel and distinct if their slopes are the same and their y-intercepts are different. The slope of the graph of the given equation, 3x = 36y - 45, in the xy-plane can be found by rewriting the equation in the form y = mx + b, where m is the slope of the graph and (0, b) is the y-intercept. Adding 45 to each side of the given equation yields 3x + 45 = 36y. Dividing each side of this equation by 36 yields 1/12x + 5/4 = y, or y = 1/12x + 5/4. It follows that the slope of the graph of the given equation is 1/12 and the y-intercept is (0, 5/4). Therefore, the graph of the second equation in the system must also have a slope of 1/12, but must not have a y-intercept of (0, 5/4). Multiplying each side of the equation given in choice B by 4 yields 1/12x = y, or y = 1/12x. It follows that the graph representing the equation in choice B has a slope of 1/12 and a y-intercept of (0, 0). Since the slopes of the graphs of the two equations are equal and the y-intercepts of the graphs of the two equations are different, the equation in choice B could be the second equation in the system. Choice A is incorrect. This equation can be rewritten as y = 1/4x. It follows that the graph of this equation has a slope of 1/4, so the system consisting of this equation and the given equation has exactly one solution, rather than no solution. Choice C is incorrect. This equation can be rewritten as y = 1/12x + 5/4. It follows that the graph of this equation has a slope of 1/12 and a y-intercept of (0, 5/4), so the system consisting of this equation and the given equation has infinitely many solutions, rather than no solution. Choice D is incorrect. This equation can be rewritten as y = 1/36x + 5/4. It follows that the graph of this equation has a slope of 1/36, so the system consisting of this equation and the given equation has exactly one solution, rather than no solution."
},
{
  "id": 3,
  "type": "free-response",
  "question": "",
  "choices": [],
  "image": "/static/March2025_Images/Algebra/SystemsOfTwoLinearEquationsInTwoVariables/12145_3.png",
  "difficulty": "hard",
  "active": "no",
  "marked": False,
  "answer": "2/7",
  "explanation": "The correct answer is 2/7. It’s given that the system has infinitely many solutions, which happens only if the two equations are equivalent. Multiplying each side of the first equation by 35/4 yields (35/4).((2/5)x + (7/5)y = (35/4)(2/7), which simplifies to (7/2)x + (49/4)y = 5/2. Since this matches the second equation, the coefficients must be equal: g = 7/2 and k = 49/4. Therefore g ÷ k = (7/2)/(49/4) = 2/7."
},
{
  "id": 4,
  "type": "multiple-choice",
  "question": "",
  "choices": [
  "A) (r, -6r/7 + 5/7)",
  "B) (r, 7r/6 + 5/6)",
  "C) (r/4 + 5, -r/4 + 20)",
  "D) (-6r/7 + 5/7, r)"
],
  "image": "/static/March2025_Images/Algebra/SystemsOfTwoLinearEquationsInTwoVariables/12146_4.png",
  "difficulty": "hard",
  "active": "no",
  "marked": False,
  "answer": "D) (-6r/7 + 5/7, r)",
  "explanation": "Choice D is correct. Dividing each side of the second equation in the given system by 4 yields 7x + 6y = 5. It follows that the two equations in the given system are equivalent and any point that lies on the graph of one equation will also lie on the graph of the other equation. Substituting r for y in the equation 7x + 6y = 5 yields 7x + 6r = 5. Subtracting 6r from each side of this equation yields 7x = -6r + 5. Dividing each side of this equation by 7 yields x = -6r/7 + 5/7. Therefore, the point (-6r/7 + 5/7, r) lies on the graph of each equation in the xy-plane for each real number r. Choice A is incorrect. Substituting r for x in the equation 7x + 6y = 5 yields 7r + 6y = 5. Subtracting 7r from each side of this equation yields 6y = -7r + 5. Dividing each side of this equation by 6 yields y = -7r/6 + 5/6. Therefore, the point (r, -7r/6 + 5/6), not the point (r, -6r/7 + 5/7), lies on the graph of each equation. Choice B is incorrect. Substituting r for x in the equation 7x + 6y = 5 yields 7r + 6y = 5. Subtracting 7r from each side of this equation yields 6y = -7r + 5. Dividing each side of this equation by 6 yields y = -7r/6 + 5/6. Therefore, the point (r, -7r/6 + 5/6), not the point (r, 7r/6 + 5/6), lies on the graph of each equation. Choice C is incorrect. Substituting r + 5 for x in the equation 7x + 6y = 5 yields 7(r + 5) + 6y = 5, or (7r + 35) + 6y = 5. Subtracting (7r + 35) from each side of this equation yields 6y = -7r - 35 + 5, or 6y = -7r - 30. Dividing each side of this equation by 6 yields y = -7r/6 - 5. Therefore, the point (r + 5, -7r/6 - 5), not the point (r + 5, -r + 20), lies on the graph of each equation."
},
{
  "id": 5,
  "type": "free-response",
  "question": "",
  "choices": [],
  "image": "/static/March2025_Images/Algebra/SystemsOfTwoLinearEquationsInTwoVariables/12148_5.png",
  "difficulty": "hard",
  "active": "no",
  "marked": False,
  "answer": "87",
  "explanation": "The correct answer is 87. It's given that in August, the car dealer completed 15 more than 3 times the number of sales the car dealer completed in September. Let x represent the number of sales the car dealer completed in September. It follows that 3x+15 represents the number of sales the car dealer completed in August. It's also given that in August and September, the car dealer completed 363 sales. It follows that x+(3x+15)=363, or 4x+15=363. Subtracting 15 from each side of this equation yields 4x=348. Dividing each side of this equation by 4 yields x=87. Therefore, the car dealer completed 87 sales in September."
},
{
  "id": 6,
  "type": "free-response",
  "question": "",
  "choices": [],
  "image": "/static/March2025_Images/Algebra/SystemsOfTwoLinearEquationsInTwoVariables/12154_6.png",
  "difficulty": "medium",
  "active": "no",
  "marked": False,
  "answer": "40",
  "explanation": "The correct answer is 40. It's given in the first equation of the system that y=−2x. Substituting −2x for y in the second equation of the system yields 3x+(−2x)=40. Combining like terms on the left-hand side of this equation yields x=40. Therefore, the value of x is 40."
},
{
  "id": 7,
  "type": "free-response",
  "question": "",
  "choices": [],
  "image": "/static/March2025_Images/Algebra/SystemsOfTwoLinearEquationsInTwoVariables/12160_7.png",
  "difficulty": "medium",
  "active": "no",
  "marked": False,
  "answer": "25",
  "explanation": "The correct answer is 25. Subtracting the second equation from the first equation in the given system of equations yields (2a−2a)+(8b−4b)=198−98, which is equivalent to 0+4b=100, or 4b=100. Dividing each side of this equation by 4 yields b=25."
},
{
  "id": 8,
  "type": "free-response",
  "question": "",
  "choices": [],
  "image": "/static/March2025_Images/Algebra/SystemsOfTwoLinearEquationsInTwoVariables/12173_8.png",
  "difficulty": "medium",
  "active": "no",
  "marked": False,
  "answer": "3",
  "explanation": "The correct answer is 3. It's given that y=9x+12. Substituting 9x+12 for y in the second equation in the system, x+7y=20, yields x+7(9x+12)=20, which gives x+63x+84=20, or 64x+84=20. Subtracting 84 from each side of this equation yields 64x=−64. Dividing each side of this equation by 64 yields x=−1. Substituting −1 for x in the first equation in the system, y=9x+12, yields y=9(−1)+12, or y=3. Therefore, the value of y is 3."
},
{
  "id": 9,
  "type": "multiple-choice",
  "question": "",
  "choices": [
  "A) y = 2(6x) + 3",
  "B) y = 2(6x + 3)",
  "C) 2(y) = 2(6x) + 3",
  "D) 2(y) = 2(6x + 3)"
],
  "image": "/static/March2025_Images/Algebra/SystemsOfTwoLinearEquationsInTwoVariables/12176_9.png",
  "difficulty": "medium",
  "active": "no",
  "marked": False,
  "answer": "D) 2(y) = 2(6x + 3)",
  "explanation": "Choice D is correct. It's given that the system has infinitely many solutions. A system of two linear equations has infinitely many solutions when the two linear equations are equivalent. When one equation is a multiple of another equation, the two equations are equivalent. Multiplying each side of the given equation by 2 yields 2(y) = 2(6x + 3). Thus, 2(y) = 2(6x + 3) is equivalent to the given equation and could be the second equation in the system. Choice A is incorrect. The system consisting of this equation and the given equation has one solution rather than infinitely many solutions. Choice B is incorrect. The system consisting of this equation and the given equation has one solution rather than infinitely many solutions. Choice C is incorrect. The system consisting of this equation and the given equation has no solutions rather than infinitely many solutions."
},
{
  "id": 10,
  "type": "free-response",
  "question": "",
  "choices": [],
  "image": "/static/March2025_Images/Algebra/SystemsOfTwoLinearEquationsInTwoVariables/12177_10.png",
  "difficulty": "medium",
  "active": "no",
  "marked": False,
  "answer": "3",
  "explanation": "The correct answer is 1. Subtracting the second equation from the first equation in the given system of equations yields (3x−3x)+(6−4)=4y−2y, which is equivalent to 0+2=2y, or 2=2y. Dividing each side of this equation by 2 yields 1=y."
},
{
  "id": 11,
  "type": "multiple-choice",
  "question": "",
  "choices": [
  "A) 2",
  "B) 3",
  "C) 48",
  "D) 71"
],
  "image": "/static/March2025_Images/Algebra/SystemsOfTwoLinearEquationsInTwoVariables/12178_11.png",
  "difficulty": "hard",
  "active": "no",
  "marked": False,
  "answer": "D) 71",
  "explanation": "Choice D is correct. Multiplying the second equation in the given system by 2 yields 10/2x + 12y = 46. Adding this equation to the first equation in the system yields (7/2x + 6y) + (10/2x + 12y) = 25 + 46, which is equivalent to (7/2x + 10/2x) + (6y + 12y) = 25 + 46, or 17/2x + 18y = 71. Therefore, the value of 17/2x + 18y is 71. Choice A is incorrect. This is the value of x, not the value of 17/2x + 18y. Choice B is incorrect. This is the value of y, not the value of 17/2x + 18y. Choice C is incorrect. This is the value of (7/2x + 6y) + (5/2x + 6y), or 6x + 12y, not the value of 17/2x + 18y."
},
{
  "id": 12,
  "type": "multiple-choice",
  "question": "",
  "choices": [
  "A) (0, 4)",
  "B) (2, 2)",
  "C) (4, 0)",
  "D) (4, 4)"
],
  "image": "/static/March2025_Images/Algebra/SystemsOfTwoLinearEquationsInTwoVariables/12184_12.png",
  "difficulty": "easy",
  "active": "no",
  "marked": False,
  "answer": "B) (2, 2)",
  "explanation": "Choice B is correct. The solution to this system of linear equations is represented by the point that lies on both lines shown, or the point of intersection of the two lines. According to the graph, the point of intersection occurs when x=2 and y=2, or at the point (2,2). Therefore, the solution (x,y) to the system is (2,2). Choice A is incorrect and may result from conceptual or calculation errors. Choice C is incorrect and may result from conceptual or calculation errors. Choice D is incorrect and may result from conceptual or calculation errors."
},
{
  "id": 13,
  "type": "multiple-choice",
  "question": "",
  "choices": [
  "A) -18",
  "B) -6",
  "C) 6",
  "D) 18"
],
  "image": "/static/March2025_Images/Algebra/SystemsOfTwoLinearEquationsInTwoVariables/12189_13.png",
  "difficulty": "medium",
  "active": "no",
  "marked": False,
  "answer": "D) 18",
  "explanation": "Choice D is correct. Adding the second equation to the first equation in the given system of equations yields 3y - 3y = 4x + 9x + 17 - 23, or 0 = 13x - 6. Adding 6 to each side of this equation yields 6 = 13x. Multiplying each side of this equation by 3 yields 18 = 39x. Therefore, the value of 39x is 18. Choice A is incorrect. This is the value of -39x, not 39x. Choice B is incorrect. This is the value of -13x, not 39x. Choice C is incorrect. This is the value of 13x, not 39x."
},
{
  "id": 14,
  "type": "multiple-choice",
  "question": "",
  "choices": [
  "A) (4, -5)",
  "B) (0, 3)",
  "C) (0, -2)",
  "D) (-2, 3)"
],
  "image": "/static/March2025_Images/Algebra/SystemsOfTwoLinearEquationsInTwoVariables/12191_14.png",
  "difficulty": "easy",
  "active": "no",
  "marked": False,
  "answer": "A) (4, -5)",
  "explanation": "Choice A is correct. The solution to this system of linear equations is represented by the point that lies on both lines shown, or the point of intersection of the two lines. According to the graph, the point of intersection occurs when x = 4 and y = -5, or at the point (4, -5). Therefore, the solution (x, y) to the system is (4, -5). Choice B is incorrect and may result from conceptual or calculation errors. Choice C is incorrect and may result from conceptual or calculation errors. Choice D is incorrect and may result from conceptual or calculation errors."
},
{
  "id": 15,
  "type": "multiple-choice",
  "question": "",
  "choices": [
  "A) (0, -7)",
  "B) (0, -3)",
  "C) (-4, -3)",
  "D) (-4, 0)"
],
  "image": "/static/March2025_Images/Algebra/SystemsOfTwoLinearEquationsInTwoVariables/12192_15.png",
  "difficulty": "easy",
  "active": "no",
  "marked": False,
  "answer": "C) (-4, -3)",
  "explanation": "Choice C is correct. The solution to a system of linear equations is represented by the point that lies on the graph of each equation in the system, or the point where the lines intersect on a graph. On the graph shown, the two lines intersect at the point (-4, -3). Therefore, the solution to the system is (-4, -3). Choice A is incorrect. This is the y-intercept of the graph of one of the lines shown, not the intersection point of the two lines. Choice B is incorrect and may result from conceptual or calculation errors. Choice D is incorrect and may result from conceptual or calculation errors."
}
]

linear_ineq_questions = [
  {
  "id": 1,
  "type": "multiple-choice",
  "question": "",
  "choices": [
  "A) (-5, -6)",
  "B) (-2, 5)",
  "C) (1, 4)",
  "D) (6, -2)"
],
  "image": "/static/March2025_Images/Algebra/LinearInequalitiesInOneOrTwoVariables/12151_1.png",
  "difficulty": "medium",
  "active": "no",
  "marked": False,
  "answer": "D) (6, -2)",
  "explanation": "Choice D is correct. Since the shaded region shown represents the solutions to an inequality, an ordered pair (x,y) is a solution to the inequality if it's represented by a point in the shaded region. Of the given choices, only (6, -2) is represented by a point in the shaded region. Therefore, the ordered pair (6, -2) is a solution to this inequality. Choice A is incorrect and may result from conceptual errors. Choice B is incorrect and may result from conceptual errors. Choice C is incorrect and may result from conceptual errors."
},
{
  "id": 2,
  "type": "multiple-choice",
  "question": "",
  "choices": [
  "A) 14",
  "B) 76",
  "C) 86",
  "D) 186"
],
  "image": "/static/March2025_Images/Algebra/LinearInequalitiesInOneOrTwoVariables/12155_2.png",
  "difficulty": "easy",
  "active": "no",
  "marked": False,
  "answer": "A) 14",
  "explanation": "Choice A is correct. It's given that Julissa already has 86 hours of flight time. Let x represent the number of additional hours of flight time Julissa needs to get her private pilot certification. After completing x hours of flight time, Julissa will have completed a total of 86 + x hours of flight time. It's given that Julissa needs at least 100 hours of flight time to get her private pilot certification. Therefore, 86 + x >= 100. Subtracting 86 from both sides of this inequality yields x >= 14. Thus, 14 is the minimum number of additional hours of flight time Julissa needs to get her private pilot certification. Choice B is incorrect and may result from conceptual or calculation errors. Choice C is incorrect. This is the number of hours of flight time Julissa already has, rather than the minimum number of additional hours of flight time Julissa needs. Choice D is incorrect. This is the number of hours of flight time Julissa will have if she completes 100 more hours of flight time, rather than the minimum number of additional hours of flight time Julissa needs."
},
{
  "id": 3,
  "type": "free-response",
  "question": "",
  "choices": [],
  "image": "/static/March2025_Images/Algebra/LinearInequalitiesInOneOrTwoVariables/12166_3.png",
  "difficulty": "medium",
  "active": "no",
  "marked": False,
  "answer": "25",
  "explanation": "The correct answer is 25. The total cost of the party is found by adding the onetime fee of the venue to the cost per attendee times the number of attendees. Let x be the number of attendees. The expression 35 + 10.25x thus represents the total cost of the party. It's given that the budget is $300, so this situation can be represented by the inequality 35 + 10.25x <= 300. Subtracting 35 from both sides of this inequality gives 10.25x <= 265. Dividing both sides of this inequality by 10.25 results in approximately x <= 25.854. Since the question is stated in terms of attendees, rounding 25.854 down to the greatest whole number gives the greatest number of attendees possible, which is 25."
},
{
  "id": 4,
  "type": "multiple-choice",
  "question": "",
  "choices": [
  "A) (19, 18), (20, 19), (21, 20)",
  "B) (19, 20), (20, 21), (21, 22)",
  "C) (22, 23), (23, 24), (24, 25)",
  "D) (23, 24), (24, 25), (25, 26)"
],
  "image": "/static/March2025_Images/Algebra/LinearInequalitiesInOneOrTwoVariables/12169_4.png",
  "difficulty": "medium",
  "active": "no",
  "marked": False,
  "answer": "A) (19, 18), (20, 19), (21, 20)",
  "explanation": "Choice A is correct. The inequality y < x indicates that for any solution to the given system of inequalities, the value of x must be greater than the corresponding value of y. The inequality x < 22 indicates that for any solution to the given system of inequalities, the value of x must be less than 22. Of the given choices, only choice A contains values of x that are each greater than the corresponding value of y and less than 22. Therefore, for choice A, all the values of x and their corresponding values of y are solutions to the given system of inequalities. Choice B is incorrect. The values in this table aren't solutions to the inequality y < x. Choice C is incorrect. The values in this table aren't solutions to the inequality x < 22. Choice D is incorrect. The values in this table aren't solutions to the inequality y < x or the inequality x < 22."
},
{
  "id": 5,
  "type": "multiple-choice",
  "question": "",
  "choices": [
  "A) (3, 17), (5, 27), (7, 37)",
  "B) (3, 25), (5, 27), (7, 37)",
  "C) (3, 25), (5, 35), (7, 45)",
  "D) (3, 21), (5, 31), (7, 41)"
],
  "image": "/static/March2025_Images/Algebra/LinearInequalitiesInOneOrTwoVariables/12172_5.png",
  "difficulty": "hard",
  "active": "no",
  "marked": False,
  "answer": "A) (3, 17), (5, 27), (7, 37)",
  "explanation": "Choice A is correct. Substituting 3 for x in the given inequality yields y < 5(3)+6, or y < 21. Therefore, when x = 3, the corresponding value of y is less than 21. Substituting 5 for x in the given inequality yields y < 5(5)+6, or y < 31. Therefore, when x = 5, the corresponding value of y is less than 31. Substituting 7 for x in the given inequality yields y < 5(7)+6, or y < 41. Therefore, when x = 7, the corresponding value of y is less than 41. For the table in choice A, when x = 3, the corresponding value of y is 17, which is less than 21; when x = 5, the corresponding value of y is 27, which is less than 31; and when x = 7, the corresponding value of y is 37, which is less than 41. Therefore, the table in choice A gives values of x and their corresponding values of y that are all solutions to the given inequality. Choice B is incorrect and may result from conceptual or calculation errors. Choice C is incorrect and may result from conceptual or calculation errors. Choice D is incorrect and may result from conceptual or calculation errors."
},
{
  "id": 6,
  "type": "multiple-choice",
  "question": "",
  "choices": [
  "A) (3, 20), (5, 32), (7, 44)",
  "B) (3, 16), (5, 30), (7, 40)",
  "C) (3, 16), (5, 28), (7, 40)",
  "D) (3, 24), (5, 36), (7, 48)"
],
  "image": "/static/March2025_Images/Algebra/LinearInequalitiesInOneOrTwoVariables/12180_6.png",
  "difficulty": "hard",
  "active": "no",
  "marked": False,
  "answer": "C) (3, 16), (5, 28), (7, 40)",
  "explanation": "Choice C is correct. All the tables in the choices have the same three values of x, so each of the three values of x can be substituted in the given inequality to compare the corresponding values of y in each of the tables. Substituting 3 for x in the given inequality yields y < 6(3)+2, or y < 20. Therefore, when x = 3, the corresponding value of y is less than 20. Substituting 5 for x in the given inequality yields y < 6(5)+2, or y < 32. Therefore, when x = 5, the corresponding value of y is less than 32. Substituting 7 for x in the given inequality yields y < 6(7)+2, or y < 44. Therefore, when x = 7, the corresponding value of y is less than 44. For the table in choice C, when x = 3, the corresponding value of y is 16, which is less than 20; when x = 5, the corresponding value of y is 28, which is less than 32; when x = 7, the corresponding value of y is 40, which is less than 44. Therefore the table in choice C gives values of x and their corresponding values of y that are all solutions to the given inequality. Choice A is incorrect. In the table for choice A, when x = 3, the corresponding value of y is 20, which is not less than 20; when x = 5, the corresponding value of y is 32, which is not less than 32; when x = 7, the corresponding value of y is 44, which is not less than 44. Choice B is incorrect. In the table for choice B, when x = 5, the corresponding value of y is 36, which is not less than 32. Choice D is incorrect. In the table for choice D, when x = 3, the corresponding value of y is 24, which is not less than 20; when x = 5, the corresponding value of y is 36, which is not less than 32; when x = 7, the corresponding value of y is 48, which is not less than 44."
},
{
  "id": 7,
  "type": "multiple-choice",
  "question": "",
  "choices": [
  "A) 12(x + 6) ≤ x + (x + 4) - 26",
  "B) 12(x + 6) ≥ 26 - (x + (x + 4))",
  "C) 12(x + 4) ≤ x + (x + 3) - 26",
  "D) 12(x + 4) ≥ 26 - (x + (x + 3))"
],
  "image": "/static/March2025_Images/Algebra/LinearInequalitiesInOneOrTwoVariables/12182_7.png",
  "difficulty": "easy",
  "active": "no",
  "marked": False,
  "answer": "A) 12(x + 6) ≤ x + (x + 4) - 26",
  "explanation": "Choice A is correct. It's given that the four odd integers are consecutive, ordered from least to greatest, and that the first odd integer is represented by x. It follows that the second odd integer is represented by x + 2, the third odd integer is represented by x + 4, and the fourth odd integer is represented by x + 6. Therefore, the product of 12 and the fourth odd integer is represented by 12(x + 6), and 26 less than the sum of the first and third odd integers is represented by x + (x + 4) - 26. Since the product of 12 and the fourth odd integer is at most 26 less than the sum of the first and third odd integers, it follows that 12(x + 6)<=x+(x + 4) - 26. Choice B is incorrect and may result from conceptual or calculation errors. Choice C is incorrect and may result from conceptual or calculation errors. Choice D is incorrect and may result from conceptual or calculation errors."
}
]
	
equivalent_expressions = [
  {
  "id": 1,
  "type": "multiple-choice",
  "question": "",
  "choices": [
  "A) 15x^6 + 5x^2 - 5x - 35",
  "B) 15x^3 + 10x^2 + 2",
  "C) 15x^6 + 5x^2 + 2",
  "D) 15x^3 + 5x^2 + 2"
],
  "image": "/static/March2025_Images/AdvancedMath/EquivalentExpressions/12138_1.png",
  "difficulty": "easy",
  "active": "no",
  "marked": False,
  "answer": "D) 15x^3 + 5x^2 + 2",
  "explanation": "Choice D is correct. The given expression can be rewritten as (9x³ + 6x³) + 5x² + 5x + (7-5). Combining like terms in this expression yields 15x³ + 5x² + 5x + 2. Choice A is incorrect and may result from conceptual or calculation errors. Choice B is incorrect and may result from conceptual or calculation errors. Choice C is incorrect and may result from conceptual or calculation errors."
},
{
  "id": 2,
  "type": "multiple-choice",
  "question": "",
  "choices": [
  "A) 23x(x^2 + 2x + 9)",
  "B) 9x(23x^2 + 2x^2 + 1)",
  "C) x(23x^2 + 2x + 9)",
  "D) 34(x^3 + x^2 + x)"
],
  "image": "/static/March2025_Images/AdvancedMath/EquivalentExpressions/12138_1.png",
  "difficulty": "easy",
  "active": "no",
  "marked": False,
  "answer": "C) x(23x^2 + 2x + 9)",
  "explanation": "Choice C is correct. Since x is a common factor of each term in the given expression, the given expression can be rewritten as x(23x² + 2x + 9). Choice A is incorrect. This expression is equivalent to 23x³ + 46x² + 207x. Choice B is incorrect. This expression is equivalent to 207x⁴ + 18x³ + 9x. Choice D is incorrect. This expression is equivalent to 34x³ + 34x² + 34x."
},
{
  "id": 3,
  "type": "multiple-choice",
  "question": "",
  "choices": [
  "A) 3x^2 + 7x + 14b",
  "B) 3x^2 + 28x + 14b",
  "C) 3x^2 + 42x + 14b",
  "D) 3x^2 + 49x + 14b"
],
  "image": "/static/March2025_Images/AdvancedMath/EquivalentExpressions/12138_1.png",
  "difficulty": "hard",
  "active": "no",
  "marked": False,
  "answer": "D) 3x^2 + 49x + 14b",
  "explanation": "Choice D is correct. Since each choice has a term of 3x², which can be written as (3x)(x), and each choice has a term of 14b, which can be written as (7)(2b), the expression that has a factor of x + 2b, where b is a positive integer constant, can be represented as (3x + 7)(x + 2b). Using the distributive property of multiplication, this expression is equivalent to 3x(x + 2b)+7(x + 2b), or 3x² + 6xb + 7x + 14b. Combining the x-terms in this expression yields 3x²+(7+6b)x+14b. It follows that the coefficient of the x-term is equal to 7+6b. Thus, from the given choices, 7+6b must be equal to 7, 28, 42, or 49. Therefore, 6b must be equal to 0, 21, 35, or 42, respectively, and b must be equal to 0, 21/6, 35/6, or 42/6, respectively. Of these four values of b, only 42/6, or 7, is a positive integer. It follows that 7+6b must be equal to 49 because this is the only choice for which the value of b is a positive integer constant. Therefore, the expression that has a factor of x + 2b is 3x² + 49x + 14b. Choice A is incorrect. If this expression has a factor of x+2b, then the value of b is 0, which isn't positive. Choice B is incorrect. If this expression has a factor of x+2b, then the value of b is 21/6, which isn't an integer. Choice C is incorrect. If this expression has a factor of x+2b, then the value of b is 35/6, which isn't an integer."
},
{
  "id": 4,
  "type": "multiple-choice",
  "question": "",
  "choices": [
  "A) h^10 / q^14",
  "B) h^3 / q^3",
  "C) h^10q^14",
  "D) h^3q^3"
],
  "image": "/static/March2025_Images/AdvancedMath/EquivalentExpressions/12138_1.png",
  "difficulty": "medium",
  "active": "no",
  "marked": False,
  "answer": "A) h^10 / q^14",
  "explanation": "Choice A is correct. For positive values of a, a^m/a^n=a^(m-n), where m and n are integers. Since it's given that h > 0 and q > 0, this property can be applied to rewrite the given expression as (h^(15-5))(q^(7-21)), which is equivalent to h^10 q^-14. For positive values of a, a^-n=1/a^n. This property can be applied to rewrite the expression h^10 q^-14 as (h^10)(1/q^14), which is equivalent to h^10/q^14. Choice B is incorrect and may result from conceptual or calculation errors. Choice C is incorrect and may result from conceptual or calculation errors. Choice D is incorrect and may result from conceptual or calculation errors."
},
{
  "id": 5,
  "type": "multiple-choice",
  "question": "",
  "choices": [
  "A) -26",
  "B) -26/9",
  "C) 1/9",
  "D) 9"
],
  "image": "/static/March2025_Images/AdvancedMath/EquivalentExpressions/12138_1.png",
  "difficulty": "hard",
  "active": "no",
  "marked": False,
  "answer": "C) 1/9",
  "explanation": "Choice C is correct. Multiplying the given functions f and g yields f(x)·g(x)=(x²+bx)(9x²-27x). Applying the distributive property to the right-hand side of this equation yields f(x)·g(x)=(x²)(9x²-27x)+(bx)(9x²-27x). Applying the distributive property once again to the right-hand side of this equation yields f(x)·g(x)=(x²)(9x²)-(x²)(27x)+(bx)(9x²)-(bx)(27x), which is equivalent to f(x)·g(x)=9x⁴-27x³+9bx³-27bx². Factoring out x³ from the second and third terms yields f(x)·g(x)=9x⁴+(-27+9b)x³-27bx². Since the left-hand sides of f(x)·g(x)=9x⁴+(-27+9b)x³-27bx² and f(x)·g(x)=9x⁴-26x³-3x² are equal, it follows that (-27+9b)x³=-26x³, or -27+9b=-26, and -27bx²=-3x², or -27b=-3. Adding 27 to each side of -27+9b=-26 yields 9b=1. Dividing each side of this equation by 9 yields b=1/9. Similarly, dividing each side of -27b=-3 by -27 yields b=1/9. Therefore, the value of b is 1/9. Choice A is incorrect and may result from conceptual or calculation errors. Choice B is incorrect and may result from conceptual or calculation errors. Choice D is incorrect and may result from conceptual or calculation errors."
},
{
  "id": 6,
  "type": "multiple-choice",
  "question": "",
  "choices": [
  "A) 16x + 31",
  "B) 16x + 240",
  "C) 16x + 1",
  "D) 16x + 15"
],
  "image": "/static/March2025_Images/AdvancedMath/EquivalentExpressions/12138_1.png",
  "difficulty": "easy",
  "active": "no",
  "marked": False,
  "answer": "B) 16x + 240",
  "explanation": "Choice B is correct. The expression 16(x + 15) can be rewritten as 16(x)+16(15), which is equivalent to 16x + 240. Choice A is incorrect and may result from conceptual or calculation errors. Choice C is incorrect and may result from conceptual or calculation errors. Choice D is incorrect and may result from conceptual or calculation errors."
}
]
	
nonlinear_equations_systems = [
  {
  "id": 1,
  "type": "free-response",
  "question": "",
  "choices": [],
  "image": "/static/March2025_Images/AdvancedMath/NonlinearEquationsSystems/12212_1.png",
  "difficulty": "hard",
  "active": "no",
  "marked": False,
  "answer": "120",
  "explanation": "The correct answer is 120. The solutions to a quadratic equation of the form ax² + bx + c = 0 can be calculated using the quadratic formula and are given by x = (-b ± sqrt(b²-4ac))/(2a). The given equation is in the form ax² + bx + c = 0, where a = 2, b = -8, and c = -7. It follows that the solutions to the given equation are x = (8 ± sqrt((-8)²-4(2)(-7)))/(2(2)), which is equivalent to x = (8 ± sqrt(64+56))/4, or x = (8 ± sqrt(120))/4. It's given that one solution to the equation 2x² - 8x - 7 = 0 can be written as (8 - sqrt(k))/4. The solution (8 - sqrt(120))/4 is in this form. Therefore, the value of k is 120."
},
{
  "id": 2,
  "type": "free-response",
  "question": "",
  "choices": [],
  "image": "/static/March2025_Images/AdvancedMath/NonlinearEquationsSystems/12214_2.png",
  "difficulty": "hard",
  "active": "no",
  "marked": False,
  "answer": "35/2",
  "explanation": "The correct answer is 35/2. Subtracting the second equation from the first equation yields (y+k)-(y-k)=x+26-(x²-5x), or 2k=-x²+6x+26. This is equivalent to x²-6x+(2k-26)=0. It's given that the system has exactly one distinct real solution; therefore, this equation has exactly one distinct real solution. An equation of the form ax²+bx+c=0, where a, b, and c are constants, has exactly one distinct real solution when the discriminant, b²-4ac, is equal to 0. The equation x²-6x+(2k-26)=0 is of this form, where a=1, b=-6, and c=2k-26. Substituting these values into the discriminant, b²-4ac, yields (-6)²-4(1)(2k-26). Setting the discriminant equal to 0 yields (-6)²-4(1)(2k-26)=0, or -8k+140=0. Subtracting 140 from both sides of this equation yields -8k=-140. Dividing both sides of this equation by -8 yields k=35/2. Note that 35/2 and 17.5 are examples of ways to enter a correct answer."
},
{
  "id": 3,
  "type": "multiple-choice",
  "question": "",
  "choices": [
  "A) -4",
  "B) 0",
  "C) 3",
  "D) 5"
],
  "image": "/static/March2025_Images/AdvancedMath/NonlinearEquationsSystems/12219_3.png",
  "difficulty": "medium",
  "active": "no",
  "marked": False,
  "answer": "B) 0",
  "explanation": "Choice B is correct. Applying the zero product property to the given equation yields 3x = 0, x - 4 = 0, and x + 5 = 0. Dividing each side of the equation 3x = 0 by 3 yields x = 0. Adding 4 to each side of the equation x - 4 = 0 yields x = 4. Subtracting 5 from each side of the equation x + 5 = 0 yields x = -5. Therefore, the solutions to the given equation are 0, 4, and -5. Thus, one of the solutions to the given equation is 0. Choice A is incorrect and may result from conceptual or calculation errors. Choice C is incorrect and may result from conceptual or calculation errors. Choice D is incorrect and may result from conceptual or calculation errors."
},
{
  "id": 4,
  "type": "multiple-choice",
  "question": "",
  "choices": [
  "A) (-1, 5)",
  "B) (0, 4)",
  "C) (1, 5)",
  "D) (4, 2)"
],
  "image": "/static/March2025_Images/AdvancedMath/NonlinearEquationsSystems/12220_4.png",
  "difficulty": "easy",
  "active": "no",
  "marked": False,
  "answer": "C) (1, 5)",
  "explanation": "Choice C is correct. The solution to the system of two equations corresponds to the point where the graphs of the equations intersect. The graphs of the linear function and the absolute value function shown intersect at the point (1, 5). Thus, the solution to the system is (1, 5). Choice A is incorrect and may result from conceptual or calculation errors. Choice B is incorrect. This is the y-intercept of the graph of the linear function. Choice D is incorrect. This is the vertex of the graph of the absolute value function."
},
{
  "id": 5,
  "type": "free-response",
  "question": "",
  "choices": [],
  "image": "/static/March2025_Images/AdvancedMath/NonlinearEquationsSystems/12222_5.png",
  "difficulty": "hard",
  "active": "no",
  "marked": False,
  "answer": "14",
  "explanation": "The correct answer is 14. It's given by the first equation of the system of equations that y = -2.5. Substituting -2.5 for y in the second given equation, y = x² + 8x + k, yields -2.5 = x² + 8x + k. Adding 2.5 to both sides of this equation yields 0 = x² + 8x + k + 2.5. A quadratic equation of the form 0 = ax² + bx + c, where a, b, and c are constants, has no real solutions if and only if its discriminant, b²-4ac, is negative. In the equation 0 = x² + 8x + k + 2.5, where k is a positive integer constant, a = 1, b = 8, and c = k + 2.5. Substituting 1 for a, 8 for b, and k + 2.5 for c in b²-4ac yields 8²-4(1)(k + 2.5), or 64-4(k + 2.5). Since this value must be negative, 64-4(k + 2.5) < 0. Adding 4(k + 2.5) to both sides of this inequality yields 64 < 4(k + 2.5). Dividing both sides of this inequality by 4 yields 16 < k + 2.5. Subtracting 2.5 from both sides of this inequality yields 13.5 < k. Since k is a positive integer constant, the least possible value of k is 14."
},
{
  "id": 6,
  "type": "multiple-choice",
  "question": "",
  "choices": [
  "A) -5/2",
  "B) -5/4",
  "C) -4/5",
  "D) -2/5"
],
  "image": "/static/March2025_Images/AdvancedMath/NonlinearEquationsSystems/12224_6.png",
  "difficulty": "medium",
  "active": "no",
  "marked": False,
  "answer": "C) -4/5",
  "explanation": "Choice C is correct. Since a product of two factors is equal to 0 if and only if at least one of the factors is 0, either 5x + 4 = 0 or 2x - 5 = 0. Subtracting 4 from each side of the equation 5x + 4 = 0 yields 5x = -4. Dividing each side of this equation by 5 yields x = -4/5. Adding 5 to each side of the equation 2x - 5 = 0 yields 2x = 5. Dividing each side of this equation by 2 yields x = 5/2. It follows that the solutions to the given equation are -4/5 and 5/2. Therefore, -4/5 is a solution to the given equation. Choice A is incorrect and may result from conceptual or calculation errors. Choice B is incorrect and may result from conceptual or calculation errors. Choice D is incorrect and may result from conceptual or calculation errors."
},
{
  "id": 7,
  "type": "multiple-choice",
  "question": "",
  "choices": [
  "A) 65 / 61",
  "B) 4",
  "C) 126",
  "D) 130"
],
  "image": "/static/March2025_Images/AdvancedMath/NonlinearEquationsSystems/12225_7.png",
  "difficulty": "easy",
  "active": "no",
  "marked": False,
  "answer": "B) 4",
  "explanation": "Choice B is correct. Subtracting 61 from each side of the given equation yields |p|=4. By the definition of absolute value, if |p|=4, then p=4 or p=-4. Of the given choices, 4 is a solution to the given equation. Choice A is incorrect. This is the quotient, not the difference, of 65 and 61. Choice C is incorrect. This is the sum, not the difference, of 65 and 61. Choice D is incorrect and may result from conceptual or calculation errors."
},
{
  "id": 8,
  "type": "multiple-choice",
  "question": "",
  "choices": [
  "A) m = 2(n + p) / 7",
  "B) m = 2(n + p)",
  "C) m = 2(n + p) - 7",
  "D) m = 2 - n - p - 7"
],
  "image": "/static/March2025_Images/AdvancedMath/NonlinearEquationsSystems/12226_8.png",
  "difficulty": "easy",
  "active": "no",
  "marked": False,
  "answer": "A) m = 2(n + p) / 7",
  "explanation": "Choice A is correct. Dividing each side of the given equation by 7 yields m=2(n+p)/7. Choice B is incorrect and may result from conceptual or calculation errors. Choice C is incorrect. This equation is equivalent to 7+m=2(n+p), not 7m=2(n+p). Choice D is incorrect and may result from conceptual or calculation errors."
},
{
  "id": 9,
  "type": "multiple-choice",
  "question": "",
  "choices": [
  "A) 7",
  "B) 9",
  "C) 16",
  "D) 63"
],
  "image": "/static/March2025_Images/AdvancedMath/NonlinearEquationsSystems/12228_9.png",
  "difficulty": "medium",
  "active": "no",
  "marked": False,
  "answer": "C) 16",
  "explanation": "Choice C is correct. Since the left-hand side of the given equation has a factor of x + 9 in both the numerator and the denominator, the solution to the given equation can be found by solving the equation x-9=7. Adding 9 to both sides of this equation yields x = 16. Substituting 16 for x in the given equation yields (16+9)(16-9)/(16+9)=7, or 7=7. Therefore, the solution to the given equation is 16. Choice A is incorrect. Substituting 7 for x in the given equation yields (7+9)(7-9)/(7+9)=7, or -2=7, which is false. Choice B is incorrect. Substituting 9 for x in the given equation yields (9+9)(9-9)/(9+9)=7, or 0=7, which is false. Choice D is incorrect. Substituting 63 for x in the given equation yields (63+9)(63-9)/(63+9)=7, or 54=7, which is false."
},
{
  "id": 10,
  "type": "multiple-choice",
  "question": "",
  "choices": [
  "A) p + r + s",
  "B) 20(p + r + s)",
  "C) prs / (pr + ps + rs)",
  "D) prs / (20p + 20r + 20s)"
],
  "image": "/static/March2025_Images/AdvancedMath/NonlinearEquationsSystems/12229_10.png",
  "difficulty": "hard",
  "active": "no",
  "marked": False,
  "answer": "C) prs / (pr + ps + rs)",
  "explanation": "Choice C is correct. Multiplying each side of the given equation by 1/20 yields 1/20(20/p)=1/20(20/q-20/r-20/s). Distributing 1/20 on each side of this equation yields 20/20p=20/20q-20/20r-20/20s, or 1/p=1/q-1/r-1/s. Adding 1/r+1/s to each side of this equation yields 1/p+1/r+1/s=1/q. Multiplying 1/p by prs/prs, 1/r by prs/prs, and 1/s by prs/prs yields prs/pr+ps+rs+prs/pr+ps+rs+prs/pr+ps+rs=1/q, which is equivalent to pr+ps+rs/prs=1/q. Since pr+ps+rs/prs=1/q and it's given that p, q, r, and s are positive, it follows that the reciprocals of each side of this equation are also equal. Thus, prs/pr+ps+rs=q, or prs/pr+ps+rs=q. Therefore, prs/pr+ps+rs is equivalent to q. Choice A is incorrect and may result from conceptual or calculation errors. Choice B is incorrect and may result from conceptual or calculation errors. Choice D is incorrect and may result from conceptual or calculation errors."
},
{
  "id": 11,
  "type": "multiple-choice",
  "question": "",
  "choices": [
  "A) t / 12",
  "B) t",
  "C) t + 1/12",
  "D) 12t"
],
  "image": "/static/March2025_Images/AdvancedMath/NonlinearEquationsSystems/12233_11.png",
  "difficulty": "medium",
  "active": "no",
  "marked": False,
  "answer": "D) 12t",
  "explanation": "Choice D is correct. Subtracting b from each side of the given equation yields 12t=c-b. Therefore, the expression 12t correctly expresses the value of c-b in terms of t. Choice A is incorrect and may result from conceptual or calculation errors. Choice B is incorrect and may result from conceptual or calculation errors. Choice C is incorrect and may result from conceptual or calculation errors."
},
{
  "id": 12,
  "type": "multiple-choice",
  "question": "",
  "choices": [
  "A) y = 57x + p",
  "B) y = px + 57",
  "C) y = 57px",
  "D) y = px / 57"
],
  "image": "/static/March2025_Images/AdvancedMath/NonlinearEquationsSystems/12245_12.png",
  "difficulty": "easy",
  "active": "no",
  "marked": False,
  "answer": "B) y = px + 57",
  "explanation": "Choice B is correct. Adding 57 to each side of the given equation yields y=px+57. Therefore, the equation y=px+57 correctly expresses y in terms of p and x. Choice A is incorrect and may result from conceptual errors. Choice C is incorrect and may result from conceptual errors. Choice D is incorrect and may result from conceptual errors."
},
{
  "id": 13,
  "type": "multiple-choice",
  "question": "",
  "choices": [
  "A) (0, 8)",
  "B) (7/2, 9/2)",
  "C) (-7/2, 9/2)",
  "D) (-3, 4)"
],
  "image": "/static/March2025_Images/AdvancedMath/NonlinearEquationsSystems/12246_13.png",
  "difficulty": "easy",
  "active": "no",
  "marked": False,
  "answer": "C) (-7/2, 9/2)",
  "explanation": "Choice C is correct. The solution to a system of two equations corresponds to the point where the graphs of the equations intersect. The graphs of the linear function and the absolute value function shown intersect at a point with an x-coordinate between -4 and -3 and a y-coordinate between 4 and 5. Of the given choices, only (-7/2, 9/2) has an x-coordinate between -4 and -3 and a y-coordinate between 4 and 5. Choice A is incorrect. This is the y-intercept of the graph of the linear function. Choice B is incorrect and may result from conceptual or calculation errors. Choice D is incorrect. This is the vertex of the graph of the absolute value function."
},
{
  "id": 14,
  "type": "multiple-choice",
  "question": "",
  "choices": [
  "A) 12tw",
  "B) 6(t - w)",
  "C) (w - t) / 6tw",
  "D) 6tw / (w - t)"
],
  "image": "/static/March2025_Images/AdvancedMath/NonlinearEquationsSystems/12247_14.png",
  "difficulty": "hard",
  "active": "no",
  "marked": False,
  "answer": "D) 6tw / (w - t)",
  "explanation": "Choice D is correct. Adding 2/t to each side of the given equation yields 12/n=-2/w+2/t. The fractions on the right side of this equation have a common denominator of tw; therefore, the equation can be written as 12/n=2w/tw-2t/tw, or 12/n=2w-2t/tw, which is equivalent to 12/n=2(w-t)/tw. Dividing each side of this equation by 2 yields 6/n=w-t/tw. Since n, t, w, and w-t are all positive quantities, taking the reciprocal of each side of the equation 6/n=w-t/tw yields an equivalent equation: n/6=tw/w-t. Multiplying each side of this equation by 6 yields n=6tw/w-t. Choice A is incorrect and may result from conceptual or calculation errors. Choice B is incorrect and may result from conceptual or calculation errors. Choice C is incorrect. This is equivalent to 1/n rather than n."
},
{
  "id": 15,
  "type": "multiple-choice",
  "question": "",
  "choices": [
  "A) 146 / 5",
  "B) -12",
  "C) 0",
  "D) 26 / 5"
],
  "image": "/static/March2025_Images/AdvancedMath/NonlinearEquationsSystems/12252_12.png",
  "difficulty": "hard",
  "active": "no",
  "marked": False,
  "answer": "D) 26 / 5",
  "explanation": "Choice D is correct. By the definition of absolute value, if |-5x+13|=73, then -5x+13=73 or -5x+13=-73. Subtracting 13 from both sides of the equation -5x+13=73 yields -5x=60. Dividing both sides of this equation by -5 yields x=-12. Subtracting 13 from both sides of the equation -5x+13=-73 yields -5x=-86. Dividing both sides of this equation by -5 yields x=86/5. Therefore, the solutions to the given equation are -12 and 86/5, and it follows that the sum of the solutions to the given equation is -12+86/5, or 26/5. Choice A is incorrect and may result from conceptual or calculation errors. Choice B is incorrect. This is a solution, not the sum of the solutions, to the given equation. Choice C is incorrect and may result from conceptual or calculation errors."
}
]
	
nonlinear_functions = [
  {
  "id": 1,
  "type": "multiple-choice",
  "question": "",
  "choices": [
  "A) The estimated value of the tablet was $225 when it was purchased.",
  "B) The estimated value of the tablet 24 months after it was purchased was $225.",
  "C) The estimated value of the tablet had decreased by $225 in the 24 months after it was purchased.",
  "D) The estimated value of the tablet decreased by approximately 2.25% each year after it was purchased."
],
  "image": "/static/March2025_Images/AdvancedMath/NonlinearFunctions/12200_1.png",
  "difficulty": "easy",
  "active": "no",
  "marked": False,
  "answer":  "A) The estimated value of the tablet was $225 when it was purchased.",
  "explanation": "Choice A is correct. It's given that the graph shown gives the estimated value y, in dollars, of a tablet as a function of the number of months since it was purchased, x. The y-intercept of a graph is the point at which the graph intersects the y-axis, or when x is 0. The graph shown intersects the y-axis at the point (0, 225). It follows that 0 months after the tablet was purchased, or when the tablet was purchased, the estimated value of the tablet was 225 dollars. Therefore, the best interpretation of the y-intercept is that the estimated value of the tablet was $225 when it was purchased. Choice B is incorrect. The estimated value of the tablet 24 months after it was purchased was $50, not $225. Choice C is incorrect. The estimated value of the tablet had decreased by $225 - $50, or $175, not $225, in the 24 months after it was purchased. Choice D is incorrect and may result from conceptual errors."
},
{
  "id": 2,
  "type": "multiple-choice",
  "question": "",
  "choices": [
  "A) I only",
  "B) II only",
  "C) I and II",
  "D) Neither I nor II"
],
  "image": "/static/March2025_Images/AdvancedMath/NonlinearFunctions/12201_2.png",
  "difficulty": "hard",
  "active": "no",
  "marked": False,
  "answer": "D) Neither I nor II",
  "explanation": "Choice D is correct. A y-intercept of a graph in the xy-plane is a point where the graph intersects the y-axis, or a point where x=0. Substituting 0 for x in the equation defining function f yields f(0)=a(2.2^0+2.2^b), or f(0)=a(1+2.2^b). So, the y-coordinate of the y-intercept of the graph is a(1+2.2^b), or equivalently, a+a(2.2^b). It's given that function g is equivalent to function f, where 0<a<b. It follows that k=2.2^b. Since a(2.2^b) can't be equal to 0, the coefficient a can't be equal to a+a(2.2^b). Since 0<a, the constant k, which is equal to 2.2^b, can't be equal to a+a(2.2^b). Therefore, function g doesn't display the y-coordinate of the y-intercept of the graph of y=f(x) in the xy-plane as a constant or coefficient. It's also given that function h is equivalent to function f, where 0<a<b. The equation defining f can be rewritten as f(x)=a(2.2^x)+a(2.2^b). It follows that m=a(2.2^b). Since a(2.2^b) can't be equal to 0, the coefficient a can't be equal to a+a(2.2^b). Since 0<a, the constant m, which is equal to a(2.2^b), can't be equal to a+a(2.2^b). Therefore, function h doesn't display the y-coordinate of the y-intercept of the graph of y=f(x) in the xy-plane as a constant or coefficient. Thus, neither function g nor function h displays the y-coordinate of the y-intercept of the graph of y=f(x) in the xy-plane as a constant or coefficient. Choice A is incorrect and may result from conceptual or calculation errors. Choice B is incorrect and may result from conceptual or calculation errors. Choice C is incorrect and may result from conceptual or calculation errors."
},
{
  "id": 3,
  "type": "multiple-choice",
  "question": "",
  "choices": [
  "A) This toy rocket reaches an estimated maximum height of 502 feet 16 seconds after it is launched into the air.",
  "B) This toy rocket reaches an estimated maximum height of 502 feet 5.6 seconds after it is launched into the air.",
  "C) This toy rocket reaches an estimated maximum height of 16 feet 502 seconds after it is launched into the air.",
  "D) This toy rocket reaches an estimated maximum height of 5.6 feet 502 seconds after it is launched into the air."
],
  "image": "/static/March2025_Images/AdvancedMath/NonlinearFunctions/12203_3.png",
  "difficulty": "medium",
  "active": "no",
  "marked": False,
  "answer": "B) This toy rocket reaches an estimated maximum height of 502 feet 5.6 seconds after it is launched into the air.",
  "explanation": "Choice B is correct. The vertex of the graph of a quadratic equation is where it reaches its minimum or maximum value. When a quadratic equation is written in the form y = a(x - h)² + k, the vertex of the parabola represented by the equation is (x, y) = (h, k). In the given equation y = -16(x - 5.6)² + 502, the value of h is 5.6 and the value of k is 502. It follows that the vertex of the graph of this equation in the xy-plane is (x, y) = (5.6, 502). Additionally, since a = -16 in the given equation, the graph of the quadratic equation opens down, and the vertex represents a maximum. It's given that the value of y represents the estimated height, in feet, of the toy rocket x seconds after it is launched into the air. Therefore, this toy rocket reaches an estimated maximum height of 502 feet 5.6 seconds after it is launched into the air. Choice A is incorrect. The 16 in the equation is an indicator of how narrow the graph of the equation is rather than where it reaches its maximum. Choice C is incorrect. The 16 in the equation is an indicator of how narrow the graph of the equation is rather than where it reaches its maximum. Choice D is incorrect. This is an interpretation of the vertex of the graph of the equation y = -16(x - 502)² + 5.6, not of the equation y = -16(x - 5.6)² + 502."
},
{
  "id": 4,
  "type": "multiple-choice",
  "question": "",
  "choices": [
  "A) g(x) = -25^x",
  "B) g(x) = -(1/25)^x",
  "C) g(x) = 25^x",
  "D) g(x) = (1/25)^x"
],
  "image": "/static/March2025_Images/AdvancedMath/NonlinearFunctions/12204_4.png",
  "difficulty": "medium",
  "active": "no",
  "marked": False,
  "answer": "D) g(x) = (1/25)^x",
  "explanation": "Choice D is correct. It's given that function g is exponential. Therefore, an equation defining g can be written in the form g(x)=a(b)^x, where a and b are constants. The table shows that when x=0, g(x)=1. Substituting 0 for x and 1 for g(x) in the equation g(x)=a(b)^x yields 1=a(b)^0, which is equivalent to 1=a. Substituting 1 for a in the equation g(x)=a(b)^x yields g(x)=(b)^x. The table also shows that when x=1, g(x)=1/25. Substituting 1 for x and 1/25 for g(x) in the equation g(x)=(b)^x yields 1/25=(b)^1, which is equivalent to 1/25=b. Substituting 1/25 for b in the equation g(x)=(b)^x yields g(x)=(1/25)^x. Choice A is incorrect. For this function, g(1) is equal to -25, not 1/25. Choice B is incorrect. For this function, g(1) is equal to -1/25, not 1/25. Choice C is incorrect. For this function, g(1) is equal to 25, not 1/25."
},
{
  "id": 5,
  "type": "multiple-choice",
  "question": "",
  "choices": [
  "A) h(x) = 1.12(0.23)^x",
  "B) h(x) = 1.12(1.23)^x",
  "C) h(x) = 1.23(0.12)^x",
  "D) h(x) = 1.23(1.12)^x"
],
  "image": "/static/March2025_Images/AdvancedMath/NonlinearFunctions/12205_5.png",
  "difficulty": "easy",
  "active": "no",
  "marked": False,
  "answer": "D) h(x) = 1.23(1.12)^x",
  "explanation": "Choice D is correct. The table shows an increasing exponential relationship between the number of years, x, since Hana started training in pole vault and the estimated height h(x), in meters, of her best pole vault for that year. The relationship can be written as h(x)=Ca^x, where C and a are positive constants. It's given that when x=0, h(x)=1.23. Substituting 0 for x and 1.23 for h(x) in h(x)=Ca^x yields 1.23=Ca^0, or 1.23=C. Substituting 1.23 for C in h(x)=Ca^x yields h(x)=1.23a^x. It's also given that when x=2, h(x)=1.54. Substituting 2 for x and 1.54 for h(x) in h(x)=1.23a^x yields 1.54=1.23a². Dividing each side of this equation by 1.23 yields 1.54/1.23=1.23a²/1.23, or a² is approximately equal to 1.252. Since a is positive, a is approximately equal to sqrt(1.252), or 1.12. Substituting 1.12 for a in h(x)=1.23a^x yields h(x)=1.23(1.12)^x. Choice A is incorrect. When x=0, the value of h(x) in this function is equal to 1.12 rather than 1.23, and it is decreasing rather than increasing. Choice B is incorrect. When x=0, the value of h(x) in this function is equal to 1.12 rather than 1.23. Choice C is incorrect. This function is decreasing rather than increasing."
},
{
  "id": 6,
  "type": "multiple-choice",
  "question": "",
  "choices": [
  "A) 46",
  "B) 45",
  "C) 44",
  "D) -1"
],
  "image": "/static/March2025_Images/AdvancedMath/NonlinearFunctions/12206_6.png",
  "difficulty": "easy",
  "active": "no",
  "marked": False,
  "answer": "B) 45",
  "explanation": "Choice B is correct. It's given that f(x)=(x-44)(x-46), which can be rewritten as f(x)=x^2-90x + 2,024. Since the coefficient of the x^2-term is positive, the graph of y = f(x) in the xy-plane opens upward and reaches its minimum value at its vertex. For an equation in the form f(x)=ax^2 + bx + c, where a, b, and c are constants, the x-coordinate of the vertex is -b/2a. For the equation f(x)=x^2-90x + 2,024, a=1, b=-90, and c = 2,024. It follows that the x-coordinate of the vertex is -(-90)/2(1), or 45. Therefore, f(x) reaches its minimum when the value of x is 45. Choice A is incorrect. This is one of the x-coordinates of the x-intercepts of the graph of y = f(x) in the xy-plane. Choice C is incorrect. This is one of the x-coordinates of the x-intercepts of the graph of y = f(x) in the xy-plane. Choice D is incorrect. This is the y-coordinate of the vertex of the graph of y = f(x) in the xy-plane."
},
{
  "id": 7,
  "type": "multiple-choice",
  "question": "",
  "choices": [
  "A) 2",
  "B) 790",
  "C) 1,580",
  "D) 40,000"
],
  "image": "/static/March2025_Images/AdvancedMath/NonlinearFunctions/12207_7.png",
  "difficulty": "easy",
  "active": "no",
  "marked": False,
  "answer": "B) 70",
  "explanation": "Choice B is correct. It's given that t minutes after an initial observation, the number of bacteria in a population is 40000(2)t/70. This expression consists of the initial number of bacteria, 40000, multiplied by the expression 2t/70. The time, in minutes, it takes for the number of bacteria to double is the increase in the value of t that causes the expression 2t/70 to double. Since the base is 2, the expression 2t/70 will double when the exponent increases by 1. Since the exponent of this expression is t/70, the exponent will increase by 1 when t increases by 70. Therefore, the time, in minutes, it takes for the number of bacteria in the population to double is 70. Choice A is incorrect. This is the base of the exponent, not the time it takes for the number of bacteria in the population to double. Choice C is incorrect. This is the number of minutes it takes for the population to double twice. Choice D is incorrect. This is the number of bacteria that are initially observed, not the time it takes for the number of bacteria in the population to double."
},
{
  "id": 8,
  "type": "multiple-choice",
  "question": "",
  "choices": [
  "A) 5/8",
  "B) 25/8",
  "C) 5",
  "D) 25"
],
  "image": "/static/March2025_Images/AdvancedMath/NonlinearFunctions/12208_8.png",
  "difficulty": "easy",
  "active": "no",
  "marked": False,
  "answer": "C) 5",
  "explanation": "Choice C is correct. It's given that the function g is defined by g(x)=√8z+1. Substituting 3 for z in the given function yields g(3)= √8(3)+1, which is equivalent to g(3)= √25, or g(3) 5. Therefore, the value of g(3) is 5. Choice A is incorrect and may result from conceptual or calculation errors. Choice B is incorrect and may result from conceptual or calculation errors. Choice D is incorrect. This is the value of 8(3)+1, not √8(3)+1."
},
{
  "id": 9,
  "type": "multiple-choice",
  "question": "",
  "choices": [
  "A) f(x) = 22(1.5)^{x+1}",
  "B) f(x) = 33(1.5)^x",
  "C) f(x) = 49.5(1.5)^{x-1}",
  "D) f(x) = 74.25(1.5)^{x-2}"
],
  "image": "/static/March2025_Images/AdvancedMath/NonlinearFunctions/12209_9.png",
  "difficulty": "easy",
  "active": "no",
  "marked": False,
  "answer": "B) f(x) = 33(1.5)^x",
  "explanation": "Choice B is correct. Each of the given choices is an equation of the form f(x)= a(b)k, where a, b, and k are constants. For an equation of this form, the coefficient, a, is equal to the value of the function when the exponent is equal to 0, or when zk. It follows that in the equation f(x)= 33(1.5), the coefficient, 33, is equal to the value of f(0). Substituting 0 for z in this equation yields f(0)= 33(1.5), which is equivalent to f(0)= 33(1), or f(0)= 33. Thus, the value of c is 33 and the equation f(x)= 33(1.5) shows the value of c as the coefficient. Choice A is incorrect. This equation shows the value of f(-1), not f(0), as the coefficient. Choice C is incorrect. This equation shows the value of f(1), not f(0), as the coefficient. Choice D is incorrect. This equation shows the value of f(2), not f(0), as the coefficient."
},
{
  "id": 10,
  "type": "multiple-choice",
  "question": "",
  "choices": [
  "A) The estimated percent decrease in the population for this species and area every 8 years after 2008",
  "B) The estimated percent decrease in the population for this species and area each year after 2008",
  "C) The estimated population for this species and area 8 years after 2008",
  "D) The estimated initial population for this species and area in 2008"
],
  "image": "/static/March2025_Images/AdvancedMath/NonlinearFunctions/12210_10.png",
  "difficulty": "easy",
  "active": "no",
  "marked": False,
  "answer": "D) The estimated initial population for this species and area in 2008",
  "explanation": "Choice D is correct. Substituting 0 for x in the given equation yields f(0)= 3,000(0.75)^0, which is equivalent to f(0)= 3,000(1), or f(0)= 3,000. It's given that the function estimates the species' population z years after 2008, so it follows that the estimated population of the species is 3,000 in 2008. Therefore, the best interpretation of 3,000 in this context is the estimated initial population for this species and area in 2008. Choice A is incorrect and may result from conceptual errors. Choice B is incorrect. The estimated percent decrease in the population for this species and area each year after 2008 is 25%, not 3,000. Choice C is incorrect. The estimated population for this species and area 8 years after 2008 is 3,000(0.75)^8, or approximately 300, not 3,000."
},
{
  "id": 11,
  "type": "multiple-choice",
  "question": "",
  "choices": [
  "A) 0 = x^2 - 24x - 2,661",
  "B) 0 = x^2 - 24x + 2,661",
  "C) 0 = x^2 + 24x - 2,661",
  "D) 0 = x^2 + 24x + 2,661"
],
  "image": "/static/March2025_Images/AdvancedMath/NonlinearFunctions/12211_11.png",
  "difficulty": "easy",
  "active": "no",
  "marked": False,
  "answer": "A) 0 = x^2 - 24x - 2,661",
  "explanation": "Choice A is correct. It's given that the banner's length x, in inches, is 24 inches longer than its width, in inches. It follows that the banner's width, in inches, can be represented by the expression x - 24. The area of a rectangle is the product of its length and its width. It's given that the area of the banner is 2,661 square inches, so it follows that 2,661 = x(x - 24), or 2,661 = x^2 - 24x. Subtracting 2,661 from each side of this equation yields 0 = x^2 - 24x - 2,661. Therefore, the equation that represents this situation is 0 = x^2 - 24x - 2,661. Choice B is incorrect and may result from representing the width, in inches, of the banner as 24 - x. rather than x - 24. Choice C is incorrect and may result from representing the width, in inches, of the banner as x + 24. rather than x - 24. Choice D is incorrect and may result from conceptual or calculation errors."
},
{
  "id": 12,
  "type": "multiple-choice",
  "question": "",
  "choices": [
  "A) 7.25",
  "B) 14.50",
  "C) 105.13",
  "D) 210.25"
],
  "image": "/static/March2025_Images/AdvancedMath/NonlinearFunctions/12213_12.png",
  "difficulty": "easy",
  "active": "no",
  "marked": False,
  "answer": "B) 14.50",
  "explanation": "Choice B is correct. It's given that the function h estimates that the object is 3364 feet above the ground when it's dropped at t = 0. Substituting 3364 for h(t) and 0 for t in the function h yields 3364 = -16(0)^2 + b, or 3364 = b. Substituting 3364 for b in the function h yields h(t)=-16t^2 + 3364. When the object hits the ground, its height will be 0 feet above the ground. Substituting 0 for h(t) in h(t)=-16t^2 + 3364 yields 0 = -16t^2 + 3364. Adding 16t^2 to each side of this equation yields 16t^2 = 3364. Dividing each side of this equation by 16 yields t^2 = 210.25. Since the object will hit the ground at a positive number of seconds after it's dropped, the value of t can be found by taking the positive square root of each side of this equation, which yields t = 14.50. It follows that the function estimates the object will hit the ground approximately 14.50 seconds after being dropped. Choice A is incorrect. The function estimates that 7.25 seconds after being dropped, the object's height will be -16(7.25)^2 + 3364 feet, or 2523 feet, above the ground. Choice C is incorrect and may result from conceptual or calculation errors. Choice D is incorrect and may result from conceptual or calculation errors."
},
{
  "id": 13,
  "type": "free-response",
  "question": "",
  "choices": [],
  "image": "/static/March2025_Images/AdvancedMath/NonlinearFunctions/12218_14.png",
  "difficulty": "medium",
  "active": "no",
  "marked": False,
  "answer": "77",
  "explanation": "The correct answer is 77. It's given that the function f is defined by f(x)=x^2+x+71. Substituting 2 for x in function f yields f(2)=2^2+2+71, which is equivalent to f(2)=4+2+71, or f(2)=77. Therefore, the value of f(2) is 77."
},
{
  "id": 14,
  "type": "free-response",
  "question": "",
  "choices": [],
  "image": "/static/March2025_Images/AdvancedMath/NonlinearFunctions/12223_16.png",
  "difficulty": "medium",
  "active": "no",
  "marked": False,
  "answer": "-19",
  "explanation": "The correct answer is -19. It's given that function f is defined by f(x)= a^x + b, where a and b are constants and a > 0. It's also given that the graph of y = f(x) in the xy-plane has a y-intercept at (0, -25) and passes through the point (2, 23). Since the graph has a y-intercept at (0, -25), f(0)=-25. Substituting 0 for x in the given equation yields f(0)= a^0 + b, or f(0)=1+ b, and substituting -25 for f(0) in this equation yields -25 = 1 + b. Subtracting 1 from each side of this equation yields -26 = b. Substituting -26 for b in the equation f(x)= a^x + b yields f(x)= a^x - 26. Since the graph also passes through the point (2, 23), f(2)= 23. Substituting 2 for x in the equation f(x)= a^x - 26 yields f(2)= a^2 - 26, and substituting 23 for f(2) yields 23 = a^2 - 26. Adding 26 to each side of this equation yields 49 = a^2. Taking the square root of both sides of this equation yields +-7 = a. Since it's given that a > 0, the value of a is 7. It follows that the value of a+b is 7-26, or -19."
},
{
  "id": 15,
  "type": "free-response",
  "question": "",
  "choices": [],
  "image": "/static/March2025_Images/AdvancedMath/NonlinearFunctions/12227_17.png",
  "difficulty": "medium",
  "active": "no",
  "marked": False,
  "answer": "68",
  "explanation": "The correct answer is 68. It's given that the function f is defined by f(x)=8x^3+4. Substituting 2 for x in this equation yields f(2)=8(2)^3+4, or f(2)=8(8)+4, which is equivalent to f(2)=68. Therefore, the value of f(2) is 68."
},
{
  "id": 16,
  "type": "multiple-choice",
  "question": "",
  "choices": [
  "A) p = 0.96(15,000)^x",
  "B) p = 1.04(15,000)^x",
  "C) p = 15,000(0.96)^x",
  "D) p = 15,000(1.04)^x"
],
  "image": "/static/March2025_Images/AdvancedMath/NonlinearFunctions/12230_18.png",
  "difficulty": "easy",
  "active": "no",
  "marked": False,
  "answer": "D) p = 15,000(1.04)^x",
  "explanation": "Choice D is correct. It's given that a model predicts the population of Bergen in 2005 was 15,000. The model also predicts that each year for the next 5 years, the population increased by 4% of the previous year's population. The predicted population in one of these years can be found by multiplying the predicted population from the previous year by 1.04. Since the predicted population in 2005 was 15,000, the predicted population 1 year later is 15,000(1.04). The predicted population 2 years later is this value times 1.04, which is 15,000(1.04)(1.04), or 15,000(1.04)2. The predicted population 3 years later is this value times 1.04, or 15,000(1.04)3. More generally, the predicted population, p, x years after 2005 is represented by the equation p = 15,000(1.04)x. Choice A is incorrect. Substituting 0 for x in this equation indicates the predicted population in 2005 was 0.96 rather than 15,000. Choice B is incorrect. Substituting 0 for x in this equation indicates the predicted population in 2005 was 1.04 rather than 15,000. Choice C is incorrect. This equation indicates the predicted population is decreasing, rather than increasing, by 4% each year."
},
{
  "id": 17,
  "type": "multiple-choice",
  "question": "",
  "choices": [
  "A) 67",
  "B) 35",
  "C) 32",
  "D) 27"
],
  "image": "/static/March2025_Images/AdvancedMath/NonlinearFunctions/12232_19.png",
  "difficulty": "easy",
  "active": "no",
  "marked": False,
  "answer": "B) 35",
  "explanation": "Choice B is correct. It's given that the table shows three values of x and their corresponding values of y for the equation y = 4(2)^x + 3. It's also given that when x = 3 the corresponding value of y is a, and a is a constant. Substituting 3 for x and a for y in the given equation yields a = 4(2)^3 + 3, or a = 35. Therefore, the value of a is 35. Choice A is incorrect and may result from conceptual or calculation errors. Choice C is incorrect and may result from conceptual or calculation errors. Choice D is incorrect and may result from conceptual or calculation errors."
},
{
  "id": 18,
  "type": "free-response",
  "question": "",
  "choices": [],
  "image": "/static/March2025_Images/AdvancedMath/NonlinearFunctions/12234_20.png",
  "difficulty": "medium",
  "active": "no",
  "marked": False,
  "answer": "3",
  "explanation": "The correct answer is 3. For the graph of the exponential function f shown, where y=f(x), it's given that the y-intercept of the graph is (0,y). The graph intersects the y-axis at the point (0,3). Therefore, the value of y is 3."
},
{
  "id": 19,
  "type": "free-response",
  "question": "",
  "choices": [],
  "image": "/static/March2025_Images/AdvancedMath/NonlinearFunctions/12235_21.png",
  "difficulty": "medium",
  "active": "no",
  "marked": False,
  "answer": "14",
  "explanation": "The correct answer is either 14, -5, or -4. The x-intercepts of a graph in the xy-plane are the points at which the graph intersects the x-axis, or when the value of y is 0. Substituting 0 for y in the given equation yields 0 = 3(x-14)(x+5)(x+4). Dividing both sides of this equation by 3 yields 0=(x-14)(x+5)(x+4). Applying the zero product property to this equation yields three equations: x - 14 = 0, x + 5 = 0, and x + 4 = 0. Adding 14 to both sides of the equation x - 14 = 0 yields x = 14, subtracting 5 from both sides of the equation x + 5 = 0 yields x = -5, and subtracting 4 from both sides of the equation x + 4 = 0 yields x = -4. Therefore, the x-coordinates of the x-intercepts of the graph of the given equation are 14, -5, and -4. Note that 14, -5, and -4 are examples of ways to enter a correct answer."
},{
  "id": 20,
  "type": "free-response",
  "question": "",
  "choices": [
  "A) M(t) = 890(1/2)^(t/10)",
  "B) M(t) = 890(1/10)^(t/2)",
  "C) M(t) = 890(2)^(t/10)",
  "D) M(t) = 890(10)^(t/2)"
],
  "image": "/static/March2025_Images/AdvancedMath/NonlinearFunctions/12236_22.png",
  "difficulty": "medium",
  "active": "no",
  "marked": False,
  "answer": "C) M(t) = 890(2)^(t/10)",
  "explanation": "Choice C is correct. It's given that t represents the number of years since the account was opened. Therefore, t/10 represents the number of 10-year periods since the account was opened. Since the value of the account doubles during each of these 10-year periods, the value of the account can be found by multiplying the initial value by t/10 factors of 2. This is equivalent to 2^(t/10). It's given that the initial value of the account is $890. Therefore, the value of the account M(t), in dollars, t years after the account was opened can be represented by M(t)= 890(2)^(t/10). Choice A is incorrect. This equation represents the value of an account if the value of the account halves, not doubles, every 10 years. Choice B is incorrect. This equation represents the value of an account if the value of the account decreases by 90%, not doubles, every 2, not 10, years. Choice D is incorrect. This equation represents the value of an account if the value of the account increases by a factor of 10, not doubles, every 2, not 10, years."
},
{
  "id": 21,
  "type": "free-response",
  "question": "",
  "choices": [],
  "image": "/static/March2025_Images/AdvancedMath/NonlinearFunctions/12237_23.png",
  "difficulty": "medium",
  "active": "no",
  "marked": False,
  "answer": "11/4",
  "explanation": "The correct answer is 11/4. It's given that the function f is defined by f(x)=5(1/4-x)^2+11/4. Substituting 1/4 for x in this equation yields f(1/4)=5(1/4-1/4)^2+11/4, which is equivalent to f(1/4)=5(0)^2+11/4, or f(1/4)=11/4. Therefore, the value of f(1/4) is 11/4. Note that 11/4 or 2.75 are examples of ways to enter a correct answer."
},
{
  "id": 22,
  "type": "free-response",
  "question": "",
  "choices": [],
  "image": "/static/March2025_Images/AdvancedMath/NonlinearFunctions/12238_24.png",
  "difficulty": "medium",
  "active": "no",
  "marked": False,
  "answer": "35",
  "explanation": "The correct answer is 35. It's given that the function g(x) = -(1/55)(x+19)(x-35) gives the depth below the surface of the ocean, in meters, of the submersible device x minutes after collecting a sample, where x > 0. It follows that when the submersible device is at the surface of the ocean, the value of g(x) is 0. Substituting 0 for g(x) in the equation g(x) = -(1/55)(x+19)(x-35) yields 0 = -(1/55)(x+19)(x-35). Multiplying both sides of this equation by -55 yields 0 = (x+19)(x-35). Since a product of two factors is equal to 0 if and only if at least one of the factors is 0, either x + 19 = 0 or x - 35 = 0. Subtracting 19 from both sides of the equation x + 19 = 0 yields x = -19. Adding 35 to both sides of the equation x - 35 = 0 yields x = 35. Since x > 0, 35 minutes after collecting the sample the submersible device reached the surface of the ocean."
},
{
  "id": 23,
  "type": "multiple-choice",
  "question": "",
  "choices": [
  "A) -20",
  "B) 5",
  "C) 10",
  "D) 45"
],
  "image": "/static/March2025_Images/AdvancedMath/NonlinearFunctions/12240_25.png",
  "difficulty": "easy",
  "active": "no",
  "marked": False,
  "answer": "C) 10",
  "explanation": "Choice C is correct. It's given that the function f is defined by f(x) = |x - 4x|. It's also given that f(5) - f(a) = -15. Substituting 5 for x in the function f(x) = |x - 4x| yields f(5) = |5 - 4(5)| and substituting a for x in the function f(x) = |x - 4x| yields f(a) = |a - 4a|. Therefore, f(5) = |5 - 20| = |-15| = 15 and f(a) = |-3a|. Substituting 15 for f(5) and |-3a| for f(a) in the equation f(5) - f(a) = -15 yields 15 - |-3a| = -15. Subtracting 15 from both sides of this equation yields -|-3a| = -30. Dividing both sides of this equation by -1 yields |-3a| = 30. By the definition of absolute value, if |-3a| = 30, then -3a = 30 or -3a = -30. Dividing both sides of each of these equations by -3 yields a = -10 or a = 10, respectively. Thus, of the given choices, a value of a that satisfies f(5) - f(a) = -15 is 10. Choices A, B and D are incorrect."
},
{
  "id": 24,
  "type": "free-response",
  "question": "",
  "choices": [],
  "image": "/static/March2025_Images/AdvancedMath/NonlinearFunctions/12241_26.png",
  "difficulty": "medium",
  "active": "no",
  "marked": False,
  "answer": "-13/2",
  "explanation": "The correct answer is −13/2. The value of x for which f(x) reaches its minimum can be found by rewriting the given equation in the form f(x) = (x − h)2 + 13x + 2, can be rewritten as f(x) = x2 + 13x + __) − __ + 2. By completing the square, this equation can be rewritten as f(x) = (x^2 + 13x + 169/4) − 169/4 + 2 = (x + 13/2)^2 − 121/4, which is equivalent to f(x) = (x + 13/2)^2 − 289/4 or f(x) = (x − (−13/2))^2 − 289/4. Therefore, f(x) reaches its minimum when the value of x is −13/2. Note that −13/2 and −6.5 are examples of ways to enter a correct answer. Another way to determine the value of x for which the function f(x) reaches its minimum is to use the fact that the graph of f(x) is a parabola. The value of x for the vertex of a parabola is the x-value of the midpoint between the two x-intercepts of the graph. The x-intercepts of a parabola in the form y = (x − a)(x − b) are a and b. It follows that the x-intercepts of the graph of y = f(x) in the xy-plane occur when x = −2 and x = −15, or at the points (−2, 0) and (−15, 0). The midpoint between two points, (x₁, y₁) and (x₂, y₂), is ((x₁ + x₂)/2, (y₁ + y₂)/2). Therefore, f(x) reaches its minimum when the value of x is (−2 + (−15))/2 = −17/2 = −13/2. Note that −13/2 and −6.5 are examples of ways to enter a correct answer."
},
{
  "id": 25,
  "type": "multiple-choice",
  "question": "",
  "choices": [
  "A) I only",
  "B) II only",
  "C) I and II",
  "D) Neither I nor II"
],
  "image": "/static/March2025_Images/AdvancedMath/NonlinearFunctions/12242_27.png",
  "difficulty": "easy",
  "active": "no",
  "marked": False,
  "answer": "B) II only",
  "explanation": "Choice B is correct. For the function f, since the base of the exponent, 1.25, is greater than 1, the value of (1.25)^x increases as x increases. Therefore, the value of f(x) = 18(1.25)^x + 41 also increases as x increases. Since f is therefore an increasing function where x ≥ 0, the function f has no maximum value. For the function g, since the base of the exponent, 0.73, is less than 1, the value of (0.73)^x decreases as x increases. Therefore, the value of g(x) = 9(0.73)^x also decreases as x increases. It follows that the maximum value of g(x) for x ≥ 0 occurs when x = 0. Substituting 0 for x in the function g yields g(0) = 9(0.73)^0, which is equivalent to g(0) = 9(1), or g(0) = 9. Therefore, the maximum value of g(x) for x ≥ 0 is 9, which appears as a coefficient in equation II. So, of the two equations given, only II displays, as a constant or coefficient, the maximum value of the function it defines, where x ≥ 0. Choice A is incorrect and may result from conceptual or calculation errors. Choice C is incorrect and may result from conceptual or calculation errors. Choice D is incorrect and may result from conceptual or calculation errors."
},
{
  "id": 26,
  "type": "multiple-choice",
  "question": "",
  "choices": [
  "A) 5",
  "B) 10",
  "C) 18",
  "D) 36"
],
  "image": "/static/March2025_Images/AdvancedMath/NonlinearFunctions/12243_2.png",
  "difficulty": "easy",
  "active": "no",
  "marked": False,
  "answer": "B) 10",
  "explanation": "Choice B is correct. The number that’s 8 more than x can be represented by the expression x + 8. It’s given that the product of x and x + 8 is 180, so it follows that (x)(x + 8) = 180, or x² + 8x = 180. Subtracting 180 from each side of this equation gives x² + 8x − 180 = 0. Factoring the left-hand side of this equation yields (x − 10)(x + 18) = 0. Applying the zero product property to this equation yields two solutions: x = 10 and x = −18. Since x is a positive number, the value of x is 10. Choice A is incorrect. If x = 5, the product of x and the number that’s 8 more than x would be (5)(13), or 65, not 180. Choice C is incorrect. This is the value of the number that’s 8 more than x, not the value of x. Choice D is incorrect. If x = 36, the product of x and the number that’s 8 more than x would be (36)(44), or 1,584, not 180."
},
{
  "id": 27,
  "type": "free-response",
  "question": "",
  "choices": [],
  "image": "/static/March2025_Images/AdvancedMath/NonlinearFunctions/12244_29.png",
  "difficulty": "medium",
  "active": "no",
  "marked": False,
  "answer": "168",
  "explanation": "The correct answer is 168. The quadratic function g gives the estimated depth of the seal, g(t), in meters, t minutes after the seal enters the water. It’s given that function g estimates that the seal reached its maximum depth of 302.4 meters 6 minutes after it entered the water. Therefore, function g can be expressed in vertex form as g(t) = a(t – 6)^2 + 302.4, where a is a constant. Since it’s also given that the seal reached the surface of the water after 12 minutes, g(12) = 0. Substituting 12 for t and 0 for g(t) in g(t) = a(t – 6)^2 + 302.4 yields 0 = a(12 – 6)^2 + 302.4, or 36a = –302.4. Dividing both sides of this equation by 36 gives a = –8.4. Substituting –8.4 for a in g(t) = a(t – 6)^2 + 302.4 gives g(t) = –8.4(t – 6)^2 + 302.4. Substituting 10 for t in g(t) gives g(10) = –8.4(10 – 6)^2 + 302.4, which is equivalent to g(10) = –8.4(4)^2 + 302.4, or g(10) = 168. Therefore, the estimated depth, to the nearest meter, of the seal 10 minutes after it entered the water was 168 meters."
},
{
  "id": 28,
  "type": "multiple-choice",
  "question": "",
  "choices": [
  "A) The predicted body mass of the animal was approximately 330 kg 362 days after it was born.",
  "B) The predicted body mass of the animal was approximately 362 kg 330 days after it was born.",
  "C) The predicted body mass of the animal was approximately 362 kg 330/7 days after it was born.",
  "D) The predicted body mass of the animal was approximately 330/7 kg 362 days after it was born."
],
  "image": "/static/March2025_Images/AdvancedMath/NonlinearFunctions/12244_30.png",
  "difficulty": "easy",
  "active": "no",
  "marked": False,
  "answer": "B) The predicted body mass of the animal was approximately 362 kg 330 days after it was born.",
  "explanation": "Choice B is correct. In the statement 'm(330) is approximately equal to 362,' the input of the function, 330, is the value of t, the elapsed time, in days, since the animal was born. The approximate value of the function, 362, is the predicted body mass, in kilograms, of the animal after that time has elapsed. Therefore, the predicted body mass of the animal was approximately 362 kg 330 days after it was born. Choice A is incorrect. This would be the best interpretation of the statement 'm(362) is approximately equal to 330.' Choice C is incorrect. The number 330/7 is the number of weeks, not the number of days, after the animal was born. Choice D is incorrect. This would be the best interpretation of the statement 'm(362) is approximately equal to 330/7.'"
},
{
  "id": 29,
  "type": "multiple-choice",
  "question": "",
  "choices": [
  "A) 4",
  "B) 3",
  "C) 2",
  "D) 1"
],
  "image": "/static/March2025_Images/AdvancedMath/NonlinearFunctions/12249_31.png",
  "difficulty": "easy",
  "active": "no",
  "marked": False,
  "answer": "B) 3",
  "explanation": "Choice B is correct. An x-intercept of a graph in the xy-plane is a point on the graph where the value of y is 0. Substituting 0 for y in the given equation yields 0 = 2(x - d)(x + d)(x + g)(x - d). By the zero product property, the solutions to this equation are x = d, x = -d, x = -g, and x = d. However, x = d and x = -d are repeated. It’s given that d and g are unique positive constants. It follows that the equation 0 = 2(x - d)(x + d)(x + g)(x - d) has 3 unique solutions: x = d, x = -d, and x = -g. Thus, the graph of the given equation has 3 distinct x-intercepts. Choice A is incorrect and may result from conceptual errors. Choice C is incorrect and may result from conceptual errors. Choice D is incorrect and may result from conceptual errors."
},
{
  "id": 30,
  "type": "multiple-choice",
  "question": "",
  "choices": [
  "A) (0, -2)",
  "B) (0, -3)",
  "C) (0, 2)",
  "D) (0, 3)"
],
  "image": "/static/March2025_Images/AdvancedMath/NonlinearFunctions/12251_32.png",
  "difficulty": "easy",
  "active": "no",
  "marked": False,
  "answer": "C) (0, 2)",
  "explanation": "Choice C is correct. The vertex of the graph of a quadratic function in the xy-plane is the point at which the graph is either at its minimum or maximum y-value. In the graph shown, the minimum y-value occurs at the point (0, 2). Choice A is incorrect. The graph shown doesn't pass through the point (0, -2). Choice B is incorrect. The graph shown doesn't pass through the point (0, -3). Choice D is incorrect. The graph shown doesn't pass through the point (0, 3)."
}
]
	
ratio_rates_proportional_units = [
  {
  "id": 1,
  "type": "multiple-choice",
  "question": "",
  "choices": [
  "A) 18",
  "B) 131",
  "C) 149",
  "D) 2,376"
],
  "image": "/static/March2025_Images/ProblemSolvingAndDataAnalysis/RatioRatesProportionalUnits/12257_1.png",
  "difficulty": "easy",
  "active": "no",
  "marked": False,
  "answer": "A) 18",
  "explanation": "Choice A is correct. It's given that there are 2358 raccoons in a 131-square-mile area. The estimated population density, in raccoons per square mile, is the estimated number of raccoons divided by the number of square miles. Therefore, the estimated population density of this area is (2358 raccoons)/(131 square miles) or 18 raccoons per square mile. Choice B is incorrect. This is the number of square miles in the area, not the estimated number of raccoons per square mile in this area. Choice C is incorrect and may result from conceptual or calculation errors. Choice D is incorrect and may result from conceptual or calculation errors."
},
{
  "id": 2,
  "type": "free-response",
  "question": "",
  "choices": [],
  "image": "/static/March2025_Images/ProblemSolvingAndDataAnalysis/RatioRatesProportionalUnits/12260_2.png",
  "difficulty": "medium",
  "active": "no",
  "marked": False,
  "answer": "90",
  "explanation": "The correct answer is 90. It's given that the ratio of x to y is equivalent to the ratio 9 to 5. It follows that x/y = 9/5. Multiplying each side of this equation by 5y yields (5y)x/y = 9(5y)/5, or 5x = 9y. Dividing each side of this equation by 9 yields 5x/9 = y. Substituting 162 for x in this equation yields 5(162)/9 = y, which is equivalent to 810/9 = y, or 90 = y. Therefore, if the value of x is 162, the value of y is 90."
},
{
  "id": 3,
  "type": "multiple-choice",
  "question": "",
  "choices": [
  "A) 0.3",
  "B) 16.3",
  "C) 195.8",
  "D) 220.4"
],
  "image": "/static/March2025_Images/ProblemSolvingAndDataAnalysis/RatioRatesProportionalUnits/12262_3.png",
  "difficulty": "hard",
  "active": "no",
  "marked": False,
  "answer": "B) 16.3",
  "explanation": "Choice B is correct. It's given that the speed of a vehicle is increasing at a rate of 7.3 meters per second squared. It's given to use 1 mile = 1,609 meters. There are 60 seconds in 1 minute; therefore, 60 squared or 3,600 seconds squared is equal to 1 minute squared. It follows that the rate of 7.3 meters per second squared is equivalent to (7.3meters/Sec^2)(1mile/1609meters)(3600sec^2/1min^2) approximately 16.33 miles per minute squared. The rate, in miles per minute squared, rounded to the nearest tenth is 16.3. Choice A is incorrect and may result from conceptual or calculation errors. Choice C is incorrect and may result from conceptual or calculation errors. Choice D is incorrect and may result from conceptual or calculation errors."
},
{
  "id": 4,
  "type": "free-response",
  "question": "",
  "choices": [],
  "image": "/static/March2025_Images/ProblemSolvingAndDataAnalysis/RatioRatesProportionalUnits/12265_4.png",
  "difficulty": "easy",
  "active": "no",
  "marked": False,
  "answer": "39000",
  "explanation": "The correct answer is 39000 Its given that the giant armadillo has a mass of 39 kilograms Since 1 kilogram is equal to 1000 grams 39 kilograms is equal to 39 kilograms 1 1000 grams 1 kilogram grams Therefore the giant armadillos mass in grams is 39000 or 39000."
},
{
  "id": 5,
  "type": "multiple-choice",
  "question": "",
  "choices": [
  "A) 61",
  "B) 67",
  "C) 94",
  "D) 192"
],
  "image": "/static/March2025_Images/ProblemSolvingAndDataAnalysis/RatioRatesProportionalUnits/12271_5.png",
  "difficulty": "easy",
  "active": "no",
  "marked": False,
  "answer": "D) 192",
  "explanation": "Choice D is correct. Since 1 yard is equal to 3 feet, 64 yards is equal to 64 yards (3 feet/1 yard), or 192 feet. It follows that 64 yards per second is equivalent to 192 feet per second. Therefore, the objects speed is 192 feet per second. Choice A is incorrect. A speed of 61 feet per second is equivalent to 61/3, not 64, yards per second. Choice B is incorrect. A speed of 67 feet per second is equivalent to 67/3, not 64, yards per second. Choice C is incorrect. A speed of 94 feet per second is equivalent to 94/3, not 64, yards per second."
},
{
  "id": 6,
  "type": "multiple-choice",
  "question": "",
  "choices": [
  "A) 306",
  "B) 402",
  "C) 25,960",
  "D) 233,640"
],
  "image": "/static/March2025_Images/ProblemSolvingAndDataAnalysis/RatioRatesProportionalUnits/12274_6.png",
  "difficulty": "easy",
  "active": "no",
  "marked": False,
  "answer": "D) 233,640",
  "explanation": "Choice D is correct. It's given that 1 furlong = 220 yards and 1 yard = 3 feet. It follows that a distance of 354 furlongs is equivalent to (354 furlongs)(220 yards/1 furlong)(3 feet/1 yard) or 233,640 feet. Choice A is incorrect and may result from conceptual or calculation errors. Choice B is incorrect and may result from conceptual or calculation errors. Choice C is incorrect and may result from conceptual or calculation errors."
},
{
  "id": 7,
  "type": "multiple-choice",
  "question": "",
  "choices": [
  "A) 9z/440",
  "B) 440z/9",
  "C) 5z/792",
  "D) 792z/5"
],
  "image": "/static/March2025_Images/ProblemSolvingAndDataAnalysis/RatioRatesProportionalUnits/12275_7.png",
  "difficulty": "hard",
  "active": "no",
  "marked": False,
  "answer": "D) 792z/5",
  "explanation": "Choice D is correct. It's given that a hose puts 88x ounces of water in a bucket in 5y minutes. Therefore, the rate at which the hose puts water in the bucket, in ounces per minute, can be represented by the expression 88x/5y. Let w represent the number of ounces of water the hose puts in the bucket in 9y minutes at this rate. It follows that the rate at which the hose puts water in the bucket, in ounces per minute, can be represented by the expression w/9y. The expressions 88x/5y and w/9y represent the same rate, so it follows that 88x/5y = w/9y. Multiplying both sides of this equation by 9y yields 792xy/5y = w, or 792x/5 = w. Therefore, the number of ounces of water the hose puts in the bucket in 9y minutes can be represented by the expression 792x/5. Choice A is incorrect and may result from conceptual or calculation errors. Choice B is incorrect and may result from conceptual or calculation errors. Choice C is incorrect and may result from conceptual or calculation errors."
},
{
  "id": 8,
  "type": "multiple-choice",
  "question": "",
  "choices": [
  "A) 0.39",
  "B) 1.27",
  "C) 13.67",
  "D) 23.24"
],
  "image": "/static/March2025_Images/ProblemSolvingAndDataAnalysis/RatioRatesProportionalUnits/12277_8.png",
  "difficulty": "hard",
  "active": "no",
  "marked": False,
  "answer": "A) 0.39",
  "explanation": "Choice A is correct. It's given that 1 meter = 3.28 feet. It follows that 1 square meter = 3.28^2 square feet, or 1 square meter = 10.7584 square feet. Since 1 hour = 60 minutes, it follows that 250 square feet per hour is equivalent to (250 square feet / 1 hour) * (1 square meter / 10.7584 square feet) * (1 hour / 60 minutes), or 250 square meters / 645.504 minutes, which is approximately 0.3873 square meters per minute. Of the given choices, 0.39 is closest to 0.3873. Choice B is incorrect and may result from conceptual or calculation errors. Choice C is incorrect and may result from conceptual or calculation errors. Choice D is incorrect and may result from conceptual or calculation errors."
}
]	
 
percentages = [
{
  "id": 1,
  "type": "free-response",
  "question": "",
  "choices": [],
  "image": "/static/March2025_Images/ProblemSolvingAndDataAnalysis/Percentages/12254_1.png",
  "difficulty": "medium",
  "active": "no",
  "marked": False,
  "answer": "110",
  "explanation": "The correct answer is 110. Let x represent the total number of items in the sample. It's given that 80% of the items are faulty and that there are 88 faulty items in the sample. Therefore, 80% of x is 88. Since 80% can be rewritten as 80/100, it follows that 80/100 x = 88. Multiplying both sides of this equation by 100 yields 80x = 8,800. Dividing both sides of this equation by 80 yields x = 110. Therefore, there are 110 total items in the sample"
},
{
  "id": 2,
  "type": "multiple-choice",
  "question": "",
  "choices": [
  "A) 22%",
  "B) 33%",
  "C) 66%",
  "D) 78%"
],
  "image": "/static/March2025_Images/ProblemSolvingAndDataAnalysis/Percentages/12255_2.png",
  "difficulty": "easy",
  "active": "no",
  "marked": False,
  "answer": "D) 78%",
  "explanation": "Choice D is correct. The proportion of the paper clips that are size large can be written as 234,000 / 300,000 or 0.78. Therefore, the percentage of the paper clips that are size large is 0.78(100), or 78%. Choice A is incorrect. This is the percentage of the paper clips that are not size large. Choice B is incorrect and may result from conceptual or calculation errors. Choice C is incorrect and may result from conceptual or calculation errors."
},
{
  "id": 3,
  "type": "multiple-choice",
  "question": "",
  "choices": [
  "A) 138",
  "B) 217",
  "C) 283",
  "D) 383"
],
  "image": "/static/March2025_Images/ProblemSolvingAndDataAnalysis/Percentages/12258_3.png",
  "difficulty": "hard",
  "active": "no",
  "marked": False,
  "answer": "D) 383",
  "explanation": "Choice D is correct. It's given that a is 230% of b. It follows that a = (230/100)b. It's also given that a is 60% of c. It follows that a = (60/100)c. Since a = (230/100)b and a = (60/100)c, it follows that (230/100)b = (60/100)c. Multiplying each side of this equation by (100/60) yields (230/60)b = c. If c is p% of b, then c = (p/100)b. It follows that (230/60) = p/100. Multiplying each side of this equation by 100 yields (23000/60) = p. It follows that the value of p is approximately 383.33. Therefore, of the given choices, 383 is closest to the value of p. Choice A is incorrect. This is closest to the value of p if b is 230% of a, rather than if a is 230% of b, and if b is p% of c, rather than if c is p% of b. Choice B is incorrect. This is closest to the value of p if a is 230% greater than b, rather than 230% of b. Choice C is incorrect. This is closest to the value of p if c is p% greater than b, rather than p% of b."
},
{
  "id": 4,
  "type": "multiple-choice",
  "question": "",
  "choices": [
  "A) 6",
  "B) 15",
  "C) 75",
  "D) 244"
],
  "image": "/static/March2025_Images/ProblemSolvingAndDataAnalysis/Percentages/12268_4.png",
  "difficulty": "easy",
  "active": "no",
  "marked": False,
  "answer": "B) 15",
  "explanation": "Choice B is correct. It's given that there are 250 trees in a park and of these trees, 6% are birch trees. The number of birch trees in the park can be calculated by multiplying the number of trees in the park by 6/100. Therefore, the number of birch trees in the park is 250(6/100), or 15. Choice A is incorrect. This is the percentage of trees in the park that are birch trees, not the number of birch trees in the park. Choice C is incorrect. This is 30%, not 6%, of 250. Choice D is incorrect and may result from conceptual or calculation errors."
},
{
  "id": 5,
  "type": "multiple-choice",
  "question": "",
  "choices": [
  "A) 12,996",
  "B) 12,312",
  "C) 38",
  "D) 36"
],
  "image": "/static/March2025_Images/ProblemSolvingAndDataAnalysis/Percentages/12272_5.png",
  "difficulty": "hard",
  "active": "no",
  "marked": False,
  "answer": "D) 36",
  "explanation": "Choice D is correct. It's given that the result of increasing the quantity x by 1,800% is 684. It follows that x+(1,800/100)x = 684, which is equivalent to x+18x = 684, or 19x = 684. Dividing each side of this equation by 19 yields x = 36. Therefore, the value of x is 36. Choice A is incorrect. The result of increasing the quantity 12,996 by 1,800% is 246,924, not 684. Choice B is incorrect. The result of increasing the quantity 12,312 by 1,800% is 233,928, not 684. Choice C is incorrect. The result of increasing the quantity 38 by 1,800% is 722, not 684."
},
{
  "id": 6,
  "type": "free-response",
  "question": "",
  "choices": [],
  "image": "/static/March2025_Images/ProblemSolvingAndDataAnalysis/Percentages/12276_6.png",
  "difficulty": "medium",
  "active": "no",
  "marked": False,
  "answer": "27",
  "explanation": "The correct answer is 27. It's given that 6% of the 450 tiles in a box are black. Therefore, the number of black tiles in the box can be calculated by multiplying the number of tiles in the box by 6/100 which is equivalent to 450(6/100), or 27."
},
{
  "id": 7,
  "type": "multiple-choice",
  "question": "",
  "choices": [
  "A) 88",
  "B) 87",
  "C) 12",
  "D) 8"
],
  "image": "/static/March2025_Images/ProblemSolvingAndDataAnalysis/Percentages/12278_7.png",
  "difficulty": "hard",
  "active": "no",
  "marked": False,
  "answer": "A) 88",
  "explanation": "Choice A is correct. It's given that a scientist studying the life cycle of dragonflies counted the number of dragonflies in a certain habitat each day for 46 days. It's also given that on February 15, there were 99 dragonflies in the habitat and that the percent increase in the number of dragonflies in the habitat from January 1 to February 15 was 12.50%. This can be represented by the equation 99 = (1 + 12.50/100)x, where x represents the number of dragonflies in the habitat on January 1. This equation can be rewritten as 99 = 1.125x. Dividing both sides of this equation by 1.125 yields 88 = x. Therefore, there were 88 dragonflies in the habitat on January 1. Choice B is incorrect and may result from conceptual or calculation errors. Choice C is incorrect and may result from conceptual or calculation errors. Choice D is incorrect and may result from conceptual or calculation errors."
}
]

one_variable_data_distributions_center_spread = [
  {
  "id": 1,
  "type": "multiple-choice",
  "question": "",
  "choices": [
  "A) 0",
  "B) 1",
  "C) 4",
  "D) 6"
],
  "image": "/static/March2025_Images/ProblemSolvingAndDataAnalysis/OneVariableDataDistributionsCenterSpread/12253_1.png",
  "difficulty": "easy",
  "active": "no",
  "marked": False,
  "answer": "D) 6",
  "explanation": "Choice D is correct. It's given that the bar graph summarizes the charge, in kilowatt-hours (kWh), a battery received each day for 15 days. The height of each bar in the bar graph shown represents the number of days the battery received the charge, in kWh, specified at the bottom of the bar. The bar for a charge of 0 kWh reaches a height of 6. Therefore, the battery received a charge of 0 kWh for 6 of these days. Choice A is incorrect. This is the charge, in kWh, that the battery received, not the number of days the battery received this charge. Choice B is incorrect. This is the number of days the battery received a charge of either 8, 16, or 23 kWh. Choice C is incorrect. This is the number of days the battery received a charge of 11 kWh."
},
{
  "id": 2,
  "type": "multiple-choice",
  "question": "",
  "choices": [
  "A) 10",
  "B) 30",
  "C) 40",
  "D) 70"
],
  "image": "/static/March2025_Images/ProblemSolvingAndDataAnalysis/OneVariableDataDistributionsCenterSpread/12256_2.png",
  "difficulty": "easy",
  "active": "no",
  "marked": False,
  "answer": "A) 10",
  "explanation": "Choice A is correct. It's given that the bar graph shows the distribution of the number of students in each of four extracurricular activities at a high school. The bar representing drama has a height of 40; therefore, there are 40 students in drama. The bar representing chess has a height of 30; therefore, there are 30 students in chess. Thus, there are 40-30, or 10 more students in drama than in chess. Choice B is incorrect. This is the number of students in chess. Choice C is incorrect. This is the number of students in drama. Choice D is incorrect. This is the sum of the number of students in drama and in chess."
},
{
  "id": 3,
  "type": "multiple-choice",
  "question": "",
  "choices": [
  "A) Blue",
  "B) Green",
  "C) Red",
  "D) Yellow"
],
  "image": "/static/March2025_Images/ProblemSolvingAndDataAnalysis/OneVariableDataDistributionsCenterSpread/12259_3.png",
  "difficulty": "easy",
  "active": "no",
  "marked": False,
  "answer": "B) Green",
  "explanation": "Choice B is correct. It's given that a data set consists of 173 colors and the bar graph shows the number of times each color appears in the data set. Therefore, for each color specified at the bottom of the bar, the frequency corresponds to the number of times that color appears in the data set. The color that appears 70 times in the data set has a frequency of 70 on the bar graph. Since the bar with a frequency of 70 corresponds to green, green is the color that appears 70 times. Choice A is incorrect. The color blue appears about 27 times, not 70 times. Choice C is incorrect. The color red appears about 33 times, not 70 times. Choice D is incorrect. The color yellow appears about 43 times, not 70 times."
},
{
  "id": 4,
  "type": "multiple-choice",
  "question": "",
  "choices": [
  "A) The mean of the new data set is greater than the mean of the original data set, and the median of the new data set is greater than the median of the original data set.",
  "B) The mean of the new data set is greater than the mean of the original data set, and the medians of the two data sets are equal.",
  "C) The mean of the new data set is less than the mean of the original data set, and the median of the new data set is less than the median of the original data set.",
  "D) The mean of the new data set is less than the mean of the original data set, and the medians of the two data sets are equal."
],
  "image": "/static/March2025_Images/ProblemSolvingAndDataAnalysis/OneVariableDataDistributionsCenterSpread/12264_4.png",
  "difficulty": "hard",
  "active": "no",
  "marked": False,
  "answer": "B) The mean of the new data set is greater than the mean of the original data set, and the medians of the two data sets are equal.",
  "explanation": "Choice B is correct. The mean of a data set is the sum of the values in the data set divided by the number of values in the data set. The new data set consists of the weights of the 71 tortoises in the original data set and one additional weight, 39. Since the additional weight, 39, is greater than any of the values in the original data set, the mean of the new data set is greater than the mean of the original data set. If a data set contains an odd number of data values, the median is represented by the middle data value in the list when the data values are listed in ascending or descending order. Since the original data set consists of the weights of 71 tortoises and is in ascending order, the median of the original data set is represented by the middle value, or the 36th value. Based on the frequencies shown in the table, the 36th value in this data set is 17. If a data set contains an even number of data values, the median is between the two middle data values when the values are listed in ascending or descending order. Since the new data set consists of the weights of 72 tortoises, the median of the new data set is between the 36th and 37th data values when the values are arranged in ascending order. To keep the data in ascending order, the additional value of 39 would be placed at the bottom of the frequency table with a frequency of 1. Therefore, based on the frequencies in the table, the 36th and 37th values in the new data set are both 17. It follows that the median of the new data set is 17, which is the same as the median of the original data set. Therefore, the mean of the new data set is greater than the mean of the original data set, and the medians of the two data sets are equal. Choice A is incorrect and may result from conceptual or calculation errors. Choice C is incorrect and may result from conceptual or calculation errors. Choice D is incorrect and may result from conceptual or calculation errors."
},
{
  "id": 5,
  "type": "multiple-choice",
  "question": "",
  "choices": [
  "A) 83",
  "B) 152",
  "C) 235",
  "D) 495"
],
  "image": "/static/March2025_Images/ProblemSolvingAndDataAnalysis/OneVariableDataDistributionsCenterSpread/12267_5.png",
  "difficulty": "easy",
  "active": "no",
  "marked": False,
  "answer": "C) 235",
  "explanation": "Choice C is correct. The table shows that for a certain region in 2016, the average number of store employees in warehouse stores was 365 and the average number of store employees in supermarkets was 130. Subtracting 130 from 365 yields 365-130, or 235. Therefore, the average number of store employees was 235 greater in warehouse stores than in supermarkets. Choice A is incorrect. For this region in 2016, this is how much greater the average number of store employees was in department stores than in supermarkets. Choice B is incorrect. For this region in 2016, this is how much greater the average number of store employees was in warehouse stores than in department stores. Choice D is incorrect. For this region in 2016, this is the sum of the average number of store employees in warehouse stores and in supermarkets."
}
]

two_variable_data_models_scatterplots = [
  {
  "id": 1,
  "type": "free-response",
  "question": "",
  "choices": [],
  "image": "/static/March2025_Images/ProblemSolvingAndDataAnalysis/TwoVariableDataModelsScatterplots/12261_1.png",
  "difficulty": "medium",
  "active": "no",
  "marked": False,
  "answer": "",
  "explanation": "The correct answer is 5. For the graph shown, x represents time, in minutes, and y represents temperature, in degrees Celsius (°C). Therefore, the average rate of change, in °C per minute, of the recorded temperature of the air in the chamber between two x-values is the difference in the corresponding y-values divided by the difference in the x-values. The graph shows that at x = 5, the corresponding y-value is 14. The graph also shows that at x = 7, the corresponding y-value is 24. It follows that the average rate of change, in °C per minute, from x = 5 to x = 7 is equivalent to 10/2 or 5. 24-14/7-5 which is equivalent to 10/2, or 5."
},
{"id": 2,
  "type": "multiple-choice",
  "question": "",
  "choices": [
  "A) y = x + 3.4",
  "B) y = x - 3.4",
  "C) y = -x + 3.4",
  "D) y = -x - 3.4"
],
  "image": "/static/March2025_Images/ProblemSolvingAndDataAnalysis/TwoVariableDataModelsScatterplots/12269_2.png",
  "difficulty": "easy",
  "active": "no",
  "marked": False,
  "answer": "A) y = x + 3.4",
  "explanation": "Choice A is correct. The line of best fit shown has a positive slope and intersects the y-axis at a positive y-value. The graph of an equation of the form y = mx + b, where m and b are constants, has a slope of m and intersects the y-axis at a y-value of b. Of the given choices, only y = x + 3.4 represents a line that has a positive slope, 1, and intersects the y-axis at a positive y-value, 3.4. Choice B is incorrect. This equation represents a line that intersects the y-axis at a negative y-value, not a positive y-value. Choice C is incorrect. This equation represents a line that has a negative slope, not a positive slope. Choice D is incorrect. This equation represents a line that has a negative slope, not a positive slope, and intersects the y-axis at a negative y-value, not a positive y-value."
},
{"id": 3,
  "type": "multiple-choice",
  "question": "",
  "choices": [
  "A) 0",
  "B) ½",
  "C) 1",
  "D) 2"
],
  "image": "/static/March2025_Images/ProblemSolvingAndDataAnalysis/TwoVariableDataModelsScatterplots/12270_3.png",
  "difficulty": "medium",
  "active": "no",
  "marked": False,
  "answer": "D) 2",
  "explanation": "Choice D is correct. A line in the xy-plane that passes through the points (x1, y1) and (x2, y2) has a slope of (y2-y1)/(x2-x1). The line of best fit shown passes approximately through the points (1,3.3) and (7, 14.5). It follows that the slope of this best fit line is approximately (14.5-3.3)/(7-1), which is equivalent to 11.2/6, or approximately 1.87. Therefore, of the given choices, 2 is closest to the slope of the line of best fit shown. Choice A is incorrect and may result from conceptual or calculation errors. Choice B is incorrect and may result from conceptual or calculation errors. Choice C is incorrect and may result from conceptual or calculation errors."
},
{"id": 4,
  "type": "multiple-choice",
  "question": "",
  "choices": [
  "A) 47",
  "B) 35",
  "C) 25",
  "D) 0"
],
  "image": "/static/March2025_Images/ProblemSolvingAndDataAnalysis/TwoVariableDataModelsScatterplots/12280_4.png",
  "difficulty": "easy",
  "active": "no",
  "marked": False,
  "answer": "B) 35",
  "explanation": "Choice B is correct. In the given scatterplot, the x-values represent the distance above sea level, in feet, and the y-values represent the temperature, in °F. The point on the line of best fit with an x-value of 4,000 has a corresponding y-value of 35. Therefore, at a distance of 4,000 feet above sea level, the temperature predicted by the line of best fit is 35°F. Choice A is incorrect. This is the temperature, in °F, predicted by the line of best fit at a distance of 0 feet above sea level. Choice C is incorrect. This is the measured temperature, in °F, at a distance of 6,000 feet above sea level. Choice D is incorrect and may result from conceptual or calculation errors."
},
{"id": 5,
  "type": "multiple-choice",
  "question": "",
  "choices": [
  "A) -3.3",
  "B) -1.1",
  "C) 1.1",
  "D) 3.3"
],
  "image": "/static/March2025_Images/ProblemSolvingAndDataAnalysis/TwoVariableDataModelsScatterplots/12281_5.png",
  "difficulty": "medium",
  "active": "no",
  "marked": False,
  "answer": "B) -1.1",
  "explanation": "Choice B is correct. A line in the xy-plane that passes through points (x1, y1) and (x2, y2) has a slope of (y2 - y1) / (x2 - x1). The line of best fit shown passes approximately through the points (0, 14) and (13, 0). It follows that the slope of this line of best fit is approximately (0 - 14) / (13 - 0) or -14/13. Of the given choices, -1.1 is closest to -14/13. Choice A is incorrect and may result from conceptual or calculation errors. Choice C is incorrect and may result from conceptual or calculation errors. Choice D is incorrect and may result from conceptual or calculation errors."
}
]

probability_conditional_probability = [
  {
  "id": 1,
  "type": "multiple-choice",
  "question": "",
  "choices": [
  "A) 28/135",
  "B) 35/135",
  "C) 100/135",
  "D) 107/135"
],
  "image": "/static/March2025_Images/ProblemSolvingAndDataAnalysis/ProbabilityConditionalProbability/12263_1.png",
  "difficulty": "easy",
  "active": "no",
  "marked": False,
  "answer": "D) 107/135",
  "explanation": "Choice D is correct. If a member of the organization is selected at random, the probability that the selected member is at least 40 years old is equal to the number of members who are at least 40 years old divided by the total number of members. According to the table, there are a total of 135 members of the organization, and 107 of these members are at least 40 years old. Therefore, the probability that the selected member is at least 40 years old is 107/135. Choice A is incorrect. This is the probability that the selected member is less than 40 years old. Choice B is incorrect. This is the probability that the selected member lives east of the river. Choice C is incorrect. This is the probability that the selected member lives west of the river."
},
{
  "id": 2,
  "type": "multiple-choice",
  "question": "",
  "choices": [
  "A) 0",
  "B) 1/3",
  "C) 2/3",
  "D) 1"
],
  "image": "/static/March2025_Images/ProblemSolvingAndDataAnalysis/ProbabilityConditionalProbability/12273_2.png",
  "difficulty": "easy",
  "active": "no",
  "marked": False,
  "answer": "B) 1/3",
  "explanation": "Choice B is correct. The probability of selecting a positive number is the number of positive numbers in the data set divided by the total number of numbers in the data set. There is 1 positive number in this data set. There are 3 total numbers in this data set. Thus, if a number from this data set is selected at random, the probability of selecting a positive number is 1/3. Choice A is incorrect and may result from conceptual or calculation errors. Choice C is incorrect. This is the probability of selecting a negative number from this data set. Choice D is incorrect and may result from conceptual or calculation errors."
}
]

inference_sample_statistics_margin_error = [
  {
  "id": 1,
  "type": "multiple-choice",
  "question": "",
  "choices": [
  "A) Plausible values for the average weight of all boxes of oranges filled by the company are between 22.91 pounds and 23.29 pounds.",
  "B) Plausible values for the average weight of all boxes of oranges filled by the company are less than 22.91 pounds or greater than 23.29 pounds.",
  "C) The average weight of all boxes of oranges filled by the company is less than 23.01 pounds.",
  "D) The average weight of all boxes of oranges filled by the company is greater than 23.01 pounds."
],
  "image": "/static/March2025_Images/ProblemSolvingAndDataAnalysis/InferenceSampleStatisticsMarginError/12266_1.png",
  "difficulty": "medium",
  "active": "no",
  "marked": False,
  "answer": "A) Plausible values for the average weight of all boxes of oranges filled by the company are between 22.91 pounds and 23.29 pounds.",
  "explanation": "Choice A is correct. It's given that the estimate for the average weight of all boxes of oranges filled by the company in an 8-hour period is 23.1 pounds, with an associated margin of error of 0.19 pounds. It follows that plausible values for this average weight are between 23.1 - 0.19 pounds and 23.1 + 0.19 pounds. Therefore, plausible values for the average weight of all boxes of oranges filled by the company are between 22.91 pounds and 23.29 pounds. Choice B is incorrect and may result from conceptual or calculation errors. Choice C is incorrect and may result from conceptual or calculation errors. Choice D is incorrect and may result from conceptual or calculation errors."
},
{
  "id": 2,
  "type": "multiple-choice",
  "question": "",
  "choices": [
  "A) It is between $4.15 and $4.31.",
  "B) It is either less than $4.15 or greater than $4.31.",
  "C) It is less than $4.15.",
  "D) It is greater than $4.31."
],
  "image": "/static/March2025_Images/ProblemSolvingAndDataAnalysis/InferenceSampleStatisticsMarginError/12279_2.png",
  "difficulty": "easy",
  "active": "no",
  "marked": False,
  "answer": "A) It is between $4.15 and $4.31.",
  "explanation": "Choice A is correct. It's given that the mean price of a carton of grape tomatoes in Utah was estimated to be $4.23, with an associated margin of error of $0.08. It follows that plausible values for this mean price are between $4.23 - $0.08 and $4.23 + $0.08. Therefore, it's plausible that the mean price of a carton of grape tomatoes for all locations that sell this product in Utah is between $4.15 and $4.31. Choice B is incorrect and may result from conceptual or calculation errors. Choice C is incorrect and may result from conceptual or calculation errors. Choice D is incorrect and may result from conceptual or calculation errors."
}
]

evaluating_statistical_claims_studies_experiments = []

area_volume = [
  {
  "id": 1,
  "type": "free-response",
  "question": "",
  "choices": [],
  "image": "/static/March2025_Images/GeometryAndTrigonometry/AreaVolume/12288_1.png",
  "difficulty": "medium",
  "active": "no",
  "marked": False,
  "answer": "1,260",
  "explanation": "The correct answer is 1,260. Since it's given that prisms X and Y are similar, all the linear measurements of prism Y are k times the respective linear measurements of prism X, where k is a positive constant. Therefore, the surface area of prism Y is k^2 times the surface area of prism X and the volume of prism Y is k^3 times the volume of prism X. It's given that the surface area of prism Y is 1,450 cm^2, and the surface area of prism X is 58 cm^2, which implies that 1,450 = 58k^2. Dividing 1,450 both sides of this equation by 58 yields 1,450/58 = k^2, or k^2 = 25. Since k is a positive constant, k = 5. It's given that the volume of prism Y is 1,250 cm^3. Therefore, the volume of prism X is equal to 1,250/k^3 cm^3, which is equivalent to 1,250/5^3 cm^3, or 10 cm^3. Thus, the sum of the volumes, in cm^3, of the two prisms is 1,250 + 10, or 1,260."
},
{
"id": 2,
  "type": "multiple-choice",
  "question": "",
  "choices": [
  "A) 6",
  "B) 10",
  "C) 60",
  "D) 150"
],
  "image": "/static/March2025_Images/GeometryAndTrigonometry/AreaVolume/12290_2.png",
  "difficulty": "easy",
  "active": "no",
  "marked": False,
  "answer": "A) 6",
  "explanation": "Choice A is correct. It's given that the length of each side of a scale model is 1/10 times the length of the corresponding side of the actual floor of a ballroom. Therefore, the area of the scale model is (1/10)^2, or 1/100 times the area of the actual floor of the ballroom. It's given that the area of the floor of the ballroom is 600 square meters. Therefore, the area, in square meters, of the scale model is (1/100)(600), or 6. Choice B is incorrect and may result from conceptual or calculation errors. Choice C is incorrect and may result from conceptual or calculation errors. Choice D is incorrect and may result from conceptual or calculation errors."
},
{
  "id": 3,
  "type": "multiple-choice",
  "question": "",
  "choices": [
  "A) 14π",
  "B) 28π",
  "C) 56π",
  "D) 116π"
],
  "image": "/static/March2025_Images/GeometryAndTrigonometry/AreaVolume/12291_3.png",
  "difficulty": "easy",
  "active": "no",
  "marked": False,
  "answer": "D) 116π",
  "explanation": "Choice D is correct. The area, A, of a circle is given by the formula A = πr², where r represents the radius of the circle. It's given that circle K has a radius of 4 millimeters (mm). Substituting 4 for r in the formula A = πr² yields A = π(4)², or A = = 16. Therefore, the area of circle K is 16π mm². It's given that circle L has an area of 100π mm². Therefore, the total area, in mm², of circles K and L is 16π + 100π, or 116π. Choice A is incorrect. This is the sum of the radii, in mm, of circles K and L multiplied by π, not the m², of the circles. 2 total area, in mm², Choice B is incorrect. This is the sum of the diameters, in mm, of circles K and L multiplied by π, not the total area, in mm², of the circles. Choice C is incorrect and may result from conceptual or calculation errors."
},
{
  "id": 4,
  "type": "multiple-choice",
  "question": "",
  "choices": [
  "A) 92",
  "B) 84",
  "C) 80",
  "D) 52"
],
  "image": "/static/March2025_Images/GeometryAndTrigonometry/AreaVolume/12293_4.png",
  "difficulty": "easy",
  "active": "no",
  "marked": False,
  "answer": "D) 52",
  "explanation": "Choice D is correct. It's given that rectangle P has an area of 72 square inches. If a rectangle with an area of 20 square inches is removed from rectangle P, the area, in square inches, of the resulting figure is 72 - 20, or 52. Choice A is incorrect and may result from conceptual or calculation errors. Choice B is incorrect and may result from conceptual or calculation errors. Choice C is incorrect and may result from conceptual or calculation errors."
},
{
  "id": 5,
  "type": "multiple-choice",
  "question": "",
  "choices": [
  "A) 2",
  "B) 8",
  "C) 10",
  "D) 24"
],
  "image": "/static/March2025_Images/GeometryAndTrigonometry/AreaVolume/12296_5.png",
  "difficulty": "easy",
  "active": "no",
  "marked": False,
  "answer": "B) 8",
  "explanation": "Choice B is correct. The perimeter of a triangle is the sum of the lengths of all three of its sides. It's given that the lengths of two sides of a triangle are 4 centimeters and 6 centimeters. Let z represent the length, in centimeters, of the third side of this triangle. The sum of the lengths, in centimeters, of all three sides of the triangle can be represented by the expression 4+6+z. Since it's given that the perimeter of the triangle is 18 centimeters, it follows that 4+6+z=18, or 10 + z = 18. Subtracting 10 from both sides of this equation yields z = 8. Therefore, the length, in centimeters, of the third side of this triangle is 8. Choice A is incorrect. If the length of the third side of this triangle were 2 centimeters, the perimeter, in centimeters, of the triangle would be 4+6+2, or 12, not 18. Choice C is incorrect. If the length of the third side of this triangle were 10 centimeters, the perimeter, in centimeters, of the triangle would be 4+6+10, or 20, not 18. Choice D is incorrect. If the length of the third side of this triangle were 24 centimeters, the perimeter, in centimeters, of the triangle would be 4+6+24, or 34, not 18."
},
{
  "id": 6,
  "type": "free-response",
  "question": "",
  "choices": [],
  "image": "/static/March2025_Images/GeometryAndTrigonometry/AreaVolume/12297_6.png",
  "difficulty": "medium",
  "active": "no",
  "marked": False,
  "answer": "4.41",
  "explanation": "The correct answer is 4.41. The area, A, of a circle is given by the formula A = πr², where r is the radius of the circle. It's given that the area of the circle is bπ square inches, where b is a constant, and the radius of the circle is 2.1 inches. Substituting bπ for A and 2.1 for r in the formula A = πr² yields bπ = π(2.1²). Dividing both sides of this equation by π yields b = 4.41. Therefore, the value of b is 4.41."
},
{
  "id": 7,
  "type": "multiple-choice",
  "question": "",
  "choices": [
  "A) 12",
  "B) 36",
  "C) 77",
  "D) 85"
],
  "image": "/static/March2025_Images/GeometryAndTrigonometry/AreaVolume/12300_7.png",
  "difficulty": "easy",
  "active": "no",
  "marked": False,
  "answer": "D) 85",
  "explanation": "Choice D is correct. The volume, V, of a right circular cone is given by the formula V = (1/3)πr²h, where πr² is the area of the circular base of the cone and h is the height. It’s given that this right circular cone has a volume of 71,148 cubic centimeters and the area of its base is 5,929π square centimeters. Substituting 71,148π for V and 5,929π for πr² in the formula V = (1/3)πr²h yields 71,148π = (1/3)(5,929π)(h). Dividing each side of this equation by 5,929π yields 12 = (1/3)h. Multiplying each side of this equation by 3 yields 36 = h. Let s represent the slant height, in centimeters, of this cone. A right triangle is formed by the radius, r, height, h, and slant height, s, of this cone, where r and h are the legs of the triangle and s is the hypotenuse. Using the Pythagorean theorem, the equation r² + h² = s² represents this relationship. Because 5,929π is the area of the base and the area of the base is πr², it follows that 5,929π = πr². Dividing both sides of this equation by π yields 5,929 = r². Substituting 5,929 for r² and 36 for h in the equation r² + h² = s² yields 5,929 + 36² = s², which is equivalent to 5,929 + 1,296 = s², or 7,225 = s². Taking the positive square root of both sides of this equation yields 85 = s. Therefore, the slant height of the cone is 85 centimeters. Choice A is incorrect. This is one-third of the height, in centimeters, not the slant height, in centimeters, of this cone. Choice B is incorrect. This is the height, in centimeters, not the slant height, in centimeters, of this cone. Choice C is incorrect. This is the radius, in centimeters, of the base, not the slant height, in centimeters, of this cone."
}
]

lines_angles_triangles = [
{
  "id": 1,
  "type": "multiple-choice",
  "question": "",
  "choices": [
  "A) 20°",
  "B) 45°",
  "C) 135°",
  "D) 160°"
],
  "image": "/static/March2025_Images/GeometryAndTrigonometry/LinesAnglesTriangles/12282_1.png",
  "difficulty": "easy",
  "active": "no",
  "marked": False,
  "answer": "B) 45°",
  "explanation": "Choice B is correct. It's given that triangles EFG and JKL are congruent such that angle E corresponds to angle J. Corresponding angles of congruent triangles are congruent, so angle E and angle J must be congruent. Therefore, if the measure of angle E is 45°, then the measure of angle J is also 45°. Choice A is incorrect. This is the measure of angle K, not angle J. Choice C is incorrect and may result from conceptual or calculation errors. Choice D is incorrect and may result from conceptual or calculation errors."
},
{
  "id": 2,
  "type": "multiple-choice",
  "question": "",
  "choices": [
  "A) 204",
  "B) 182",
  "C) 60",
  "D) 12"
],
  "image": "/static/March2025_Images/GeometryAndTrigonometry/LinesAnglesTriangles/12285_2.png",
  "difficulty": "easy",
  "active": "no",
  "marked": False,
  "answer": "D) 12",
  "explanation": "Choice D is correct. It's given that triangle ABC is similar to triangle XYZ, where A, B, and C correspond to X, Y, and Z, respectively. It follows that side AB corresponds to side XY and side BC corresponds to side YZ. Since the lengths of corresponding sides in similar triangles are proportional, it follows that XY/AB = YZ/BC. Substituting 170 for AB, 60 for YZ, and 850 for BC in this equation yields XY/170 = 60/850. Multiplying each side of this equation by 170 yields XY = 12. Therefore, the length of XY is 12. Choice A is incorrect and may result from conceptual or calculation errors. Choice B is incorrect and may result from conceptual or calculation errors. Choice C is incorrect. This is the length of YZ, not XY."
},
{
  "id": 3,
  "type": "multiple-choice",
  "question": "",
  "choices": [
  "A) 29/28",
  "B) 1",
  "C) 28/29",
  "D) 0"
],
  "image": "/static/March2025_Images/GeometryAndTrigonometry/LinesAnglesTriangles/12289_3.png",
  "difficulty": "easy",
  "active": "no",
  "marked": False,
  "answer": "A) 29/28",
  "explanation": "Choice A is correct. It's given that each side of equilateral triangle S is multiplied by a scale factor of k to create equilateral triangle T. Since the length of each side of triangle T is greater than the length of each side of triangle S, the scale factor of k must be greater than 1. Of the given choices, only 29/28 is greater than 1. Choice B is incorrect. If each side of equilateral triangle S is multiplied by a scale factor of 1, the length of each side of triangle T would be equal to the length of each side of triangle S. Choice C is incorrect. If each side of equilateral triangle S is multiplied by a scale factor of 28/29, the length of each side of triangle T would be less than the length of each side of triangle S. Choice D is incorrect and may result from conceptual or calculation errors."
},
{
  "id": 4,
  "type": "free-response",
  "question": "",
  "choices": [],
  "image": "/static/March2025_Images/GeometryAndTrigonometry/LinesAnglesTriangles/12298_4.png",
  "difficulty": "medium",
  "active": "no",
  "marked": False,
  "answer": "153",
  "explanation": "The correct answer is 153. Since it's given that PQ is parallel to XY and angle Y is a right angle, angle ZQP is also a right angle. Angle ZPQ is complementary to angle XZY, which means its measure, in degrees, is 90 – 63, or 27. Since angle XPQ is supplementary to angle ZPQ, its measure, in degrees, is 180 – 27, or 153."
},
{
  "id": 5,
  "type": "multiple-choice",
  "question": "",
  "choices": [
  "A) (90 - (t - k))°",
  "B) (90 - (t + k))°",
  "C) (90 - t)°",
  "D) (90 + k)°"
],
  "image": "/static/March2025_Images/GeometryAndTrigonometry/LinesAnglesTriangles/12299_5.png",
  "difficulty": "easy",
  "active": "no",
  "marked": False,
  "answer": "C) (90 - t)°",
  "explanation": "Choice C is correct. Since P=(4, 5) and Q =(4, 7), side PQ is parallel to the y-axis and has a length of 2. Since P=(4,5) and R=(6, 5), side PR is parallel to the x-axis and has a length of 2. Therefore, triangle PQR is a right isosceles triangle, where ∠P has measure 90° and ∠Q and ∠R each have measure 45°. It follows that if the measure of ∠Q is t°, then t = 45. Since L =(4,5) and M=(4,7+k), side LM is parallel to the y-axis and has a length of k + 2. Since L =(4,5) and N=(6+k, 5), side LN is parallel to the x-axis and has a length of k + 2. Therefore, triangle LMN is a right isosceles triangle, where ∠L has measure 90° and ∠M and ∠N each have measure 45°. Of the given choices, only (90-t)° is equal to 45°, so the measure of ∠N is (90-t)°. Choice A is incorrect and may result from conceptual or calculation errors. Choice B is incorrect and may result from conceptual or calculation errors. Choice D is incorrect and may result from conceptual or calculation errors."
},
{
  "id": 6,
  "type": "free-response",
  "question": "",
  "choices": [],
  "image": "/static/March2025_Images/GeometryAndTrigonometry/LinesAnglesTriangles/12302_6.png",
  "difficulty": "medium",
  "active": "no",
  "marked": False,
  "answer": "162",
  "explanation": "The correct answer is 162. It's given that line r is parallel to line s. Since line n intersects both lines r and s, it's a transversal. The angles in the figure marked as 162° and x° are on the same side of the transversal, where one is an interior angle with line s as a side, and the other is an exterior angle with line r as a side. Thus, the marked angles are corresponding angles. When two parallel lines are intersected by a transversal, corresponding angles are congruent and, therefore, have equal measure. It follows that the value of x is 162."
},
{
  "id": 7,
  "type": "multiple-choice",
  "question": "",
  "choices": [
  "A) 36",
  "B) 45",
  "C) 72",
  "D) 108"
],
  "image": "/static/March2025_Images/GeometryAndTrigonometry/LinesAnglesTriangles/12303_7.png",
  "difficulty": "easy",
  "active": "no",
  "marked": False,
  "answer": "C) 72",
  "explanation": "Choice C is correct. The sum of the interior angles of a triangle is 180°. It's given that the interior angles of triangle ABC are 54°, 90°, and (k/2)°. It follows that 54 + 90 + k/2 = 180, or 144 + k/2 = 180. Subtracting 144 from each side of this equation yields k/2 = 36. Multiplying each side of this equation by 2 yields k = 72. Therefore, the value of k is 72. Choice A is incorrect. This is the value of k/2, not k. Choice B is incorrect and may result from conceptual or calculation errors. Choice D is incorrect and may result from conceptual or calculation errors."
},
{
  "id": 8,
  "type": "free-response",
  "question": "",
  "choices": [
  "A) 52",
  "B) 90",
  "C) 142",
  "D) 180"
],
  "image": "/static/March2025_Images/GeometryAndTrigonometry/LinesAnglesTriangles/12304_8.png",
  "difficulty": "medium",
  "active": "no",
  "marked": False,
  "answer": "1,660",
  "explanation": "The correct answer is 1,660. It's given that a line intersects two parallel lines, forming four acute angles and four obtuse angles. When two parallel lines are intersected by a transversal line, the angles formed have the following properties: two adjacent angles are supplementary, and alternate interior angles are congruent. Therefore, each of the four acute angles have the same measure, and each of the four obtuse angles have the same measure. It's also given that the measure of one of the acute angles is (9x-560)°. If two angles are supplementary, then the sum of their measures is 180°. Therefore, the measure of the obtuse angle adjacent to any of the acute angles is (180-(9x-560))°, or (180-9x+560)°, which is equivalent to (-9x+740)°. It's given that the sum of the measures of one of the acute angles and three of the obtuse angles is (-18x + w)°. It follows that (9x-560)+3(-9x+740)=(-18x + w), which is equivalent to 9x-560-27x+2,220=-18x+w, or -18x+1,660=-18x+w. Adding 18x to both sides of this equation yields 1,660 = w."
},
{
  "id": 9,
  "type": "multiple-choice",
  "question": "",
  "choices": [
  "A) 52",
  "B) 90",
  "C) 142",
  "D) 180"
  ],
  "image": "/static/March2025_Images/GeometryAndTrigonometry/LinesAnglesTriangles/12306_9.png",
  "difficulty": "easy",
  "active": "no",
  "marked": False,
  "answer": "D) 180",
  "explanation": "Choice D is correct. In the figure shown, the angle marked x° and the angle marked 142° form a linear pair of angles. If two angles form a linear pair of angles, the sum of the measures of the angles is 180°. Therefore, the value of x + 142 is 180. Choice A is incorrect. This is 90 less than 142, not the sum of x and 142. Choice B is incorrect and may result from conceptual or calculation errors. Choice C is incorrect. This is the measure, in degrees, of one of the angles shown."
}
]

right_triangles_trigonometry = [
{
  "id": 1,
  "type": "multiple-choice",
  "question": "",
  "choices": [
  "A) 188",
  "B) 168",
  "C) 84",
  "D) 71"
],
  "image": "/static/March2025_Images/GeometryAndTrigonometry/RightTrianglesTrigonometry/12283_1.png",
  "difficulty": "easy",
  "active": "no",
  "marked": False,
  "answer": "B) 168",
  "explanation": "Choice B is correct. It's given that angle Z in triangle XYZ is a right angle. Thus, side YZ is the leg opposite angle X and side XZ is the leg adjacent to angle X. The tangent of an acute angle in a right triangle is the ratio of the length of the leg opposite the angle to the length of the leg adjacent to the angle. It follows that tan X = YZ/XZ. It's given that tan X = 12/35 and the length of side YZ is 24 units. Substituting 12/35 for tan X and 24 for YZ in the equation tan X = YZ/XZ yields 12/35 = 24/XZ. Multiplying both sides of this equation by 35(XZ) yields 12(XZ) = 24(35), or 12(XZ) = 840. Dividing both sides of this equation by 12 yields XZ = 70. The length XY can be calculated using the Pythagorean theorem, which states that if a right triangle has legs with lengths of a and b and a hypotenuse with length c, then a² + b² = c². Substituting 70 for a and 24 for b in this equation yields 70² + 24² = c², or 5,476 = c². Taking the square root of both sides of this equation yields ±74 = c. Since the length of the hypotenuse must be positive, 74 = c. Therefore, the length of XY is 74 units. The perimeter of a triangle is the sum of the lengths of all sides. Thus, (74 + 70 + 24) units, or 168 units, is the perimeter of triangle XYZ. Choice A is incorrect and may result from conceptual or calculation errors. Choice C is incorrect. This would be the perimeter, in units, for a right triangle where the length of side YZ is 12 units, not 24 units. Choice D is incorrect and may result from conceptual or calculation errors."
},
{
  "id": 2,
  "type": "free-response",
  "question": "",
  "choices": [],
  "image": "/static/March2025_Images/GeometryAndTrigonometry/RightTrianglesTrigonometry/12286_2.png",
  "difficulty": "medium",
  "active": "no",
  "marked": False,
  "answer": "338",
  "explanation": "The correct answer is 338. The tangent of an acute angle in a right triangle is the ratio of the length of the leg opposite the angle to the length of the leg adjacent to the angle. In triangle XYZ, it's given that angle Y is a right angle. Thus, XY is the leg opposite of angle Z and YZ is the leg adjacent to angle Z. It follows that tan Z = XY/YZ. It's also given that the measure of angle Z is 33° and the length of YZ is 26 units. Substituting 33° for Z and 26 for YZ in the equation tan Z = XY/YZ yields tan 33° = XY/26. Multiplying each side of this equation by 26 yields 26 tan 33° = XY. Therefore, the length of XY is 26 tan 33°. The area of a triangle is half the product of the lengths of its legs. Since the length of YZ is 26 and the length of XY is 26 tan 33°, it follows that the area of triangle XYZ is (1/2)(26)(26 tan 33°) square units, or 338 tan 33° square units. It's given that the area, in square units, of triangle XYZ can be represented by the expression k tan 33°, where k is a constant. Therefore, 338 is the value of k."
},
{
  "id": 3,
  "type": "multiple-choice",
  "question": "",
  "choices": [
  "A) 1 / 171",
  "B) 35 / 171",
  "C) 171 / 35",
  "D) 171"
],
  "image": "/static/March2025_Images/GeometryAndTrigonometry/RightTrianglesTrigonometry/12287_3.png",
  "difficulty": "easy",
  "active": "no",
  "marked": False,
  "answer": "B) 35 / 171",
  "explanation": "Choice B is correct. The sine of an acute angle in a right triangle is the ratio of the length of the side opposite that angle to the length of the hypotenuse. The hypotenuse of a right triangle is the side opposite the right angle. In right triangle ABC, side BC is the side opposite angle A and side AB is the hypotenuse. It's given that the length of side BC is 35 units and the length of side AB is 171 units. Therefore, the value of sin A is 35/171. Choice A is incorrect and may result from conceptual or calculation errors. Choice C is incorrect. This is the ratio of the length of the hypotenuse to the length of the side opposite angle A rather than the ratio of the length of the side opposite angle A to the length of the hypotenuse. Choice D is incorrect. This is the length of the hypotenuse rather than sin A."
},
{
  "id": 4,
  "type": "multiple-choice",
  "question": "",
  "choices": [
  "A) 43.2",
  "B) 120",
  "C) 192",
  "D) 201.5"
],
  "image": "/static/March2025_Images/GeometryAndTrigonometry/RightTrianglesTrigonometry/12294_4.png",
  "difficulty": "easy",
  "active": "no",
  "marked": False,
  "answer": "C) 192",
  "explanation": "Choice C is correct. The Pythagorean theorem states that for a right triangle, the sum of the squares of the lengths of the two legs is equal to the square of the length of the hypotenuse. It's given that one leg of a right triangle has a length of 43.2 millimeters. It's also given that the hypotenuse of the triangle has a length of 196.8 millimeters. Let b represent the length of the other leg of the triangle, in millimeters. Therefore, by the Pythagorean theorem, 43.2^2 + b^2 = 196.8^2, or 1,866.24 + b^2 = 38,730.24. Subtracting 1,866.24 from both sides of this equation yields b^2 = 36,864. Taking the positive square root of both sides of this equation yields b = 192. Therefore, the length of the other leg of the triangle, in millimeters, is 192. Choice A is incorrect and may result from conceptual or calculation errors. Choice B is incorrect and may result from conceptual or calculation errors. Choice D is incorrect and may result from conceptual or calculation errors."
},
{
  "id": 5,
  "type": "free-response",
  "question": "",
  "choices": [],
  "image": "/static/March2025_Images/GeometryAndTrigonometry/RightTrianglesTrigonometry/12295_5.png",
  "difficulty": "medium",
  "active": "no",
  "marked": False,
  "answer": "284/3",
  "explanation": "The correct answer is 284/3. Since the perimeter of a triangle is the sum of the lengths of its sides, and the given triangle is equilateral, the length of each side is 852/3, or 284, centimeters (cm). Right triangle AMO can be formed, where M is the midpoint of one of the triangle's sides, A is one of this side's endpoints, and O is the center of the circle. It follows that AM is 284/2, or 142, cm. Additionally, triangle AMO has angles measuring 30°, 60°, and 90°, where the measure of angle OMA is 90° and the measure of angle OAM is 30°. It follows that the length of side MO is half the length of hypotenuse AO, and the length of side AM is sqrt(3) times the length of side MO. It's given that AO = wsqrt(3) cm. Therefore, MO = wsqrt(3)/2 cm and AM = 3w*sqrt(3)/2 cm, which is equivalent to AM = 3w/2 cm. Since AM = 142 cm, it follows that 3w/2 = 142. Multiplying both sides of this equation by 2 yields 3w = 284. Dividing both sides of this equation by 3 yields w = 284/3. Note that 284/3, 94.66, and 94.67 are examples of ways to enter a correct answer."
},
{
  "id": 6,
  "type": "multiple-choice",
  "question": "",
  "choices": [
  "A) 2(cos 66°)(sin 24°)",
  "B) 2(cos 66°) + 2(cos 24°)",
  "C) (cos 66°)^2 + (cos 24°)^2",
  "D) (cos 66°)^2 + (sin 24°)^2"
],
  "image": "/static/March2025_Images/GeometryAndTrigonometry/RightTrianglesTrigonometry/12301_6.png",
  "difficulty": "easy",
  "active": "no",
  "marked": False,
  "answer": "C) (cos 66°)^2 + (cos 24°)^2",
  "explanation": "Choice C is correct. The sine of an angle is equal to the cosine of its complementary angle. Since angles with measures 24° and 66° are complementary to each other, sin 24° is equal to cos 66° and sin 66° is equal to cos 24°. Substituting cos 66° for sin 24° and cos 24° for sin 66° in the given expression yields (cos 66°)(cos 66°)+(cos 24°)(cos 24°), or (cos 66°)² + (cos 24°)². Choice A is incorrect and may result from conceptual or calculation errors. Choice B is incorrect and may result from conceptual or calculation errors. Choice D is incorrect and may result from conceptual or calculation errors."
}
]

circles = [
  {
"id": 1,
  "type": "multiple-choice",
  "question": "",
  "choices": [
  "A) 13√2",
  "B) 13",
  "C) 9√2",
  "D) 9"
],
  "image": "/static/March2025_Images/GeometryAndTrigonometry/circles/12284_1.png",
  "difficulty": "easy",
  "active": "no",
  "marked": False,
  "answer": "B) 13",
  "explanation": "Choice B is correct. Since it's given that P is the center of a circle with a radius of 9 inches, and that points Q and R lie on that circle, it follows that PQ and RP of triangle PQR each have a length of 9 inches. Let the length of QR be x inches. It follows that the perimeter of triangle PQR is 9 + 9 + x inches. Since it's given that the perimeter of triangle PQR is 31 inches, it follows that 9 + 9 + x = 31, or 18 + x = 31. Subtracting 18 from both sides of this equation gives x = 13. Therefore, the length, in inches, of QR is 13. Choice A is incorrect and may result from conceptual or calculation errors. Choice C is incorrect and may result from conceptual or calculation errors. Choice D is incorrect and may result from conceptual or calculation errors."
},
{
  "id": 2,
  "type": "multiple-choice",
  "question": "",
  "choices": [
  "A) Center: (13, k), Radius: 8",
  "B) Center: (k, 13), Radius: 8",
  "C) Center: (k, 13), Radius: 64",
  "D) Center: (13, k), Radius: 64"
],
  "image": "/static/March2025_Images/GeometryAndTrigonometry/circles/12292_2.png",
  "difficulty": "easy",
  "active": "no",
  "marked": False,
  "answer": "A) Center: (13, k), Radius: 8",
  "explanation": "Choice A is correct. For a circle in the xy-plane that has the equation (x-h)^2+(y-k)^2 = r^2, where h, k, and r are constants, (h, k) is the center of the circle and the positive value of r is the radius of the circle. In the given equation, h = 13 and r^2 = 64. Taking the square root of each side of r^2 = 64 yields r = +-8. Therefore, the center of the circle is at (13, k) and the radius is 8. Choice B is incorrect. This gives the center and radius of a circle with equation (x-k)^2+(y-13)^2 = 64, not (x-13)^2 + (y - k)^2 = 64. Choice C is incorrect. This gives the center and radius of a circle with equation (x-k)^2+(y-13)^2 = 4,096, not (x-13)^2 + (y -k)^2 = 64. Choice D is incorrect. This gives the center and radius of a circle with equation (x-13)^2+(y-k)^2 = 4,096, not (x-13)^2 + (y - k)^2 = 64."
},
{
  "id": 3,
  "type": "multiple-choice",
  "question": "",
  "choices": [
  "A) √109",
  "B) √149",
  "C) √167",
  "D) √341"
],
  "image": "/static/March2025_Images/GeometryAndTrigonometry/circles/12305_3.png",
  "difficulty": "easy",
  "active": "no",
  "marked": False,
  "answer": "C) √167",
  "explanation": "Choice C is correct. It's given that in the xy-plane, the graph of the given equation is a circle. The equation of a circle in the xy-plane can be written in the form (x-h)²+(y-k)² = r², where (h, k) is the center of the circle and r is the length of the circle's radius. Subtracting 6y from both sides of the equation x² + 14x + y² = 6y + 109 yields x² + 14x + y² - 6y = 109. By completing the square, this equation can be rewritten as (x²+14x+(14/2)²) + (y²-6y+(-6/2)²) = 109 + (14/2)² + (-6/2)². This equation can be rewritten as (x² + 14x + 49) + (y² - 6y + 9) = 109 + 49 + 9, or (x + 7)² + (y - 3)² = 167. Therefore, r² = 167. Taking the square root of both sides of this equation yields r = √167 and r = -√167. Since r is the length of the circle's radius, r must be positive. Therefore, the length of the circle's radius is √167. Choice A is incorrect and may result from conceptual or calculation errors. Choice B is incorrect and may result from conceptual or calculation errors. Choice D is incorrect and may result from conceptual or calculation errors"
},
{
  "id": 4,
  "type": "multiple-choice",
  "question": "",
  "choices": [
  "A) 0",
  "B) 1/2",
  "C) √2 / 2",
  "D) 1"
],
  "image": "/static/March2025_Images/GeometryAndTrigonometry/circles/12307_4.png",
  "difficulty": "easy",
  "active": "no",
  "marked": False,
  "answer": "A) 0",
  "explanation": "Choice A is correct. The sine of a number t is the y-coordinate of the point arrived at by traveling a distance of t units counterclockwise around the unit circle from the starting point (1, 0). Since the unit circle has a circumference of 2π units, it follows that one full rotation around the circle is equal to a distance of 2π units. Therefore, a distance of 42π units around the circle from the starting point (1,0) would result in exactly 21 full rotations, arriving back at the point (1, 0). So, sin 42π is equal to the y-coordinate of the point (1, 0), which is 0. Choice B is incorrect and may result from conceptual or calculation errors. Choice C is incorrect and may result from conceptual or calculation errors. Choice D is incorrect. This is the value of cos 42π, not sin 42π."
}
]

questions = {
    'linear-equations-one-variable': linear_eq_questions,
    'linear-functions': linear_functions_questions,
    'linear-equations-two-variables': linear_eq_two_questions,
    'systems-two-linear-equations-two-variables': system_linear_eq_questions,
    'linear-inequalities': linear_ineq_questions,
    'equivalent-expressions': equivalent_expressions,
    'nonlinear-equations-systems': nonlinear_equations_systems,
    'nonlinear-functions': nonlinear_functions,
    'ratio-rates-proportional-units': ratio_rates_proportional_units,
    'percentages': percentages,
    'one-variable-data-distributions-center-spread': one_variable_data_distributions_center_spread,
    'two-variable-data-models-scatterplots': two_variable_data_models_scatterplots,
    'probability-conditional-probability': probability_conditional_probability,
    'inference-sample-statistics-margin-error': inference_sample_statistics_margin_error,
    'evaluating-statistical-claims-studies-experiments': evaluating_statistical_claims_studies_experiments,
    'area-volume': area_volume,
    'lines-angles-triangles': lines_angles_triangles,
    'right-triangles-trigonometry': right_triangles_trigonometry,
    'circles': circles
}

@app.route('/category/<main_slug>/<mini_slug>', methods=['GET', 'POST'])
def mini_category(main_slug, mini_slug):
	main_cat = next((c for c in categories if c['slug'] == main_slug), None)
	mini_cat = None
	if main_cat:
		mini_cat = next((m for m in main_cat.get('mini_categories', []) if m['slug'] == mini_slug), None)
	# Get selected difficulties from query or form
	if request.method == 'POST':
		selected_difficulties = request.form.getlist('difficulty')
		marked_filter = request.form.get('marked_filter', request.args.get('marked_filter', 'all'))
	else:
		selected_difficulties = request.args.getlist('difficulty')
		marked_filter = request.args.get('marked_filter', 'all')
	print('Selected difficulties:', selected_difficulties)
	# Get all questions for this mini-category
	mini_cat_questions = questions.get(mini_slug, [])
	# Only re-filter on GET requests (initial load or filter change)
	if request.method == 'GET':
		if selected_difficulties:
			qs = [q for q in mini_cat_questions if q.get('difficulty') in selected_difficulties]
		else:
			qs = mini_cat_questions
		if marked_filter == 'yes':
			qs = [q for q in qs if q.get('marked', False)]
		elif marked_filter == 'no':
			qs = [q for q in qs if not q.get('marked', False)]
		session[f'filtered_qs_{mini_slug}'] = [q.get('id') for q in qs]
	else:
		# On POST, use the last filtered set from session
		qs_ids = session.get(f'filtered_qs_{mini_slug}', [])
		qs = [q for q in mini_cat_questions if q.get('id') in qs_ids]
	print('Filtered questions:', qs)

	progress_key = f'progress_{mini_slug}'
	answers_key = f'answers_{mini_slug}'
	feedback_key = f'feedback_{mini_slug}'
	last_attempt_key = f'last_attempt_{mini_slug}'
	marked_key = f'marked_{mini_slug}'

	# Always use the full mini-category question list for session arrays
	all_questions = questions.get(mini_slug, [])
	if request.method == 'GET':
		reset_needed = (
			progress_key not in session or
			answers_key not in session or len(session[answers_key]) != len(all_questions) or
			feedback_key not in session or len(session[feedback_key]) != len(all_questions) or
			marked_key not in session or len(session[marked_key]) != len(all_questions)
		)
		if reset_needed:
			session[progress_key] = 0
			session[answers_key] = [None] * len(all_questions)
			session[feedback_key] = [None] * len(all_questions)
			session[marked_key] = [q.get('marked', False) for q in all_questions]
		# Only sync session marked status to global questions data for all questions in mini-category on GET
		marked_session = session.get(marked_key, [q.get('marked', False) for q in all_questions])
		for idx, real_q in enumerate(all_questions):
			if idx < len(marked_session):
				real_q['marked'] = marked_session[idx]
	# For filtered questions, use the correct indices from the full session arrays
	# Map filtered qs to their index in all_questions for marking, answers, etc.

	current_index = session.get(progress_key, 0)
	# Reset index if out of bounds for filtered questions
	if current_index >= len(qs):
		current_index = 0
		session[progress_key] = 0
	current_question = qs[current_index] if current_index < len(qs) else None
	answers = session.get(answers_key, [None] * len(qs))
	feedback = session.get(feedback_key, [None] * len(qs))
	last_attempt = session.get(last_attempt_key)
	# Map marked status for filtered questions from the full session marked array
	full_marked = session.get(marked_key, [q.get('marked', False) for q in all_questions])
	marked = []
	for q in qs:
		idx = next((i for i, real_q in enumerate(all_questions) if real_q.get('id') == q.get('id')), None)
		marked.append(full_marked[idx] if idx is not None else False)

	show_feedback = None

	if request.method == 'POST':
		action = request.form.get('action')
		answer = request.form.get('answer')
		# Preserve difficulty filter in redirect
		difficulties = request.form.getlist('difficulty')
		marked_filter_val = request.form.get('marked_filter', marked_filter)
		difficulty_query = '&'.join([f'difficulty={d}' for d in difficulties])
		if marked_filter_val:
			difficulty_query += f'&marked_filter={marked_filter_val}'
		if action == 'submit':
			# Save answer and feedback
			if answer is not None and answer != '':
				answers[current_index] = answer
				correct = (answer == current_question.get('answer'))
				feedback[current_index] = 'Correct!' if correct else f'Incorrect. Correct answer: {current_question.get("answer")}'
				session[answers_key] = answers
				session[feedback_key] = feedback
				show_feedback = feedback[current_index]
		elif action == 'next':
			# Move to next question without submitting
			if current_index < len(qs) - 1:
				session[progress_key] = current_index + 1
			else:
				session[progress_key] = current_index
		elif action == 'prev':
			if current_index > 0:
				session[progress_key] = current_index - 1
		elif action == 'toggle_marked':
			# Find the index of the current question in the full mini-category question list
			all_questions = questions.get(mini_slug, [])
			filtered_q = qs[current_index]
			real_index = next((i for i, q in enumerate(all_questions) if q.get('id') == filtered_q.get('id')), None)
			if real_index is not None:
				marked_session = session.get(marked_key, [q.get('marked', False) for q in all_questions])
				# Toggle only the intended question
				marked_session[real_index] = not marked_session[real_index]
				session[marked_key] = marked_session
				all_questions[real_index]['marked'] = marked_session[real_index]
		# After marking/unmarking, do NOT re-filter; just reload the same filtered set
		return redirect(url_for('mini_category', main_slug=main_slug, mini_slug=mini_slug) + ('?' + difficulty_query if difficulty_query else ''))

	finished = current_index >= len(qs)
	if current_index < len(feedback):
		show_feedback = feedback[current_index]

	return render_template(
		'mini_category.html',
		main_category=main_cat,
		mini_category=mini_cat,
		question=current_question,
		finished=finished,
		answers=answers,
		total=len(qs),
		current_index=current_index,
		show_feedback=show_feedback,
		last_attempt=last_attempt,
		marked=marked
	)





# SAT Math main categories with mini-categories
categories = [
	{
		'name': 'Algebra',
		'slug': 'algebra',
		'mini_categories': [
			{'name': 'Linear Equations in One Variable', 'slug': 'linear-equations-one-variable'},
			{'name': 'Linear Functions', 'slug': 'linear-functions'},
			{'name': 'Linear Equations in Two Variables', 'slug': 'linear-equations-two-variables'},
			{'name': 'Systems of Two Linear Equations in Two Variables', 'slug': 'systems-two-linear-equations-two-variables'},
			{'name': 'Linear Inequalities', 'slug': 'linear-inequalities'}
		]
	},
	{
		'name': 'Advanced Math',
		'slug': 'advanced-math',
		'mini_categories': [
			{'name': 'Equivalent Expressions', 'slug': 'equivalent-expressions'},
			{'name': 'Nonlinear Equations in One Variable and Systems of Equations in Two Variables', 'slug': 'nonlinear-equations-systems'},
			{'name': 'Nonlinear Functions', 'slug': 'nonlinear-functions'}
		]
	},
	{
		'name': 'Problem-Solving and Data Analysis',
		'slug': 'problem-solving-data-analysis',
		'mini_categories': [
			{'name': 'Ratio, Rates, Proportional Relationships, and Units', 'slug': 'ratio-rates-proportional-units'},
			{'name': 'Percentages', 'slug': 'percentages'},
			{'name': 'One-Variable Data: Distributions and Measures of Center and Spread', 'slug': 'one-variable-data-distributions-center-spread'},
			{'name': 'Two-Variable Data: Models and Scatterplots', 'slug': 'two-variable-data-models-scatterplots'},
			{'name': 'Probability and Conditional Probability', 'slug': 'probability-conditional-probability'},
			{'name': 'Inference from Sample Statistics and Margin of Error', 'slug': 'inference-sample-statistics-margin-error'},
			{'name': 'Evaluating Statistical Claims: Observational Studies and Experiments', 'slug': 'evaluating-statistical-claims-studies-experiments'}
		]
	},
	{
		'name': 'Geometry and Trigonometry',
		'slug': 'geometry-trigonometry',
		'mini_categories': [
			{'name': 'Area and Volume', 'slug': 'area-volume'},
			{'name': 'Lines, Angles, and Triangles', 'slug': 'lines-angles-triangles'},
			{'name': 'Right Triangles and Trigonometry', 'slug': 'right-triangles-trigonometry'},
			{'name': 'Circles', 'slug': 'circles'}
		]
	}
]

@app.route('/')
def home():
	# Get selected difficulties from form or query
	selected_difficulties = request.args.getlist('difficulty')
	if not selected_difficulties:
		selected_difficulties = ['easy', 'medium', 'hard']
	marked_filter = request.args.get('marked_filter', 'all')
	bluebook_filter = request.args.get('bluebook_filter', 'both')
	# Remove release_date_filter
	# release_date_filter = request.args.get('release_date_filter', 'all')

	# Add question counts to each mini-category based on filter
	categories_with_counts = []
	for cat in categories:
		mini_with_counts = []
		for mini in cat['mini_categories']:
			filtered_questions = [q for q in questions.get(mini['slug'], []) if q.get('difficulty') in selected_difficulties]
			if marked_filter == 'yes':
				filtered_questions = [q for q in filtered_questions if q.get('marked', False)]
			elif marked_filter == 'no':
				filtered_questions = [q for q in filtered_questions if not q.get('marked', False)]
			# Bluebook filter
			if bluebook_filter == 'yes':
				filtered_questions = [q for q in filtered_questions if q.get('active', '') == 'yes']
			elif bluebook_filter == 'no':
				filtered_questions = [q for q in filtered_questions if q.get('active', '') != 'yes']
			# Remove release_date filter
			# if release_date_filter != 'all':
			#     filtered_questions = [q for q in filtered_questions if q.get('release_date', '') == release_date_filter]
			count = len(filtered_questions)
			mini_with_counts.append({**mini, 'count': count})
		categories_with_counts.append({**cat, 'mini_categories': mini_with_counts})
	return render_template('index.html', categories=categories_with_counts, selected_difficulties=selected_difficulties, marked_filter=marked_filter, bluebook_filter=bluebook_filter)

@app.route('/category/<slug>')
def category(slug):
	qs = questions.get(slug, [])
	cat = next((c for c in categories if c['slug'] == slug), None)
	return render_template('category.html', category=cat, questions=qs)

if __name__ == '__main__':
	app.run(debug=True)
