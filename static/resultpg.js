let Positive=document.getElementById("Positive");
let Nuteral=document.getElementById("Nuteral");
let Negative=document.getElementById("Negative");
let result_comment=document.getElementById("result_comment");

// Get results by your sentiment analysis program
// Here are example result

let result_pos= pos_num;
let result_neg= neg_num;
let result_nut= neu_num;

Positive.textContent=result_pos+"%";
Negative.textContent=result_neg+"%";
Nuteral.textContent=result_nut+"%";


// ResultComment

result_comment.classList.remove("pos","neg","nut");
if(result_pos>=70){
    result_comment.classList.add("pos");
    result_comment.textContent="Highly positive feedback! Customers are overwhelmingly satisfied with the product/service."
}
else if(result_pos>=50 || (result_pos+result_nut)>=75){
    result_comment.classList.add("pos");
    result_comment.textContent= "Positive feedback! Customers generally express satisfaction with the product/service."
}
else if(result_nut>result_pos&&result_nut>result_neg){
    result_comment.classList.add("nut");
    result_comment.textContent= "Mixed feedback! Opinions vary, suggesting a neutral sentiment overall."
}
else if(result_neg>result_pos&&result_neg>result_neg&&result_neg<=55){
    result_comment.classList.add("neg");
    result_comment.textContent= "Negative feedback! Customers express dissatisfaction or concerns about the product/service.";
}
else{
    result_comment.classList.add("neg");
    result_comment.textContent="Highly negative feedback! Address urgent concerns to improve customer satisfaction."
}

// This section generates graph

var ctx = document.getElementById('myChart').getContext('2d');
var myPieChart = new Chart(ctx, {
    type: 'doughnut',
    data: {
        labels: ['Positive', 'Negative', 'Neutral'],
        datasets: [{
            data: [result_pos, result_neg, result_nut],
            backgroundColor: [
                'rgb(0, 148, 0)',
                'rgb(54, 162, 235)',
                'rgb(138, 0, 0)'
            ]
        }]
    },
    options: {
        // Add wedging effect
        
        // Removes border
        elements: {
            arc: {
                borderWidth: 0
            }
        },
        
        // Disable legends
        legend: {
            display: false // Set display to false to hide legends
        }
    }
});

