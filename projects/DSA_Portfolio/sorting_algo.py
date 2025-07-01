from flask import Flask, render_template, request
from MergeSort import mergeSort
from BubbleSort import bubbleSort
from SelectionSort import selectionSort
from InsertionSort import insertionSort
from QuickSort import quicksort
import timeit


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('sortingalgo.html')

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
if __name__ == '__main__':
    app.run(debug=True)
