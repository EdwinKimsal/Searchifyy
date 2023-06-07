// Variables
var index = [];

function search(){
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
            index = 'No results.'
        }

        // Set output paragraph's HTML to the index array
        document.getElementById('result').innerHTML = index;

        // Reset Element and Variable
        document.getElementById('searchArea').value = '';
        input = '';
        index = [];
    }

    else{
        // Reset Element and Variable
        document.getElementById('searchArea').value = '';
        input = '';
        index = [];

        // Set output paragraph's HTML to the index array
        document.getElementById('result').innerHTML = index;
    }
}

