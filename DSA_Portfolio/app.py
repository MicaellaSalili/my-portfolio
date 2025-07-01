import timeit
from flask import Flask, request, jsonify, render_template, make_response
from exponential_search import exponential_search, exponential_search_wrapper
from binary_search import binary_search, binary_search_wrapper
from interpolation_search import interpolation_search, interpolation_search_wrapper
from jump_search import jump_search, jump_search_wrapper
from linear_search import linear_search, linear_search_wrapper
from ternary_search import ternary_search, ternary_search_wrapper
from data_generator import small_data_set, medium_data_set, large_data_set
from Queue_and_Deque import Queue, Deque
from collections import deque
from Hash_Table import hash_table, process_commands
from Stack import infix_to_postfix
from MergeSort import mergeSort
from BubbleSort import bubbleSort
from SelectionSort import selectionSort
from InsertionSort import insertionSort
from QuickSort import quicksort
from flask import Response, redirect, url_for
import math

app = Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html")

#ALIJAH PORTFOLIO

@app.route('/alijahindex')
def alijahindex():
    return render_template('alijahindex.html')

@app.route('/alijahprofile')
def profile():
    return render_template('alijahprofile.html')

@app.route('/alijahworks')
def works():
    return render_template('alijahwork.html')

@app.route('/UpperCase', methods=['GET', 'POST'])
def Uppercase():
    result = None
    if request.method == 'POST':
        input_string = request.form.get('inputString', '')
        result = input_string.upper()
    return render_template('touppercase.html', result=result)

@app.route('/areaOfcircle', methods=['GET', 'POST'])
def areaOfcircle():
    result_area = None
    if request.method == 'POST':
        input_number = request.form.get('inputNumber',0)
        input_diameter = request.form.get('inputDiameter',0)

        try:
            input_number = float(input_number)
            input_diameter = float(input_diameter)
        except ValueError:
            # Handle invalid input (non-numeric input) here
            pass
        except TypeError:
            # Handle invalid input (non-numeric input) here
            pass

        if input_diameter > 0:
            result_area = (math.pi * (input_diameter ** 2)) /4
        elif input_number > 0:
            result_area = math.pi * (input_number ** 2)
        else:
            result_area = None

    return render_template('areaOfcircle.html', result=result_area)

@app.route('/areaOfTriangle', methods=['GET', 'POST'])
def areaOfTriangle():
    result_area = None
    if request.method == 'POST':
        input_Base = request.form.get('inputBase', '')
        input_Height = request.form.get('inputHeight','')
        result_area = (int(input_Height)*int(input_Base))/2
    return render_template('areaOfTriangle.html', result=(str(result_area)+" squared unit"))

# Initialize a global list to store contacts
contact_info = []

@app.route('/alijahcontact', methods=['GET','POST'])
def contact():
    if request.method == 'POST':
        input_Name = request.form.get('inputName', '')
        input_Number = request.form.get('inputNumber', '')
        input_Email = request.form.get('inputEmail','')
        result_contact = {"Name": input_Name,
                          "Number": input_Number,
                          "Email": input_Email}

        contact_info.append(result_contact)

    return render_template('alijahcontact.html', result=contact_info)

#ELLA PORTOFLIO

@app.route('/ella')
def ellahome():
    return redirect(url_for('ellaindex'))

@app.route('/ellahome', methods=['GET', 'POST'])
def ellaindex():
    return render_template('ellaindex.html')

@app.route('/ellaprofile')
def ellaprofile():
    return render_template('ellaprofile.html')

@app.route('/ellaworks', methods=['GET', 'POST'])
def ellaworks():
    return render_template('ellaworks.html')

@app.route('/ella-touppercase', methods=['GET', 'POST'])
def ellaupper():
    result = None
    if request.method == 'POST':
        input_string = request.form.get('inputString', '')
        result = input_string.upper()
    return render_template('ellatouppercase.html', result=result)

@app.route('/ellacontact')
def ellacontact():
    return render_template('ellacontacts.html')

@app.route('/ella-areaofcircle', methods=['GET', 'POST'])
def ellacircle():
    radius = None
    result = None
    pi = 3.142
    if request.method == 'POST':
        try:
            radius = request.form.get('inputRadius', '')
            result = pi * float(radius)**2
        except ValueError:
            pass
    return render_template('ellacircle.html', radius=radius, result=result)

@app.route('/ella-areaoftriangle', methods=['GET', 'POST'])
def ellatriangle():
    base = None
    height = None
    result = None
    constant = 1/2
    if request.method == 'POST':
        try:
            base = request.form.get('inputBase', '')
            height = request.form.get('inputHeight', '')
            result = constant * float(base) * float(height)
        except ValueError:
            pass
    return render_template('ellatriangle.html', base=base, height=height, result=result)

