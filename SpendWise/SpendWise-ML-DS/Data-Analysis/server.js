const express = require('express');
const path = require('path');
const { spawn } = require('child_process'); // For running Python script
const app = express();
const port = 3001;

// Serve static files (images) from the 'static' folder
app.use('/static', express.static(path.join(__dirname, 'static')));

// Route to run the Python script and generate graphs
app.get('/generate-plot', (req, res) => {
  const python = spawn('python', ['generate_plot.py']);
  
  python.on('close', (code) => {
    if (code === 0) {
      res.send('Graphs generated successfully');
    } else {
      res.status(500).send('Error generating graphs');
    }
  });
});

// Routes to get the image URLs for each graph
app.get('/graph/expense', (req, res) => {
  res.json({ imageUrl: '/static/expense_graph.png' });
});

app.get('/graph/category', (req, res) => {
  res.json({ imageUrl: '/static/category_graph.png' });
});

app.get('/graph/paymentmode', (req, res) => {
  res.json({ imageUrl: '/static/payment_mode_graph.png' });
});

app.get('/graph/impulse', (req, res) => {
  res.json({ imageUrl: '/static/impulse_need_graph.png' });
});

// Start the Express server
app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}`);
});
