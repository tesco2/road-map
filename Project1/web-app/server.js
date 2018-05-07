const express = require('express')
const app = express()
const bodyParser = require('body-parser');
const spawn = require("child_process").spawn;

app.set('view engine','ejs')
app.use(express.static('public'));
app.use(bodyParser.urlencoded({ extended: true }));

app.get('/', function (req, res) {
  res.render('mappage',{red: null,green:null,blue:null, lat:-37.82701522389683, lng:144.96238708496094});
})

app.post('/',function (req,res){
	var Latitude = req.body.lat;
	var Longitude = req.body.lng;
	var pythonProcess = spawn('python',["../test.py", Latitude, Longitude]);
	pythonProcess.stdout.on('data',function (data){
		var pythondata = data.toString();
		var RGB = pythondata.split("\n");
		console.log(RGB[0]);
		res.render('mappage',{red: RGB[0], green:RGB[1],blue:RGB[2], lat:Latitude, lng:Longitude});
	});

})

app.listen(3000, function () {
  console.log('Example app listening on port 3000!')
})