function scatter(exp_data){
	var data = JSON.parse(exp_data);
	var tlen = {};

	for(var x = 0; x < data.exp_data.length; x++){
	  	tlen[x] = x;
	}

	document.getElementById("output_test").innerHTML = data.exp_data.length;
	document.getElementById("output_test").innerHTML += "".concat("  Gene: ",data.gene);
 	if(data.plot == "scatter"){
		var trace1 = {
		  x: tlen,
		  y: data.exp_data,
		  mode: 'markers',
		  type: 'scatter',
		  name: data.gene,
		};
	
		var data = [trace1];
		Plotly.newPlot('output_test', data);

	}else if(data.plot == "boxplot"){
		var trace1 = {
			y: data.exp_data,
			type: 'box',
			name: data.gene,
		}

		var data = [trace1];
		Plotly.newPlot('output_test', data);

	}else if(data.plot == "histogram"){
		var max = Math.max.apply(data.exp_data);
		autobinx: false;

		var binSize = 0.025 * max;
		var trace1 = {
			x: data.exp_data,
			type: 'histogram',
			name: data.gene,

			xbins: {
				start: 0,
				end: max,
				size: binSize,
			}
		};
		
		var data = [trace1];
		Plotly.newPlot('output_test', data);

	}else if(data.plot == "kaplan-meier"){
		alert(data.plot);

	}else{
		alert("No chart type selected");
	}

	/*
		to add multiple plots per plotly graph mush use Plotly.addTraces()
		to overwrite previous data.  this would be used to compare
		different cohorts, msi status, gender, etc.

		https://plot.ly/javascript/plotlyjs-function-reference/
	*/
}