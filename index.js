const express = require('express');
const app = express();
app.use(express.json()); // lee el JSON recibido

let alumnos = [{ id: 1, nombre: 'Ana Torres', edad: 20 }];

// LEER: lista de alumnos
app.get('/alumnos', (req, res) => res.json(alumnos));

// CREAR: nuevo alumno
app.post('/alumnos', (req, res) => {
 const nuevo = { id: alumnos.length + 1, ...req.body };
 alumnos.push(nuevo);
 res.status(201).json(nuevo); // 201 = Creado
});

app.listen(3000, () => console.log('API en http://localhost:3000'));