#ASHANTI PORTFOLIO

@app.route('/ashanti')
def ashantiindex():
    return render_template('ashantiindex.html')

@app.route('/ashantiprofile')
def ashantiprofile():
    return render_template('ashantiprofile.html')

@app.route('/ashantiworks', methods=['GET', 'POST'])
def ashantitouppercase():
    result = None
    if request.method == 'POST':
        input_string = request.form.get('inputString', '')
        result = input_string.upper()
    return render_template('ashantitouppercase.html', result=result)

@app.route('/ashanticontact')
def ashanticontact():
    return render_template('ashanticontacts.html')

@app.route('/ashantiprogworks')
def ashantiprogworks():
    return render_template('ashantiprogworks.html')

@app.route('/ashanti-areaOfcirle', methods=['GET', 'POST'])
def ashantiareaOfcirle():
    area_result = None
    radius = None
    pi = 3.14159
    if request.method == 'POST':
        try:
            radius = int(request.form.get('radius'))
            area_result = pi * int(radius)**2
        except ValueError:
            pass
    return render_template('ashantiareaOfcirle.html', area_result=area_result, radius=radius)

@app.route('/ashanti-areaOfTriangle', methods=['GET','POST'])
def ashantiareaOfTriangle():
    area_result = None
    if request.method == 'POST':
        base_str = request.form.get('base')
        height_str = request.form.get('height')
        try:
            base = int(base_str)
            height = int(height_str)
            area_result = 0.5 * base * height
        except ValueError:
            pass
    return render_template('ashantiareaOfTriangle.html', area_result=area_result)

#MICA PORTFOLIO

@app.route('/mica')
def micaindex():
    return render_template('micaindex.html')

@app.route('/micaprofile')
def micaprofile():
    return render_template('micaprofile.html')

@app.route('/micaworks')
def micaworks():
    return render_template('micaworks.html')

@app.route('/micacontact')
def micacontact():
    return render_template('micacontact.html')

@app.route('/mica-uppercase_convert', methods=['GET', 'POST'])
def micaconvert():
    result = None
    if request.method == 'POST':
        input_string = request.form.get('inputString', '')
        result = input_string.upper()
    return render_template('micatouppercase.html', result=result)

@app.route('/mica-areaOfcircle', methods=['GET', 'POST'])
def micaarea_of_circle():
    area_circle = None
    radius = None
    if request.method == 'POST':
        radius = (request.form.get('radius', 0))
        area_circle = 3.14159 * float(radius) ** 2
        area_circle = round(area_circle, 2)
    return render_template('micacircle_area.html', area_circle=area_circle , radius=radius)

@app.route('/mica-areaOftriangle', methods=['GET', 'POST'])
def micaarea_of_triangle():
    area_triangle = None
    base = None
    height = None
    if request.method == 'POST':
        base = float(request.form.get('base', 0))
        height = float(request.form.get('height', 0))
        area_triangle = 0.5 * base * height
        area_triangle = round(area_triangle, 2)
    return render_template('micatriangle_area.html', area_triangle=area_triangle, base=base, height = height)

#KIM PORTFOLIO
@app.route('/kim')
def kimindex():
    return render_template('kimindex.html')


@app.route('/kimprofile')
def kimprofile():
    return render_template('kimprofile.html')

@app.route('/kimworks', methods=['GET', 'POST'])
def kimworks():
    return render_template('kimworks.html')

@app.route('/kimto-upper-case', methods=['GET', 'POST'])
def kimtouppercase():
    result = None
    if request.method == 'POST':
        input_string = request.form.get('inputString', '')
        result = input_string.upper()
    return render_template('kimtouppercase.html', result=result)

@app.route('/kimarea-of-circle', methods=['GET', 'POST'])
def kimareaOfcircle():
    result = None
    if request.method == 'POST':
        input_num = request.form.get('inputNum','')
        result = 3.14 * int(input_num) ** 2
    return render_template('kimarea-of-a-circle.html', result=result)

@app.route('/kimarea-of-triangle', methods=['GET', 'POST'])
def kimareaOfTriangle():
    result = None
    if request.method == 'POST':
        input_Base = request.form.get('inputBase','')
        input_Height = request.form.get('inputHeight','')
        result = int(input_Base) * int(input_Height) / 2
    return render_template('kimarea-of-triangle.html', result=result)

@app.route('/kimcontact')
def kimcontact():
    return render_template('kimcontact.html')

