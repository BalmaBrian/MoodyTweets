const express = require('express');
const router = express.Router();

const renderMoodScreen = require('../controllers/renderMoodScreen').renderMoodScreen;

router.get('/mood', renderMoodScreen);

module.exports = router;