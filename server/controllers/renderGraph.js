const request = require('request');
const admin = require('firebase-admin');
var Chart = require('chart.js');

exports.renderGraph = async (req, res) => {
    const handle = req.query.handle;


    const db = admin.firestore();

    let userRef = db.collection('users').doc(handle);

    userRef.set({

    })

    let moods = await userRef.collection('moods').get();
    moods = moods.docs.map(doc => doc.data());

    let times = moods.map(doc => new Date(doc.timestamp._seconds * 1000));


    let backgroundColors = [];
    let backgroundColorRGBs = {
        '0': 'rgb(255,10,0)',
        '1': 'rgb(25,28,105)',
        '2': 'rgb(128,128,128)',
        '3': 'rgb(192,152,13)',
        '4': 'rgb(84,255,94)',
        '5': 'rgba(247,255,44,0.99)'
    }

    moods.forEach(moodDoc => backgroundColors.push(backgroundColorRGBs[(moodDoc.mood - 1)]));




    let borderColors = [];

    // 'rgba(255, 99, 132, 1)',
    //     'rgba(54, 162, 235, 1)',
    //     'rgba(255, 206, 86, 1)',
    //     'rgba(75, 192, 192, 1)',
    //     'rgba(153, 102, 255, 1)',
    //     'rgba(255, 159, 64, 1)'

    res.render('graph/graph', {
        moods: moods.map(doc => doc.mood),
        handle: handle,
        times: times,
        backgroundColors: backgroundColors.join('|'),
        borderColors: borderColors
    });

    // const getTweetsCloudFunctionURL = 'https://us-central1-moody-tweets-62047.cloudfunctions.net/getTweets';
    // const MLgetMoodCloudFunctionURL = 'https://us-central1-moody-tweets-62047.cloudfunctions.net/MLgetMood';

    // request({
    //     url: getTweetsCloudFunctionURL,
    //     method: 'POST',
    //     json: {"handle": handle}
    // }, (err, response, tweets) => {
    //
    //     request({
    //         url: MLgetMoodCloudFunctionURL,
    //         method: 'POST',
    //         json: {"tweets": tweets}
    //     }, (err, response, mood) => {
    //
    //         //log to firestore
    //
    //         const db = admin.firestore();
    //
    //         let userRef = db.collection('users').doc(handle);
    //
    //         userRef.set({
    //
    //         })
    //
    //         let userMoodsRef = userRef.collection('moods');
    //
    //         userMoodsRef.add({
    //             mood: mood,
    //             timestamp: admin.firestore.FieldValue.serverTimestamp()
    //         }).then((doc) => {
    //             switch(mood) {
    //                 case 1:
    //                     res.render('moods/angry/angry');
    //                     break;
    //                 case 2:
    //                     res.render('moods/sad/sad');
    //                     break;
    //                 case 3:
    //                     res.render('moods/neutral/neutral');
    //                     break;
    //                 case 4:
    //                     res.render('moods/fearful/fearful');
    //                     break;
    //                 case 5:
    //                     res.render('moods/surprised/surprised');
    //                     break;
    //                 case 6:
    //                     res.render('moods/happy/happy');
    //                     break;
    //                 default:
    //                     res.send(`Hello, World!`);
    //             }
    //         })
    //     });
    // });
}