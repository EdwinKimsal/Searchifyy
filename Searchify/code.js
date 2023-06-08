// Variables
var index = [];

// Search Algorithm
function search(){
    // Variable
    document.getElementById('result').innerHTML = '';
    var input = document.getElementById('searchArea').value;

    if(input != ''){
        // Find matching results
        for(let i = 0; i < sitemap.length; i++){
            if(sitemap[i].includes(input)){
                index.push("https://quotes.toscrape.com" + sitemap[i]);
            }
        }

        // Check if there are any results
        if(index == ''){
            index = 'No results.';
            document.getElementById('result').innerHTML = index;

            // Reset Element and Variable
            input = '';
            index = [];
        }

        else{
            for(let i = 0; i < index.length; i++){
                // Set output paragraph's HTML to the index array
                var link = document.createElement('a');
                var linebreak = document.createElement("br");
                link.href = index[i];
                link.innerHTML = index[i];
                document.getElementById('result').appendChild(link);
                document.getElementById('result').appendChild(linebreak);
            }
    
            // Reset Element and Variable
            input = '';
            index = [];    
        }
    }

    else{
        // Reset Element and Variable
        input = '';
        index = [];

        // Set output paragraph's HTML to the index array
        document.getElementById('result').innerHTML = index;
    }
}