#DENISE PORTFOLIO

@app.route('/denise')
def deniseindex():
    return render_template('deniseindex.html')

@app.route('/deniseprofile')
def deniseprofile():
    return render_template('deniseprofile.html')

@app.route('/denisecontact')
def denisecontact():
    return render_template('denisecontact.html')

@app.route('/denisecircle', methods=['GET', 'POST'])
def denisecircle():
    area = None
    if request.method == 'POST':
        radius = float(request.form.get('radius', 0.0))
        area = 3.14159*radius**2
    return render_template('denisecircle.html', area=area)

@app.route('/denisetriangle', methods=['GET', 'POST'])
def denisetriangle():
    area = None
    if request.method =='POST':
        base = float(request.form.get('base', 0.0))
        height = float(request.form.get('height', 0.0))
        area = 0.5*base*height
    return render_template('denisetriangle.html', area=area)

@app.route('/denisetouppercase', methods=['GET', 'POST'])
def denisetouppercase():
    result = None
    if request.method == 'POST':
        input_string = request.form.get('inputString', '')
        result = input_string.upper()
    return render_template('denisetouppercase.html', result=result)

@app.route('/deniseworks', methods=['GET', 'POST'])
def deniseworks():
    operation = None
    if request.method == 'POST':
        operation = request.form.get('operation')
        if operation == "touppercase":
            return redirect(url_for('touppercase'))
        elif operation == "triangle":
            return redirect(url_for('triangle'))
        elif operation == "circle":
            return redirect(url_for('circle'))
    return render_template('deniseworks.html')

#SEARCH ALGORITHM
@app.route("/get_test_data", methods=["GET"])
def get_test_data():
    size = request.args.get("size", "small")
    if size == "small":
        return Response(", ".join(map(str, small_data_set)), content_type="text/plain")
    elif size == "medium":
        return Response(", ".join(map(str, medium_data_set)), content_type="text/plain")
    elif size == "large":
        return Response(", ".join(map(str, large_data_set)), content_type="text/plain")
    else:
        return make_response("Invalid data set size", 400, {"Content-Type": "text/plain"})


@app.route("/SearchAlgorithm", methods=["GET", "POST"])
def SearchAlgorithm():
    numbers = ""
    test_data = ", ".join(map(str, numbers))
    execution_time = 0  # Initialize execution_time outside the try block

    if request.method == "POST":
        array_str = request.form.get("array")
        target_str = request.form.get("target")
        search_type = request.form.get("search_type")

        try:
            array = list(map(int, array_str.split(",")))
            target = int(target_str)
            low, high = 0, len(array) - 1

            result = -1  # Initialize result before the conditional statements

            if search_type == "exponential":
                execution_time = timeit.timeit("exponential_search_wrapper(exponential_search, array, target)",
                                               globals={**globals(), "array": array, "target": target}, number=1) * 10000
                result = exponential_search_wrapper(binary_search, array, target)
                # result = exponential_search(array, target)
            elif search_type == "binary":
                # arr = list(map(int, array_str.split(",")))
                execution_time = timeit.timeit("binary_search_wrapper(binary_search, array, target)",
                                               globals={**globals(), "array": array, "target": target}, number=1) * 10000
                result = binary_search_wrapper(binary_search, array, target)
            elif search_type == "interpolation":
                execution_time = timeit.timeit("interpolation_search_wrapper(interpolation_search, array, target)",
                                               globals={**globals(), "array": array, "target": target}, number=1) * 10000
                result = interpolation_search_wrapper(interpolation_search, array, target)
                # result = interpolation_search(array, target)
            elif search_type == "jump":
                execution_time = timeit.timeit("jump_search_wrapper(jump_search, array, target)",
                                               globals={**globals(), "array": array, "target": target}, number=1) * 10000
                result = jump_search_wrapper(interpolation_search, array, target)
                # result = jump_search(array, target)
            elif search_type == "linear":
                execution_time = timeit.timeit("linear_search_wrapper(linear_search, array, target)",
                                               globals={**globals(), "array": array, "target": target}, number=1) * 10000
                result = linear_search_wrapper(linear_search, array, target)
                # result = linear_search(array, target)
            elif search_type == "ternary":
                execution_time = timeit.timeit("ternary_search_wrapper(ternary_search, array, target, low, high)",
                                               globals={**globals(), "array": array, "target": target, "low": low,
                                                        "high": high}, number=1) * 1000
                result = ternary_search_wrapper(ternary_search, array, target, low, high)
                # result = ternary_search(array, target, low, high)

            if result == -1:
                error_message = f"Target {target} not found in the array."
                return render_template("SearchAlgorithm.html", error=error_message, test_data=test_data)

            return render_template("SearchAlgorithm.html", result=result, search_type=search_type, execution_time=execution_time,
                                   test_data=test_data)
        except ValueError:
            return render_template("SearchAlgorithm.html", error="Invalid input. Ensure the array and target are integers.")

    return render_template("SearchAlgorithm.html", test_data=test_data)

