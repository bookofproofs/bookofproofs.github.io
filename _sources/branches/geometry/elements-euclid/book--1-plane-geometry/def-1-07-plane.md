layout: definition
categories: branches,geometry,elements-euclid,book--1-plane-geometry
nodeid: bookofproofs$647
orderid: 600
parentid: bookofproofs$685
title: 1.07: Plane
description: 1.07: PLANE &#9733; bring your math skills to the graduate level &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: 
keywords: 2 3, center.y + + scale,def,dx, 2,plane,plane surface,x + ct,x - st,y + cp,y + st,y - ct
contributors: bookofproofs

---


---



> A **plane surface** is any [surface][bookofproofs$646] which lies evenly with the [straight lines][bookofproofs$645] on itself.

### Modern Definition

A [surface][bookofproofs$646] `\(s\)` is called a **plane**, if for two arbitrary [points][bookofproofs$631] `\(A,B\)` in this surface also the [straight line][bookofproofs$645] `\(\overline{AB}\)` [joining them][bookofproofs$692] lies wholly in the surface.

`\[A,B\in s\Longrightarrow\overline{AB}\subset s.\]`

<div style='text-align:center'><canvas id="cnvE16498" class="centered" style="min-width:700px" height="500"></canvas></div>

§§§1

---

§§§1

<script type="text/javascript">
//JXG.JSXGraph - please do not delete this line
//The 3d concept for this script can be found in a great article of Jérémy Heleine at https://www.sitepoint.com/building-3d-engine-javascript/

var Vertex = function(x, y, z) {
    this.x = parseFloat(x);
    this.y = parseFloat(y);
    this.z = parseFloat(z);
}

var Vertex2D = function(x, y) {
    this.x = parseFloat(x);
    this.y = parseFloat(y); 
}

var Surface = function(center, scale) {
    // Generate the vertices
    scale=scale/1.5;
    trans=scale/4;

    this.vertices = [
        new Vertex(center.x, center.y, center.z),
        new Vertex(center.x + scale, center.y, center.z),
        new Vertex(center.x + scale, center.y + scale, center.z),
        new Vertex(center.x, center.y + scale, center.z),
        new Vertex(center.x+ scale/3, center.y + + scale/3, center.z+ scale/3),
        new Vertex(center.x+ scale*2/3, center.y + + scale*2/3, center.z+ scale*2/3),
    ];

    // Generate the faces
    this.faces = [
        [this.vertices[^0], this.vertices[^1], this.vertices[^2], this.vertices[^3]],
    ];
} 

function project(M) {
    return new Vertex2D(M.x, M.z);
}

function render(objects, ctx, dx, dy) {
    // Clear the previous frame
    ctx.clearRect(0, 0, 2*dx, 2*dy);

    // For each object
    for (var i = 0, n_obj = objects.length; lt(i,  n_obj); ++i) {
        // For each face
        for (var j = 0, n_faces = objects[i].faces.length; lt(j, n_faces); ++j) {
            // Current face
            var face = objects[i].faces[j];

            // Draw the first vertex
            var P = project(face[^0]);
            ctx.beginPath();
            ctx.moveTo(P.x + dx, -P.y + dy);

            // Draw the other vertices
            for (var k = 1, n_vertices = face.length; lt(k,n_vertices); ++k) {
                P = project(face[k]);
                ctx.lineTo(P.x + dx, -P.y + dy);
            }




            // Close the path and draw the face
            ctx.closePath();
            ctx.stroke();
            ctx.fill();
        }
    }
}

(function() {
    // Fix the canvas width and height
    var canvas = document.getElementById('cnvE16498');
    canvas.width = canvas.offsetWidth;
    canvas.height = canvas.offsetHeight;
    var dx = canvas.width / 2;
    var dy = canvas.height / 2;

    // Objects style
    var ctx = canvas.getContext('2d');
    ctx.strokeStyle = 'rgba(0, 0, 0, 0.3)';
    ctx.fillStyle = 'rgba(0, 150, 255, 0.3)';

    // Create the Surfaces
    var tet_center = new Vertex(0, 11*dy/10, 0);
    var tet = new Surface(tet_center, dy);
    var objects = [tet];

    // First render
    render(objects, ctx, dx, dy);

    // Events
    var mousedown = false;
    var mx = 0;
    var my = 0;

    canvas.addEventListener('mousedown', initMove);
    document.addEventListener('mousemove', move);
    document.addEventListener('mouseup', stopMove);

    // Rotate a vertice
    function rotate(M, center, theta, phi) {
        // Rotation matrix coefficients
        var ct = Math.cos(theta);
        var st = Math.sin(theta);
        var cp = Math.cos(phi);
        var sp = Math.sin(phi);

        // Rotation
        var x = M.x - center.x;
        var y = M.y - center.y;
        var z = M.z - center.z;

        M.x = ct * x - st * cp * y + st * sp * z + center.x;
        M.y = st * x + ct * cp * y - ct * sp * z + center.y;
        M.z = sp * y + cp * z + center.z;
    }

    // Initialize the movement
    function initMove(evt) {
        clearTimeout(autorotate_timeout);
        mousedown = true;
        mx = evt.clientX;
        my = evt.clientY;
    }

    function move(evt) {
        if (mousedown) {
            var theta = (evt.clientX - mx) * Math.PI / 360;
            var phi = (evt.clientY - my) * Math.PI / 180;

            for (var i = 0, n_vertices = tet.vertices.length; lt(i,n_vertices); ++i)
                rotate(tet.vertices[i], tet_center, theta, phi);

            mx = evt.clientX;
            my = evt.clientY;

            render(objects, ctx, dx, dy);
        }
    }

    function stopMove() {
        mousedown = false;
        autorotate_timeout = setTimeout(autorotate, 2000);
    }

    function autorotate() {
        for (var i = 0, n_vertices = tet.vertices.length; lt(i, n_vertices); ++i)
            rotate(tet.vertices[i], tet_center, -Math.PI / 720, Math.PI / 720);

        render(objects, ctx, dx, dy);

        autorotate_timeout = setTimeout(autorotate, 30);
    }
    autorotate_timeout = setTimeout(autorotate, 2000);
})();

</script>

