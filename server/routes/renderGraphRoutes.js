const express = require('express');
const router = express.Router();

const renderGraph = require('../controllers/renderGraph').renderGraph

router.get('/graph', renderGraph);

module.exports = router;