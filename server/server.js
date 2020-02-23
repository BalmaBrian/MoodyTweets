require('dotenv').config();

const express = require('express');
const bodyParser = require('body-parser');
const request = require('request');

const homePageRoutes = require('./routes/getHomePageRoutes');
const renderMoodRoutes = require('./routes/renderMoodScreenRoutes');
const renderGraphRoutes = require('./routes/renderGraphRoutes');
const get404 = require('./controllers/404').get404;

const app = express();
// Listen to the App Engine-specified port, or 8080 otherwise
const PORT = process.env.PORT || 8080;

app.use(bodyParser.urlencoded({extended: false}));
app.use(bodyParser.json());

app.set('view engine', 'ejs');
app.set('views', 'views');
app.use(express.static(__dirname + '/public'));

app.use(homePageRoutes);
app.use(renderMoodRoutes);
app.use(renderGraphRoutes);
app.use(get404);

app.listen(PORT, () => {
    console.log(`Server listening on port ${PORT}...`);
});