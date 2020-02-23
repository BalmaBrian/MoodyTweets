const request = require('request');

exports.renderMoodScreen = (req, res) => {
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
                    res.render('moods/neutral/neutral');
                    break;
                case 4:
                    res.render('moods/fearful/fearful');
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
}