@app.route("/search", methods=["POST"])
def search():
    data = request.get_json()

    if not data or "array" not in data or "target" not in data:
        return jsonify({"error": "Invalid request data. Provide 'array' and 'target'."}), 400

    array = data["array"]
    target = data["target"]

    result_iterative = exponential_search(array, target)
    # result_recursive = exponential_search_recursive(array, target)

    return jsonify({
        "iterative_search_result": result_iterative,
        # "recursive_search_result": result_recursive
    })

#STACK ALGORITHM

@app.route('/Stack')
def StackIndex():
    return render_template('Stack.html')

@app.route('/stackconvert', methods=['POST'])
def stackconvert():
    infix_expression = request.form['infix_expression']
    postfix_expressions = infix_to_postfix(infix_expression)

    return render_template('Stack.html', infix_expression=infix_expression, postfix_expressions=postfix_expressions)

#QUEUE ALGORITHM

# Initialize the queue as a global variable
queue = Queue()

def display_queue(queue):
    elements = []
    current = queue.front
    while current:
        elements.append(current.data)
        current = current.next
    return elements

@app.route("/Queue", methods=["GET", "POST"])
def queue_showcase():
    global queue
    queue_result = []

    if request.method == "POST":
        user_input = request.form.get("inputFront", "")
        numbers = user_input.split()

        for num in numbers:
            queue.enqueue(num)

        if "dequeue" in request.form:
            queue.dequeue()

        queue_result = display_queue(queue)

    return render_template('Queue.html', result=queue_result)

#DEQUE ALGORITHM
# Initialize the deque as a global variable
deque_app = Deque()
def display_deque(deque_app):
    elements = []
    current = deque_app.front
    while current:
        elements.append(current.data)
        current = current.next
    return elements

@app.route("/Deque", methods=["GET", "POST"])
def deque_showcase():
    global deque_app
    deque_result = []

    if request.method == "POST":
        user_input_front = request.form.get("inputFront", "")
        front_input = user_input_front.split()

        for num in front_input:
            deque_app.add_front(num)

        if "dequeue_front" in request.form:
            deque_app.remove_front()

        elif "enqueue_rear" in request.form:
            user_input_rear = request.form.get("inputRear", "")
            rear_input = user_input_rear.split()

            for num in rear_input:
                deque_app.add_rear(num)

        elif "dequeue_rear" in request.form:
            deque_app.remove_rear()

        deque_result = display_deque(deque_app)

    return render_template('Deque.html', result=deque_result)

#HASH TABLE

@app.route('/Hash', methods=['GET', 'POST'])
def hash():
    if request.method == 'POST':
        hash_function = int(request.form.get('hash_function', 1))
        num_commands = int(request.form.get('num_commands', 0))
        commands = request.form.get('commands', '').split('\n')

        # Validate input values
        if 1 <= hash_function <= 3 and num_commands >= 0:
            process_commands(hash_function, num_commands, commands)

    return render_template('hash.html', hash_table=hash_table)

#MRT LINE GRAPH & TREES

class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        self.vertices[vertex] = []

    def add_edge(self, source, target):
        self.vertices[source].append(target)
        self.vertices[target].append(source)

    def shortest_path_bfs(self, start, end):
        if start not in self.vertices or end not in self.vertices:
            return None

        queue_graph = deque([(start, [start])])

        while queue_graph:
            current_station, path = queue_graph.popleft()

            if current_station == end:
                return ' -> '.join(path)

            for neighbor in self.vertices[current_station]:
                if neighbor not in path:
                    queue_graph.append((neighbor, path + [neighbor]))

        return None

graph = Graph()

stations = ["North Avenue", "Quezon Avenue", "Kamuning", "Cubao", "Santolan-Anapolis", "Ortigas", "Shaw Blvd.", "Boni", "Guadalupe", "Buendia", "Ayala", "Magallanes", "Taft",
"Recto", "Legarda", "Pureza", "V. Mapa", "J. Ruiz", "Gilmore", "Betty Go-Belmonte", "Cubao", "Anonas", "Katipunan", "Santolan", "Marikina", "Antipolo",
"Baclaran", "EDSA", "Libertad", "Gil Puyat", "Vito Cruz", "Quirino", "Pedro Gil", "United Nation", "Central Terminal", "Carriedo",
"Doroteo Jose", "Bambang", "Tayuman", "Blumentritt", "Abad Santos", "R. Papa", "5th Avenue", "Monumento", "Malvar", "Balintawak", "Roosevelt", "North Ave."]

