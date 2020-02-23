const express = require('express');
const router = express.Router();

const renderMoodScreen = require('../controllers/renderMoodScreen').renderMoodScreen;

router.get('/submit-username', renderMoodScreen);

module.exports = router;