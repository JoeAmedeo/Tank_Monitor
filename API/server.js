var express = require('express');
var bodyParser = require('body-parser');
var mysql = require('mysql')

var connection = mysql.createConnection({
	host: "localhost",
	user: "root",
	password: "",
	database: "SensorData"
});

var app = express();

app.use(bodyParser.json());

app.get('/', function(req, res) {
	connection.connect(function(err) {
		if (err) throw err;
		console.log("connected to db");
		connection.query("(SELECT * FROM Data WHERE GPIO_number = 17 ORDER BY Time DESC LIMIT 1) UNION (SELECT * FROM Data WHERE GPIO_number = 18 ORDER BY Time DESC LIMIT 1)", function(err, result) {
			if (err) throw err;
			console.log(result);
			res.send(result);
		});
	});
});

app.listen(8080);
