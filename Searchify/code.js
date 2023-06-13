// Search Algorithm
function score(){
    // Variables
    var input = document.getElementById('searchArea').value.toLowerCase();
    var output = document.getElementById('result');
    var newUrlArray = [];
    var countArray = [];
    var count = 0;
    output.innerHTML = '';

    // Copying urlArray to newUrlArray
    for (var i = 0; i < urlArray.length; i++){
        newUrlArray.push(urlArray[i]);
    }

    if (input != ''){
        // Creating Scores
        for (var i = 0; i < htmlArray.length; i++){
            var re = new RegExp(input, 'gi');
            count = (htmlArray[i].match(re) || []).length;

            countArray.push(count);
        }

        for (var i = 0; i < countArray.length; i++){
            if (newUrlArray[i].includes(input) == true){
                countArray[i] = countArray[i] ** 2;
            }
        }

        // Greatest Score to Lowest Score
        for (var i = 0; i < countArray.length; i++){
            for (var j = 0; j < countArray.length; j++){
                if (countArray[j] < countArray[j + 1]){
                    var tempCount = countArray[j];
                    countArray[j] = countArray[j + 1];
                    countArray[j + 1] = tempCount;

                    var tempUrl = newUrlArray[j];
                    newUrlArray[j] = newUrlArray[j + 1];
                    newUrlArray[j + 1] = tempUrl;
                }
            }
        }

        // Showing Results
        for (var i = 0; i < newUrlArray.length; i++){
            if (countArray[i] > 0){
                // Set output paragraph's HTML to the index array
                const link = document.createElement('a');
                const linebreak = document.createElement('br');
                link.href = newUrlArray[i];
                link.innerHTML = newUrlArray[i];
                output.appendChild(link);
                output.appendChild(linebreak);
            }
        }
    }

    // Result if query is blank
    else{
        output.innerHTML = ''
    }
}