for station in stations:
    graph.add_vertex(station)

edges = [("North Avenue", "Quezon Avenue"), ("Quezon Avenue", "Kamuning"), ("Kamuning", "Cubao"),
         ("Cubao", "Santolan-Anapolis"), ("Santolan-Anapolis", "Ortigas"), ("Ortigas", "Shaw Blvd."), ("Shaw Blvd.", "Boni"),
         ("Boni", "Guadalupe"), ("Guadalupe", "Buendia"), ("Buendia", "Ayala"), ("Ayala", "Magallanes"), ("Magallanes", "Taft"), ("Taft", "EDSA"),
         ("Recto", "Legarda"), ("Legarda", "Pureza"), ("Pureza", "V. Mapa"), ("V. Mapa", "J. Ruiz"), ("J. Ruiz", "Gilmore"),
         ("Gilmore", "Betty Go-Belmonte"), ("Betty Go-Belmonte", "Cubao"), ("Cubao", "Anonas"),
         ("Anonas", "Katipunan"), ("Katipunan", "Santolan"), ("Santolan", "Marikina"), ("Marikina", "Antipolo"), ("Baclaran", "EDSA"), ("EDSA", "Libertad"), ("Libertad", "Gil Puyat"),("Gil Puyat", "Vito Cruz"),
         ("Vito Cruz", "Quirino"), ("Quirino", "Pedro Gil"), ("Pedro Gil", "United Nation"), ("United Nation", "Central Terminal"), ("Central Terminal", "Carriedo"),
         ("Carriedo", "Doroteo Jose"), ("Doroteo Jose", "Bambang"), ("Doroteo Jose", "Recto"), ("Bambang", "Tayuman"), ("Tayuman", "Blumentritt"), ("Blumentritt", "Abad Santos"),
         ("Abad Santos", "R. Papa"), ("R. Papa", "5th Avenue"), ("5th Avenue", "Monumento"), ("Monumento", "Balintawak"), ("Balintawak", "Roosevelt")]

for edge in edges:
    graph.add_edge(edge[0], edge[1])

@app.route('/MRTGraph', methods=['GET', 'POST'])
def shortest_path():
    if request.method == 'POST':
        start_station = request.form['start']
        end_station = request.form['end']
        shortest_path = graph.shortest_path_bfs(start_station, end_station)

        if shortest_path:
            shortest_path_stations = shortest_path.split(' -> ')
            return render_template('Graph.html', start_station=start_station, end_station=end_station, shortest_path=shortest_path, shortest_path_stations=shortest_path_stations)
        else:
            shortest_path_stations = []
            return render_template('Graph.html', start_station=start_station, end_station=end_station, shortest_path='None. Make sure to input correct stations!',shortest_path_stations=shortest_path_stations)

    return render_template('Graph.html')

#SORTING ALGORITHM

@app.route('/sort', methods=['GET', 'POST'])
def sort():
    if request.method == 'POST':
        array_str = request.form['array']
        search_type = request.form['search_type']

        input_array = [int(num) for num in array_str.split(',')]

        if search_type == 'merge_sort':
            def merge_sort():
                mergeSort(input_array)

            execution_time = timeit.timeit(merge_sort, number=1) * 1000
            sorted_output = input_array

        elif search_type == 'bubble_sort':
            def bubble_sort():
                bubbleSort(input_array)

            execution_time = timeit.timeit(bubble_sort, number=1) * 1000
            sorted_output = input_array

        elif search_type == 'selection_sort':
            def selection_sort():
                selectionSort(input_array, len(input_array))

            execution_time = timeit.timeit(selection_sort, number=1) * 1000
            sorted_output = input_array

        elif search_type == 'insertion_sort':
            def insertion_sort():
                insertionSort(input_array)

            execution_time = timeit.timeit(insertion_sort, number=1) * 1000
            sorted_output = input_array

        elif search_type == 'quick_sort':
            def quick_sort():
                quicksort(input_array, 0, len(input_array) - 1)

            execution_time = timeit.timeit(quick_sort, number=1) * 1000
            sorted_output = input_array

        return render_template('sortingalgo.html', sorted_output=sorted_output, test_data=array_str,
                               execution_time=execution_time)

    return render_template('sortingalgo.html', sorted_output=None, test_data=None)

if __name__ == "__main__":
    app.run(debug=True)