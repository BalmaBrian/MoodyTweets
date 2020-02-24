const express = require('express');
const router = express.Router();

const getHomePage = require('../controllers/getHomePage').getHomePage;

router.get('/', getHomePage);

module.exports = router;