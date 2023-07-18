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
                    totalCount += countArray[((queryArray.length * i) + j)] / countFrequency[j];
                }
            }

            // pushing/resetting totalCount
            totalCountArray.push(totalCount);
            totalCount = 0;
        }
        
        // greatest score to lowest score
        for (var i = 0; i < totalCountArray.length; i++){
            for (var j = 0; j < totalCountArray.length; j++){
                if (totalCountArray[j] < totalCountArray[j + 1]){
                    var tempCount = totalCountArray[j];
                    totalCountArray[j] = totalCountArray[j + 1];
                    totalCountArray[j + 1] = tempCount;

                    var tempUrl = newUrlArray[j];
                    newUrlArray[j] = newUrlArray[j + 1];
                    newUrlArray[j + 1] = tempUrl;
                }
            }
        }

        // showing results
        for (var i = 0; i < newUrlArray.length; i++){
            if (totalCountArray[i] > 0){
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