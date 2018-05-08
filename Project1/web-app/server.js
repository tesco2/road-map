const express = require('express')
const app = express()
const bodyParser = require('body-parser');
const spawn = require("child_process").spawn;

app.set('view engine','ejs')
app.use(express.static('public'));
app.use(bodyParser.urlencoded({ extended: true }));

app.get('/', function (req, res) {
  res.render('mappage',{red: null,green:null,blue:null, lat:-37.82701522389683, lng:144.96238708496094,total:null});
})

app.post('/',function (req,res){
	var Latitude = req.body.lat;
	var Longitude = req.body.lng;
	var pythonProcess = spawn('python',["../test.py", Latitude, Longitude]);
	pythonProcess.stdout.on('data',function (data){
		var pythondata = data.toString();
		var RGB = pythondata.split("\n");
		var total = parseInt(RGB[0])+parseInt(RGB[1])+parseInt(RGB[2])
		console.log(total);
		res.render('mappage',{red: RGB[2], green:RGB[0],blue:RGB[1], lat:Latitude, lng:Longitude, total:total});
	});

})

app.listen(3000, function () {
  console.log('Example app listening on port 3000!')
})