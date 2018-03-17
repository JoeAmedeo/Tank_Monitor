var express = require('express');
var body-parser = require('body-parser');
var mysql = require('mysql')

var connection = mysql.createConnection({
	host: "localhost",
	user: "root",
	password: "something"
});

var app = express();

app.get('/', function(req, res) {
	connection.connect(function(err) {
		if (err) throw err;
		console.log("connected to db");
		connection.query("SELECT * FROM Data ORDER BY Time DESC LIMIT 1", function(err, result) {
			if (err) throw err;
			console.log(result);
		});
	});
});
