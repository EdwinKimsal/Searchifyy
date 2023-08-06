// greatest score to lowest score
// heapify
function heapify(arr, n, i){
    // variables
    largest = i;
    l = 2 * i + 1;
    r = 2 * i + 2;

    // is the left child greater than the parent
    if (l < n  && arr[i] < arr[l]){
        largest = l;
    }

    // is the right child greater than the parent
    if (r < n  && arr[largest] < arr[r]){
        largest = r;
    }
    
    // does the parent need chanegd
    if (largest != i){
        // swapping child and parent
        var tempLargest = arr[largest] // creating tempLargest to swap
        arr[largest] = arr[i]; // largest = i
        arr[i] = tempLargest // i = tempLargest (largest)

        // calling heapify
        heapify(arr, n, largest);
    }
}

// heapSort (the main function to sort the array though maxheap)
function heapSort(arr){
    n = arr.length;

    // last parent is ((n % 2) - 1)
    for (var i = 0; i < ((n % 2) - 1); i++){
        // calling heapify
        heapify(arr, n, i);
    }

    // extract elements one at a time
    for (var i = (n - 1); i >= 0; i--){         
        // swapping child and parent
        var tempZero = arr[0] // creating tempZero to swap
        arr[0] = arr[i]; // 0 = i
        arr[i] = tempZero // i = 0 (tempZero)

        // calling heapify
        heapify(arr, i, 0);
    }
}

// Below this line is for testing

function testCase(){
    // variables
    var amount = 10;
    var max = 6;
    var tca = [];

    // generating random array
    for (var i = 0; i < amount; i++){
        tca.push(Math.floor(Math.random() * max));
    }

    // console.log sorted arrray
    console.log(tca);

    // calling heapSort
    heapSort(tca);
    
    // console.log sorted arrray
    console.log(tca);
}