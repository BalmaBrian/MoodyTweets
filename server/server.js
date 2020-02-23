require('dotenv').config();

const path = require('path');
const express = require('express');
const bodyParser = require('body-parser');
const app = express();

app.use(bodyParser.urlencoded({extended: false}));
app.use(bodyParser.json());

app.set('view engine', 'ejs');
app.set('views', 'views');
app.use(express.static(__dirname + '/public'));


app.get('/', (req, res) => {
    res.render('index/Experiment');
});

app.get('/submit-username', (req, res) => {
    const handle = req.body.handle;

    res.send(handle);

    // let tweets = await callGetTweets(handle);

    //let mood = await ML(tweets);  //1...10

    // switch(mood) {
    //     case 1:
    //         res.render('moods/sad/sad');
    //     case 2;
    //         res.render('normal');
    //         .....
    // }
});

// Listen to the App Engine-specified port, or 8080 otherwise
const PORT = process.env.PORT || 8080;

app.listen(PORT, () => {
    console.log(`Server listening on port ${PORT}...`);
});