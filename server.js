// sets up webserver and sends it to routes.js
const express = require('express'); 
const app = express();
const bodyParser = require('body-parser');
var routes = require("./routes/routes.js");
var port = "6969"
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));
routes(app);
var server = app.listen(port, function () {
    console.log(`i'm running on port ${port}!`);
});
