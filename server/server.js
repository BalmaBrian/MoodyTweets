require('dotenv').config();

const express = require('express');
const bodyParser = require('body-parser');
const request = require('request');

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
    const handle = req.query.handle.split('@')[1];
    const getTweetsCloudFunctionURL = 'https://us-central1-moody-tweets-62047.cloudfunctions.net/getTweets';
    const MLgetMoodCloudFunctionURL = 'https://us-central1-moody-tweets-62047.cloudfunctions.net/MLgetMood';

    request({
        url: getTweetsCloudFunctionURL,
        method: 'POST',
        json: {"handle": handle}
    }, (err, response, tweets) => {

        request({
            url: MLgetMoodCloudFunctionURL,
            method: 'POST',
            json: {"tweets": tweets}
        }, (err, response, mood) => {
            switch(mood) {
                case 1:
                    res.render('moods/angry/angry');
                    break;
                case 2:
                    res.render('moods/sad/sad');
                    break;
                case 3:
                    res.render('moods/fearful/fearful');
                    break;
                case 4:
                    res.render('moods/neutral/neutral');
                    break;
                case 5:
                    res.render('moods/surprised/surprised');
                    break;
                case 6:
                    res.render('moods/happy/happy');
                    break;
                default:
                    res.send(`Hello, World!`);
            }
        });
    });
});

// Listen to the App Engine-specified port, or 8080 otherwise
const PORT = process.env.PORT || 8080;

app.listen(PORT, () => {
    console.log(`Server listening on port ${PORT}...`);
});