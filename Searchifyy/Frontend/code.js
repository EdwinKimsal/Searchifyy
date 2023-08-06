// search algorithm
function score(){
    // variables
    var query = document.getElementById('searchArea').value.toLowerCase();
    var output = document.getElementById('result');
    var booleanCountArray = [];
    var totalCountArray = [];
    var newUrlArray = [];
    var queryArray = [];
    var countFrequency = [];
    var countArray = [];
    var totalCount = 0;
    var count = 0;
    output.innerHTML = '';

    // copying arrays into newArrays
    for (var i = 0; i < urlArray.length; i++){
        newUrlArray.push(urlArray[i]);
    }

    // transforming query into queryArray
    queryArray = query.split(" ");

    // checking if query IS NOT blank
    if (queryArray != []){
        // creating scores
        for (var i = 0; i < newUrlArray.length; i++){
            // checking each word individualy
            for (var j = 0; j < queryArray.length; j++){
                var re = new RegExp(queryArray[j], 'gi');
                count = ((urlArray[i].match(re) || []).length);
            
                // resetting count
                countArray.push(count);
                count = 0;
            }
        }

        // adding content to booleanCountArray
        for (var i = 0; i < countArray.length; i++){
            if (countArray[i] > 0){
                booleanCountArray.push(1);
            }

            else{
                booleanCountArray.push(0);
            }
        }

        // adding content to countFrequency
        for (var i = 0; i < queryArray.length; i++){
            countFrequency.push(0);
        }

        // getting frequency of each word per page
        for (var i = 0; i < countFrequency.length; i++){
            for (var j = 0; j < booleanCountArray.length/countFrequency.length; j++){
                countFrequency[i] += booleanCountArray[((countFrequency.length * j) + i)];
            }
        }

        // updating the final scores for each page
        for (var i = 0; i < newUrlArray.length; i++){
            for (var j = 0; j < queryArray.length; j++){
                if (countFrequency[j] != 0){
                    totalCount += (countArray[((queryArray.length * i) + j)] / countFrequency[j]);
                }
            }

            // pushing/resetting totalCount
            totalCountArray.push(totalCount);
            totalCount = 0;
        }

        // removing all zero score pages from the index
        for (var i = totalCountArray.length; i >= 0; i--){
            if (totalCountArray[i] == 0){
                totalCountArray.splice(i, 1);
                newUrlArray.splice(i, 1)
            }
        }
        
        function heapSort(arr){
            var N = arr.length;
        
            // Build heap (rearrange array)
            for (var i = Math.floor(N / 2) - 1; i >= 0; i--)
                heapify(arr, N, i);
        
            // One by one extract an element from heap
            for (var i = N - 1; i > 0; i--) {
                // Move current root to end
                var temp = arr[0];
                arr[0] = arr[i];
                arr[i] = temp;

                var temp = newUrlArray[0];
                newUrlArray[0] = newUrlArray[i];
                newUrlArray[i] = temp;
        
                // call max heapify on the reduced heap
                heapify(arr, i, 0);
            }
        }
        
        // To heapify a subtree rooted with node i which is
        // an index in arr[]. n is size of heap
        function heapify(arr, N, i){
            var largest = i; // Initialize largest as root
            var l = 2 * i + 1; // left = 2*i + 1
            var r = 2 * i + 2; // right = 2*i + 2
        
            // If left child is larger than root
            if (l < N && arr[l] > arr[largest])
                largest = l;
        
            // If right child is larger than largest so far
            if (r < N && arr[r] > arr[largest])
                largest = r;
        
            // If largest is not root
            if (largest != i) {
                var swap = arr[i];
                arr[i] = arr[largest];
                arr[largest] = swap;

                var swap = newUrlArray[i];
                newUrlArray[i] = newUrlArray[largest];
                newUrlArray[largest] = swap;
        
                // Recursively heapify the affected sub-tree
                heapify(arr, N, largest);
            }
        }

        // calling heapSort
        heapSort(totalCountArray, newUrlArray);

        // showing results
        for (var i = newUrlArray.length - 1; i > newUrlArray.length - 100; i--){
            if (i > 0){
                // Set output paragraph's HTML to the index array
                const section = document.createElement('section')
                const link = document.createElement('a');
                const linebreak = document.createElement('br');
                link.href = newUrlArray[i];
                link.innerHTML = newUrlArray[i];
                section.appendChild(link);
                section.appendChild(linebreak);
                output.appendChild(section);
            }
        }

        console.log(totalCountArray);
    }

    // reset output if query is blank
    else{
        output.innerHTML = ''
    }
}