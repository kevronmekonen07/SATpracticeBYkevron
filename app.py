from flask import Flask, render_template, url_for, request, session, redirect, url_for
import json

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Change this to a secure random value

try:
	with open('Static/March2025_Q&A/Algebra/linear_equations_one_variable11.json', 'r', encoding='utf-8') as f:
		linear_eq_questions = json.load(f)
	with open('Static/March2025_Q&A/Algebra/linear_functions.json', 'r', encoding='utf-8') as f:
		linear_functions_questions = json.load(f)
	with open('Static/March2025_Q&A/Algebra/linear_equations_two_variable.json', 'r', encoding='utf-8') as f:
		linear_eq_two_questions = json.load(f)
	with open('Static/March2025_Q&A/Algebra/Systems_Two_Linear_Equations_Two_Variables.json', 'r', encoding='utf-8') as f:
		system_linear_eq_questions = json.load(f)
	with open('Static/March2025_Q&A/Algebra/Linear_InequalitiesIn_One_Two_Variables.json', 'r', encoding='utf-8') as f:
		linear_ineq_questions = json.load(f)
	with open('Static/March2025_Q&A/AdvancedMath/equivalent_expressions.json', 'r', encoding='utf-8') as f:
		equivalent_expressions = json.load(f)
	with open('Static/March2025_Q&A/AdvancedMath/nonlinear_equations_systems.json', 'r', encoding='utf-8') as f:
		nonlinear_equations_systems = json.load(f)
	with open('Static/March2025_Q&A/AdvancedMath/nonlinear_functions.json', 'r', encoding='utf-8') as f:
		nonlinear_functions = json.load(f)

	with open('Static/March2025_Q&A/ProblemSolvingAndDataAnalysis/ratio_rates_proportional_units.json', 'r', encoding='utf-8') as f:
		ratio_rates_proportional_units = json.load(f)
	with open('Static/March2025_Q&A/ProblemSolvingAndDataAnalysis/Percentages.json', 'r', encoding='utf-8') as f:
		percentages = json.load(f)
	with open('Static/March2025_Q&A/ProblemSolvingAndDataAnalysis/one_variable_data_distributions_center_spread.json', 'r', encoding='utf-8') as f:
		one_variable_data_distributions_center_spread = json.load(f)
	with open('Static/March2025_Q&A/ProblemSolvingAndDataAnalysis/two_variable_data_models_scatterplots.json', 'r', encoding='utf-8') as f:
		two_variable_data_models_scatterplots = json.load(f)
	with open('Static/March2025_Q&A/ProblemSolvingAndDataAnalysis/probability_conditional_probability.json', 'r', encoding='utf-8') as f:
		probability_conditional_probability = json.load(f)
	with open('Static/March2025_Q&A/ProblemSolvingAndDataAnalysis/inference_sample_statistics_margin_error.json', 'r', encoding='utf-8') as f:
		inference_sample_statistics_margin_error = json.load(f)
	with open('Static/March2025_Q&A/ProblemSolvingAndDataAnalysis/evaluating_statistical_claims_studies_experiments.json', 'r', encoding='utf-8') as f:
		evaluating_statistical_claims_studies_experiments = json.load(f)
	with open('Static/March2025_Q&A/GeometryAndTrigonometry/area_volume.json', 'r', encoding='utf-8') as f:
		area_volume = json.load(f)
	with open('Static/March2025_Q&A/GeometryAndTrigonometry/lines_angles_triangles.json', 'r', encoding='utf-8') as f:
		lines_angles_triangles = json.load(f)
	with open('Static/March2025_Q&A/GeometryAndTrigonometry/right_triangles_trigonometry.json', 'r', encoding='utf-8') as f:
		right_triangles_trigonometry = json.load(f)
	with open('Static/March2025_Q&A/GeometryAndTrigonometry/circles.json', 'r', encoding='utf-8') as f:
		circles = json.load(f)
except FileNotFoundError:
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



    system_linear_eq_questions = []
    linear_ineq_questions = []
    equivalent_expressions = []
    nonlinear_equations_systems = []
    nonlinear_functions = []
    ratio_rates_proportional_units = []
    percentages = []
    one_variable_data_distributions_center_spread = []
    two_variable_data_models_scatterplots = []
    probability_conditional_probability = []
    inference_sample_statistics_margin_error = []
    evaluating_statistical_claims_studies_experiments = []
    area_volume = []
    lines_angles_triangles = []
    right_triangles_trigonometry = []
    circles = []

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
