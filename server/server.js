require('dotenv').config();

const express = require('express');
const app = express();

app.get('/', (req, res) => {
    res.send('Hello from App Engine!');
});

app.get('/submit-username', (req, res) => {
    const handle = req.body.handle;

    // let tweets = await callGetTweets(handle);

    //let mood = await ML(tweets);  //1...10

    // switch(mood) {
    //     case 1:
    //         render('sad');
    //     case 2;
    //         render('normal');
    //         .....
    // }
});

// Listen to the App Engine-specified port, or 8080 otherwise
const PORT = process.env.PORT || 8080;

app.listen(PORT, () => {
    console.log(`Server listening on port ${PORT}...`);
});