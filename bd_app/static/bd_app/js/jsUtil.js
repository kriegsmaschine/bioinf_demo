function scatter(exp_data){
	var data = JSON.parse(exp_data);
	var tlen = {};

	for(var x = 0; x < data.exp_data.length; x++){
	  	tlen[x] = x;
	}

	document.getElementById("output_test").innerHTML = data.exp_data.length;

	var trace1 = {
	  x: tlen,
	  y: data.exp_data,
	  mode: 'markers',
	  type: 'scatter'
	};

	var data = [trace1];

	Plotly.newPlot('output_test', data);

	/*
		to add multiple plots per plotly graph mush use Plotly.addTraces()
		to overwrite previous data.  this would be used to compare
		different cohorts, msi status, gender, etc.

		https://plot.ly/javascript/plotlyjs-function-reference/
	*/
}